import aiosqlite
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
import config

DB_PATH = "bot_database.sqlite"

async def init_db():
    """Ma'lumotlar bazasini va jadvallarni yaratish hamda yangilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                username TEXT,
                current_grade TEXT DEFAULT '8',
                is_allowed INTEGER DEFAULT 0,
                subscription_until TIMESTAMP,
                total_tests INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Ustunlar mavjud bo'lmasa qo'shish
        try:
            await db.execute("ALTER TABLE users ADD COLUMN current_grade TEXT DEFAULT '8'")
        except Exception:
            pass

        try:
            await db.execute("ALTER TABLE users ADD COLUMN is_allowed INTEGER DEFAULT 0")
        except Exception:
            pass

        try:
            await db.execute("ALTER TABLE users ADD COLUMN subscription_until TIMESTAMP")
        except Exception:
            pass

        # Admins jadvali
        await db.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                user_id INTEGER PRIMARY KEY,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Birlamchi adminlarni ro'yxatga qo'shish
        for a_id in config.ADMIN_IDS:
            await db.execute("INSERT OR IGNORE INTO admins (user_id) VALUES (?)", (a_id,))
            await db.execute("""
                INSERT INTO users (user_id, full_name, username, current_grade, is_allowed, subscription_until)
                VALUES (?, 'Administrator', 'admin', '8', 1, NULL)
                ON CONFLICT(user_id) DO UPDATE SET is_allowed = 1, subscription_until = NULL
            """, (a_id,))

        # Test natijalari jadvali
        await db.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                grade TEXT,
                topic_title TEXT,
                score INTEGER,
                total_questions INTEGER,
                finished_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        
        try:
            await db.execute("ALTER TABLE test_results ADD COLUMN topic_title TEXT")
        except Exception:
            pass

        # 1. AI ga berilgan savollar jadvali (O'qituvchi hisoboti uchun)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS ai_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                full_name TEXT,
                grade TEXT,
                question TEXT,
                answer TEXT,
                asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 2. Haftalik nazorat testlari jadvali (O'zlashtirish monitoringi)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS weekly_tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                full_name TEXT,
                grade TEXT,
                score INTEGER,
                total INTEGER,
                mastery_percent REAL,
                status TEXT,
                taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 3. Masalalar va vazifalar topshirilishi jadvali
        await db.execute("""
            CREATE TABLE IF NOT EXISTS problem_submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                grade TEXT,
                category TEXT,
                problem_title TEXT,
                user_answer TEXT,
                is_correct INTEGER,
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        await db.commit()


async def is_admin(user_id: int) -> bool:
    """Foydalanuvchi admin ekanligini tekshirish"""
    if user_id in config.ADMIN_IDS:
        return True
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id FROM admins WHERE user_id = ?", (user_id,)) as cur:
            return bool(await cur.fetchone())


async def add_admin(user_id: int):
    """Yangi admin qo'shish"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT OR IGNORE INTO admins (user_id) VALUES (?)", (user_id,))
        await db.execute("UPDATE users SET is_allowed = 1 WHERE user_id = ?", (user_id,))
        await db.commit()


async def remove_admin(user_id: int):
    """Adminlikdan chiqarish (asosiy adminga tegmaslik)"""
    if user_id in config.ADMIN_IDS:
        return False
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM admins WHERE user_id = ?", (user_id,))
        await db.commit()
    return True


async def get_all_admins() -> List[int]:
    """Barcha adminlar ro'yxati"""
    admin_list = set(config.ADMIN_IDS)
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT user_id FROM admins") as cur:
                rows = await cur.fetchall()
                for r in rows:
                    admin_list.add(r[0])
    except Exception:
        pass
    return list(admin_list)


def parse_db_datetime(dt_val) -> Optional[datetime]:
    """Bazadagi sana formatlarini xavfsiz datetime obyektiga o'tkazish"""
    if not dt_val:
        return None
    if isinstance(dt_val, datetime):
        return dt_val
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(dt_val), fmt)
        except ValueError:
            continue
    return None


