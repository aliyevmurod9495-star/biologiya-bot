import json
import logging
import asyncio
from typing import Dict, Any

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.types import (
    Message,
    CallbackQuery,
    PollAnswer,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputPollOption
)

import config
import database

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispetcher obyektlari
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Savollarni yuklash
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS_DATA: Dict[str, list] = json.load(f)

# O'quvchilarning faol test sessiyalarini saqlash
# user_id -> { "grade_name": str, "questions": list, "index": int, "score": int, "last_poll_id": str }
active_sessions: Dict[int, Dict[str, Any]] = {}
poll_to_user: Dict[str, int] = {}

# AI rejimida turgan foydalanuvchilar
ai_mode_users = set()

# Asosiy menyu klaviaturasi
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧪 Test topshirish"), KeyboardButton(text="🧠 AI Ustoz")],
        [KeyboardButton(text="📊 Mening natijalarim"), KeyboardButton(text="🏆 O'quvchilar reytingi")],
        [KeyboardButton(text="ℹ️ Bot haqida")]
    ],
    resize_keyboard=True
)

def get_grades_keyboard() -> InlineKeyboardMarkup:
    """Sinflarni tanlash uchun inline tugmalar"""
    buttons = [
        [InlineKeyboardButton(text="🌱 5-sinf (Botanika)", callback_data="grade_5"),
         InlineKeyboardButton(text="🌿 6-sinf (Botanika)", callback_data="grade_6")],
        [InlineKeyboardButton(text="🦎 7-sinf (Zoologiya)", callback_data="grade_7"),
         InlineKeyboardButton(text="🫀 8-sinf (Anatomiya)", callback_data="grade_8")],
        [InlineKeyboardButton(text="🔬 9-sinf (Biologiya)", callback_data="grade_9"),
         InlineKeyboardButton(text="🧬 10-sinf (Genetika)", callback_data="grade_10")],
        [InlineKeyboardButton(text="🌍 11-sinf (Ekologiya)", callback_data="grade_11")],
        [InlineKeyboardButton(text="🎲 Barcha sinflardan aralash test", callback_data="grade_all")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(CommandStart())
async def handle_start(message: Message):
    """Start komandasi berilganda"""
    user = message.from_user
    await database.add_or_update_user(
        user_id=user.id,
        full_name=user.full_name or "Noma'lum",
        username=user.username or ""
    )
    
    welcome_text = (
        f"Assalomu alaykum, <b>{user.first_name}</b>!\n\n"
        "🧬 <b>Biologiya fanidan test va viktorina botiga xush kelibsiz!</b>\n\n"
        "Bu bot orqali siz:\n"
        "• 5–11 sinf biologiya darsliklari bo'yicha bilimlaringizni sinashingiz;\n"
        "• Qiziqarli viktorinalarda qatnashishingiz;\n"
        "• Natijalaringizni ko'rib, reytingda yuqorilashingiz mumkin.\n\n"
        "Quyidagi menyudan kerakli bo'limni tanlang:"
    )
    await message.answer(welcome_text, reply_markup=MAIN_KEYBOARD)


@dp.message(F.text == "🧪 Test topshirish")
async def choose_grade_message(message: Message):
    """Test topshirish uchun sinf tanlash"""
    text = "📚 <b>Qaysi sinf darsligi bo'yicha test topshirmoqchisiz?</b>\n\nQuyidagi ro'yxatdan tanlang:"
    await message.answer(text, reply_markup=get_grades_keyboard())


@dp.message(F.text == "📊 Mening natijalarim")
async def show_my_stats(message: Message):
    """Foydalanuvchi statistikasini ko'rsatish"""
    stats = await database.get_user_stats(message.from_user.id)
    if not stats or stats["total"] == 0:
        await message.answer(
            "📊 Siz hali birorta ham test topshirmagansiz.\n"
            "\"🧪 Test topshirish\" tugmasini bosing va bilimlaringizni sinang!",
            reply_markup=MAIN_KEYBOARD
        )
        return

    total = stats["total"]
    correct = stats["correct"]
    percent = round((correct / total) * 100, 1)

    text = (
        f"📊 <b>Sizning umumiy natijalaringiz:</b>\n\n"
        f"🔹 Jami ishlangan savollar: <b>{total} ta</b>\n"
        f"✅ To'g'ri javoblar: <b>{correct} ta</b>\n"
        f"❌ Noto'g'ri javoblar: <b>{total - correct} ta</b>\n"
        f"🎯 Samaradorlik: <b>{percent}%</b>\n\n"
        f"📅 A'zo bo'lgan vaqt: <i>{stats['joined_at']}</i>"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


@dp.message(F.text == "🏆 O'quvchilar reytingi")
async def show_leaderboard(message: Message):
    """Eng yuqori ball to'plagan o'quvchilar reytingi"""
    top_users = await database.get_top_leaderboard(limit=10)
    if not top_users:
        await message.answer("🏆 Reyting hozircha bo'sh. Birinchi bo'lib test topshiring!")
        return

    text = "🏆 <b>Eng faol o'quvchilar reytingi (Top-10):</b>\n\n"
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, (full_name, username, correct, total) in enumerate(top_users):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        user_tag = f"(@{username})" if username else ""
        text += f"{medal} <b>{full_name}</b> {user_tag}\n"
        text += f"   └ To'g'ri: {correct} ta / Jami: {total} ta\n"

    await message.answer(text, reply_markup=MAIN_KEYBOARD)


@dp.message(F.text == "ℹ️ Bot haqida")
async def show_about(message: Message):
    """Bot haqida ma'lumot"""
    total_users = await database.get_total_users_count()
    text = (
        "🤖 <b>Biologiya Viktorina Boti (@Biologiya1_N2_bot)</b>\n\n"
        "Ushbu bot maktab o'quvchilari va abituriyentlar uchun biologiya fanidan "
        "bilimlarni mustahkamlash, test sinovlari va Sun'iy Intellekt yordamida o'rganishga yordam beradi.\n\n"
        f"👥 Foydalanuvchilar soni: <b>{total_users} nafar</b>\n"
        "⚡️ Dasturlash tili: Python (aiogram 3 + Google Gemini AI)"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


async def ask_gemini_ai(prompt: str) -> str:
    """Google Gemini AI orqali biologik savolga javob olish"""
    if not config.GEMINI_API_KEY:
        return (
            "⚠️ <b>Sun'iy intellekt (AI) API kaliti ulanmagan.</b>\n\n"
            "Admin tomonidan Google Gemini API kaliti sozlanishi kerak."
        )
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={config.GEMINI_API_KEY}"
    
    system_prompt = (
        "Siz o'zbek tilida so'zlashuvchi biologiya fani bo'yicha yuqori malakali o'qituvchi va repetitorsiz (AI Ustoz). "
        "O'quvchining savoliga o'zbek tilida aniq, tushunarli, darslikka asoslangan va ilmiy to'g'ri javob bering. "
        "Agar biologiya yoki genetika masalasi bo'lsa, uni bosqichma-bosqich formulasi, yechimi va javobi bilan tushuntiring. "
        "Javobni Telegram HTML formatida chiroyli sarlavha va qalin matnlar bilan bezating."
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{system_prompt}\n\nO'quvchi savoli: {prompt}"}
                ]
            }
        ]
    }
    
    import aiohttp
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=aiohttp.ClientTimeout(total=40)) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    candidates = data.get("candidates", [])
                    if candidates and "content" in candidates[0]:
                        parts = candidates[0]["content"].get("parts", [])
                        if parts:
                            return parts[0].get("text", "Kechirasiz, javob olishda xatolik yuz berdi.")
                    return "Kechirasiz, sun'iy intellektdan javob kelmadi."
                else:
                    return f"⚠️ Sun'iy intellekt serverida xatolik yuz berdi (Status: {resp.status})."
    except Exception as e:
        logging.error(f"Gemini API xatoligi: {e}")
        return "⚠️ Sun'iy intellekt bilan bog'lanishda vaqt tugadi. Iltimos qaytadan urinib ko'ring."


