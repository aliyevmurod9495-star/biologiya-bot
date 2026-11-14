"""
titul_checker.py - Milliy Sertifikat (43 talik) Titul va Yozma Ishlarni (41-43)
AI Vision (Gemini 3 Flash) orqali to'liq tekshirish va baholash tizimi.
Tezkor, bitta so'rovli (Single-Shot) va optimallashgan arxitektura.
"""

import os
import sys
import io
import json
import base64
import sqlite3
import logging
import urllib.request
import urllib.error
from typing import Dict, Any, Optional, Tuple
from PIL import Image

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TitulChecker")

# Import config for GEMINI_API_KEY
try:
    from . import config
except ImportError:
    import config

DB_PATH = os.path.join(os.path.dirname(__file__), "bot_database.sqlite")
GEMINI_MODEL = "models/gemini-3-flash-preview"


# ==========================================================
# 1. MA'LUMOTLAR BAZASI (SQLITE) JADVALLARI VA DEFAULT KALITLAR
# ==========================================================

def init_milliy_db():
    """Milliy sertifikat test kalitlari va topshiriqlar jadvallarini yaratadi."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. Test kalitlari va mezonlar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS milliy_test_keys (
            test_code TEXT PRIMARY KEY,
            subject TEXT,
            title TEXT,
            keys_1_32 TEXT,       -- JSON: {"1": "A", "2": "C", ...}
            keys_33_35 TEXT,      -- JSON: {"33": "E", "34": "A", "35": "F"}
            keys_36_40 TEXT,      -- JSON: {"36": "24", "37": "1:2:1", ...}
            rubrics_41_43 TEXT,   -- JSON: mezonlar va namunaviy yechimlar
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 2. O'quvchilar topshirgan natijalar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS milliy_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            user_full_name TEXT,
            test_code TEXT,
            submission_type TEXT, -- 'titul_page_1' yoki 'written_work_41_43'
            score REAL,
            max_score REAL,
            percentage REAL,
            tier TEXT,
            detailed_results TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    # Namunaviy 8392004 (tituldagi kod) kalitlarini kiritamiz
    seed_default_keys(conn)
    conn.close()


def seed_default_keys(conn):
    """Standart test kalitlarini bazaga kiritadi."""
    cur = conn.cursor()
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392004'")
    if not cur.fetchone():
        keys_1_32 = {
            "1": "A", "2": "C", "3": "B", "4": "D", "5": "A", "6": "C", "7": "B",
            "8": "D", "9": "A", "10": "C", "11": "B", "12": "D", "13": "A", "14": "C",
            "15": "B", "16": "D", "17": "A", "18": "B", "19": "C", "20": "D", "21": "A",
            "22": "C", "23": "B", "24": "D", "25": "A", "26": "C", "27": "B", "28": "D",
            "29": "A", "30": "C", "31": "B", "32": "D"
        }
        keys_33_35 = {
            "33": "E", "34": "A", "35": "F"
        }
        keys_36_40 = {
            "36": "24",
            "37": "1:2:1",
            "38": "50",
            "39": "AaBb",
            "40": "1452000"
        }
        rubrics_41_43 = {
            "41": {
                "title": "Quyonlarda birikkan holda irsiylanish va krossingover",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Belgilar va ota-ona genotiplarini to'g'ri aniqlash (RRCCFF x rrccff)", "points": 2.0},
                    {"step": 2, "desc": "Gametalar va F1 genotipini to'g'ri yozish", "points": 2.0},
                    {"step": 3, "desc": "Qo'sh krossingover miqdorini (%) to'g'ri hisoblash (amaliy)", "points": 2.0},
                    {"step": 4, "desc": "Interferensiya miqdorini aniqlash", "points": 2.0},
                    {"step": 5, "desc": "C va F genlari orasidagi masofani (morganida) to'g'ri topish", "points": 2.0}
                ]
            },
            "42": {
                "title": "G'o'za o'simligida oraliq irsiylanish va tola rangi",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Tolaning novvotrang (Aa) va oq (aa) genotiplarini belgilash", "points": 2.5},
                    {"step": 2, "desc": "Chatishtirish sxemasi va Panet katagini to'g'ri tuzish", "points": 2.5},
                    {"step": 3, "desc": "Avlodlardagi fenotipik nisbatlarni to'g'ri hisoblash", "points": 2.5},
                    {"step": 4, "desc": "Yakuniy xulosani to'g'ri ifodalash", "points": 2.5}
                ]
            },
            "43": {
                "title": "Populyatsiya genetikasi va qon guruhlari taqsimoti (Hardy-Weinberg)",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "1-qon guruhli (OO) chastotasini (r^2) hisoblash", "points": 3.0},
                    {"step": 2, "desc": "r (O alleli) chastotasini ildizdan chiqarib aniqlash", "points": 3.0},
                    {"step": 3, "desc": "2-qon guruhli gomozigota (AA) orqali p (A alleli) chastotasini topish", "points": 3.0},
                    {"step": 4, "desc": "q (B alleli) chastotasini p+q+r=1 orqali aniqlash", "points": 3.0},
                    {"step": 5, "desc": "Aholi orasidagi geterozigota 3-qon guruh sonini hisoblash", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392004",
            "Biologiya",
            "Milliy Sertifikat Rasmiy Namunaviy Test 2025",
            json.dumps(keys_1_32),
            json.dumps(keys_33_35),
            json.dumps(keys_36_40),
            json.dumps(rubrics_41_43)
        ))
        conn.commit()


# ==========================================================
# 2. RASMNI SIQISH VA TEZKOR VISION SO'ROVI
# ==========================================================

def compress_image_for_ai(image_bytes: bytes, max_dim: int = 1500) -> bytes:
    """Rasmni sifatini yo'qotmagan holda optimal hajmga keltiradi (tezkor API uchun)."""
    try:
        img = Image.open(io.BytesIO(image_bytes))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > max_dim:
            ratio = max_dim / max(w, h)
            new_size = (int(w * ratio), int(h * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        out_buf = io.BytesIO()
        img.save(out_buf, format="JPEG", quality=85, optimize=True)
        return out_buf.getvalue()
    except Exception as e:
        logger.warning(f"Rasm siqishda xatolik (asl nusxa ishlatiladi): {e}")
        return image_bytes


# Yagona, universal va o'ta aniq tahlil prompti
MASTER_TITUL_PROMPT = """
Sen O'zbekiston Milliy sertifikatining rasmiy javoblar varaqasini (titul) va yozma ishlarni (41-43) tekshiruvchi mutaxassissan.
Rasmga qarab avval uning TURINI aniqla:

VARIANT A: Agar bu 1-bet (Javoblar varaqasi - OMR doirachali va katakchali 1-40) bo'lsa:
- "booklet_number": 7 xonali test kodi (masalan: 8392004).
- "student_name": Talabgor familiyasi va ismi.
- "bubble_answers": 1-32 savollardagi bo'yalgan doirachalar (A, B, C, D) va 33-35 dagi (A, B, C, D, E, F). Belgilanmagan bo'lsa null.
- "short_answers": 36-40 katakchalardagi qo'lyozma son/formula/nisbatlar.
Qat'iy format:
{
  "sheet_type": "titul_page_1",
  "booklet_number": "8392004",
  "student_name": "Familiya Ism",
  "bubble_answers": {"1": "A", "2": "B", ... "35": "F"},
  "short_answers": {"36": "24", "37": "1:2:1", "38": "50", "39": "AaBb", "40": "1452000"}
}

VARIANT B: Agar bu 41, 42 yoki 43-savollarning yozma ish daftari (katakli varaq) bo'lsa:
- "question_number": Savol raqami (41, 42 yoki 43).
- "student_name": Talabgor F.I.O.
- "descriptors": Yechimning qadamma-qadam deskriptor tahlili (har bir qadam uchun: step, title, earned_points, max_points, status: "correct"|"partial"|"incorrect", comment).
- "total_score": To'plangan umumiy ball (float).
- "max_score": Ushbu masala uchun maksimal ball (odatda 8.0 dan 15.0 gacha).
- "general_feedback": O'quvchiga tavsiya va xatolar izohi.
Qat'iy format:
{
  "sheet_type": "written_work",
  "question_number": 41,
  "student_name": "Familiya Ism",
  "descriptors": [
    {"step": 1, "title": "Genotiplar", "earned_points": 2.0, "max_points": 2.0, "status": "correct", "comment": "To'g'ri"},
    {"step": 2, "title": "Gametalar", "earned_points": 2.0, "max_points": 2.0, "status": "correct", "comment": "To'g'ri"}
  ],
  "total_score": 7.0,
  "max_score": 10.0,
  "general_feedback": "Yaxshi yechim..."
}

VARIANT C: Agar rasm Milliy sertifikat titul varaqasi ham, biologiya yozma ish daftari ham BO'LMASA (masalan, shaxsiy rasm, darslik sahifasi, tabiat rasmi va h.k.):
Qat'iy format:
{
  "sheet_type": "unknown",
  "reason": "Yuborilgan fotosurat Milliy sertifikat titul blanki yoki biologiya yozma ish daftari emas."
}
"""

def call_gemini_vision(image_bytes: bytes, prompt: str) -> Optional[dict]:
    """Gemini 3 Flash modeliga rasm va tizimli prompt yuborib, JSON javob oladi."""
    compressed_bytes = compress_image_for_ai(image_bytes)
    img_b64 = base64.b64encode(compressed_bytes).decode("utf-8")
    
    api_key = getattr(config, "GEMINI_API_KEY", "")
    if not api_key:
        logger.error("GEMINI_API_KEY topilmadi!")
        return None

    url = f"https://generativelanguage.googleapis.com/v1beta/{GEMINI_MODEL}:generateContent?key={api_key}"
    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": "image/jpeg", "data": img_b64}}
            ]
        }],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.1
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=65) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(raw_text)
    except Exception as e:
        logger.error(f"Gemini API chaqiruvida xatolik: {e}")
        return None