async def get_user_subscription_info(user_id: int) -> Dict[str, Any]:
    """Foydalanuvchining obuna holati haqida to'liq ma'lumot"""
    if await is_admin(user_id):
        return {
            "is_admin": True,
            "is_allowed": True,
            "is_active": True,
            "is_expired": False,
            "is_lifetime": True,
            "subscription_until": None,
            "formatted_date": "Cheksiz (Admin)",
            "days_left": 9999
        }

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT is_allowed, subscription_until FROM users WHERE user_id = ?", (user_id,)) as cur:
            row = await cur.fetchone()
            if not row:
                return {
                    "is_admin": False,
                    "is_allowed": False,
                    "is_active": False,
                    "is_expired": False,
                    "is_lifetime": False,
                    "subscription_until": None,
                    "formatted_date": "Ruxsat berilmagan",
                    "days_left": 0
                }

            is_allowed = bool(row[0])
            sub_dt = parse_db_datetime(row[1])
            now = datetime.now()

            if not is_allowed:
                return {
                    "is_admin": False,
                    "is_allowed": False,
                    "is_active": False,
                    "is_expired": False,
                    "is_lifetime": False,
                    "subscription_until": sub_dt,
                    "formatted_date": "Tasdiqlanmagan",
                    "days_left": 0
                }

            # Agar is_allowed = 1 va subscription_until yo'q bo'lsa (doimiy/cheksiz)
            if sub_dt is None:
                return {
                    "is_admin": False,
                    "is_allowed": True,
                    "is_active": True,
                    "is_expired": False,
                    "is_lifetime": True,
                    "subscription_until": None,
                    "formatted_date": "Cheksiz",
                    "days_left": 9999
                }

            if sub_dt > now:
                days_left = max(0, (sub_dt - now).days)
                return {
                    "is_admin": False,
                    "is_allowed": True,
                    "is_active": True,
                    "is_expired": False,
                    "is_lifetime": False,
                    "subscription_until": sub_dt,
                    "formatted_date": sub_dt.strftime("%d.%m.%Y %H:%M"),
                    "days_left": days_left
                }
            else:
                return {
                    "is_admin": False,
                    "is_allowed": False,
                    "is_active": False,
                    "is_expired": True,
                    "is_lifetime": False,
                    "subscription_until": sub_dt,
                    "formatted_date": sub_dt.strftime("%d.%m.%Y %H:%M"),
                    "days_left": 0
                }


async def is_user_allowed(user_id: int) -> bool:
    """Foydalanuvchiga botdan foydalanishga faol ruxsat borligini tekshirish"""
    info = await get_user_subscription_info(user_id)
    return info["is_active"]


async def set_user_subscription(user_id: int, days: int = 30) -> Optional[datetime]:
    """
    Foydalanuvchi obunasini belgilash yoki uzaytirish.
    days > 0: joriy muddatga yoki hozirdan boshlab N kun qo'shish (1 oy = 30 kun).
    days == 0: cheksiz (lifetime) qilib belgilash.
    """
    now = datetime.now()
    if days == 0:
        new_end = None
        new_end_str = None
    else:
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("SELECT subscription_until FROM users WHERE user_id = ?", (user_id,)) as cur:
                row = await cur.fetchone()
                current_end = parse_db_datetime(row[0]) if row else None

        if current_end and current_end > now:
            new_end = current_end + timedelta(days=days)
        else:
            new_end = now + timedelta(days=days)
        new_end_str = new_end.strftime("%Y-%m-%d %H:%M:%S")

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            UPDATE users 
            SET is_allowed = 1, subscription_until = ? 
            WHERE user_id = ?
        """, (new_end_str, user_id))
        await db.commit()
    return new_end


async def set_user_allowed(user_id: int, is_allowed: int = 1, days: Optional[int] = 30):
    """Foydalanuvchiga ruxsat berish (1) yoki bekor qilish (0)"""
    if is_allowed == 1:
        if days is not None and days > 0:
            return await set_user_subscription(user_id, days)
        else:
            async with aiosqlite.connect(DB_PATH) as db:
                await db.execute("UPDATE users SET is_allowed = 1, subscription_until = NULL WHERE user_id = ?", (user_id,))
                await db.commit()
            return None
    else:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("UPDATE users SET is_allowed = 0 WHERE user_id = ?", (user_id,))
            await db.commit()
        return None


async def add_or_update_user(user_id: int, full_name: str, username: str, default_allowed: int = 0):
    """Foydalanuvchini ro'yxatga olish yoki yangilash"""
    is_adm = await is_admin(user_id)
    initial_allowed = 1 if is_adm else default_allowed
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (user_id, full_name, username, current_grade, is_allowed)
            VALUES (?, ?, ?, '8', ?)
            ON CONFLICT(user_id) DO UPDATE SET
                full_name = excluded.full_name,
                username = excluded.username
        """, (user_id, full_name, username, initial_allowed))
        await db.commit()


async def get_user_info(user_id: int) -> Optional[Dict[str, Any]]:
    """Foydalanuvchi to'liq ma'lumoti"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None


