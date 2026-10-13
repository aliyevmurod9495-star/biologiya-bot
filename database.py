import aiosqlite
from datetime import datetime
from typing import Optional, List, Dict, Any

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


async def add_or_update_user(user_id: int, full_name: str, username: str):
    """Foydalanuvchini ro'yxatga olish yoki yangilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (user_id, full_name, username, current_grade)
            VALUES (?, ?, ?, '8')
            ON CONFLICT(user_id) DO UPDATE SET
                full_name = excluded.full_name,
                username = excluded.username
        """, (user_id, full_name, username))
        await db.commit()


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