@dp.message(F.text == "🧠 AI Ustoz")
async def start_ai_mode(message: Message):
    """AI ustoz rejimini yoqish"""
    ai_mode_users.add(message.from_user.id)
    text = (
        "🧠 <b>Assalomu alaykum! Men sizning biologiya bo‘yicha Sun'iy Intellekt Ustozingizman.</b>\n\n"
        "Menga biologiyadan istalgan savolingizni yozing yoki masalani yuboring:\n"
        "• <i>«Fotosintez qanday sodir bo'ladi?»</i>\n"
        "• <i>«Mitoz va meyozning farqi nima?»</i>\n"
        "• <i>Genetika yoki DNK masalalarining matni</i>\n\n"
        "✍️ <b>Savolingizni yoki masalangizni yozib yuboring:</b>"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


@dp.message(F.text & ~F.text.startswith("/") & ~F.text.in_(["🧪 Test topshirish", "📊 Mening natijalarim", "🏆 O'quvchilar reytingi", "ℹ️ Bot haqida", "🧠 AI Ustoz"]))
async def handle_ai_question(message: Message):
    """Foydalanuvchi erkin savol yozganda AI orqali javob berish"""
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    loading_msg = await message.answer("🤔 <i>Sun'iy intellekt javob tayyorlamoqda...</i>")
    
    answer = await ask_gemini_ai(message.text)
    
    if len(answer) > 4000:
        await loading_msg.delete()
        for i in range(0, len(answer), 4000):
            chunk = answer[i:i+4000]
            try:
                await message.answer(chunk, parse_mode="HTML")
            except Exception:
                await message.answer(chunk)
    else:
        try:
            await loading_msg.edit_text(answer, parse_mode="HTML")
        except Exception:
            await loading_msg.edit_text(answer)


@dp.callback_query(F.data.startswith("grade_"))
async def start_quiz_session(callback: CallbackQuery):
    """Tanlangan sinf bo'yicha testni boshlash"""
    await callback.answer()
    grade = callback.data.replace("grade_", "")
    user_id = callback.from_user.id

    if grade == "all":
        questions = []
        for g_list in QUESTIONS_DATA.values():
            questions.extend(g_list)
        grade_name = "Aralash (5–11 sinf)"
    else:
        questions = QUESTIONS_DATA.get(grade, [])
        grade_name = f"{grade}-sinf"

    if not questions:
        await callback.message.answer("⚠️ Bu sinf bo'yicha hozircha savollar mavjud emas.")
        return

    # Sessiyani saqlash
    active_sessions[user_id] = {
        "grade_name": grade_name,
        "questions": questions,
        "index": 0,
        "score": 0,
        "last_poll_id": None
    }

    await callback.message.answer(
        f"🎯 <b>{grade_name}</b> bo'yicha test boshlandi!\n"
        f"Jami savollar: <b>{len(questions)} ta</b>\n\n"
        "<i>Har bir savol uchun to'g'ri javobni tanlang. Omad!</i>"
    )

    await send_next_question(user_id)


async def send_next_question(user_id: int):
    """Navbatdagi savolni Telegram Quiz ko'rinishida yuborish"""
    session = active_sessions.get(user_id)
    if not session:
        return

    index = session["index"]
    questions = session["questions"]

    if index >= len(questions):
        await finish_quiz(user_id)
        return

    q = questions[index]
    options_list = [InputPollOption(text=str(opt)) for opt in q["options"]]

    try:
        poll_msg = await bot.send_poll(
            chat_id=user_id,
            question=f"[{index + 1}/{len(questions)}] {q['question']}",
            options=options_list,
            type="quiz",
            correct_option_id=q["correct_option_id"],
            explanation=q.get("explanation", "To'g'ri javob belgilandi!"),
            is_anonymous=False
        )

        session["last_poll_id"] = poll_msg.poll.id
        poll_to_user[poll_msg.poll.id] = user_id
    except Exception as e:
        logging.error(f"Savol yuborishda xatolik: {e}")
        await bot.send_message(user_id, "Savolni yuborishda xatolik yuz berdi.")


@dp.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    """Foydalanuvchi variantni belgilaganda"""
    poll_id = poll_answer.poll_id
    user_id = poll_to_user.get(poll_id)

    if not user_id or user_id not in active_sessions:
        return

    session = active_sessions[user_id]
    index = session["index"]
    questions = session["questions"]
    q = questions[index]

    chosen_option = poll_answer.option_ids[0] if poll_answer.option_ids else -1
    if chosen_option == q["correct_option_id"]:
        session["score"] += 1

    session["index"] += 1

    if poll_id in poll_to_user:
        del poll_to_user[poll_id]

    await asyncio.sleep(1.2)
    await send_next_question(user_id)


async def finish_quiz(user_id: int):
    """Test yakunlanganda natijani hisoblash va xabar berish"""
    session = active_sessions.pop(user_id, None)
    if not session:
        return

    total = len(session["questions"])
    score = session["score"]
    percent = round((score / total) * 100, 1)
    grade_name = session["grade_name"]

    await database.record_test_result(
        user_id=user_id,
        grade=grade_name,
        score=score,
        total=total
    )

    if percent >= 85:
        congrats = "🌟 <b>Ajoyib natija! Barakalla!</b>"
    elif percent >= 60:
        congrats = "👍 <b>Yaxshi natija! Yana ozroq takrorlash kerak.</b>"
    else:
        congrats = "📖 <b>Mavzularni yana bir bor o'qib chiqishni tavsiya qilamiz.</b>"

    summary_text = (
        f"🏁 <b>Test yakunlandi!</b>\n\n"
        f"📚 Bo'lim: <b>{grade_name}</b>\n"
        f"📝 Jami savollar: <b>{total} ta</b>\n"
        f"✅ To'g'ri javoblar: <b>{score} ta</b>\n"
        f"❌ Xato javoblar: <b>{total - score} ta</b>\n"
        f"🎯 Natija: <b>{percent}%</b>\n\n"
        f"{congrats}\n\n"
        "Yana test ishlash uchun <b>\"🧪 Test topshirish\"</b> tugmasini bosing!"
    )

    await bot.send_message(user_id, summary_text, reply_markup=MAIN_KEYBOARD)


async def run_web_server():
    """Bulutli serverlar (Render, Koyeb) uchun portni ochiq ushlab turuvchi veb-server"""
    import os
    from aiohttp import web
    
    async def health_check(request):
        return web.Response(text="Biologiya Test Boti 24/7 faol ishlamoqda! 🟢")
        
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    
    port = int(os.getenv("PORT", "8080"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logging.info(f"Veb-server port {port} da ishga tushirildi.")

async def main():
    """Botni ishga tushirish funksiyasi"""
    if config.BOT_TOKEN == "SIZNING_BOT_TOKENINGIZ":
        print("\n" + "="*50)
        print("DIQQAT: config.py yoki .env faylida BOT_TOKEN ko'rsatilmagan!")
        print("Telegramdan @BotFather orqali token olib, uni kiriting.")
        print("="*50 + "\n")
        return

    await database.init_db()
    print("Bot muvaffaqiyatli ishga tushirildi: @Biologiya1_N2_bot")
    
    # Bulutli server portini ochish
    try:
        await run_web_server()
    except Exception as e:
        logging.warning(f"Veb-serverni ishga tushirishda ogohlantirish: {e}")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi.")