# ==========================================================
# 3. BALLARNI HISOBLASH VA MEZONIY DARAJA (A+, A, B...)
# ==========================================================

def calculate_tier(score: float, max_score: float) -> Tuple[str, str, float]:
    """Ballga qarab Milliy Sertifikat darajasini va izohini aniqlaydi."""
    percentage = (score / max_score) * 100 if max_score > 0 else 0
    
    if percentage >= 86.0:
        return "A+", "Oliy daraja (OTMga 100% maksimal ball imtiyozi! 🏆)", percentage
    elif percentage >= 80.0:
        return "A", "Yuqori daraja (A darajali imtiyozli sertifikat 🥇)", percentage
    elif percentage >= 70.0:
        return "B+", "Yaxshi daraja (B+ darajali sertifikat 🥈)", percentage
    elif percentage >= 60.0:
        return "B", "Qoniqarli daraja (B darajali sertifikat 🥉)", percentage
    elif percentage >= 50.0:
        return "C", "Quyi daraja (C darajali sertifikat)", percentage
    else:
        return "Qoniqarsiz", "Ball yetarli emas (Sertifikat berilmaydi)", percentage


def grade_titul_submission(extracted_data: dict) -> dict:
    """Tituldan olingan javoblarni bazadagi to'g'ri kalitlar bilan solishtirib ball hisoblaydi."""
    test_code = extracted_data.get("booklet_number", "8392004")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT keys_1_32, keys_33_35, keys_36_40 FROM milliy_test_keys WHERE test_code = ?", (test_code,))
    row = cur.fetchone()
    
    if not row:
        cur.execute("SELECT keys_1_32, keys_33_35, keys_36_40 FROM milliy_test_keys WHERE test_code = '8392004'")
        row = cur.fetchone()
    conn.close()

    correct_1_32 = json.loads(row[0]) if row else {}
    correct_33_35 = json.loads(row[1]) if row else {}
    correct_36_40 = json.loads(row[2]) if row else {}

    student_bubbles = extracted_data.get("bubble_answers", {})
    student_short = extracted_data.get("short_answers", {})

    total_score = 0.0
    max_score = 0.0
    correct_count = 0
    incorrect_count = 0
    details = []

    # 1 - 32 savollar (har biri 1.5 ball -> jami 48 ball)
    for q_num in range(1, 33):
        q_str = str(q_num)
        max_score += 1.5
        c_ans = correct_1_32.get(q_str, "").strip().upper()
        s_ans = str(student_bubbles.get(q_str, "") or "").strip().upper()

        if s_ans and s_ans == c_ans:
            total_score += 1.5
            correct_count += 1
            details.append({"q": q_str, "status": "correct", "student": s_ans, "correct": c_ans, "points": 1.5})
        else:
            incorrect_count += 1
            details.append({"q": q_str, "status": "incorrect", "student": s_ans or "Belgilanmagan", "correct": c_ans, "points": 0.0})

    # 33 - 35 savollar (har biri 2.0 ball -> jami 6 ball)
    for q_num in range(33, 36):
        q_str = str(q_num)
        max_score += 2.0
        c_ans = correct_33_35.get(q_str, "").strip().upper()
        s_ans = str(student_bubbles.get(q_str, "") or "").strip().upper()

        if s_ans and s_ans == c_ans:
            total_score += 2.0
            correct_count += 1
            details.append({"q": q_str, "status": "correct", "student": s_ans, "correct": c_ans, "points": 2.0})
        else:
            incorrect_count += 1
            details.append({"q": q_str, "status": "incorrect", "student": s_ans or "Belgilanmagan", "correct": c_ans, "points": 0.0})

    # 36 - 40 savollar (har biri 2.5 ball -> jami 12.5 ball)
    for q_num in range(36, 41):
        q_str = str(q_num)
        max_score += 2.5
        c_ans = str(correct_36_40.get(q_str, "")).strip().lower().replace(" ", "")
        s_ans = str(student_short.get(q_str, "") or "").strip().lower().replace(" ", "")

        if s_ans and s_ans == c_ans:
            total_score += 2.5
            correct_count += 1
            details.append({"q": q_str, "status": "correct", "student": s_ans, "correct": c_ans, "points": 2.5})
        else:
            incorrect_count += 1
            details.append({"q": q_str, "status": "incorrect", "student": s_ans or "Yozilmagan", "correct": c_ans, "points": 0.0})

    tier, tier_desc, percentage = calculate_tier(total_score, max_score)

    return {
        "test_code": test_code,
        "student_name": extracted_data.get("student_name", "Talabgor"),
        "total_score": round(total_score, 1),
        "max_score": round(max_score, 1),
        "percentage": round(percentage, 1),
        "tier": tier,
        "tier_desc": tier_desc,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "details": details
    }


