# -*- coding: utf-8 -*-
"""
10-sinf Yangi darslik: Yopiq testlar (Javob yozish) boshqaruv moduli.
O'quvchi A, B, C, D variantlarisiz nuqtalar o'rniga so'z, termin yoki son yozadi.
Bot avtomatik solishtiradi, o'quvchi o'z-o'zini baholashi uchun etalon javobni ko'rsatadi
va natijalarni umumiy ball/statistika bazasiga yozadi.
"""

import os
import html
import random
import logging
from typing import Dict, Any, Optional

from aiogram import Bot
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile
)

import database
from yopiq_tests_data import YOPIQ_TESTS_10

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Kategoriya xaritasi
CATEGORIES_MAP: Dict[str, Dict[str, Any]] = {c["id"]: c for c in YOPIQ_TESTS_10}

# Faol sessiyalar: user_id -> Dict
active_yopiq_sessions: Dict[int, Dict[str, Any]] = {}


def build_yopiq_menu_keyboard() -> InlineKeyboardMarkup:
    """Yopiq testlar mavzulari ro'yxati inline klaviaturasi"""
    buttons = []
    
    icons = ["🌱", "🧪", "🔬", "🧬", "🌸", "🌿", "🔀", "💉", "🌍", "🦖"]
    for idx, c in enumerate(YOPIQ_TESTS_10):
        icon = icons[idx % len(icons)]
        btn_text = f"{icon} {c['short_title']} ({c['questions_count']} ta)"
        buttons.append([InlineKeyboardButton(text=btn_text, callback_data=f"ytest_start_{c['id']}")])
        
    # Tasodifiy aralash test
    buttons.append([
        InlineKeyboardButton(text="🎲 10-sinf Aralash Yopiq Test (15 ta)", callback_data="ytest_start_mixed_15")
    ])
    buttons.append([
        InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="ytest_close")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def send_yopiq_menu(message: Message):
    """Yopiq testlar bosh menyusini yuborish"""
    text = (
        "✍️ <b>10-SINF YANGI DARSLIK: YOPIQ TESTLAR (JAVOB YOZISH)</b>\n\n"
        "Ushbu bo'limda tayyor A, B, C, D javob variantlari berilmaydi.\n"
        "Savollardagi nuqtalar o'rniga mos <b>so'z, termin, son yoki biologik tushunchani</b> "
        "chatga yozib jo'natasiz!\n\n"
        "💡 <i>Bot javobingizni avtomatik tekshiradi, etalon javobni ko'rsatadi va ballaringizni hisoblab boradi.</i>\n\n"
        "👇 <b>Ishlamoqchi bo'lgan mavzuingizni tanlang:</b>"
    )
    kb = build_yopiq_menu_keyboard()
    await message.answer(text, reply_markup=kb)


async def start_yopiq_session(bot: Bot, chat_id: int, user_id: int, cat_id: str):
    """Yangi yopiq test sessiyasini boshlash"""
    logging.info(f"Ytest: starting session for user {user_id}, cat {cat_id}")
    if cat_id == "mixed_15":
        all_qs = []
        for c in YOPIQ_TESTS_10:
            for q in c["questions"]:
                q_copy = dict(q)
                q_copy["cat_title"] = c["short_title"]
                all_qs.append(q_copy)
        random.shuffle(all_qs)
        selected_qs = all_qs[:15]
        cat_title = "10-sinf Aralash Yopiq Test"
        short_title = "Aralash test"
    else:
        cat = CATEGORIES_MAP.get(cat_id)
        if not cat:
            logging.error(f"Ytest: category {cat_id} not found!")
            return
        selected_qs = list(cat["questions"])
        cat_title = cat["title"]
        short_title = cat["short_title"]

    active_yopiq_sessions[user_id] = {
        "cat_id": cat_id,
        "cat_title": cat_title,
        "short_title": short_title,
        "questions": selected_qs,
        "index": 0,
        "score": 0,
        "total": len(selected_qs),
        "status": "waiting_answer",
        "last_answer_status": None
    }

    await send_yopiq_question(bot, chat_id, user_id)


async def send_yopiq_question(bot: Bot, chat_id: int, user_id: int):
    """Joriy savolni foydalanuvchiga yuborish"""
    session = active_yopiq_sessions.get(user_id)
    if not session:
        return

    idx = session["index"]
    total = session["total"]
    if idx >= total:
        await finish_yopiq_session(bot, chat_id, user_id)
        return

    q = session["questions"][idx]
    session["status"] = "waiting_answer"

    q_title = q.get("cat_title", session["short_title"])
    question_text = (
        f"✍️ <b>10-sinf Yopiq test | {q_title}</b>\n"
        f"🔢 <b>Savol {idx + 1} / {total}:</b>\n\n"
        f"{q['question']}\n\n"
        "💬 <i>Javobingizni chatga yozib jo'nating:</i>"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💡 Javobni ko'rish", callback_data="ytest_reveal")],
        [InlineKeyboardButton(text="⏭ O'tkazib yuborish", callback_data="ytest_skip"),
         InlineKeyboardButton(text="🛑 Testni to'xtatish", callback_data="ytest_quit")]
    ])

    img_rel = q.get("image")
    if img_rel:
        img_name = os.path.basename(img_rel)
        # Qidirish yo'llari:
        # 1. images_yopiq_10 papkasi ichida
        # 2. botning asosiy (root) katalogida (agar fayllar papkasiz yuklangan bo'lsa)
        # 3. img_rel ning o'zi
        candidates = [
            os.path.join(BASE_DIR, "images_yopiq_10", img_name),
            os.path.join(BASE_DIR, img_name),
            os.path.join(BASE_DIR, img_rel),
            img_rel
        ]

        found_path = None
        for p in candidates:
            if os.path.exists(p) and os.path.getsize(p) > 0:
                found_path = p
                break

        photo_sent = False
        # 1-usul: Diskdagi mahalliy fayldan jo'natish
        if found_path:
            try:
                photo = FSInputFile(found_path)
                await bot.send_photo(chat_id=chat_id, photo=photo, caption=question_text, reply_markup=kb)
                photo_sent = True
            except Exception as e:
                logging.warning(f"send_photo with FSInputFile ({found_path}) failed: {e}")

        # 2-usul (Zaxira): Agar serverda fayl topilmasa, to'g'ridan-to'g'ri GitHub URL orqali jo'natish
        if not photo_sent:
            github_url = f"https://raw.githubusercontent.com/aliyevmurod9495-star/biologiya-bot/main/{img_name}"
            try:
                await bot.send_photo(chat_id=chat_id, photo=github_url, caption=question_text, reply_markup=kb)
                photo_sent = True
            except Exception as e:
                logging.warning(f"send_photo with GitHub URL failed: {e}")

        if photo_sent:
            return

    await bot.send_message(chat_id=chat_id, text=question_text, reply_markup=kb)


