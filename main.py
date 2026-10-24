import os
import json
import logging
import asyncio
import random
from typing import Dict, Any, Optional, Callable, Awaitable

from aiogram import Bot, Dispatcher, F, BaseMiddleware
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
    InputPollOption,
    TelegramObject,
    FSInputFile
)

import config
import database
import materials
import problems

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispetcher obyektlari
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()



class AuthMiddleware(BaseMiddleware):
    """Foydalanuvchilarning admin tomonidan tasdiqlanganligini tekshirish middleware"""
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        # 1. Admin har doim barcha huquqlarga ega
        if user.id in config.ADMIN_IDS or await database.is_admin(user.id):
            return await handler(event, data)

        # 2. Agar callback adminlar tomonidan bosilayotgan auth_ yoki check_sub_ tugmasi bo'lsa
        if isinstance(event, CallbackQuery) and event.data and (event.data.startswith("auth_") or event.data.startswith("check_sub_")):
            return await handler(event, data)

        # 3. Foydalanuvchiga ruxsat berilganligini va obuna holatini tekshirish
        sub_info = await database.get_user_subscription_info(user.id)
        if sub_info["is_active"]:
            return await handler(event, data)

        # 4. Agar foydalanuvchining 1 oylik obuna muddati tugagan bo'lsa
        if sub_info["is_expired"]:
            if isinstance(event, Message):
                expired_msg = (
                    "⏳ <b>Sizning 1 oylik foydalanish muddatingiz tugadi!</b>\n\n"
                    f"📅 <b>Yakunlangan sana:</b> <code>{sub_info['formatted_date']}</code>\n\n"
                    "Botdagi barcha sinflar (5-11) bo'yicha mavzulashtirilgan testlar, konspektlar, "
                    "video darslar va AI yordamchisidan foydalanishni davom ettirish uchun "
                    "iltimos, <b>administratorga murojaat qiling</b> va obunangizni uzaytiring.\n\n"
                    "👨‍🏫 <b>Administrator:</b> @Murod_Aliyev_9495"
                )
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="✍️ Adminga bog'lanish", url="https://t.me/Murod_Aliyev_9495")],
                    [InlineKeyboardButton(text="🔄 Qayta tekshirish", callback_data=f"check_sub_{user.id}")]
                ])
                await event.answer(expired_msg, reply_markup=kb)
                return
            elif isinstance(event, CallbackQuery):
                await event.answer(
                    "⏳ Sizning 1 oylik foydalanish muddatingiz tugagan!\nUzaytirish uchun adminga murojaat qiling.",
                    show_alert=True
                )
                return

        # 5. Agar hali ruxsat berilmagan bo'lsa
        if isinstance(event, Message):
            if event.text and event.text.startswith("/start"):
                # Ro'yxatga olish (kutilmoqda holatida)
                await database.add_or_update_user(
                    user_id=user.id,
                    full_name=user.full_name or "Noma'lum",
                    username=user.username or "",
                    default_allowed=0
                )

                # Foydalanuvchiga bildirishnoma
                waiting_msg = (
                    f"🔒 <b>Assalomu alaykum, {user.first_name}!</b>\n\n"
                    "Ushbu biologiya ta'lim boti yopiq tizim hisoblanadi.\n"
                    "Botdan to‘liq foydalanish uchun <b>administrator ruxsati</b> talab qilinadi.\n\n"
                    "⏳ <i>Sizning so‘rovingiz adminga yuborildi. Administrator tasdiqlagach, bot to‘liq ochiladi va sizga xabar beriladi.</i>"
                )
                await event.answer(waiting_msg)

                # Adminga ruxsat so'rovi yuborish (1 oy / cheksiz / rad)
                admin_kb = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(text="✅ 1 oylik ruxsat (30 kun)", callback_data=f"auth_app30_{user.id}")
                    ],
                    [
                        InlineKeyboardButton(text="♾ Cheksiz ruxsat", callback_data=f"auth_applife_{user.id}"),
                        InlineKeyboardButton(text="❌ Rad etish", callback_data=f"auth_reject_{user.id}")
                    ]
                ])
                admin_text = (
                    "🔔 <b>Yangi foydalanuvchi ruxsat so'ramoqda!</b>\n\n"
                    f"👤 <b>F.I.SH:</b> {user.full_name}\n"
                    f"🆔 <b>Telegram ID:</b> <code>{user.id}</code>\n"
                    f"🔗 <b>Username:</b> @{user.username or 'yo‘q'}\n\n"
                    "Ushbu foydalanuvchiga botdan foydalanishga ruxsat berasizmi?"
                )
                for admin_id in await database.get_all_admins():
                    try:
                        await bot.send_message(admin_id, admin_text, reply_markup=admin_kb)
                    except Exception as e:
                        logging.warning(f"Adminga so'rov yuborishda xatolik ({admin_id}): {e}")
                return

            else:
                await event.answer(
                    "🔒 <b>Botdan foydalanish cheklangan!</b>\n\n"
                    "Sizga hali administrator tomonidan ruxsat berilmagan.\n"
                    "Iltimos, administrator tasdiqlashini kuting."
                )
                return

        elif isinstance(event, CallbackQuery):
            await event.answer("🔒 Botdan foydalanish uchun administrator ruxsati kerak!", show_alert=True)
            return

        return None


dp.message.middleware(AuthMiddleware())
dp.callback_query.middleware(AuthMiddleware())


# Savollarni yuklash (BOM bilan ham, BOM siz ham xatosiz yuklash)
try:
    with open("questions.json", "r", encoding="utf-8-sig") as f:
        QUESTIONS_DATA: Dict[str, Any] = json.load(f)
except Exception as e:
    logging.error(f"questions.json yuklashda xatolik: {e}")
    QUESTIONS_DATA: Dict[str, Any] = {}

# O'quvchilarning faol test sessiyalarini saqlash
active_sessions: Dict[int, Dict[str, Any]] = {}
poll_to_user: Dict[str, int] = {}