# ==========================================================
# 4. TELEGRAM XABAR FORMATLOVCHILARI
# ==========================================================

def format_titul_result_message(result: dict) -> str:
    """Titul tekshiruv natijasini chiroyli Telegram xabariga aylantiradi."""
    lines = [
        f"📋 <b>MILLIY SERTIFIKAT TEST NATIJASI #{result['test_code']}</b>",
        f"👤 <b>Talabgor:</b> {result['student_name']}",
        f"🔬 <b>Fan:</b> Biologiya (Milliy Standart)",
        "",
        "📊 <b>NATIJALAR XULOSASI:</b>",
        f"• To'g'ri javoblar: <b>{result['correct_count']} ta</b> ✅",
        f"• Noto'g'ri/Bo'sh: <b>{result['incorrect_count']} ta</b> ❌",
        f"• Umumiy ball: <b>{result['total_score']} / {result['max_score']} ball</b>",
        f"• Foiz ko'rsatkichi: <b>{result['percentage']}%</b>",
        "",
        f"🎖 <b>SERTIFIKAT DARAJASI:</b> <b>[{result['tier']}]</b>",
        f"<i>{result['tier_desc']}</i>",
        "",
        "🔍 <b>SAVOLLAR BO'YICHA TAHLIL:</b>"
    ]

    incorrect_list = [d for d in result["details"] if d["status"] == "incorrect"]
    if incorrect_list:
        lines.append("❌ <b>Xato qilingan savollar:</b>")
        for item in incorrect_list[:10]:
            lines.append(f"  • <b>№ {item['q']}:</b> Sizniki: <code>{item['student']}</code> | To'g'ri: <code>{item['correct']}</code>")
        if len(incorrect_list) > 10:
            lines.append(f"  <i>...va yana {len(incorrect_list) - 10} ta savol.</i>")
    else:
        lines.append("🎉 <b>Barcha savollarga to'liq to'g'ri javob berilgan! Qoyilmaqom!</b>")

    lines.extend([
        "",
        "⚠️ <b>Eslatma:</b> Ushbu ball 1–40 testlar bo'yicha hisoblandi.",
        "41, 42, 43-savollar (yozma ish) bahosini olish uchun daftardagi yechim rasmini jo'nating! 📸"
    ])

    return "\n".join(lines)