async def process_yopiq_answer(bot: Bot, message: Message) -> bool:
    """Foydalanuvchi yozgan javobni qabul qilish va tekshirish"""
    user_id = message.from_user.id
    session = active_yopiq_sessions.get(user_id)
    if not session:
        return False

    if session.get("status") != "waiting_answer":
        return False

    idx = session["index"]
    q = session["questions"][idx]
    user_text = message.text.strip()
    user_clean = user_text.lower()

    ref_clean = q.get("clean_answer", "").strip().lower()
    keywords = q.get("keywords", [])

    is_correct = False
    if len(user_clean) >= 2 and (user_clean in ref_clean or ref_clean in user_clean):
        is_correct = True
    elif keywords:
        match_count = sum(1 for kw in keywords if kw in user_clean)
        if match_count >= max(1, len(keywords) // 2):
            is_correct = True

    session["status"] = "feedback_shown"

    if is_correct:
        session["score"] += 1
        feedback = (
            f"✅ <b>BARAKALLA! JAVOBINGIZ TO'G'RI (+1 ball)</b>\n\n"
            f"👤 <b>Sizning javobingiz:</b> <i>{html.escape(user_text)}</i>\n\n"
            f"📖 <b>Etalon javob:</b>\n"
            f"<code>{html.escape(q['clean_answer'])}</code>\n\n"
            f"📊 <b>Joriy ball:</b> {session['score']} / {idx + 1}"
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Keyingi savol", callback_data="ytest_next")]
        ])
    else:
        feedback = (
            f"❌ <b>NOTO'G'RI YOKI TO'LIQ EMAS!</b>\n\n"
            f"👤 <b>Sizning javobingiz:</b> <i>{html.escape(user_text)}</i>\n\n"
            f"📖 <b>To'g'ri (etalon) javob:</b>\n"
            f"<code>{html.escape(q['clean_answer'])}</code>\n\n"
            "💡 <i>Agar javobingiz ma'nodosh yoki to'g'ri bo'lsa-yu, bot qabul qilmagan bo'lsa, "
            "pastdagi tugma orqali ballni hisobga olishingiz mumkin:</i>"
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Menda ham to'g'ri edi (+1 ball)", callback_data="ytest_override")],
            [InlineKeyboardButton(text="➡️ Keyingi savol", callback_data="ytest_next")]
        ])

    await message.answer(feedback, reply_markup=kb)
    return True


