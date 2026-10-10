import aiosqlite
from datetime import datetime

DB_PATH = "bot_database.sqlite"

async def init_db():
    """Ma'lumotlar bazasini va jadvallarni yaratish"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                username TEXT,
                total_tests INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                grade TEXT,
                score INTEGER,
                total_questions INTEGER,
                finished_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        await db.commit()

async def add_or_update_user(user_id: int, full_name: str, username: str):
    """Foydalanuvchini ro'yxatga olish yoki yangilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (user_id, full_name, username)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                full_name = excluded.full_name,
                username = excluded.username
        """, (user_id, full_name, username))
        await db.commit()

async def record_test_result(user_id: int, grade: str, score: int, total: int):
    """Test yakunlanganida natijani saqlash va umumiy statistikani yangilash"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO test_results (user_id, grade, score, total_questions)
            VALUES (?, ?, ?, ?)
        """, (user_id, grade, score, total))

        await db.execute("""
            UPDATE users
            SET total_tests = total_tests + ?,
                correct_answers = correct_answers + ?
            WHERE user_id = ?
        """, (total, score, user_id))
        await db.commit()

async def get_user_stats(user_id: int):
    """Foydalanuvchi statistikasini olish"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
            SELECT total_tests, correct_answers, joined_at
            FROM users
            WHERE user_id = ?
        """, (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return {
                    "total": row[0],
                    "correct": row[1],
                    "joined_at": row[2]
                }
            return None

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

async def get_total_users_count():
    """Jami bot foydalanuvchilari soni"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0