def format_written_result_message(eval_data: dict) -> str:
    """Yozma ish (41-43) natijasini chiroyli xabarga aylantiradi."""
    q_num = eval_data.get("question_number", 41)
    t_score = eval_data.get("total_score", 0.0)
    m_score = eval_data.get("max_score", 10.0)
    perc = (t_score / m_score) * 100 if m_score > 0 else 0

    lines = [
        f"✍️ <b>YOZMA ISH BAHOLASH NATIJASI: {q_num}-SAVOL</b>",
        f"👤 <b>Talabgor:</b> {eval_data.get('student_name', 'Talabgor')}",
        "",
        f"🎯 <b>To'plangan ball:</b> <b>{t_score} / {m_score} ball</b> ({perc:.1f}%)",
        "",
        "📝 <b>QADAMMA-QADAM DESKRIPTOR TAHLILI:</b>"
    ]

    for d in eval_data.get("descriptors", []):
        icon = "✅" if d.get("status") == "correct" else ("⚠️" if d.get("status") == "partial" else "❌")
        lines.append(
            f"{icon} <b>{d.get('step')}-qadam: {d.get('title')}</b>\n"
            f"   Ball: <b>{d.get('earned_points')}/{d.get('max_points')}</b> | <i>{d.get('comment')}</i>"
        )

    if eval_data.get("general_feedback"):
        lines.extend([
            "",
            "💡 <b>AI EKSPERT MASLAHATI:</b>",
            f"<i>{eval_data['general_feedback']}</i>"
        ])

    return "\n".join(lines)