async def handle_yopiq_callback(bot: Bot, callback: CallbackQuery):
    """Yopiq test inline tugmalari bilan ishlash"""
    data = callback.data
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id if callback.message else user_id

    try:
        await callback.answer()
    except Exception as e:
        logging.debug(f"callback.answer error: {e}")

    if data.startswith("ytest_start_"):
        cat_id = data.replace("ytest_start_", "")
        try:
            if callback.message:
                await callback.message.delete()
        except Exception:
            pass
        await start_yopiq_session(bot, chat_id, user_id, cat_id)

    elif data == "ytest_reveal":
        session = active_yopiq_sessions.get(user_id)
        if not session:
            await callback.message.answer("Sessiya tugagan.")
            return
        idx = session["index"]
        q = session["questions"][idx]
        session["status"] = "feedback_shown"

        text = (
            f"💡 <b>SAVOLNING TO'G'RI JAVOBI:</b>\n\n"
            f"📖 <code>{html.escape(q['clean_answer'])}</code>\n\n"
            f"O'rganib olgan bo'lsangiz, keyingi savolga o'ting:"
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Keyingi savol", callback_data="ytest_next")]
        ])
        await callback.message.answer(text, reply_markup=kb)

    elif data == "ytest_skip":
        session = active_yopiq_sessions.get(user_id)
        if session:
            session["index"] += 1
            await send_yopiq_question(bot, chat_id, user_id)

    elif data == "ytest_override":
        session = active_yopiq_sessions.get(user_id)
        if session:
            session["score"] += 1
            session["index"] += 1
            try:
                if callback.message:
                    await callback.message.edit_text(
                        f"✅ <b>Javobingiz to'g'ri deb qabul qilindi (+1 ball)!</b>\n\n"
                        f"📊 <b>Ball:</b> {session['score']} / {session['index']}",
                        reply_markup=None
                    )
            except Exception:
                pass
            await send_yopiq_question(bot, chat_id, user_id)

    elif data == "ytest_next":
        session = active_yopiq_sessions.get(user_id)
        if session:
            session["index"] += 1
            await send_yopiq_question(bot, chat_id, user_id)

    elif data == "ytest_quit":
        await finish_yopiq_session(bot, chat_id, user_id)

    elif data == "ytest_menu":
        await send_yopiq_menu(callback.message)

    elif data == "ytest_close":
        try:
            if callback.message:
                await callback.message.delete()
        except Exception:
            pass


async def finish_yopiq_session(bot: Bot, chat_id: int, user_id: int):
    """Yopiq testni yakunlash va natijani saqlash"""
    session = active_yopiq_sessions.pop(user_id, None)
    if not session:
        return

    score = session["score"]
    total = session["total"]
    percent = round((score / total) * 100, 1) if total > 0 else 0

    if percent >= 90:
        badge = "⭐️⭐️⭐️⭐️⭐️ A'LO NATIJA!"
        praise = "Mavzuni mukammal darajada o'zlashtiribsiz! Qoyilmaqom bilim!"
    elif percent >= 70:
        badge = "⭐️⭐️⭐️⭐️ YAXSHI NATIJA!"
        praise = "Juda yaxshi! Xatolarni ko'rib chiqsangiz yanada zo'r bo'ladi."
    elif percent >= 50:
        badge = "⭐️⭐️⭐️ QONIQARLI!"
        praise = "Mavzuni yana bir bor takrorlashni tavsiya qilamiz."
    else:
        badge = "⭐️ KO'PROQ O'QISH TAVSIYA ETILADI"
        praise = "Konspektlar va darslikni yaxshilab o'qib, qayta urinib ko'ring."

    try:
        await database.record_test_result(
            user_id=user_id,
            grade="10new",
            score=score,
            total=total,
            topic_title=f"Yopiq: {session['short_title']}"
        )
    except Exception as e:
        logging.warning(f"record_test_result error: {e}")

    result_text = (
        f"🏆 <b>YOPIQ TEST YAKUNLANDI!</b>\n\n"
        f"📚 <b>Mavzu:</b> {session['cat_title']}\n"
        f"🎖 <b>Baholash:</b> {badge}\n\n"
        f"📊 <b>Natijangiz:</b>\n"
        f"• Jami savollar: <b>{total} ta</b>\n"
        f"• To'g'ri javoblar: <b>{score} ta</b>\n"
        f"• Noto'g'ri/O'tkazilgan: <b>{total - score} ta</b>\n"
        f"• O'zlashtirish darajasi: <b>{percent}%</b>\n\n"
        f"💬 <i>{praise}</i>"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Qayta ishlash", callback_data=f"ytest_start_{session['cat_id']}")],
        [InlineKeyboardButton(text="📚 Boshqa mavzular", callback_data="ytest_menu")]
    ])

    await bot.send_message(chat_id=chat_id, text=result_text, reply_markup=kb)
