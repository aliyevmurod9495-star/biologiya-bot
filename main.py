import json
import logging
import asyncio
import random
from typing import Dict, Any, Optional

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
import materials

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispetcher obyektlari
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Savollarni yuklash
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS_DATA: Dict[str, Any] = json.load(f)

# O'quvchilarning faol test sessiyalarini saqlash
active_sessions: Dict[int, Dict[str, Any]] = {}
poll_to_user: Dict[str, int] = {}

# Asosiy menyu klaviaturasi (Aynan rasmdagidek)
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Mavzular"), KeyboardButton(text="📝 Testlar")],
        [KeyboardButton(text="🎥 Video darslar"), KeyboardButton(text="🧬 Animatsiyalar")],
        [KeyboardButton(text="🏆 Reyting"), KeyboardButton(text="📊 Natijalar")],
        [KeyboardButton(text="💳 Premium"), KeyboardButton(text="👨‍🏫 O'qituvchi")],
        [KeyboardButton(text="🤖 AI Biologiya")],
        [KeyboardButton(text="🔄 Sinfni almashtirish")]
    ],
    resize_keyboard=True
)

GRADE_NAMES = {
    "5": "🌱 5-sinf (Botanika)",
    "6": "🌿 6-sinf (Botanika)",
    "7": "🦎 7-sinf (Zoologiya)",
    "8": "🫀 8-sinf (Odam anatomiyasi)",
    "9": "🔬 9-sinf (Sitologiya)",
    "10": "🧬 10-sinf (Genetika)",
    "11": "🌍 11-sinf (Ekologiya)"
}