async def get_user_counts() -> Dict[str, int]:
    """Admin panel uchun hisob-kitoblar"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cur:
            total = (await cur.fetchone())[0]
            
        async with db.execute("""
            SELECT COUNT(*) FROM users 
            WHERE is_allowed = 1 AND (subscription_until IS NULL OR subscription_until > ?)
        """, (now_str,)) as cur:
            allowed = (await cur.fetchone())[0]
            
        async with db.execute("""
            SELECT COUNT(*) FROM users 
            WHERE is_allowed = 1 AND subscription_until IS NOT NULL AND subscription_until <= ?
        """, (now_str,)) as cur:
            expired = (await cur.fetchone())[0]
            
        async with db.execute("SELECT COUNT(*) FROM users WHERE is_allowed = 0") as cur:
            pending = (await cur.fetchone())[0]
            
        admins = len(await get_all_admins())
        return {
            "total": total,
            "allowed": allowed,
            "expired": expired,
            "pending": pending,
            "admins": admins
        }


async def get_users_list(is_allowed: int = 1, filter_type: str = "allowed", limit: int = 20) -> List[Dict[str, Any]]:
    """Ruxsat berilgan, muddati tugagan yoki kutilayotgan foydalanuvchilar ro'yxati"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        if filter_type == "expired":
            query = """
                SELECT user_id, full_name, username, joined_at, subscription_until
                FROM users
                WHERE is_allowed = 1 AND subscription_until IS NOT NULL AND subscription_until <= ?
                ORDER BY subscription_until DESC
                LIMIT ?
            """
            params = (now_str, limit)
        elif filter_type == "pending" or is_allowed == 0:
            query = """
                SELECT user_id, full_name, username, joined_at, subscription_until
                FROM users
                WHERE is_allowed = 0
                ORDER BY joined_at DESC
                LIMIT ?
            """
            params = (limit,)
        else: # active / allowed
            query = """
                SELECT user_id, full_name, username, joined_at, subscription_until
                FROM users
                WHERE is_allowed = 1 AND (subscription_until IS NULL OR subscription_until > ?)
                ORDER BY joined_at DESC
                LIMIT ?
            """
            params = (now_str, limit)
            
        async with db.execute(query, params) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


async def set_user_grade(user_id: int, grade: str):
    """Foydalanuvchi faol sinfini belgilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            UPDATE users SET current_grade = ? WHERE user_id = ?
        """, (str(grade), user_id))
        await db.commit()


async def get_user_grade(user_id: int) -> str:
    """Foydalanuvchi faol sinfini olish (sukut bo'yicha 8)"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT current_grade FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row and row[0]:
                return str(row[0])
            return "8"


async def record_test_result(user_id: int, grade: str, score: int, total: int, topic_title: Optional[str] = None):
    """Test natijasini saqlash va statistikani yangilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO test_results (user_id, grade, topic_title, score, total_questions)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, grade, topic_title or "Aralash test", score, total))

        await db.execute("""
            UPDATE users
            SET total_tests = total_tests + ?,
                correct_answers = correct_answers + ?
            WHERE user_id = ?
        """, (total, score, user_id))
        await db.commit()


async def get_user_stats(user_id: int) -> Optional[Dict[str, Any]]:
    """Foydalanuvchi statistikasi"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT total_tests, correct_answers, current_grade, joined_at
            FROM users
            WHERE user_id = ?
        """, (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return {
                    "total": row[0],
                    "correct": row[1],
                    "current_grade": row[2] or "8",
                    "joined_at": row[3]
                }
            return None


async def get_user_recent_results(user_id: int, limit: int = 5) -> List[Dict[str, Any]]:
    """O'quvchining oxirgi ishlagan testlari ro'yxati"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT grade, topic_title, score, total_questions, finished_at
            FROM test_results
            WHERE user_id = ?
            ORDER BY finished_at DESC
            LIMIT ?
        """, (user_id, limit)) as cursor:
            rows = await cursor.fetchall()
            results = []
            for r in rows:
                results.append({
                    "grade": r[0],
                    "topic_title": r[1] or "Umumiy test",
                    "score": r[2],
                    "total": r[3],
                    "finished_at": r[4]
                })
            return results


