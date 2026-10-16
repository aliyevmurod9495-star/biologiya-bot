import aiosqlite
from datetime import datetime
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
                total_tests INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # current_grade ustuni mavjud bo'lmasa qo'shish
        try:
            await db.execute("ALTER TABLE users ADD COLUMN current_grade TEXT DEFAULT '8'")
        except Exception:
            pass

        # is_allowed ustuni mavjud bo'lmasa qo'shish
        try:
            await db.execute("ALTER TABLE users ADD COLUMN is_allowed INTEGER DEFAULT 0")
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
                INSERT INTO users (user_id, full_name, username, current_grade, is_allowed)
                VALUES (?, 'Administrator', 'admin', '8', 1)
                ON CONFLICT(user_id) DO UPDATE SET is_allowed = 1
            """, (a_id,))

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


async def is_user_allowed(user_id: int) -> bool:
    """Foydalanuvchiga botdan foydalanishga ruxsat berilganligini tekshirish"""
    if await is_admin(user_id):
        return True
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT is_allowed FROM users WHERE user_id = ?", (user_id,)) as cur:
            row = await cur.fetchone()
            if row and row[0] == 1:
                return True
    return False


async def set_user_allowed(user_id: int, is_allowed: int = 1):
    """Foydalanuvchiga ruxsat berish (1) yoki bekor qilish (0)"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET is_allowed = ? WHERE user_id = ?", (is_allowed, user_id))
        await db.commit()


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
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cur:
            total = (await cur.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM users WHERE is_allowed = 1") as cur:
            allowed = (await cur.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM users WHERE is_allowed = 0") as cur:
            pending = (await cur.fetchone())[0]
        admins = len(await get_all_admins())
        return {"total": total, "allowed": allowed, "pending": pending, "admins": admins}


async def get_users_list(is_allowed: int, limit: int = 20) -> List[Dict[str, Any]]:
    """Ruxsat berilgan yoki kutilayotgan foydalanuvchilar ro'yxati"""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT user_id, full_name, username, joined_at
            FROM users
            WHERE is_allowed = ?
            ORDER BY joined_at DESC
            LIMIT ?
        """, (is_allowed, limit)) as cur:
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