def get_grades_inline_keyboard() -> InlineKeyboardMarkup:
    """Sinflarni almashtirish uchun inline tugmalar"""
    buttons = [
        [InlineKeyboardButton(text="🌱 5-sinf (Botanika)", callback_data="setgrade_5"),
         InlineKeyboardButton(text="🌿 6-sinf (Botanika)", callback_data="setgrade_6")],
        [InlineKeyboardButton(text="🦎 7-sinf (Zoologiya)", callback_data="setgrade_7"),
         InlineKeyboardButton(text="🫀 8-sinf (Anatomiya)", callback_data="setgrade_8")],
        [InlineKeyboardButton(text="🔬 9-sinf (Biologiya)", callback_data="setgrade_9"),
         InlineKeyboardButton(text="🧬 10-sinf (Genetika)", callback_data="setgrade_10")],
        [InlineKeyboardButton(text="🌍 11-sinf (Ekologiya)", callback_data="setgrade_11")]
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
    grade = await database.get_user_grade(user.id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    welcome_text = (
        f"Assalomu alaykum, <b>{user.first_name}</b>!\n\n"
        "🧬 <b>Biologiya ta'lim va test botiga xush kelibsiz!</b>\n\n"
        f"📌 Joriy faol sinf: <b>{grade_name}</b>\n\n"
        "Quyidagi menyudan kerakli bo'limni tanlang:\n"
        "• 📖 <b>Mavzular</b> — Darslik ma'ruzalari va konspektlar\n"
        "• 📝 <b>Testlar</b> — Mavzulashtirilgan viktorina testlari\n"
        "• 🎥 <b>Video darslar</b> — Mavzuga oid videoroliklar\n"
        "• 🧬 <b>Animatsiyalar</b> — 3D biologik animatsiyalar\n"
        "• 📊 <b>Natijalar</b> — Sizning test natijalaringiz\n"
        "• 🏆 <b>Reyting</b> — Eng iqtidorli o'quvchilar ro'yxati\n"
        "• 🤖 <b>AI Biologiya</b> — Sun'iy Intellektdan javob olish\n"
        "• 👨‍🏫 <b>O'qituvchi</b> — Ustoz bilan bog'lanish"
    )
    await message.answer(welcome_text, reply_markup=MAIN_KEYBOARD)


# ==========================================
# 1. MAVZULAR (MA'RUZALAR) BO'LIMI
# ==========================================
@dp.message(F.text == "📖 Mavzular")
async def show_topics_menu(message: Message):
    """Tanlangan sinf bo'yicha mavzular ma'ruzasini ko'rsatish"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    grade_data = QUESTIONS_DATA.get(grade, {})
    topics_from_q = grade_data.get("topics", [])

    buttons = []
    if lectures:
        for lec in lectures:
            buttons.append([
                InlineKeyboardButton(
                    text=f"📖 {lec['title']}",
                    callback_data=f"read_topic_{grade}_{lec['id']}"
                )
            ])
    elif topics_from_q:
        for t in topics_from_q:
            buttons.append([
                InlineKeyboardButton(
                    text=f"📖 {t['title']}",
                    callback_data=f"read_topic_{grade}_{t['id']}"
                )
            ])
    else:
        await message.answer(
            f"⚠️ <b>{grade_name}</b> bo'yicha hozircha ma'ruzalar tayyorlanmoqda.\n"
            "Boshqa sinfni tanlash uchun <b>\"🔄 Sinfni almashtirish\"</b> tugmasini bosing.",
            reply_markup=MAIN_KEYBOARD
        )
        return

    buttons.append([
        InlineKeyboardButton(text="🔄 Boshqa sinfni tanlash", callback_data="switch_grade_prompt")
    ])

    await message.answer(
        f"📚 <b>{grade_name} — Mavzular va Ma'ruzalar</b>\n\n"
        "O'rganmoqchi bo'lgan mavzungizni tanlang:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("read_topic_"))
async def read_topic_content(callback: CallbackQuery):
    """Mavzu ma'ruzasini ko'rsatish"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[2]
    topic_id = parts[3]

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    lec = next((l for l in lectures if str(l["id"]) == str(topic_id)), None)

    if not lec:
        # Agar materials.py da bo'lmasa, questions.json dan qidiramiz
        grade_data = QUESTIONS_DATA.get(grade, {})
        topic_info = next((t for t in grade_data.get("topics", []) if str(t["id"]) == str(topic_id)), None)
        title = topic_info["title"] if topic_info else f"{topic_id}-mavzu"
        lecture_text = (
            f"📖 <b>{title}</b>\n\n"
            "Ushbu mavzu bo'yicha qisqa konspekt va asosiy qoidalar tayyorlanmoqda.\n"
            "Darhol mavzu bo'yicha test ishlab bilimlaringizni sinashingiz mumkin!"
        )
    else:
        lecture_text = lec["text"]

    buttons = [
        [InlineKeyboardButton(text="📝 Ushbu mavzudan test ishlash", callback_data=f"topic_{grade}_{topic_id}")],
        [InlineKeyboardButton(text="⬅️ Barcha mavzular ro'yxati", callback_data=f"back_to_topics_{grade}")]
    ]

    await callback.message.answer(
        lecture_text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("back_to_topics_"))
async def back_to_topics_callback(callback: CallbackQuery):
    """Mavzular ro'yxatiga qaytish"""
    await callback.answer()
    grade = callback.data.split("_")[3]
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")
    lectures = materials.TOPICS_CONTENT.get(grade, [])

    buttons = []
    for lec in lectures:
        buttons.append([
            InlineKeyboardButton(text=f"📖 {lec['title']}", callback_data=f"read_topic_{grade}_{lec['id']}")
        ])
    buttons.append([InlineKeyboardButton(text="🔄 Sinfni almashtirish", callback_data="switch_grade_prompt")])

    await callback.message.answer(
        f"📚 <b>{grade_name} — Mavzular ro'yxati:</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


# ==========================================
# 2. TESTLAR BO'LIMI
# ==========================================
@dp.message(F.text == "📝 Testlar")
async def show_tests_menu(message: Message):
    """Mavzulashtirilgan testlar ro'yxatini chiqarish"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    if not topics:
        await message.answer(
            f"⚠️ <b>{grade_name}</b> bo'yicha testlar kiritilmoqda.\n"
            "Boshqa sinfni tanlash uchun <b>\"🔄 Sinfni almashtirish\"</b> tugmasini bosing.",
            reply_markup=MAIN_KEYBOARD
        )
        return

    buttons = []
    total_q = 0
    for t in topics:
        q_count = len(t.get("questions", []))
        total_q += q_count
        buttons.append([
            InlineKeyboardButton(
                text=f"📝 {t['title']} ({q_count} ta)",
                callback_data=f"topic_{grade}_{t['id']}"
            )
        ])

    buttons.append([
        InlineKeyboardButton(
            text=f"🎲 Barcha mavzulardan aralash test ({total_q} ta)",
            callback_data=f"topic_{grade}_all"
        )
    ])
    buttons.append([
        InlineKeyboardButton(text="🔄 Boshqa sinf testlari", callback_data="switch_grade_prompt")
    ])

    await message.answer(
        f"📝 <b>{grade_name} — Mavzulashtirilgan testlar</b>\n\n"
        "Qaysi mavzudan test topshirmoqchisiz? Tanlang:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("topic_"))
async def start_topic_quiz(callback: CallbackQuery):
    """Tanlangan mavzu bo'yicha viktorina testini boshlash"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    user_id = callback.from_user.id

    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    if topic_id == "all":
        questions = []
        for t in topics:
            questions.extend(t.get("questions", []))
        session_title = f"{GRADE_NAMES.get(grade, grade)} (Barcha mavzular)"
    else:
        topic = next((t for t in topics if str(t["id"]) == str(topic_id)), None)
        if not topic:
            await callback.message.answer("⚠️ Mavzu topilmadi.")
            return
        questions = topic.get("questions", [])
        session_title = f"{topic['title']}"

    if not questions:
        await callback.message.answer("⚠️ Bu mavzu bo'yicha savollar mavjud emas.")
        return

    # Savollarni aralashtirib berish (bitta sessiya uchun 25 ta, aralash test uchun 30 ta)
    quiz_questions = questions[:]
    random.shuffle(quiz_questions)
    if topic_id == "all" and len(quiz_questions) > 30:
        quiz_questions = quiz_questions[:30]
    elif len(quiz_questions) > 25:
        quiz_questions = quiz_questions[:25]

    active_sessions[user_id] = {
        "grade": grade,
        "grade_name": session_title,
        "questions": quiz_questions,
        "index": 0,
        "score": 0,
        "last_poll_id": None
    }

    await callback.message.answer(
        f"🎯 <b>{session_title}</b> bo'yicha test boshlandi!\n"
        f"Jami savollar: <b>{len(quiz_questions)} ta</b>\n\n"
        "<i>Har bir savol uchun to'g'ri javobni belgilang. Omad!</i>"
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
    
    # Telegram Quiz cheklovlariga qarshi himoya
    q_text = f"[{index + 1}/{len(questions)}] {q['question']}"
    if len(q_text) > 295:
        q_text = q_text[:292] + "..."
        
    options_list = []
    for opt in q["options"]:
        opt_text = str(opt).strip()
        if len(opt_text) > 95:
            opt_text = opt_text[:92] + "..."
        options_list.append(InputPollOption(text=opt_text))

    expl_text = q.get("explanation", "To'g'ri javob belgilandi!")
    if len(expl_text) > 195:
        expl_text = expl_text[:192] + "..."

    try:
        poll_msg = await bot.send_poll(
            chat_id=user_id,
            question=q_text,
            options=options_list,
            type="quiz",
            correct_option_id=q["correct_option_id"],
            explanation=expl_text,
            is_anonymous=False
        )

        session["last_poll_id"] = poll_msg.poll.id
        poll_to_user[poll_msg.poll.id] = user_id
    except Exception as e:
        logging.error(f"Savol yuborishda xatolik: {e}")
        # Xatolik bo'lsa, qotib qolmasdan keyingi savolga o'tish
        session["index"] += 1
        await send_next_question(user_id)


@dp.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    """Foydalanuvchi variantni belgilaganda javobni tekshirish"""
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
    grade = session.get("grade", "8")
    session_title = session["grade_name"]

    await database.record_test_result(
        user_id=user_id,
        grade=grade,
        score=score,
        total=total,
        topic_title=session_title
    )

    if percent >= 85:
        congrats = "🌟 <b>Ajoyib natija! Barakalla!</b>"
    elif percent >= 60:
        congrats = "👍 <b>Yaxshi natija! Yana ozroq takrorlash kerak.</b>"
    else:
        congrats = "📖 <b>Mavzularni yana bir bor o'qib chiqishni tavsiya qilamiz.</b>"

    summary_text = (
        f"🏁 <b>Test yakunlandi!</b>\n\n"
        f"📚 Mavzu: <b>{session_title}</b>\n"
        f"📝 Jami savollar: <b>{total} ta</b>\n"
        f"✅ To'g'ri javoblar: <b>{score} ta</b>\n"
        f"❌ Xato javoblar: <b>{total - score} ta</b>\n"
        f"🎯 Samaradorlik: <b>{percent}%</b>\n\n"
        f"{congrats}\n\n"
        "<i>Natijalaringiz bazaga saqlandi.</i>"
    )

    finish_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📊 Mening natijalarim", callback_data="show_my_stats_cb")],
            [InlineKeyboardButton(text="📝 Boshqa test ishlash", callback_data="show_tests_cb")]
        ]
    )

    await bot.send_message(user_id, summary_text, reply_markup=finish_keyboard)


# ==========================================
# 3. VIDEO DARSLAR BO'LIMI
# ==========================================
@dp.message(F.text == "🎥 Video darslar")
async def show_videos_menu(message: Message):
    """Video darslar katalogi"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    videos = materials.VIDEO_LESSONS.get(grade, [])
    if not videos:
        await message.answer(
            f"🎥 <b>{grade_name}</b> bo'yicha video darslar yuklanmoqda.\n"
            "Hozirda 8-sinf anatomiyasi bo'yicha to'liq video darslar mavjud!",
            reply_markup=MAIN_KEYBOARD
        )
        return

    buttons = []
    for v in videos:
        buttons.append([
            InlineKeyboardButton(text=f"🎥 {v['title']}", callback_data=f"vid_{grade}_{v['id']}")
        ])

    await message.answer(
        f"🎥 <b>{grade_name} — Video Darslar</b>\n\n"
        "Mavzuni mukammal o'zlashtirish uchun kerakli videoni tanlang:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("vid_"))
async def show_video_item(callback: CallbackQuery):
    """Video dars haqida ma'lumot"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    v_id = parts[2]

    videos = materials.VIDEO_LESSONS.get(grade, [])
    vid = next((v for v in videos if v["id"] == v_id), None)
    if not vid:
        await callback.message.answer("⚠️ Video topilmadi.")
        return

    text = (
        f"🎥 <b>{vid['title']}</b>\n"
        f"⏱ Davomiyligi: <b>{vid['duration']}</b>\n\n"
        f"📝 <b>Dars tavsifi:</b>\n{vid['desc']}\n\n"
        "🎬 <i>Video darslar Telegram boti va o'quv kanali orqali taqdim etiladi.</i>"
    )
    await callback.message.answer(text)


# ==========================================
# 4. ANIMATSIYALAR BO'LIMI
# ==========================================
@dp.message(F.text == "🧬 Animatsiyalar")
async def show_animations_menu(message: Message):
    """3D Animatsiyalar ro'yxati"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    anims = materials.ANIMATIONS_3D.get(grade, [])
    if not anims:
        await message.answer(
            f"🧬 <b>{grade_name}</b> bo'yicha 3D animatsiyalar tez kunda qo'shiladi.",
            reply_markup=MAIN_KEYBOARD
        )
        return

    buttons = []
    for a in anims:
        buttons.append([
            InlineKeyboardButton(text=f"🧬 {a['title']}", callback_data=f"anim_{grade}_{a['id']}")
        ])

    await message.answer(
        f"🧬 <b>{grade_name} — 3D Biologik Animatsiyalar</b>\n\n"
        "Odam anatomiyasi va hayotiy jarayonlarni 3D ko'rinishda o'rganing:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("anim_"))
async def show_animation_item(callback: CallbackQuery):
    """Animatsiya haqida ma'lumot"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    a_id = parts[2]

    anims = materials.ANIMATIONS_3D.get(grade, [])
    anim = next((a for a in anims if a["id"] == a_id), None)
    if not anim:
        await callback.message.answer("⚠️ Animatsiya topilmadi.")
        return

    text = (
        f"🧬 <b>{anim['title']}</b>\n\n"
        f"🔬 <b>Tavsif:</b>\n{anim['desc']}\n\n"
        "💡 <i>3D animatsion videolar murakkab anatomik jarayonlarni oson va qiziqarli tushunishga yordam beradi!</i>"
    )
    await callback.message.answer(text)


# ==========================================
# 5. REYTING BO'LIMI
# ==========================================
@dp.message(F.text == "🏆 Reyting")
async def show_leaderboard(message: Message):
    """Top-10 o'quvchilar reytingi"""
    top_users = await database.get_top_leaderboard(limit=10)
    if not top_users:
        await message.answer("🏆 Reyting hozircha bo'sh. Birinchi bo'lib test topshiring!")
        return

    text = "🏆 <b>Eng bilimdon o'quvchilar reytingi (Top-10):</b>\n\n"
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, (full_name, username, correct, total) in enumerate(top_users):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        user_tag = f"(@{username})" if username else ""
        pct = round((correct / total) * 100, 1) if total > 0 else 0
        text += f"{medal} <b>{full_name}</b> {user_tag}\n"
        text += f"   └ Natija: {correct}/{total} ta ({pct}%)\n"

    await message.answer(text, reply_markup=MAIN_KEYBOARD)


# ==========================================
# 6. NATIJALAR BO'LIMI
# ==========================================
@dp.message(F.text == "📊 Natijalar")
async def show_my_stats(message: Message):
    """O'quvchining shaxsiy natijalari va test hisoboti"""
    user_id = message.from_user.id
    stats = await database.get_user_stats(user_id)
    if not stats or stats["total"] == 0:
        await message.answer(
            "📊 <b>Siz hali birorta ham test ishlamagansiz.</b>\n\n"
            "Bilimlaringizni sinash uchun <b>\"📝 Testlar\"</b> tugmasini bosing!",
            reply_markup=MAIN_KEYBOARD
        )
        return

    total = stats["total"]
    correct = stats["correct"]
    percent = round((correct / total) * 100, 1)
    grade = stats.get("current_grade", "8")
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    recent_tests = await database.get_user_recent_results(user_id, limit=5)

    text = (
        f"📊 <b>Sizning shaxsiy natijalaringiz:</b>\n\n"
        f"👤 O'quvchi: <b>{message.from_user.full_name}</b>\n"
        f"📚 Joriy tanlangan sinf: <b>{grade_name}</b>\n"
        f"🔹 Jami ishlangan savollar: <b>{total} ta</b>\n"
        f"✅ To'g'ri javoblar: <b>{correct} ta</b>\n"
        f"❌ Noto'g'ri javoblar: <b>{total - correct} ta</b>\n"
        f"🎯 O'rtacha aniqlik: <b>{percent}%</b>\n\n"
        "📋 <b>Oxirgi topshirilgan testlaringiz:</b>\n"
    )

    if recent_tests:
        for r in recent_tests:
            r_pct = round((r['score'] / r['total']) * 100, 1) if r['total'] > 0 else 0
            text += f"• <b>{r['topic_title']}</b>: {r['score']}/{r['total']} ta ({r_pct}%)\n"
    else:
        text += "<i>Hozircha saqlangan testlar yo'q.</i>\n"

    await message.answer(text, reply_markup=MAIN_KEYBOARD)


@dp.callback_query(F.data == "show_my_stats_cb")
async def show_my_stats_callback(callback: CallbackQuery):
    await callback.answer()
    await show_my_stats(callback.message)


@dp.callback_query(F.data == "show_tests_cb")
async def show_tests_callback(callback: CallbackQuery):
    await callback.answer()
    await show_tests_menu(callback.message)


# ==========================================
# 7. PREMIUM BO'LIMI
# ==========================================
@dp.message(F.text == "💳 Premium")
async def show_premium_info(message: Message):
    """Premium ta'lim va imkoniyatlar"""
    text = (
        "💳 <b>Biologiya Premium Ta'lim Bo'limi</b>\n\n"
        "Abituriyentlar, repetitorlar va biologiyani chuqur o'rganuvchilar uchun maxsus imkoniyatlar:\n\n"
        "✨ <b>Premium obunachilar uchun:</b>\n"
        "• Barcha 5–11 sinf mavzulari bo'yicha to'liq video darslar;\n"
        "• DTM va Milliy sertifikat darajasidagi mualliflik testlari;\n"
        "• Murakkab genetika, sitologiya va biokimyo masalalari yechimlari;\n"
        "• Ustoz Murod Aliyev bilan shaxsiy savol-javob va nazorat;\n"
        "• Haftalik saralash va mock imtihonlari.\n\n"
        "📞 <b>Ulanish va to'lov shartlari uchun:</b>\n"
        "Ustozga murojaat qiling: @Murod_Aliyev_9495"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


# ==========================================
# 8. O'QITUVCHI BO'LIMI
# ==========================================
@dp.message(F.text == "👨‍🏫 O'qituvchi")
async def show_teacher_info(message: Message):
    """Ustoz haqida ma'lumot"""
    text = (
        "👨‍🏫 <b>Biologiya fani ustozi: Murod Aliyev</b>\n\n"
        "📚 Oliy toifali biologiya o'qituvchisi va tajribali repetitor.\n"
        "🎯 Tibbiyot institutlari, DTM testlari va olimpiadalarga tayyorlovchi mutaxassis.\n\n"
        "💬 <b>Telegram profil:</b> @Murod_Aliyev_9495\n"
        "💡 <i>Savollaringiz, takliflaringiz yoki darslarga yozilish bo'yicha to'g'ridan-to'g'ri yozishingiz mumkin!</i>"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


# ==========================================
# 9. AI BIOLOGIYA (GEMINI AI)
# ==========================================
async def ask_gemini_ai(prompt: str) -> str:
    """Google Gemini AI orqali biologik savolga javob olish"""
    if not config.GEMINI_API_KEY:
        return (
            "⚠️ <b>Sun'iy intellekt (AI) API kaliti ulanmagan.</b>\n\n"
            "Admin tomonidan Google Gemini API kaliti sozlanishi kerak."
        )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={config.GEMINI_API_KEY}"

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


@dp.message(F.text == "🤖 AI Biologiya")
async def start_ai_mode(message: Message):
    """AI biologiya rejimi haqida ma'lumot"""
    text = (
        "🤖 <b>AI Biologiya — Sun'iy Intellekt Ustozingiz</b>\n\n"
        "Menga biologiyadan istalgan savolingizni yoki masalangizni yozib yuboring:\n"
        "• <i>«Fotosintezning yorug'lik va qorong'ulik bosqichlari qanday farqlanadi?»</i>\n"
        "• <i>«Odamda qon bosimi qanday boshqariladi?»</i>\n"
        "• <i>Genetika masalalari matni (DNK, mitoz, Mendel qonunlari)</i>\n\n"
        "✍️ <b>Savolingizni pastga yozib yuboring, men darhol tushuntirib beraman:</b>"
    )
    await message.answer(text, reply_markup=MAIN_KEYBOARD)


# ==========================================
# 10. SINFLARNI ALMASHTIRISH BO'LIMI
# ==========================================
@dp.message(F.text == "🔄 Sinfni almashtirish")
@dp.message(Command("sinflar"))
async def choose_grade_command(message: Message):
    """Sinfni tanlash yoki almashtirish menyusi"""
    text = (
        "📚 <b>O'zingiz tahsil olayotgan yoki o'rganmoqchi bo'lgan sinfni tanlang:</b>\n\n"
        "Har bir sinf uchun alohida mavzular, testlar, videolar va animatsiyalar mavjud:"
    )
    await message.answer(text, reply_markup=get_grades_inline_keyboard())


@dp.callback_query(F.data == "switch_grade_prompt")
async def switch_grade_prompt_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📚 Qaysi sinf darsligiga o'tmoqchisiz? Tanlang:",
        reply_markup=get_grades_inline_keyboard()
    )


@dp.callback_query(F.data.startswith("setgrade_"))
async def set_active_grade(callback: CallbackQuery):
    """Foydalanuvchining faol sinfini saqlash"""
    await callback.answer()
    grade = callback.data.split("_")[1]
    user_id = callback.from_user.id

    await database.set_user_grade(user_id, grade)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    await callback.message.answer(
        f"✅ Faol sinf: <b>{grade_name}</b> ga muvaffaqiyatli o'zgartirildi!\n\n"
        "Endi pastki menyudagi <b>\"📖 Mavzular\"</b>, <b>\"📝 Testlar\"</b> va <b>\"🎥 Video darslar\"</b> "
        "ushbu sinfga mos holda chiqadi.",
        reply_markup=MAIN_KEYBOARD
    )


# ==========================================
# ERKIN SAVOLLAR (AI JAVOBI)
# ==========================================
KNOWN_BUTTONS = [
    "📖 Mavzular", "📝 Testlar", "🎥 Video darslar", "🧬 Animatsiyalar",
    "🏆 Reyting", "📊 Natijalar", "💳 Premium", "👨‍🏫 O'qituvchi",
    "🤖 AI Biologiya", "🔄 Sinfni almashtirish"
]

@dp.message(F.text & ~F.text.startswith("/") & ~F.text.in_(KNOWN_BUTTONS))
async def handle_user_free_text(message: Message):
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


# ==========================================
# VEB-SERVER VA RENDER KEEP-ALIVE
# ==========================================
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


async def self_ping_task():
    """Server uxillab qolmasligi uchun har 10 daqiqada o'ziga o'zi signal yuboradi"""
    await asyncio.sleep(60)
    url = "https://biologiya-bot-hf2u.onrender.com/health"
    while True:
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                    logging.info(f"Keep-alive signal yuborildi: status={resp.status}")
        except Exception as e:
            logging.debug(f"Keep-alive ogohlantirish: {e}")
        await asyncio.sleep(600)


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
        asyncio.create_task(self_ping_task())
    except Exception as e:
        logging.warning(f"Veb-serverni ishga tushirishda ogohlantirish: {e}")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi.")