# Asosiy menyu klaviaturasi (Aynan rasmdagidek va yangi bo'limlar bilan)
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Mavzular"), KeyboardButton(text="📝 Testlar")],
        [KeyboardButton(text="📅 Haftalik Test"), KeyboardButton(text="📐 Masalalar")],
        [KeyboardButton(text="🎥 Video darslar"), KeyboardButton(text="🧬 Animatsiyalar")],
        [KeyboardButton(text="🏆 Reyting"), KeyboardButton(text="📊 Natijalar")],
        [KeyboardButton(text="🤖 AI Biologiya"), KeyboardButton(text="👨‍🏫 O'qituvchi")],
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
    "11": "🌍 11-sinf (Ekologiya va filogenez)"
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
        [InlineKeyboardButton(text="🌍 11-sinf (Ekologiya va filogenez)", callback_data="setgrade_11")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(CommandStart())
async def handle_start(message: Message):
    """Start komandasi berilganda"""
    user = message.from_user
    is_adm = await database.is_admin(user.id) or user.id in config.ADMIN_IDS
    await database.add_or_update_user(
        user_id=user.id,
        full_name=user.full_name or "Noma'lum",
        username=user.username or "",
        default_allowed=1 if is_adm else 0
    )
    grade = await database.get_user_grade(user.id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    admin_note = "👑 <b>Siz administratorsiz</b> <i>(Boshqaruv paneli: /admin)</i>\n\n" if is_adm else ""

    welcome_text = (
        f"Assalomu alaykum, <b>{user.first_name}</b>!\n\n"
        f"{admin_note}"
        "🧬 <b>Biologiya ta'lim va test botiga xush kelibsiz!</b>\n\n"
        f"📌 Joriy faol sinf: <b>{grade_name}</b>\n\n"
        "Quyidagi menyudan kerakli bo'limni tanlang:\n"
        "• 📖 <b>Mavzular</b> — Darslik ma'ruzalari va konspektlar\n"
        "• 📝 <b>Testlar</b> — Mavzulashtirilgan viktorina testlari\n"
        "• 📅 <b>Haftalik Test</b> — O'zlashtirish darajasini aniqlovchi nazorat\n"
        "• 📐 <b>Masalalar</b> — DNK, oqsil, ATF va genetika masalalari\n"
        "• 🎥 <b>Video darslar</b> — Mavzuga oid videoroliklar\n"
        "• 🧬 <b>Animatsiyalar</b> — 3D biologik animatsiyalar\n"
        "• 📊 <b>Natijalar</b> — Sizning o'zlashtirish ko'rsatkichingiz\n"
        "• 🏆 <b>Reyting</b> — Eng iqtidorli o'quvchilar ro'yxati\n"
        "• 🤖 <b>AI Biologiya</b> — Darslik asosidagi Sun'iy Intellekt\n"
        "• 👨‍🏫 <b>O'qituvchi</b> — Ustoz bilan bog'lanish"
    )
    await message.answer(welcome_text, reply_markup=MAIN_KEYBOARD)



# ==========================================
# ADMINISTRATOR BOSHQARUVI VA RUXSAT BERISH TIZIMI
# ==========================================

@dp.callback_query(F.data.startswith("auth_app30_"))
@dp.callback_query(F.data.startswith("auth_approve_"))
async def handle_auth_app30(callback: CallbackQuery):
    """Adminga foydalanuvchiga 1 oylik (30 kun) ruxsat berish tugmasi"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        await callback.answer("Faqat adminlar uchun!", show_alert=True)
        return

    parts = callback.data.split("_")
    target_user_id = int(parts[-1])
    end_dt = await database.set_user_subscription(target_user_id, days=30)
    formatted = end_dt.strftime("%d.%m.%Y") if end_dt else "30 kun"

    await callback.message.edit_text(
        f"{callback.message.html_text}\n\n"
        f"✅ <b>1 oylik (30 kun) ruxsat berildi!</b>\n"
        f"📅 <b>Amal qilish muddati:</b> <code>{formatted}</code> gacha\n"
        f"👮 Tasdiqlagan admin: <b>{callback.from_user.first_name}</b>"
    )
    await callback.answer("✅ Foydalanuvchiga 1 oylik ruxsat berildi!")

    try:
        grade = await database.get_user_grade(target_user_id)
        grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")
        welcome_approved = (
            "🎉 <b>Tabriklaymiz! Administrator sizga botdan 1 oy (30 kun) foydalanish uchun ruxsat berdi!</b>\n\n"
            f"📅 <b>Obuna muddati:</b> <code>{formatted}</code> gacha\n"
            f"📌 Joriy faol sinf: <b>{grade_name}</b>\n\n"
            "Quyidagi menyudan kerakli bo'limni tanlab darslik va testlarni boshlashingiz mumkin:"
        )
        await bot.send_message(target_user_id, welcome_approved, reply_markup=MAIN_KEYBOARD)
    except Exception as e:
        logging.warning(f"Foydalanuvchiga tasdiq xabari bormadi ({target_user_id}): {e}")


@dp.callback_query(F.data.startswith("auth_applife_"))
async def handle_auth_applife(callback: CallbackQuery):
    """Adminga foydalanuvchiga cheksiz ruxsat berish tugmasi"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        await callback.answer("Faqat adminlar uchun!", show_alert=True)
        return

    target_user_id = int(callback.data.split("_")[2])
    await database.set_user_subscription(target_user_id, days=0)

    await callback.message.edit_text(
        f"{callback.message.html_text}\n\n"
        f"♾ <b>Cheksiz ruxsat berildi!</b>\n"
        f"👮 Tasdiqlagan admin: <b>{callback.from_user.first_name}</b>"
    )
    await callback.answer("♾ Cheksiz ruxsat berildi!")

    try:
        grade = await database.get_user_grade(target_user_id)
        grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")
        welcome_approved = (
            "🎉 <b>Tabriklaymiz! Administrator sizga botdan foydalanish uchun cheksiz ruxsat berdi!</b>\n\n"
            f"📌 Joriy faol sinf: <b>{grade_name}</b>\n\n"
            "Quyidagi menyudan kerakli bo'limni tanlab darslik va testlarni boshlashingiz mumkin:"
        )
        await bot.send_message(target_user_id, welcome_approved, reply_markup=MAIN_KEYBOARD)
    except Exception as e:
        logging.warning(f"Foydalanuvchiga tasdiq xabari bormadi ({target_user_id}): {e}")


@dp.callback_query(F.data.startswith("auth_ext30_"))
async def handle_auth_ext30(callback: CallbackQuery):
    """Adminga foydalanuvchi obunasini 1 oyga uzaytirish tugmasi"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        await callback.answer("Faqat adminlar uchun!", show_alert=True)
        return

    target_user_id = int(callback.data.split("_")[2])
    new_end = await database.set_user_subscription(target_user_id, days=30)
    formatted = new_end.strftime("%d.%m.%Y") if new_end else "30 kun"

    await callback.answer(f"✅ Obuna +1 oyga uzaytirildi ({formatted} gacha)!", show_alert=True)

    try:
        await bot.send_message(
            target_user_id,
            f"🎉 <b>Hurmatli o'quvchi! Administrator sizning obunangizni yana 1 oyga uzaytirdi!</b>\n\n"
            f"📅 <b>Yangi amal qilish muddati:</b> <code>{formatted}</code> gacha.\n\n"
            "Botdan bemalol foydalanishda davom etishingiz mumkin!",
            reply_markup=MAIN_KEYBOARD
        )
    except Exception as e:
        logging.warning(f"Foydalanuvchiga uzaytirish xabari bormadi ({target_user_id}): {e}")


@dp.callback_query(F.data.startswith("check_sub_"))
async def handle_check_sub(callback: CallbackQuery):
    """Foydalanuvchi o'z obunasi holatini qayta tekshirish tugmasi"""
    user_id = callback.from_user.id
    sub_info = await database.get_user_subscription_info(user_id)
    if sub_info["is_active"]:
        await callback.answer("🎉 Sizning obunangiz faol! Xush kelibsiz!", show_alert=True)
        try:
            await callback.message.delete()
        except Exception:
            pass
        await callback.message.answer(
            f"🎉 <b>Obunangiz faol holatda!</b>\n📅 Amal qilish muddati: <b>{sub_info['formatted_date']}</b> gacha.",
            reply_markup=MAIN_KEYBOARD
        )
    else:
        await callback.answer("⏳ Obuna muddati hali uzaytirilmadi. Iltimos, adminga murojaat qiling.", show_alert=True)


@dp.callback_query(F.data.startswith("auth_reject_"))
async def handle_auth_reject(callback: CallbackQuery):
    """Adminga foydalanuvchi so'rovini rad etish tugmasi"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        await callback.answer("Faqat adminlar uchun!", show_alert=True)
        return

    target_user_id = int(callback.data.split("_")[2])
    await database.set_user_allowed(target_user_id, 0)

    await callback.message.edit_text(
        f"{callback.message.html_text}\n\n"
        f"❌ <b>Rad etildi!</b>\n"
        f"👮 Rad qilgan admin: <b>{callback.from_user.first_name}</b>"
    )
    await callback.answer("❌ So'rov rad etildi.")

    try:
        await bot.send_message(
            target_user_id,
            "❌ <b>Afsuski, administrator sizning botdan foydalanish so'rovingizni rad etdi.</b>"
        )
    except Exception:
        pass


@dp.message(Command("admin", "panel"))
async def handle_admin_panel(message: Message):
    """Admin boshqaruv paneli"""
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        await message.answer("⚠️ Bu buyruq faqat bot administratorlari uchun!")
        return

    counts = await database.get_user_counts()
    admin_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f"🟢 Faol obuna ({counts['allowed']})", callback_data="admin_list_allowed"),
            InlineKeyboardButton(text=f"🔴 Tugaganlar ({counts.get('expired', 0)})", callback_data="admin_list_expired")
        ],
        [
            InlineKeyboardButton(text=f"⏳ Kutilayotganlar ({counts['pending']})", callback_data="admin_list_pending"),
            InlineKeyboardButton(text="📑 O'quvchilar hisoboti", callback_data="admin_students_report")
        ],
        [
            InlineKeyboardButton(text="❓ AI savollari tarixi", callback_data="admin_ai_questions_history"),
            InlineKeyboardButton(text=f"👑 Adminlar ({counts['admins']})", callback_data="admin_list_admins")
        ],
        [
            InlineKeyboardButton(text="🔄 Yangilash", callback_data="admin_refresh")
        ]
    ])

    panel_text = (
        "👮 <b>ADMINISTRATOR BOSHQARUV PANELI</b>\n\n"
        f"👥 <b>Jami foydalanuvchilar:</b> {counts['total']} ta\n"
        f"🟢 <b>Faol obunachilar:</b> {counts['allowed']} ta\n"
        f"🔴 <b>Muddati tugaganlar:</b> {counts.get('expired', 0)} ta\n"
        f"⏳ <b>Tasdiq kutayotganlar:</b> {counts['pending']} ta\n"
        f"👑 <b>Adminlar:</b> {counts['admins']} ta\n\n"
        "<b>Boshqaruv buyruqlari:</b>\n"
        "• <code>/allow &lt;ID&gt; [kun]</code> — Foydalanuvchiga obuna berish (sukut bo'yicha 30 kun)\n"
        "• <code>/extend &lt;ID&gt; [kun]</code> — Foydalanuvchi obunasini uzaytirish (sukut bo'yicha +30 kun)\n"
        "• <code>/block &lt;ID&gt;</code> — Foydalanuvchini bloklash (ruxsatini bekor qilish)\n"
        "• <code>/report</code> — O'quvchilarning umumiy o'zlashtirish hisoboti\n"
        "• <code>/report &lt;ID&gt;</code> — Muayyan o'quvchi bo'yicha batafsil hisobot\n"
        "• <code>/questions</code> — O'quvchilar AI ga bergan oxirgi savollar\n"
        "• <code>/add_admin &lt;ID&gt;</code> — Yangi admin qo'shish\n"
        "• <code>/admins</code> — Barcha adminlar ro'yxati"
    )
    await message.answer(panel_text, reply_markup=admin_kb)


@dp.callback_query(F.data == "admin_refresh")
async def handle_admin_refresh(callback: CallbackQuery):
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    counts = await database.get_user_counts()
    admin_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f"🟢 Faol obuna ({counts['allowed']})", callback_data="admin_list_allowed"),
            InlineKeyboardButton(text=f"🔴 Tugaganlar ({counts.get('expired', 0)})", callback_data="admin_list_expired")
        ],
        [
            InlineKeyboardButton(text=f"⏳ Kutilayotganlar ({counts['pending']})", callback_data="admin_list_pending"),
            InlineKeyboardButton(text="📑 O'quvchilar hisoboti", callback_data="admin_students_report")
        ],
        [
            InlineKeyboardButton(text="❓ AI savollari tarixi", callback_data="admin_ai_questions_history"),
            InlineKeyboardButton(text=f"👑 Adminlar ({counts['admins']})", callback_data="admin_list_admins")
        ],
        [
            InlineKeyboardButton(text="🔄 Yangilash", callback_data="admin_refresh")
        ]
    ])
    panel_text = (
        "👮 <b>ADMINISTRATOR BOSHQARUV PANELI</b>\n\n"
        f"👥 <b>Jami foydalanuvchilar:</b> {counts['total']} ta\n"
        f"🟢 <b>Faol obunachilar:</b> {counts['allowed']} ta\n"
        f"🔴 <b>Muddati tugaganlar:</b> {counts.get('expired', 0)} ta\n"
        f"⏳ <b>Tasdiq kutayotganlar:</b> {counts['pending']} ta\n"
        f"👑 <b>Adminlar:</b> {counts['admins']} ta\n\n"
        "<b>Boshqaruv buyruqlari:</b>\n"
        "• <code>/allow &lt;ID&gt; [kun]</code> — Foydalanuvchiga obuna berish (sukut bo'yicha 30 kun)\n"
        "• <code>/extend &lt;ID&gt; [kun]</code> — Foydalanuvchi obunasini uzaytirish (sukut bo'yicha +30 kun)\n"
        "• <code>/block &lt;ID&gt;</code> — Foydalanuvchini bloklash\n"
        "• <code>/report</code> — O'quvchilarning umumiy o'zlashtirish hisoboti\n"
        "• <code>/report &lt;ID&gt;</code> — Muayyan o'quvchi bo'yicha batafsil hisobot\n"
        "• <code>/questions</code> — O'quvchilar AI ga bergan oxirgi savollar\n"
        "• <code>/add_admin &lt;ID&gt;</code> — Yangi admin qo'shish\n"
        "• <code>/admins</code> — Barcha adminlar ro'yxati"
    )
    try:
        await callback.message.edit_text(panel_text, reply_markup=admin_kb)
        await callback.answer("Yangilandi!")
    except Exception:
        await callback.answer()


@dp.callback_query(F.data == "admin_students_report")
async def handle_admin_students_report(callback: CallbackQuery):
    """Admin uchun o'quvchilar ro'yxati va ularning o'zlashtirish ko'rsatkichlari"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    await callback.answer()
    summary = await database.get_all_students_mastery_summary()
    if not summary:
        await callback.message.edit_text(
            "📊 <b>Hozircha o'quvchilar mavjud emas yoki faoliyat boshlanmagan.</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")]])
        )
        return

    text = f"📑 <b>O'QUVCHILARNING O'ZLASHTIRISH VA SAVOLLAR HISOBOTI:</b>\n<i>(Jami o'quvchilar: {len(summary)} nafar)</i>\n\n"
    buttons = []
    for s in summary[:10]:
        u_name = s['full_name']
        u_id = s['user_id']
        u_pct = s['overall_mastery']
        badge_short = s['mastery_badge'].split()[0]
        text += f"• <b>{u_name}</b> (<code>{u_id}</code>): <b>{u_pct}%</b> {badge_short}\n"
        buttons.append([InlineKeyboardButton(text=f"🔍 {u_name[:18]} batafsil", callback_data=f"admin_std_rep_{u_id}")])

    buttons.append([InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("admin_std_rep_"))
async def handle_admin_std_rep_detail(callback: CallbackQuery):
    """Bitta o'quvchi bo'yicha to'liq pedagogik tahlil"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    await callback.answer()
    target_id = int(callback.data.replace("admin_std_rep_", ""))
    report = await database.get_student_comprehensive_report(target_id)
    if not report:
        await callback.answer("O'quvchi topilmadi!", show_alert=True)
        return

    text = (
        f"📑 <b>O'QUVCHINING SHAXSIY PEDAGOGIK HISOBOTI</b>\n\n"
        f"👤 <b>F.I.SH:</b> {report['full_name']} (@{report['username'] or 'yo‘q'})\n"
        f"🆔 <b>Telegram ID:</b> <code>{report['user_id']}</code>\n"
        f"📚 <b>Faol sinfi:</b> {report['current_grade']}-sinf\n"
        f"🏆 <b>O'ZLASHTIRISH DARAJASI:</b>\n"
        f"<b>{report['mastery_badge']} ({report['overall_mastery']}%)</b>\n\n"
        f"📝 <b>Mavzuviy testlar:</b> {report['test_correct']}/{report['test_total']} ta ({report['test_percent']}%)\n"
    )
    if report['last_weekly']:
        lw = report['last_weekly']
        text += f"📅 <b>Oxirgi haftalik nazorat:</b> {lw['score']}/{lw['total']} ({lw['mastery_percent']}%) — {lw['status']}\n"
    else:
        text += "📅 <b>Haftalik nazorat:</b> <i>Hali topshirilmagan</i>\n"

    ps = report['problem_stats']
    text += f"📐 <b>Ishlangan masalalar:</b> {ps['correct']}/{ps['total']} ta to'g'ri ({ps['percent']}%)\n\n"

    if report['ai_questions']:
        text += "❓ <b>O'quvchi AI ga bergan oxirgi savollari:</b>\n"
        for q in report['ai_questions'][:5]:
            text += f"• <i>«{q['question'][:75]}»</i>\n"
    else:
        text += "❓ <i>O'quvchi hali AI ga savol bermagan.</i>\n"

    buttons = [
        [InlineKeyboardButton(text="◀️ Ro'yxatga qaytish", callback_data="admin_students_report")],
        [InlineKeyboardButton(text="🏠 Admin panel", callback_data="admin_refresh")]
    ]
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data == "admin_ai_questions_history")
async def handle_admin_ai_questions_history(callback: CallbackQuery):
    """O'quvchilar AI ga bergan savollar tarixi"""
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    await callback.answer()
    questions = await database.get_all_recent_ai_questions(limit=12)
    if not questions:
        await callback.message.edit_text(
            "❓ <b>Hozircha o'quvchilar tomonidan AI ga savol berilmagan.</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")]])
        )
        return

    text = "❓ <b>O'QUVCHILARNING AI GA BERGAN OXIRGI SAVOLLARI:</b>\n\n"
    for q in questions:
        text += f"👤 <b>{q['full_name']}</b> ({q['grade']}-sinf):\n<i>«{q['question'][:90]}»</i>\n\n"

    buttons = [[InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")]]
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.message(Command("report"))
async def handle_cmd_report(message: Message):
    """Admin uchun /report komandasi"""
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return

    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        target_id = int(args[1])
        report = await database.get_student_comprehensive_report(target_id)
        if not report:
            await message.answer(f"⚠️ {target_id} raqamli o'quvchi topilmadi.")
            return

        text = (
            f"📑 <b>O'QUVCHINING SHAXSIY HISOBOTI</b>\n\n"
            f"👤 <b>F.I.SH:</b> {report['full_name']} (@{report['username'] or 'yo‘q'})\n"
            f"🆔 <b>ID:</b> <code>{report['user_id']}</code>\n"
            f"📚 <b>Sinf:</b> {report['current_grade']}-sinf\n"
            f"🏆 <b>O'ZLASHTIRISH DARAJASI:</b>\n"
            f"<b>{report['mastery_badge']} ({report['overall_mastery']}%)</b>\n\n"
            f"📝 <b>Testlar:</b> {report['test_correct']}/{report['test_total']} ta ({report['test_percent']}%)\n"
        )
        if report['last_weekly']:
            lw = report['last_weekly']
            text += f"📅 <b>Haftalik nazorat:</b> {lw['score']}/{lw['total']} ({lw['mastery_percent']}%) — {lw['status']}\n"
        ps = report['problem_stats']
        text += f"📐 <b>Masalalar:</b> {ps['correct']}/{ps['total']} ta ({ps['percent']}%)\n\n"

        if report['ai_questions']:
            text += "❓ <b>AI ga bergan oxirgi savollari:</b>\n"
            for q in report['ai_questions'][:5]:
                text += f"• <i>«{q['question'][:70]}»</i>\n"
        await message.answer(text)
        return

    summary = await database.get_all_students_mastery_summary()
    if not summary:
        await message.answer("📊 Hozircha tasdiqlangan o'quvchilar mavjud emas.")
        return

    text = f"📑 <b>O'QUVCHILAR O'ZLASHTIRISH HISOBOTI:</b>\n<i>(Jami: {len(summary)} nafar)</i>\n\n"
    for i, s in enumerate(summary[:12], 1):
        text += (
            f"<b>{i}. {s['full_name']}</b> (<code>{s['user_id']}</code>):\n"
            f"   • O'zlashtirish: <b>{s['overall_mastery']}%</b> {s['mastery_badge'].split()[0]}\n"
            f"   • Testlar: {s['test_correct']}/{s['test_total']} ta | Masalalar: {s['problem_stats']['correct']}/{s['problem_stats']['total']} ta\n"
        )
        if s['ai_questions']:
            text += f"   • Oxirgi savoli: <i>«{s['ai_questions'][0]['question'][:40]}...»</i>\n"
        text += "\n"

    text += "💡 <i>Bitta o'quvchi bo'yicha batafsil ko'rish uchun: <code>/report &lt;ID&gt;</code> buyrug'ini yuboring.</i>"
    await message.answer(text)


@dp.message(Command("questions"))
async def handle_cmd_questions(message: Message):
    """Admin uchun /questions komandasi"""
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    questions = await database.get_all_recent_ai_questions(limit=15)
    if not questions:
        await message.answer("❓ Hozircha o'quvchilar tomonidan AI ga savol berilmagan.")
        return

    text = "❓ <b>O'QUVCHILARNING AI GA BERGAN OXIRGI SAVOLLARI:</b>\n\n"
    for q in questions:
        text += f"👤 <b>{q['full_name']}</b> ({q['grade']}-sinf):\n<i>«{q['question'][:100]}»</i>\n\n"
    await message.answer(text)



@dp.callback_query(F.data == "admin_list_pending")
async def handle_admin_list_pending(callback: CallbackQuery):
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    pending = await database.get_users_list(is_allowed=0, filter_type="pending", limit=15)
    if not pending:
        await callback.answer("Kutilayotgan yangi so'rovlar yo'q!", show_alert=True)
        return

    text = "⏳ <b>Tasdiq kutayotgan foydalanuvchilar (oxirgi 15 ta):</b>\n\n"
    buttons = []
    for u in pending:
        u_name = u['full_name'] or 'Noma\'lum'
        u_id = u['user_id']
        u_handle = f"@{u['username']}" if u['username'] else "username yo'q"
        text += f"• <b>{u_name}</b> ({u_handle}) — <code>{u_id}</code>\n"
        buttons.append([
            InlineKeyboardButton(text=f"✅ {u_name[:12]} (1 oy)", callback_data=f"auth_app30_{u_id}"),
            InlineKeyboardButton(text="♾ Cheksiz", callback_data=f"auth_applife_{u_id}"),
            InlineKeyboardButton(text="❌ Rad", callback_data=f"auth_reject_{u_id}")
        ])

    buttons.append([InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data == "admin_list_allowed")
async def handle_admin_list_allowed(callback: CallbackQuery):
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    allowed = await database.get_users_list(is_allowed=1, filter_type="allowed", limit=15)
    if not allowed:
        await callback.answer("Hozircha faol obunachilar yo'q!", show_alert=True)
        return

    text = "🟢 <b>Faol obunachilar (oxirgi 15 ta):</b>\n\n"
    buttons = []
    for u in allowed:
        u_name = u['full_name'] or 'Noma\'lum'
        u_id = u['user_id']
        u_handle = f"@{u['username']}" if u['username'] else "username yo'q"
        u_sub = await database.get_user_subscription_info(u_id)
        if u_sub['is_lifetime']:
            sub_lbl = "♾ Cheksiz"
        else:
            sub_lbl = f"📅 {u_sub['formatted_date'][:10]} ({u_sub['days_left']} kun qoldi)"
        text += f"• <b>{u_name}</b> ({u_handle}) — <code>{u_id}</code>\n   └ {sub_lbl}\n"
        buttons.append([
            InlineKeyboardButton(text=f"➕ {u_name[:12]} (+1 oy)", callback_data=f"auth_ext30_{u_id}"),
            InlineKeyboardButton(text="🚫 Blok", callback_data=f"auth_reject_{u_id}")
        ])

    buttons.append([InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data == "admin_list_expired")
async def handle_admin_list_expired(callback: CallbackQuery):
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    expired = await database.get_users_list(is_allowed=1, filter_type="expired", limit=15)
    if not expired:
        await callback.answer("Muddati tugagan foydalanuvchilar yo'q!", show_alert=True)
        return

    text = "🔴 <b>Obuna muddati tugagan foydalanuvchilar (oxirgi 15 ta):</b>\n\n"
    buttons = []
    for u in expired:
        u_name = u['full_name'] or 'Noma\'lum'
        u_id = u['user_id']
        u_handle = f"@{u['username']}" if u['username'] else "username yo'q"
        u_sub = await database.get_user_subscription_info(u_id)
        text += f"• <b>{u_name}</b> ({u_handle}) — <code>{u_id}</code>\n   └ ⏳ Tugagan: {u_sub['formatted_date']}\n"
        buttons.append([
            InlineKeyboardButton(text=f"➕ {u_name[:12]} (+1 oy berish)", callback_data=f"auth_ext30_{u_id}"),
            InlineKeyboardButton(text="🚫 Blok", callback_data=f"auth_reject_{u_id}")
        ])

    buttons.append([InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data == "admin_list_admins")
async def handle_admin_list_admins(callback: CallbackQuery):
    if not (await database.is_admin(callback.from_user.id) or callback.from_user.id in config.ADMIN_IDS):
        return
    admins = await database.get_all_admins()
    text = "👑 <b>Bot administratorlari ro'yxati:</b>\n\n"
    for a in admins:
        text += f"• Telegram ID: <code>{a}</code>\n"
    text += "\n<i>Yangi admin qo'shish uchun: <code>/add_admin &lt;ID&gt;</code></i>"
    buttons = [[InlineKeyboardButton(text="◀️ Ortga", callback_data="admin_refresh")]]
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.message(Command("allow"))
async def handle_cmd_allow(message: Message):
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("⚠️ Foydalanish: <code>/allow &lt;USER_ID&gt; [kunlar (sukut bo'yicha 30)]</code>")
        return
    target_id = int(args[1])
    days = 30
    if len(args) >= 3 and args[2].isdigit():
        days = int(args[2])

    end_dt = await database.set_user_subscription(target_id, days=days)
    if end_dt:
        dt_str = end_dt.strftime("%d.%m.%Y")
        msg = f"✅ <b>{target_id}</b> raqamli foydalanuvchiga <b>{days} kunlik (1 oylik)</b> ruxsat berildi! Muddat: <code>{dt_str}</code> gacha."
        notify = (
            f"🎉 <b>Administrator sizga botdan foydalanish uchun {days} kunlik ruxsat berdi!</b>\n\n"
            f"📅 <b>Amal qilish muddati:</b> <code>{dt_str}</code> gacha.\n\n"
            "Quyidagi <b>/start</b> tugmasini bosib testlarni boshlashingiz mumkin:"
        )
    else:
        msg = f"✅ <b>{target_id}</b> raqamli foydalanuvchiga <b>cheksiz</b> ruxsat berildi!"
        notify = (
            "🎉 <b>Administrator sizga botdan foydalanish uchun cheksiz ruxsat berdi!</b>\n\n"
            "Quyidagi <b>/start</b> tugmasini bosib testlarni boshlashingiz mumkin:"
        )

    await message.answer(msg)
    try:
        await bot.send_message(target_id, notify, reply_markup=MAIN_KEYBOARD)
    except Exception:
        pass


@dp.message(Command("extend"))
async def handle_cmd_extend(message: Message):
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("⚠️ Foydalanish: <code>/extend &lt;USER_ID&gt; [qo'shiladigan kunlar (sukut bo'yicha 30)]</code>")
        return
    target_id = int(args[1])
    days = 30
    if len(args) >= 3 and args[2].isdigit():
        days = int(args[2])

    end_dt = await database.set_user_subscription(target_id, days=days)
    if end_dt:
        dt_str = end_dt.strftime("%d.%m.%Y")
        await message.answer(f"✅ <b>{target_id}</b> obunasi <b>+{days} kunga</b> uzaytirildi! Yangi muddat: <code>{dt_str}</code> gacha.")
        try:
            await bot.send_message(
                target_id,
                f"🎉 <b>Administrator sizning obunangizni yana {days} kunga uzaytirdi!</b>\n\n"
                f"📅 <b>Yangi muddat:</b> <code>{dt_str}</code> gacha.",
                reply_markup=MAIN_KEYBOARD
            )
        except Exception:
            pass


@dp.message(Command("block"))
async def handle_cmd_block(message: Message):
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("⚠️ Foydalanish: <code>/block 123456789</code>")
        return
    target_id = int(args[1])
    if target_id in config.ADMIN_IDS:
        await message.answer("❌ Asosiy adminni bloklab bo'lmaydi!")
        return
    await database.set_user_allowed(target_id, 0)
    await message.answer(f"🚫 <b>{target_id}</b> raqamli foydalanuvchi bloklandi (ruxsati bekor qilindi)!")
    try:
        await bot.send_message(target_id, "🔒 <b>Sizning botdan foydalanish ruxsatingiz bekor qilindi.</b>")
    except Exception:
        pass


@dp.message(Command("add_admin"))
async def handle_cmd_add_admin(message: Message):
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("⚠️ Foydalanish: <code>/add_admin 123456789</code>")
        return
    new_admin_id = int(args[1])
    await database.add_admin(new_admin_id)
    await message.answer(f"👑 <b>{new_admin_id}</b> muvaffaqiyatli adminlar ro'yxatiga qo'shildi!")
    try:
        await bot.send_message(
            new_admin_id,
            "👑 <b>Siz biologiya boti administratori etib tayinlandingiz!</b>\n"
            "Boshqaruv paneli uchun <b>/admin</b> buyrug'ini bosing.",
            reply_markup=MAIN_KEYBOARD
        )
    except Exception:
        pass


@dp.message(Command("admins"))
async def handle_cmd_admins(message: Message):
    if not (await database.is_admin(message.from_user.id) or message.from_user.id in config.ADMIN_IDS):
        return
    admins = await database.get_all_admins()
    text = "👑 <b>Barcha bot adminlari:</b>\n\n"
    for a in admins:
        text += f"• <code>{a}</code>\n"
    await message.answer(text)



# ==========================================
# 1. MAVZULAR (MA'RUZALAR) BO'LIMI VA SAHIFALASH
# ==========================================
TOPICS_PER_PAGE = 10


def build_topics_keyboard(grade: str, page: int = 1) -> tuple[str, Optional[InlineKeyboardMarkup]]:
    """Mavzular ro'yxatini 10 tadan sahifalab inline klaviatura tuzish"""
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    grade_data = QUESTIONS_DATA.get(grade, {})
    topics_from_q = grade_data.get("topics", [])

    topic_items = []
    if lectures:
        for lec in lectures:
            topic_items.append({"id": str(lec["id"]), "title": lec["title"]})
    elif topics_from_q:
        for t in topics_from_q:
            topic_items.append({"id": str(t["id"]), "title": t["title"]})

    total_topics = len(topic_items)
    if total_topics == 0:
        return (
            f"⚠️ <b>{grade_name}</b> bo'yicha hozircha ma'ruzalar tayyorlanmoqda.\n"
            "Boshqa sinfni tanlash uchun <b>\"🔄 Sinfni almashtirish\"</b> tugmasini bosing.",
            None
        )

    total_pages = max(1, (total_topics + TOPICS_PER_PAGE - 1) // TOPICS_PER_PAGE)
    page = max(1, min(page, total_pages))

    start_idx = (page - 1) * TOPICS_PER_PAGE
    end_idx = min(start_idx + TOPICS_PER_PAGE, total_topics)
    page_items = topic_items[start_idx:end_idx]

    buttons = []
    for item in page_items:
        buttons.append([
            InlineKeyboardButton(
                text=f"📖 {item['title']}",
                callback_data=f"read_topic_{grade}_{item['id']}_{page}"
            )
        ])

    # Sahifalar o'rtasida o'tish tugmalari
    if total_pages > 1:
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"topics_page_{grade}_{page - 1}"))
        nav_row.append(InlineKeyboardButton(text=f"📄 {page}/{total_pages}", callback_data=f"page_info_{page}_{total_pages}"))
        if page < total_pages:
            nav_row.append(InlineKeyboardButton(text="Keyingi ➡️", callback_data=f"topics_page_{grade}_{page + 1}"))
        buttons.append(nav_row)

    buttons.append([
        InlineKeyboardButton(text="🔄 Boshqa sinfni tanlash", callback_data="switch_grade_prompt")
    ])

    text = (
        f"📚 <b>{grade_name} — Mavzular va Ma'ruzalar</b>\n"
        f"<i>(Jami: {total_topics} ta mavzu, {page}/{total_pages}-sahifa)</i>\n\n"
        "O'rganmoqchi bo'lgan mavzungizni tanlang:"
    )
    return text, InlineKeyboardMarkup(inline_keyboard=buttons)


def build_tests_keyboard(grade: str, page: int = 1) -> tuple[str, Optional[InlineKeyboardMarkup]]:
    """Testlar ro'yxatini 10 tadan sahifalab inline klaviatura tuzish"""
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")
    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    if not topics:
        return (
            f"⚠️ <b>{grade_name}</b> bo'yicha testlar kiritilmoqda.\n"
            "Boshqa sinfni tanlash uchun <b>\"🔄 Sinfni almashtirish\"</b> tugmasini bosing.",
            None
        )

    total_topics = len(topics)
    total_q = sum(len(t.get("questions", [])) for t in topics)
    total_pages = max(1, (total_topics + TOPICS_PER_PAGE - 1) // TOPICS_PER_PAGE)
    page = max(1, min(page, total_pages))

    start_idx = (page - 1) * TOPICS_PER_PAGE
    end_idx = min(start_idx + TOPICS_PER_PAGE, total_topics)
    page_items = topics[start_idx:end_idx]

    buttons = []
    for t in page_items:
        q_count = len(t.get("questions", []))
        buttons.append([
            InlineKeyboardButton(
                text=f"📝 {t['title']} ({q_count} ta)",
                callback_data=f"tquiz_choose_{grade}_{t['id']}_{page}"
            )
        ])

    if total_pages > 1:
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"tests_page_{grade}_{page - 1}"))
        nav_row.append(InlineKeyboardButton(text=f"📄 {page}/{total_pages}", callback_data=f"page_info_{page}_{total_pages}"))
        if page < total_pages:
            nav_row.append(InlineKeyboardButton(text="Keyingi ➡️", callback_data=f"tests_page_{grade}_{page + 1}"))
        buttons.append(nav_row)

    buttons.append([
        InlineKeyboardButton(
            text=f"🎲 Barcha mavzulardan aralash test ({total_q} ta)",
            callback_data=f"tquiz_choose_{grade}_all_{page}"
        )
    ])
    buttons.append([
        InlineKeyboardButton(text="🔄 Boshqa sinf testlari", callback_data="switch_grade_prompt")
    ])

    text = (
        f"📝 <b>{grade_name} — Mavzulashtirilgan testlar</b>\n"
        f"<i>(Jami: {total_topics} ta mavzu, {total_q} ta savol, {page}/{total_pages}-sahifa)</i>\n\n"
        "Qaysi mavzudan test topshirmoqchisiz? Tanlang:"
    )
    return text, InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(F.text == "📖 Mavzular")
async def show_topics_menu(message: Message):
    """Tanlangan sinf bo'yicha mavzular ma'ruzasini ko'rsatish"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    text, markup = build_topics_keyboard(grade, page=1)
    if markup is None:
        await message.answer(text, reply_markup=MAIN_KEYBOARD)
        return
    await message.answer(text, reply_markup=markup)


@dp.callback_query(F.data.startswith("topics_page_"))
async def paginate_topics_callback(callback: CallbackQuery):
    """Mavzular sahifasini almashtirish (10 tadan)"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[2]
    page = int(parts[3])
    text, markup = build_topics_keyboard(grade, page)
    try:
        await callback.message.edit_text(text, reply_markup=markup)
    except Exception:
        await callback.message.answer(text, reply_markup=markup)


@dp.callback_query(F.data.startswith("page_info_"))
async def page_info_callback(callback: CallbackQuery):
    """Hozirgi sahifa raqami axboroti"""
    parts = callback.data.split("_")
    page = parts[2]
    total = parts[3]
    await callback.answer(f"📄 Hozirgi sahifa: {page} dan {total} gacha", show_alert=False)


@dp.callback_query(F.data.startswith("read_topic_") | F.data.startswith("thub_"))
async def read_topic_content(callback: CallbackQuery):
    """Mavzu Boshqaruv Markazi (Topic Hub) — Ma'ruza, Qo'llanma, Video va Testlar"""
    await callback.answer()
    parts = callback.data.split("_")
    if parts[0] == "read":
        grade = parts[2]
        topic_id = parts[3]
        page = int(parts[4]) if len(parts) > 4 else 1
    else:
        grade = parts[1]
        topic_id = parts[2]
        page = int(parts[3]) if len(parts) > 3 else 1

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    lec = next((l for l in lectures if str(l["id"]) == str(topic_id)), None)

    grade_data = QUESTIONS_DATA.get(grade, {})
    topic_info = next((t for t in grade_data.get("topics", []) if str(t["id"]) == str(topic_id)), None)

    title = lec["title"] if lec else (topic_info["title"] if topic_info else f"{topic_id}-mavzu")
    q_count = len(topic_info.get("questions", [])) if topic_info else 0

    hub_text = (
        f"🧬 <b>{title.upper()}</b>\n\n"
        f"Ushbu mavzu bo'yicha bazada <b>{q_count} ta</b> rasmiy test savoli mavjud.\n\n"
        "Kerakli o'quv bo'limini tanlang:\n"
        "• 📖 <b>Ma'ruza matni</b> — Darslik konspekti va nazariya\n"
        "• 📘 <b>Qisqa qo'llanma</b> — Muhim formulalar, atamalar va faktlar\n"
        "• 🎥 <b>Video va 3D Animatsiya</b> — Mavzuga oid darslik videolari\n"
        "• 📝 <b>Test ishlash</b> — 10 ta, 20 ta yoki to'liq hajmda\n"
        "• 📊 <b>Mening natijam</b> — Ushbu mavzudagi shaxsiy ko'rsatkichingiz"
    )

    buttons = [
        [InlineKeyboardButton(text="📖 Ma'ruza matni (Konspekt)", callback_data=f"tlec_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="📘 Qisqa qo'llanma (Faktlar)", callback_data=f"tgui_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="🎥 Video dars va 3D Animatsiya", callback_data=f"tmed_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text=f"📝 Test ishlash ({q_count} ta savol)", callback_data=f"tquiz_choose_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="📊 Mening ushbu mavzudagi natijam", callback_data=f"tstat_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="⬅️ Barcha mavzular ro'yxati", callback_data=f"back_to_topics_{grade}_{page}")]
    ]

    await callback.message.answer(
        hub_text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("tlec_"))
async def show_topic_lecture(callback: CallbackQuery):
    """Mavzu ma'ruzasini ko'rsatish"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    page = int(parts[3]) if len(parts) > 3 else 1

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    lec = next((l for l in lectures if str(l["id"]) == str(topic_id)), None)

    if not lec:
        text = "📖 Ushbu mavzu ma'ruzasi tayyorlanmoqda."
    else:
        text = lec["text"]

    buttons = [
        [InlineKeyboardButton(text="📘 Qisqa qo'llanma", callback_data=f"tgui_{grade}_{topic_id}_{page}"),
         InlineKeyboardButton(text="📝 Test ishlash", callback_data=f"tquiz_choose_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="⬅️ Mavzu bosh menyusi", callback_data=f"thub_{grade}_{topic_id}_{page}")]
    ]
    await callback.message.answer(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("tgui_"))
async def show_topic_guide(callback: CallbackQuery):
    """Mavzu bo'yicha qisqa qo'llanma (savol-javob, muhim faktlar)"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    page = int(parts[3]) if len(parts) > 3 else 1

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    lec = next((l for l in lectures if str(l["id"]) == str(topic_id)), None)

    guide_text = lec.get("guide") if (lec and "guide" in lec) else (
        "📘 <b>QISQA QO'LLANMA:</b>\n\n"
        "Ushbu mavzu bo'yicha asosiy formulalar va tayanch tushunchalar ma'ruza matnida keltirilgan."
    )

    buttons = [
        [InlineKeyboardButton(text="📖 Ma'ruza matni", callback_data=f"tlec_{grade}_{topic_id}_{page}"),
         InlineKeyboardButton(text="📝 Test ishlash", callback_data=f"tquiz_choose_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="⬅️ Mavzu bosh menyusi", callback_data=f"thub_{grade}_{topic_id}_{page}")]
    ]
    await callback.message.answer(guide_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("tmed_"))
async def show_topic_media(callback: CallbackQuery):
    """Mavzuga oid Video dars va 3D Animatsiya ma'lumotlari"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    page = int(parts[3]) if len(parts) > 3 else 1

    lectures = materials.TOPICS_CONTENT.get(grade, [])
    lec = next((l for l in lectures if str(l["id"]) == str(topic_id)), None)

    media_text = lec.get("media") if (lec and "media" in lec) else (
        "🎥 <b>MULTIMEDIA MATERIALLARI:</b>\n\n"
        "Ushbu mavzuga oid qo'shimcha video roliklar va 3D animatsiyalar tayyorlanmoqda."
    )

    buttons = [
        [InlineKeyboardButton(text="📝 Test ishlash", callback_data=f"tquiz_choose_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="⬅️ Mavzu bosh menyusi", callback_data=f"thub_{grade}_{topic_id}_{page}")]
    ]
    await callback.message.answer(media_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("tstat_"))
async def show_topic_user_stats(callback: CallbackQuery):
    """O'quvchining ushbu mavzudagi shaxsiy natijasini ko'rsatish"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    page = int(parts[3]) if len(parts) > 3 else 1
    user_id = callback.from_user.id

    grade_data = QUESTIONS_DATA.get(grade, {})
    topic_info = next((t for t in grade_data.get("topics", []) if str(t["id"]) == str(topic_id)), None)
    title = topic_info["title"] if topic_info else f"{topic_id}-mavzu"

    result = await database.get_user_topic_result(user_id, grade, topic_id)

    if result:
        score = result["score"]
        total = result["total"]
        pct = round((score / total) * 100, 1) if total > 0 else 0
        mark = "A'lo (5 baho) ⭐️" if pct >= 85 else ("Yaxshi (4 baho) 👍" if pct >= 70 else ("Qoniqarli (3 baho) 👌" if pct >= 55 else "Qayta tayyorlaning (2 baho) ⚠️"))
        stat_text = (
            f"📊 <b>SIZNING USHBU MAVZUDAGI NATIJANGIZ:</b>\n\n"
            f"📌 Mavzu: <b>{title}</b>\n"
            f"✅ Oxirgi natija: <b>{score} / {total}</b> ({pct}%)\n"
            f"🏆 Baho: <b>{mark}</b>\n"
            f"🕒 Topshirilgan vaqt: <i>{result['finished_at']}</i>\n\n"
            "<i>Natijangizni yanada yaxshilash uchun qaytadan test topshirishingiz mumkin!</i>"
        )
    else:
        stat_text = (
            f"ℹ️ <b>Siz hali {title} bo'yicha test topshirmagansiz!</b>\n\n"
            "Mavzuni qanchalik yaxshi o'zlashtirganingizni bilish uchun hoziroq testni boshlang."
        )

    buttons = [
        [InlineKeyboardButton(text="📝 Test topshirish", callback_data=f"tquiz_choose_{grade}_{topic_id}_{page}")],
        [InlineKeyboardButton(text="⬅️ Mavzu bosh menyusi", callback_data=f"thub_{grade}_{topic_id}_{page}")]
    ]
    await callback.message.answer(stat_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("back_to_topics_"))
async def back_to_topics_callback(callback: CallbackQuery):
    """Mavzular ro'yxatiga qaytish (sahifani saqlagan holda)"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[3]
    page = int(parts[4]) if len(parts) > 4 else 1
    
    text, markup = build_topics_keyboard(grade, page)
    try:
        await callback.message.edit_text(text, reply_markup=markup)
    except Exception:
        await callback.message.answer(text, reply_markup=markup)


# ==========================================
# 2. TESTLAR BO'LIMI (TEST SIZE CHOOSER)
# ==========================================
@dp.message(F.text == "📝 Testlar")
async def show_tests_menu(message: Message):
    """Mavzulashtirilgan testlar ro'yxatini chiqarish (sahifalash bilan)"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    text, markup = build_tests_keyboard(grade, page=1)
    if markup is None:
        await message.answer(text, reply_markup=MAIN_KEYBOARD)
        return
    await message.answer(text, reply_markup=markup)


@dp.callback_query(F.data.startswith("tests_page_"))
async def paginate_tests_callback(callback: CallbackQuery):
    """Testlar sahifasini almashtirish (10 tadan)"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[2]
    page = int(parts[3])
    text, markup = build_tests_keyboard(grade, page)
    try:
        await callback.message.edit_text(text, reply_markup=markup)
    except Exception:
        await callback.message.answer(text, reply_markup=markup)


@dp.callback_query(F.data.startswith("tquiz_choose_") | F.data.startswith("topic_"))
async def choose_quiz_mode(callback: CallbackQuery):
    """Test hajmiga qarab tanlov berish (1-variant: 10 ta, 20 ta yoki Barchasi)"""
    await callback.answer()
    parts = callback.data.split("_")
    # Callback either: tquiz_choose_{grade}_{topic_id}_{page} or topic_{grade}_{topic_id}_{page}
    if parts[0] == "tquiz":
        grade = parts[2]
        topic_id = parts[3]
        page = int(parts[4]) if len(parts) > 4 else 1
    else:
        grade = parts[1]
        topic_id = parts[2]
        page = int(parts[3]) if len(parts) > 3 else 1

    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    if topic_id == "all":
        total_q = sum(len(t.get("questions", [])) for t in topics)
        title = f"{GRADE_NAMES.get(grade, grade)} (Barcha mavzular)"
        prompt_text = (
            f"🎲 <b>{title}</b>\n\n"
            f"Bazada jami <b>{total_q} ta</b> savol mavjud.\n"
            "Nechta savol ishlamoqchisiz? Tanlang:"
        )
        buttons = [
            [InlineKeyboardButton(text="⚡️ Tezkor aralash test (15 ta savol)", callback_data=f"quizstart_{grade}_all_15")],
            [InlineKeyboardButton(text="📝 Standart DTM bloki (30 ta savol)", callback_data=f"quizstart_{grade}_all_30")],
            [InlineKeyboardButton(text="⬅️ Ortga", callback_data=f"tests_page_{grade}_{page}")]
        ]
    else:
        topic = next((t for t in topics if str(t["id"]) == str(topic_id)), None)
        if not topic:
            await callback.message.answer("⚠️ Mavzu topilmadi.")
            return
        total_q = len(topic.get("questions", []))
        title = topic["title"]
        prompt_text = (
            f"📝 <b>{title}</b>\n\n"
            f"Ushbu mavzu bo'yicha bazada <b>{total_q} ta</b> savol mavjud.\n"
            "O'zingizga qulay test rejimini tanlang:"
        )
        buttons = [
            [InlineKeyboardButton(text="⚡️ Tezkor test (10 ta savol)", callback_data=f"quizstart_{grade}_{topic_id}_10")],
            [InlineKeyboardButton(text="📝 Standart test (20 ta savol)", callback_data=f"quizstart_{grade}_{topic_id}_20")],
            [InlineKeyboardButton(text=f"🏆 To'liq test (Barcha {total_q} ta)", callback_data=f"quizstart_{grade}_{topic_id}_all")],
            [InlineKeyboardButton(text="⬅️ Mavzu bosh menyusi", callback_data=f"thub_{grade}_{topic_id}_{page}")]
        ]

    await callback.message.answer(
        prompt_text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


@dp.callback_query(F.data.startswith("quizstart_"))
async def start_quiz_with_count(callback: CallbackQuery):
    """Tanlangan miqdorda viktorina testini boshlash"""
    await callback.answer()
    parts = callback.data.split("_")
    grade = parts[1]
    topic_id = parts[2]
    count_str = parts[3]
    user_id = callback.from_user.id

    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    if topic_id == "all":
        questions = []
        for t in topics:
            questions.extend(t.get("questions", []))
        session_title = f"{GRADE_NAMES.get(grade, grade)} (Aralash test)"
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

    # Savollarni aralashtirib berish va tanlangan miqdorda kesish
    quiz_questions = questions[:]
    random.shuffle(quiz_questions)

    if count_str != "all":
        try:
            limit = int(count_str)
            quiz_questions = quiz_questions[:limit]
        except ValueError:
            pass

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
        f"Tanlangan savollar soni: <b>{len(quiz_questions)} ta</b>\n\n"
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

    # Rasmli testlar uchun rasmni yuborish
    img_rel = q.get("image")
    if img_rel:
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), img_rel) if not os.path.isabs(img_rel) else img_rel
        if os.path.exists(img_path):
            try:
                await bot.send_photo(
                    chat_id=user_id,
                    photo=FSInputFile(img_path),
                    caption=f"📸 <b>Savol #{index + 1} uchun rasm:</b>"
                )
            except Exception as img_err:
                logging.warning(f"Rasm yuborishda xatolik: {img_err}")

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
    percent = round((score / total) * 100, 1) if total > 0 else 0
    grade = session.get("grade", "8")
    session_title = session["grade_name"]

    # Agar haftalik nazorat testi bo'lsa
    if session.get("is_weekly"):
        user_info = await database.get_user_info(user_id)
        full_name = user_info.get("full_name", "Noma'lum") if user_info else "O'quvchi"
        username = user_info.get("username", "") if user_info else ""

        w_res = await database.record_weekly_test_result(
            user_id=user_id,
            full_name=full_name,
            grade=grade,
            score=score,
            total=total
        )
        status_text = w_res["status"]

        summary_text = (
            "🏁 <b>Haftalik Nazorat Testi yakunlandi!</b>\n\n"
            f"👤 O'quvchi: <b>{full_name}</b>\n"
            f"📚 Sinf: <b>{grade}-sinf</b>\n"
            f"📝 Jami nazorat savollari: <b>{total} ta</b>\n"
            f"✅ To'g'ri javoblar: <b>{score} ta</b>\n"
            f"❌ Xato javoblar: <b>{total - score} ta</b>\n"
            f"🎯 O'zlashtirish ko'rsatkichi: <b>{percent}%</b>\n\n"
            f"📊 <b>O'zlashtirish darajangiz:</b>\n<b>{status_text}</b>\n\n"
            "<i>Ushbu natija o'qituvchingiz hisobotida aks etadi va profilingizda qayd etildi.</i>"
        )

        finish_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="📊 Mening o'zlashtirishim", callback_data="show_my_stats_cb")],
                [InlineKeyboardButton(text="📐 Masalalar bo'limi", callback_data="prob_menu")],
                [InlineKeyboardButton(text="📝 Boshqa test ishlash", callback_data="show_tests_cb")]
            ]
        )

        await bot.send_message(user_id, summary_text, reply_markup=finish_keyboard)

        # Adminga / O'qituvchiga natijani xabar qilish
        admin_alert = (
            "📢 <b>Yangi Haftalik Nazorat Testi topshirildi!</b>\n\n"
            f"👤 <b>O'quvchi:</b> {full_name} (@{username or 'yo‘q'})\n"
            f"🆔 <b>ID:</b> <code>{user_id}</code>\n"
            f"📚 <b>Sinf:</b> {grade}-sinf\n"
            f"🎯 <b>Natija:</b> {score}/{total} ta ({percent}%)\n"
            f"📊 <b>Baholash:</b> {status_text}"
        )
        for adm_id in await database.get_all_admins():
            try:
                await bot.send_message(adm_id, admin_alert)
            except Exception:
                pass
        return

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
    """O'quvchining shaxsiy natijalari va to'liq o'zlashtirish hisoboti"""
    user_id = message.from_user.id
    report = await database.get_student_comprehensive_report(user_id)
    if not report or (report["test_total"] == 0 and not report["last_weekly"] and report["problem_stats"]["total"] == 0):
        await message.answer(
            "📊 <b>Siz hali birorta ham test yoki masala ishlamagansiz.</b>\n\n"
            "Bilimlaringizni sinash uchun <b>\"📝 Testlar\"</b> yoki <b>\"📅 Haftalik Test\"</b> tugmasini bosing!",
            reply_markup=MAIN_KEYBOARD
        )
        return

    grade = report.get("current_grade", "8")
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")
    total = report["test_total"]
    correct = report["test_correct"]
    percent = report["test_percent"]
    ps = report["problem_stats"]
    lw = report["last_weekly"]

    recent_tests = await database.get_user_recent_results(user_id, limit=3)
    sub_info = await database.get_user_subscription_info(user_id)
    if sub_info["is_admin"]:
        sub_str = "👑 Admin (Cheksiz)"
    elif sub_info["is_lifetime"]:
        sub_str = "♾ Cheksiz (Doimiy)"
    elif sub_info["is_active"]:
        sub_str = f"🟢 <b>{sub_info['formatted_date'][:10]} gacha</b> (<i>{sub_info['days_left']} kun qoldi</i>)"
    else:
        sub_str = f"🔴 <b>Muddati tugagan</b> ({sub_info['formatted_date']})"

    text = (
        f"📊 <b>SIZNING SHAXSIY PEDAGOGIK HISOBOTINGIZ:</b>\n\n"
        f"👤 O'quvchi: <b>{message.from_user.full_name}</b>\n"
        f"⏳ Obuna holati: {sub_str}\n"
        f"📚 Joriy tanlangan sinf: <b>{grade_name}</b>\n"
        f"🏆 <b>O'ZLASHTIRISH DARAJANGIZ:</b>\n"
        f"<b>{report['mastery_badge']} ({report['overall_mastery']}%)</b>\n\n"
        f"📝 <b>Mavzuviy testlar:</b> {correct}/{total} ta ({percent}%)\n"
    )

    if lw:
        text += f"📅 <b>Oxirgi haftalik nazorat:</b> {lw['score']}/{lw['total']} ({lw['mastery_percent']}%) — {lw['status']}\n"
    else:
        text += "📅 <b>Haftalik nazorat:</b> <i>Hali topshirilmagan (Boshlash: «📅 Haftalik Test»)</i>\n"

    text += f"📐 <b>Masalalar va topshiriqlar:</b> {ps['correct']}/{ps['total']} ta ({ps['percent']}%)\n\n"

    if recent_tests:
        text += "📋 <b>Oxirgi ishlagan testlaringiz:</b>\n"
        for r in recent_tests:
            r_pct = round((r['score'] / r['total']) * 100, 1) if r['total'] > 0 else 0
            text += f"• <b>{r['topic_title']}</b>: {r['score']}/{r['total']} ta ({r_pct}%)\n"

    text += "\n💡 <i>Muntazam test va masalalar ishlab, o'zlashtirish darajangizni 90%+ ga yetkazing!</i>"

    buttons = [
        [InlineKeyboardButton(text="📅 Haftalik Test topshirish", callback_data="start_weekly_cb")],
        [InlineKeyboardButton(text="📐 Masalalar yechish", callback_data="prob_menu")],
        [InlineKeyboardButton(text="📝 Testlar bo'limi", callback_data="show_tests_cb")]
    ]
    await message.answer(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data == "show_my_stats_cb")
async def show_my_stats_callback(callback: CallbackQuery):
    await callback.answer()
    await show_my_stats(callback.message)


@dp.callback_query(F.data == "show_tests_cb")
async def show_tests_callback(callback: CallbackQuery):
    await callback.answer()
    await show_tests_menu(callback.message)


# ==========================================
# HAFTALIK NAZORAT TESTI
# ==========================================
@dp.message(F.text == "📅 Haftalik Test")
async def start_weekly_test(message: Message):
    """O'quvchining joriy sinfi bo'yicha haftalik o'zlashtirish darajasini aniqlovchi nazorat testi"""
    user_id = message.from_user.id
    grade = await database.get_user_grade(user_id)
    grade_name = GRADE_NAMES.get(grade, f"{grade}-sinf")

    grade_data = QUESTIONS_DATA.get(grade, {})
    topics = grade_data.get("topics", [])

    all_questions = []
    for t in topics:
        all_questions.extend(t.get("questions", []))

    if not all_questions:
        await message.answer(
            f"⚠️ <b>{grade_name}</b> bo'yicha haftalik nazorat testlari shakllantirilmoqda.\n"
            "Boshqa sinfni tanlash uchun <b>«🔄 Sinfni almashtirish»</b> tugmasini bosing.",
            reply_markup=MAIN_KEYBOARD
        )
        return

    # Haftalik test uchun mavzular bo'ylab 15 ta saralangan savol
    shuffled_questions = all_questions[:]
    random.shuffle(shuffled_questions)
    weekly_questions = shuffled_questions[:15]

    active_sessions[user_id] = {
        "grade": grade,
        "grade_name": f"{grade}-sinf Haftalik Nazorat Testi",
        "questions": weekly_questions,
        "index": 0,
        "score": 0,
        "last_poll_id": None,
        "is_weekly": True
    }

    start_text = (
        f"📅 <b>HAFTALIK NAZORAT TESTI ({grade_name})</b>\n\n"
        "Ushbu test siz o'tgan darslik mavzularini qay darajada o'zlashtirganingizni aniqlash uchun tuzilgan.\n\n"
        f"📝 <b>Savollar soni:</b> 15 ta\n"
        "⏱ <b>Vaqt chegarasi yo'q</b> — savollarni diqqat bilan o'qib javob bering.\n"
        "📊 Test yakunlangach, o'zlashtirish foizingiz hisoblanadi va o'qituvchingizga hisobot taqdim etiladi.\n\n"
        "<i>Boshlaymiz! Omad!</i>"
    )
    await message.answer(start_text)
    await send_next_question(user_id)


@dp.callback_query(F.data == "start_weekly_cb")
async def start_weekly_cb(callback: CallbackQuery):
    await callback.answer()
    await start_weekly_test(callback.message)


# ==========================================
# BIOLOGIYA MASALALARI VA TOPSHIRIQLAR
# ==========================================
@dp.message(F.text == "📐 Masalalar")
async def show_problems_main_menu(message: Message):
    """Biologiya masalalari va amaliy topshiriqlar asosiy menyusi"""
    text = (
        "📐 <b>BIOLOGIYA MASALALARI VA AMALIY TOPSHIRIQLAR</b>\n\n"
        "Ushbu bo'limda siz darslikdagi masalalarni yechish qoidalari, formulalari bilan tanishishingiz, "
        "namunaviy masalalarni bosqichma-bosqich o'rganishingiz va topshiriqlarni bajarishingiz mumkin:\n\n"
        "🔹 <b>Qoidalar va formulalar:</b> DNK, oqsil, ATF, mitoz/meyoz va genetika formulalari\n"
        "🔹 <b>Namunaviy masalalar:</b> Batafsil yechimlari bilan tushuntirilgan masalalar\n"
        "🔹 <b>Uyga vazifalar:</b> O'zlashtirishni tekshiruvchi maxsus masalalar to'plami\n"
        "🔹 <b>Mening natijalarim:</b> Masalalar bo'yicha shaxsiy ko'rsatkichlaringiz"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Yechish qoidalari va formulalari", callback_data="prob_rules_list")],
        [InlineKeyboardButton(text="✍️ Namunaviy masalalar (Yechimlari bilan)", callback_data="prob_practice_list")],
        [InlineKeyboardButton(text="📋 Uyga vazifalar (Topshiriqlar)", callback_data="prob_hw_list")],
        [InlineKeyboardButton(text="📊 Masalalar bo'yicha ko'rsatkichim", callback_data="prob_my_stats")]
    ])
    await message.answer(text, reply_markup=kb)


@dp.callback_query(F.data == "prob_menu")
async def prob_menu_cb(callback: CallbackQuery):
    await callback.answer()
    text = (
        "📐 <b>BIOLOGIYA MASALALARI VA AMALIY TOPSHIRIQLAR</b>\n\n"
        "Kerakli bo'limni tanlang:"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Yechish qoidalari va formulalari", callback_data="prob_rules_list")],
        [InlineKeyboardButton(text="✍️ Namunaviy masalalar (Yechimlari bilan)", callback_data="prob_practice_list")],
        [InlineKeyboardButton(text="📋 Uyga vazifalar (Topshiriqlar)", callback_data="prob_hw_list")],
        [InlineKeyboardButton(text="📊 Masalalar bo'yicha ko'rsatkichim", callback_data="prob_my_stats")]
    ])
    try:
        await callback.message.edit_text(text, reply_markup=kb)
    except Exception:
        await callback.message.answer(text, reply_markup=kb)


@dp.callback_query(F.data == "prob_rules_list")
async def prob_rules_list_cb(callback: CallbackQuery):
    await callback.answer()
    buttons = []
    for cat_key, guide in problems.PROBLEM_GUIDES.items():
        buttons.append([InlineKeyboardButton(text=guide["title"], callback_data=f"view_formula_{cat_key}")])
    buttons.append([InlineKeyboardButton(text="◀️ Masalalar bosh menyusi", callback_data="prob_menu")])
    text = (
        "📖 <b>MASALALARNI YECHISH QOIDALARI VA FORMULALARI</b>\n\n"
        "Qaysi mavzudagi masalalar formulalari va qoidalarini o'rganmoqchisiz? Tanlang:"
    )
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("view_formula_"))
async def view_formula_cb(callback: CallbackQuery):
    await callback.answer()
    cat_key = callback.data.replace("view_formula_", "")
    guide = problems.PROBLEM_GUIDES.get(cat_key)
    if not guide:
        await callback.answer("Ma'lumot topilmadi!", show_alert=True)
        return
    text = (
        f"{guide['title']}\n"
        f"<i>{guide['description']}</i>\n\n"
        f"{guide['rules']}"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Ushbu mavzudan mashq ishlash", callback_data="prob_practice_list")],
        [InlineKeyboardButton(text="◀️ Qoidalar ro'yxati", callback_data="prob_rules_list")],
        [InlineKeyboardButton(text="🏠 Masalalar menyusi", callback_data="prob_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)


@dp.callback_query(F.data == "prob_practice_list")
async def prob_practice_list_cb(callback: CallbackQuery):
    await callback.answer()
    buttons = []
    for p in problems.PRACTICE_PROBLEMS:
        buttons.append([InlineKeyboardButton(text=f"🔹 {p['title']}", callback_data=f"solve_prob_{p['id']}")])
    buttons.append([InlineKeyboardButton(text="◀️ Masalalar menyusi", callback_data="prob_menu")])
    text = (
        "✍️ <b>NAMUNAVIY MASALALAR VA BOSQICHMA-BOSQICH YECHIMLAR</b>\n\n"
        "O'zingiz qiziqqan masalani tanlang, uning berilishi va to'liq yechilish usulini o'rganing:"
    )
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("solve_prob_"))
async def solve_prob_cb(callback: CallbackQuery):
    await callback.answer()
    prob_id = callback.data.replace("solve_prob_", "")
    prob = next((p for p in problems.PRACTICE_PROBLEMS if p["id"] == prob_id), None)
    if not prob:
        await callback.answer("Masala topilmadi!", show_alert=True)
        return

    text = f"{prob['task']}\n\nJavob variantlaridan birini tanlang yoki to'liq yechimni ko'ring:"
    buttons = []
    for i, opt in enumerate(prob["options"]):
        buttons.append([InlineKeyboardButton(text=f"{chr(65+i)}) {opt}", callback_data=f"ans_prob_{prob_id}_{i}")])
    buttons.append([InlineKeyboardButton(text="💡 To'g'ridan-to'g'ri yechimni ko'rish", callback_data=f"ans_prob_{prob_id}_expl")])
    buttons.append([InlineKeyboardButton(text="◀️ Masalalar ro'yxati", callback_data="prob_practice_list")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("ans_prob_"))
async def ans_prob_cb(callback: CallbackQuery):
    await callback.answer()
    parts = callback.data.split("_")
    prob_id = parts[2]
    choice = parts[3]
    prob = next((p for p in problems.PRACTICE_PROBLEMS if p["id"] == prob_id), None)
    if not prob:
        return

    if choice == "expl":
        result_header = "💡 <b>NAMUNAVIY MASALANING TO'LIQ YECHILISH USULI:</b>\n\n"
    else:
        chosen_idx = int(choice)
        is_corr = (chosen_idx == prob["correct_option_id"])
        if is_corr:
            result_header = "✅ <b>Juda to'g'ri! Barakalla!</b>\n\n"
        else:
            correct_chr = chr(65 + prob["correct_option_id"])
            result_header = f"❌ <b>Noto'g'ri tanlandi. To'g'ri javob: {correct_chr} varianti edi.</b>\n\n"

    text = (
        f"{result_header}"
        f"<b>Masala sharti:</b>\n{prob['task']}\n\n"
        f"📝 <b>Bosqichma-bosqich yechilishi:</b>\n"
        f"{prob['explanation']}"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Boshqa masala ishlash", callback_data="prob_practice_list")],
        [InlineKeyboardButton(text="📋 Uyga vazifalar", callback_data="prob_hw_list")],
        [InlineKeyboardButton(text="🏠 Masalalar menyusi", callback_data="prob_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)


@dp.callback_query(F.data == "prob_hw_list")
async def prob_hw_list_cb(callback: CallbackQuery):
    await callback.answer()
    buttons = []
    for hw in problems.HOMEWORK_TASKS:
        buttons.append([InlineKeyboardButton(text=f"📋 {hw['title']}", callback_data=f"view_hw_{hw['id']}")])
    buttons.append([InlineKeyboardButton(text="◀️ Masalalar menyusi", callback_data="prob_menu")])
    text = (
        "📋 <b>UYGA VAZIFALAR VA MUSTAQIL ISHLAR</b>\n\n"
        "Mavzular bo'yicha bilimlaringizni sinash uchun berilgan topshiriqni tanlang va yeching.\n"
        "Natijalaringiz avtomatik hisoblanib profilingizga yoziladi:"
    )
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("view_hw_"))
async def view_hw_cb(callback: CallbackQuery):
    await callback.answer()
    hw_id = callback.data.replace("view_hw_", "")
    hw = next((h for h in problems.HOMEWORK_TASKS if h["id"] == hw_id), None)
    if not hw:
        await callback.answer("Vazifa topilmadi!", show_alert=True)
        return

    text = f"{hw['task']}\n\nTo'g'ri javobni belgilang:"
    buttons = []
    for i, opt in enumerate(hw["options"]):
        buttons.append([InlineKeyboardButton(text=f"{chr(65+i)}) {opt}", callback_data=f"ans_hw_{hw_id}_{i}")])
    buttons.append([InlineKeyboardButton(text="◀️ Vazifalar ro'yxati", callback_data="prob_hw_list")])
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@dp.callback_query(F.data.startswith("ans_hw_"))
async def ans_hw_cb(callback: CallbackQuery):
    await callback.answer()
    parts = callback.data.split("_")
    hw_id = parts[2]
    chosen_idx = int(parts[3])
    user_id = callback.from_user.id
    grade = await database.get_user_grade(user_id)

    hw = next((h for h in problems.HOMEWORK_TASKS if h["id"] == hw_id), None)
    if not hw:
        return

    is_correct = (chosen_idx == hw["correct_option_id"])
    user_ans_text = hw["options"][chosen_idx] if chosen_idx < len(hw["options"]) else str(chosen_idx)

    # Natijani bazaga saqlash
    await database.record_problem_submission(
        user_id=user_id,
        grade=grade,
        category=hw.get("topic", "Genetika"),
        problem_title=hw["title"],
        user_answer=user_ans_text,
        is_correct=is_correct
    )

    if is_correct:
        status_msg = "✅ <b>Ajoyib! Javobingiz to'g'ri!</b>\n\n"
    else:
        correct_chr = chr(65 + hw["correct_option_id"])
        status_msg = f"❌ <b>Javobingiz xato. To'g'ri javob: {correct_chr} varianti edi.</b>\n\n"

    text = (
        f"{status_msg}"
        f"<b>Vazifa:</b> {hw['title']}\n\n"
        f"📝 <b>Masalaning to'liq yechilishi:</b>\n"
        f"{hw['explanation']}\n\n"
        "<i>Topshiriq natijasi sizning o'zlashtirish hisobotingizga qo'shildi.</i>"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Boshqa vazifa ishlash", callback_data="prob_hw_list")],
        [InlineKeyboardButton(text="📊 O'zlashtirish ko'rsatkichim", callback_data="prob_my_stats")],
        [InlineKeyboardButton(text="🏠 Masalalar menyusi", callback_data="prob_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)


@dp.callback_query(F.data == "prob_my_stats")
async def prob_my_stats_cb(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    p_stats = await database.get_user_problem_stats(user_id)
    text = (
        "📊 <b>SIZNING MASALALAR BO'YICHA O'ZLASHTIRISHINGIZ:</b>\n\n"
        f"👤 O'quvchi: <b>{callback.from_user.full_name}</b>\n"
        f"🔹 Jami topshirilgan masalalar: <b>{p_stats['total']} ta</b>\n"
        f"✅ To'g'ri yechilgan: <b>{p_stats['correct']} ta</b>\n"
        f"❌ Xato yechilgan: <b>{p_stats['total'] - p_stats['correct']} ta</b>\n"
        f"🎯 Aniqlik ko'rsatkichi: <b>{p_stats['percent']}%</b>\n\n"
        "💡 <i>Muntazam masalalar yechish orqali natijalaringizni oshirib boring!</i>"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Masala ishlash", callback_data="prob_practice_list")],
        [InlineKeyboardButton(text="📋 Uyga vazifalar", callback_data="prob_hw_list")],
        [InlineKeyboardButton(text="◀️ Masalalar menyusi", callback_data="prob_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)


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
import re
import html

def find_relevant_textbook_context(prompt: str, grade: str = "8") -> str:
    """O'quvchi savoliga mos maktab darslik mavzulari, formulalar va qoidalarni qidirish"""
    try:
        p_lower = prompt.lower()
        context_chunks = []

        # 1. Masala formulalari va qoidalari tekshiruvi (problems.PROBLEM_GUIDES)
        keywords_map = {
            "dnk": ["dnk", "rnk", "nukleotid", "chargaff", "vodorod", "komplementar", "adenin", "timin", "guanin", "sitozin", "pirimidin", "purin"],
            "protein": ["oqsil", "aminokislota", "triplet", "kodon", "antikodon", "translyatsiya", "polipeptid", "irnk", "trnk"],
            "atf": ["atf", "glikoliz", "energetik", "parchalanish", "glyukoza", "mitoxondriya", "sut kislota", "kaloriya"],
            "mitoz": ["mitoz", "meyoz", "xromosoma", "xromatida", "interfaza", "profaza", "metafaza", "anafaza", "telofaza", "reduksion"],
            "genetika": ["genetika", "mendel", "genotip", "fenotip", "dominant", "retsessiv", "duragay", "digeterozigota", "chatishtirish", "allell"]
        }

        for cat_key, words in keywords_map.items():
            if any(w in p_lower for w in words):
                guide = problems.PROBLEM_GUIDES.get(cat_key)
                if guide:
                    clean_rules = re.sub(r'<[^>]+>', '', guide["rules"])
                    context_chunks.append(f"[Mavzu qoidalari va formulasi: {guide['title']}]\n{clean_rules}")

        # 2. Darslik ma'ruzalari va konspektlaridan qidirish (materials.TOPICS_CONTENT)
        raw_words = re.findall(r'[a-zA-Zа-яА-Яo‘O‘g‘G‘o\'O\'g\'G\']+', p_lower)
        search_terms = [w for w in raw_words if len(w) >= 3 and w not in ["uchun", "haqida", "qanday", "nima", "qaysi", "bilan", "emas", "kerak"]]

        matched_topics = []
        grades_to_check = [grade] + [g for g in materials.TOPICS_CONTENT.keys() if g != grade]

        for g in grades_to_check:
            t_list = materials.TOPICS_CONTENT.get(g, [])
            for topic in t_list:
                score = 0
                t_title = topic.get("title", "").lower()
                t_guide = topic.get("guide", "").lower()
                t_text = topic.get("text", "").lower()

                for term in search_terms:
                    if term in t_title:
                        score += 5
                    if term in t_guide:
                        score += 3
                    if term in t_text:
                        score += 1

                if score > 0:
                    matched_topics.append((score, g, topic))

        matched_topics.sort(key=lambda x: x[0], reverse=True)
        for score, g, t in matched_topics[:2]:
            t_title = t.get("title", "")
            clean_guide = re.sub(r'<[^>]+>', '', t.get("guide", ""))
            clean_text = re.sub(r'<[^>]+>', '', t.get("text", ""))[:800]
            context_chunks.append(f"[{g}-sinf Darslik mavzusi: {t_title}]\n{clean_guide}\n{clean_text}...")

        # 3. Darslik test savollaridan qidirish (QUESTIONS_DATA)
        g_data = QUESTIONS_DATA.get(grade, {})
        for t in g_data.get("topics", []):
            for q in t.get("questions", []):
                q_text = q.get("question", "").lower()
                if any(term in q_text for term in search_terms if len(term) >= 4):
                    corr_opt = q["options"][q["correct_option_id"]] if q["correct_option_id"] < len(q["options"]) else ""
                    context_chunks.append(f"[Darslik testi namunasi: {q['question']}] To'g'ri javob: {corr_opt}. Izoh: {q.get('explanation', '')}")
                    break
            if len(context_chunks) >= 4:
                break

        return "\n\n".join(context_chunks)
    except Exception as e:
        logging.warning(f"find_relevant_textbook_context xatolik: {e}")
        return ""


def format_gemini_markdown_to_telegram_html(text: str) -> str:
    """Gemini qaytargan matnni xavfsiz Telegram HTML formatiga aylantirish"""
    try:
        code_blocks = []
        def code_repl(m):
            code_blocks.append(html.escape(m.group(1)))
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"

        text = re.sub(r'```(?:[a-zA-Z0-9_]+)?\n?(.*?)```', code_repl, text, flags=re.DOTALL)

        inline_codes = []
        def inline_repl(m):
            inline_codes.append(html.escape(m.group(1)))
            return f"__INLINE_CODE_{len(inline_codes)-1}__"
        text = re.sub(r'`([^`]+)`', inline_repl, text)

        text = html.escape(text)

        # **matn** -> <b>matn</b>
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        # *matn* -> <i>matn</i>
        text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
        # Sarlavhalar #, ##, ### Sarlavha -> <b>Sarlavha</b>
        text = re.sub(r'^(?:#{1,6})\s*(.+)$', r'<b>\1</b>', text, flags=re.MULTILINE)

        for i, code in enumerate(code_blocks):
            text = text.replace(f"__CODE_BLOCK_{i}__", f"<pre><code>{code}</code></pre>")
        for i, code in enumerate(inline_codes):
            text = text.replace(f"__INLINE_CODE_{i}__", f"<code>{code}</code>")

        return text
    except Exception as e:
        logging.warning(f"format_gemini_markdown_to_telegram_html xatolik: {e}")
        return html.escape(text)


async def ask_gemini_ai(prompt: str, grade: str = "8") -> str:
    """Google Gemini AI orqali maktab biologiya darsliklari asosida savolga javob olish"""
    if not config.GEMINI_API_KEY:
        return (
            "⚠️ <b>Sun'iy intellekt (AI) API kaliti ulanmagan.</b>\n\n"
            "Admin tomonidan Google Gemini API kaliti sozlanishi kerak."
        )

    context = find_relevant_textbook_context(prompt, grade)

    system_prompt = (
        "Siz O'zbekiston Respublikasi umumiy o'rta ta'lim maktablarining biologiya fani darsliklari "
        "(5-, 6-, 7-, 8-, 9-, 10-, 11-sinf Botanika, Zoologiya, Odam va uning salomatligi, Sitologiya va Umumiy biologiya) "
        "bo'yicha rasmiy AI ustozisiz.\n\n"
        "QAT'IY QOIDALAR:\n"
        "1. Faqat va faqat O'zbekiston maktab biologiya darsliklari dasturidagi rasmiy ilmiy ma'lumotlar, formulalar, "
        "jadvallar, rasmlar mazmuni va darslik qoidalari asosida javob bering.\n"
        "2. Darslikdan tashqari boshqa fanlar yoki mavzular (siyosat, iqtisod, filmlar, IT, boshqa sohalar va hokazo) so'ralsa, "
        "yoki savol maktab biologiya dasturiga kiritilmagan bo'lsa, QAT'IY RAVISHDA quyidagicha javob bering:\n"
        "\"Kechirasiz, bu ma'lumot maktab biologiya darsligi dasturiga kiritilmagan. Men faqat O'zbekiston maktab biologiya darsliklari (6-, 8-, 9-, 11-sinf) asosida savollarga javob beraman.\"\n"
        "3. Javoblarni aniq, ilmiy va o'quvchiga tushunarli tilda bering.\n"
        "4. Agar biologik masala (DNK, oqsil, ATF, mitoz, meyoz, genetika) berilsa, uni bosqichma-bosqich: "
        "1) Berilgani, 2) Formulalar va qoidalar, 3) Yechish jarayoni, 4) Aniq javob ko'rinishida yozib bering.\n"
        "5. O'zbek tilida bexato va chiroyli tartibda yozing."
    )

    full_user_content = f"{system_prompt}\n\n"
    if context:
        full_user_content += f"--- DARSLIKDAN OSHIRILGAN MANBA VA KONTEKST ---\n{context}\n------------------------------------------\n\n"
    full_user_content += f"O'quvchi savoli / topshirig'i: {prompt}"

    import aiohttp
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_user_content}
                ]
            }
        ],
        "generationConfig": {
            "thinkingConfig": {
                "thinkingLevel": "low"
            },
            "maxOutputTokens": 2048,
            "temperature": 0.4
        }
    }

    # Eng tezkor va faol yangi modellar (javob berish vaqti 1-3 soniya)
    models_to_try = ["gemini-3.5-flash", "gemini-3.8-flash", "gemini-3.5-flash-lite"]
    last_error = ""

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={config.GEMINI_API_KEY}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, 
                    json=payload, 
                    headers={"Content-Type": "application/json"},
                    timeout=aiohttp.ClientTimeout(total=20, connect=8, sock_read=20)
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            # Fikrlash (thought) qismlarini chetlab o'tib, asosiy javob matnini olish
                            text_parts = [p.get("text", "") for p in parts if not p.get("thought", False) and p.get("text")]
                            if text_parts:
                                return "\n".join(text_parts).strip()
                            elif parts and parts[-1].get("text"):
                                return parts[-1].get("text").strip()
                        return "Kechirasiz, sun'iy intellektdan javob kelmadi."
                    else:
                        resp_text = await resp.text()
                        logging.warning(f"Gemini {model_name} xatolik berdi ({resp.status}): {resp_text[:120]}")
                        last_error = f"Status: {resp.status}"
        except Exception as e:
            logging.error(f"Gemini {model_name} ulanish xatoligi: {e}")
            last_error = str(e)

    return f"⚠️ Sun'iy intellekt bilan bog'lanishda vaqt tugadi ({last_error}). Iltimos qaytadan urinib ko'ring."


@dp.message(F.text == "🤖 AI Biologiya")
async def start_ai_mode(message: Message):
    """AI biologiya rejimi haqida ma'lumot"""
    text = (
        "🤖 <b>AI Biologiya — Sun'iy Intellekt Ustozingiz</b>\n\n"
        "Ushbu sun'iy intellekt faqat O'zbekiston maktab biologiya darsliklari (6-, 8-, 9-sinf) asosida ishlaydi.\n\n"
        "Menga biologiyadan istalgan savolingizni yoki masalangizni yozib yuboring:\n"
        "• <i>«Fotosintezning yorug'lik va qorong'ulik bosqichlari qanday farqlanadi?»</i>\n"
        "• <i>«Odamda qon bosimi qanday boshqariladi?»</i>\n"
        "• <i>Genetika masalalari matni (DNK, oqsil, ATF, mitoz, Mendel qonunlari)</i>\n\n"
        "✍️ <b>Savolingizni pastga yozib yuboring, men darslik asosida darhol tushuntirib beraman:</b>"
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
    "📖 Mavzular", "📝 Testlar", "📅 Haftalik Test", "📐 Masalalar",
    "🎥 Video darslar", "🧬 Animatsiyalar", "🏆 Reyting", "📊 Natijalar",
    "💳 Premium", "👨‍🏫 O'qituvchi", "🤖 AI Biologiya", "🔄 Sinfni almashtirish"
]

@dp.message(F.text & ~F.text.startswith("/") & ~F.text.in_(KNOWN_BUTTONS))
async def handle_user_free_text(message: Message):
    """Foydalanuvchi erkin savol yozganda AI orqali javob berish"""
    user = message.from_user
    user_id = user.id
    grade = await database.get_user_grade(user_id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    loading_msg = await message.answer("🤔 <i>Sun'iy intellekt darsliklar asosida javob tayyorlamoqda...</i>")

    try:
        raw_answer = await ask_gemini_ai(message.text, grade=grade)

        # Savol va javobni bazaga yozib borish (o'qituvchi hisoboti uchun)
        try:
            await database.record_ai_question(
                user_id=user_id,
                full_name=user.full_name or "Noma'lum",
                grade=grade,
                question=message.text,
                answer=raw_answer
            )
        except Exception as e:
            logging.error(f"AI savolini bazaga yozishda xatolik: {e}")

        formatted_answer = format_gemini_markdown_to_telegram_html(raw_answer)

        # Telegram xabari chegarasi (4096 belgi)
        if len(formatted_answer) > 4000:
            try:
                await loading_msg.delete()
            except Exception:
                pass
            for i in range(0, len(formatted_answer), 4000):
                chunk = formatted_answer[i:i+4000]
                try:
                    await message.answer(chunk, parse_mode="HTML")
                except Exception:
                    await message.answer(chunk, parse_mode=None)
        else:
            try:
                await loading_msg.edit_text(formatted_answer, parse_mode="HTML")
            except Exception as e:
                logging.warning(f"HTML formatlash xatoligi, parse_mode=None orqali yuborilmoqda: {e}")
                try:
                    await loading_msg.edit_text(raw_answer, parse_mode=None)
                except Exception as e2:
                    logging.error(f"Xabarni tahrirlashda xatolik: {e2}")
                    await message.answer(raw_answer, parse_mode=None)
    except Exception as e:
        logging.error(f"handle_user_free_text kutilmagan xatolik: {e}")
        try:
            await loading_msg.edit_text(
                "⚠️ Kechirasiz, javob tayyorlashda xatolik yuz berdi. Iltimos, savolingizni qaytadan yuboring.",
                parse_mode=None
            )
        except Exception:
            await message.answer(
                "⚠️ Kechirasiz, javob tayyorlashda xatolik yuz berdi. Iltimos, savolingizni qaytadan yuboring.",
                parse_mode=None
            )


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