async def get_top_leaderboard(limit: int = 10):
    """Eng yuqori natijaga ega o'quvchilar reytingi"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT full_name, username, correct_answers, total_tests
            FROM users
            WHERE total_tests > 0
            ORDER BY correct_answers DESC, total_tests ASC
            LIMIT ?
        """, (limit,)) as cursor:
            return await cursor.fetchall()


async def get_total_users_count() -> int:
    """Jami bot foydalanuvchilari soni"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0


async def get_user_topic_result(user_id: int, grade: str, topic_id_or_title: str) -> Optional[Dict[str, Any]]:
    """O'quvchining muayyan mavzu bo'yicha oxirgi natijasini olish"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT score, total_questions, finished_at
            FROM test_results
            WHERE user_id = ? AND grade = ? AND (topic_title LIKE ? OR topic_title LIKE ?)
            ORDER BY finished_at DESC
            LIMIT 1
        """, (user_id, grade, f"%{topic_id_or_title}%", f"%{topic_id_or_title}-mavzu%")) as cursor:
            row = await cursor.fetchone()
            if row:
                return {
                    "score": row[0],
                    "total": row[1],
                    "finished_at": row[2]
                }
            return None


# ==========================================
# 4. AI SAVOLLARI VA O'QITUVCHI HISOBOTI FUNKSIYALARI
# ==========================================

async def record_ai_question(user_id: int, full_name: str, grade: str, question: str, answer: str):
    """O'quvchi AI ga bergan savol va javobini bazada saqlash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO ai_questions (user_id, full_name, grade, question, answer)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, full_name, grade, question, answer))
        await db.commit()


async def get_student_ai_questions(user_id: int, limit: int = 10) -> List[Dict[str, Any]]:
    """Muayyan o'quvchi AI ga bergan oxirgi savollari"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT question, answer, grade, asked_at
            FROM ai_questions
            WHERE user_id = ?
            ORDER BY asked_at DESC
            LIMIT ?
        """, (user_id, limit)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


async def get_all_recent_ai_questions(limit: int = 30) -> List[Dict[str, Any]]:
    """Barcha o'quvchilar tomonidan berilgan so'nggi savollar"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT user_id, full_name, grade, question, asked_at
            FROM ai_questions
            ORDER BY asked_at DESC
            LIMIT ?
        """, (limit,)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# ==========================================
# 5. HAFTALIK TEST VA O'ZLASHTIRISH MONITORINGI
# ==========================================

async def record_weekly_test_result(user_id: int, full_name: str, grade: str, score: int, total: int) -> Dict[str, Any]:
    """Haftalik nazorat testi natijasini saqlash va o'zlashtirish darajasini hisoblash"""
    percent = round((score / total) * 100, 1) if total > 0 else 0
    if percent >= 90:
        status = "🟢 A'lo (Darslik to'liq o'zlashtirilgan)"
    elif percent >= 75:
        status = "🟡 Yaxshi (Mavzular yaxshi o'zlashtirilgan)"
    elif percent >= 60:
        status = "🟠 Qoniqarli (Ayrim mavzularni takrorlash kerak)"
    else:
        status = "🔴 Sust (Mavzularni qayta o'qish tavsiya etiladi)"

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO weekly_tests (user_id, full_name, grade, score, total, mastery_percent, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, full_name, grade, score, total, percent, status))
        await db.commit()

    return {
        "score": score,
        "total": total,
        "percent": percent,
        "status": status
    }


async def get_user_weekly_results(user_id: int, limit: int = 5) -> List[Dict[str, Any]]:
    """O'quvchining haftalik testlari tarixi"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT grade, score, total, mastery_percent, status, taken_at
            FROM weekly_tests
            WHERE user_id = ?
            ORDER BY taken_at DESC
            LIMIT ?
        """, (user_id, limit)) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]