# ==========================================================
# 5. UNIVERSAL RASM TEKSHIRUV ENTRYPOINTI
# ==========================================================

def process_titul_image(image_bytes: bytes) -> Tuple[str, str, dict]:
    """
    Rasm qabul qilib, bitta tezkor Vision so'rovi orqali uning 1-bet (OMR) yoki
    Yozma ish (41-43) ekanligini aniqlaydi va tayyor natijani beradi.
    """
    logger.info("Rasm Gemini 3 Flash orqali tahlil qilinmoqda...")
    extracted = call_gemini_vision(image_bytes, MASTER_TITUL_PROMPT)
    if not extracted:
        return "error", "❌ Rasmni tahlil qilishda xatolik yuz berdi. Iltimos, rasmni tiniqroq qilib qayta yuboring.", {}

    sheet_type = extracted.get("sheet_type", "titul_page_1")
    
    if sheet_type == "unknown":
        logger.info("Rasm titul yoki yozma ish emas deb topildi.")
        msg_text = (
            "ℹ️ <b>Yuborilgan fotosurat tanilmadi</b>\n\n"
            f"<i>{extracted.get('reason', 'Ushbu rasm Milliy sertifikat titul varaqasi yoki yozma ish daftari emas.')}</i>\n\n"
            "💡 <b>To'g'ri tekshirtirish uchun:</b>\n"
            "• Milliy sertifikat rasmiy 43 talik javoblar varaqasi (titul)ni to'ldirib, rasmga olib yuboring.\n"
            "• Yoki 41, 42, 43-masalalarning daftardagi qo'lyozma yechimini rasmga olib yuboring.\n"
            "• Titul blanki yo'q bo'lsa, /sertifikat menyusidan yuklab oling!"
        )
        return "unknown", msg_text, extracted
    elif sheet_type == "written_work":
        logger.info("Yozma ish (41-43) natijasi formatlanmoqda...")
        msg_text = format_written_result_message(extracted)
        return "written_work", msg_text, extracted
    else:
        logger.info("Titul 1-bet natijasi solishtirilmoqda...")
        grade_res = grade_titul_submission(extracted)
        msg_text = format_titul_result_message(grade_res)
        return "titul_page_1", msg_text, grade_res


if __name__ == "__main__":
    init_milliy_db()
    print("Milliy DB initialized.")