# ==========================================
# 6. MASALALAR VA VAZIFALAR TOPWSHIRILISHI
# ==========================================

async def record_problem_submission(user_id: int, grade: str, category: str, problem_title: str, user_answer: str, is_correct: bool):
    """O'quvchining masala vazifasi yechimini saqlash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO problem_submissions (user_id, grade, category, problem_title, user_answer, is_correct)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, grade, category, problem_title, user_answer, 1 if is_correct else 0))
        await db.commit()


async def get_user_problem_stats(user_id: int) -> Dict[str, Any]:
    """O'quvchining masala yechish ko'rsatkichlari"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM problem_submissions WHERE user_id = ?", (user_id,)) as cur:
            total = (await cur.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM problem_submissions WHERE user_id = ? AND is_correct = 1", (user_id,)) as cur:
            correct = (await cur.fetchone())[0]
        percent = round((correct / total) * 100, 1) if total > 0 else 0
        return {"total": total, "correct": correct, "percent": percent}


# ==========================================
# 7. O'QITUVCHI UCHUN YAGONA O'ZLASHTIRISH HISOBOTI
# ==========================================

async def get_student_comprehensive_report(user_id: int) -> Optional[Dict[str, Any]]:
    """Bitta o'quvchi bo'yicha to'liq pedagogik tahliliy hisobot"""
    user = await get_user_info(user_id)
    if not user:
        return None

    user_stats = await get_user_stats(user_id) or {"total": 0, "correct": 0, "current_grade": "8"}
    problem_stats = await get_user_problem_stats(user_id)
    weekly_history = await get_user_weekly_results(user_id, limit=3)
    ai_questions = await get_student_ai_questions(user_id, limit=5)

    test_total = user_stats["total"]
    test_correct = user_stats["correct"]
    test_percent = round((test_correct / test_total) * 100, 1) if test_total > 0 else 0

    # Integral o'zlashtirish darajasini hisoblash (Vaznli formula)
    # 50% oddiy testlar + 35% haftalik testlar + 15% masalalar
    last_weekly = weekly_history[0] if weekly_history else None
    weekly_pct = last_weekly["mastery_percent"] if last_weekly else test_percent
    prob_pct = problem_stats["percent"] if problem_stats["total"] > 0 else test_percent

    if test_total == 0 and not last_weekly and problem_stats["total"] == 0:
        overall_mastery = 0.0
        mastery_badge = "⚪️ Hali test va topshiriqlar boshlanmagan"
    else:
        overall_mastery = round(0.50 * test_percent + 0.35 * weekly_pct + 0.15 * prob_pct, 1)
        if overall_mastery >= 88:
            mastery_badge = "🟢 A'lo daraja (90-100%)"
        elif overall_mastery >= 72:
            mastery_badge = "🟡 Yaxshi daraja (75-88%)"
        elif overall_mastery >= 55:
            mastery_badge = "🟠 Qoniqarli daraja (55-71%)"
        else:
            mastery_badge = "🔴 Past daraja — Qayta o'qitish zarur (<55%)"

    return {
        "user_id": user_id,
        "full_name": user.get("full_name", "Noma'lum"),
        "username": user.get("username", ""),
        "current_grade": user_stats["current_grade"],
        "joined_at": user.get("joined_at", ""),
        "test_total": test_total,
        "test_correct": test_correct,
        "test_percent": test_percent,
        "last_weekly": last_weekly,
        "problem_stats": problem_stats,
        "ai_questions": ai_questions,
        "overall_mastery": overall_mastery,
        "mastery_badge": mastery_badge
    }


async def get_all_students_mastery_summary() -> List[Dict[str, Any]]:
    """Barcha ruxsat berilgan o'quvchilar bo'yicha umumiy reyting va o'zlashtirish hisoboti"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT user_id, full_name, username, current_grade, total_tests, correct_answers
            FROM users
            WHERE is_allowed = 1
            ORDER BY correct_answers DESC
        """) as cur:
            rows = await cur.fetchall()

    summary = []
    for r in rows:
        u_dict = dict(r)
        u_id = u_dict["user_id"]
        # Skip admins from student list
        if await is_admin(u_id):
            continue
        report = await get_student_comprehensive_report(u_id)
        if report:
            summary.append(report)
    return summary
