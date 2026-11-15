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
        # Variant 1 saqlandi
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392004",
            "Biologiya",
            "1-Namunaviy Variant (Rasmiy 2025/2026)",
            json.dumps(keys_1_32),
            json.dumps(keys_33_35),
            json.dumps(keys_36_40),
            json.dumps(rubrics_41_43)
        ))
        conn.commit()

    # 2-VARIANTNI TEKSHIRISH VA KIRITISH (8392005)
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392005'")
    if not cur.fetchone():
        keys_1_32_v2 = {
            "1": "B", "2": "D", "3": "A", "4": "C", "5": "B", "6": "D", "7": "A",
            "8": "C", "9": "B", "10": "D", "11": "A", "12": "C", "13": "B", "14": "D",
            "15": "A", "16": "C", "17": "B", "18": "D", "19": "A", "20": "C", "21": "B",
            "22": "D", "23": "A", "24": "C", "25": "B", "26": "D", "27": "A", "28": "C",
            "29": "B", "30": "D", "31": "A", "32": "C"
        }
        keys_33_35_v2 = {"33": "C", "34": "D", "35": "B"}
        keys_36_40_v2 = {
            "36": "1500",
            "37": "17",
            "38": "1:1:1:1",
            "39": "Bb",
            "40": "364500"
        }
        rubrics_41_43_v2 = {
            "41": {
                "title": "Itlarda birikkan holda irsiylanish (S, B, L) va koensidensiya",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Ota-ona genotiplarini (SSBBLL x ssbbll) va fenotiplarini to'g'ri yozish", "points": 2.0},
                    {"step": 2, "desc": "F1 gametalari va tahliliy chatishtirish sxemasi", "points": 2.0},
                    {"step": 3, "desc": "Amaliy krossingover foizini to'g'ri hisoblash", "points": 2.0},
                    {"step": 4, "desc": "S va B genlari orasidagi masofani (morgan) aniqlash", "points": 2.0},
                    {"step": 5, "desc": "Koensidensiya va interferensiya miqdorini aniqlash", "points": 2.0}
                ]
            },
            "42": {
                "title": "Drozofila meva pashshasida komplementar ko'z rangi va birikkan irsiylanish",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Komplementar genotiplarni (C_D_, C_dd, ccD_, ccdd) to'g'ri belgilash", "points": 2.5},
                    {"step": 2, "desc": "Kulrang/qora tana va uzun/kalta qanot 17% krossingoverini hisoblash", "points": 2.5},
                    {"step": 3, "desc": "F1 dagi 12000 ta avlod orasidan so'ralgan genotiplarni aniqlash", "points": 2.5},
                    {"step": 4, "desc": "Kalta qanotli pashshalar orasidagi qizil ko'zlilar foizini hisoblash", "points": 2.5}
                ]
            },
            "43": {
                "title": "Zomin aholisida soch rangi oraliq irsiylanishi (Hardy-Weinberg)",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "BB (qora), Bb (malla), bb (sarg'imtir) genotiplarini ifodalash", "points": 3.0},
                    {"step": 2, "desc": "Jami 1.8 mln aholidan qora+malla orqali q^2 (bb) chastotasini topish", "points": 3.0},
                    {"step": 3, "desc": "q (sarg'imtir allel) va p (qora allel) chastotasini aniqlash", "points": 3.0},
                    {"step": 4, "desc": "Populyatsiyadagi geterozigota (Bb) malla sochlilar sonini hisoblash", "points": 3.0},
                    {"step": 5, "desc": "Gomozigota (BB va bb) insonlar soni va foizini to'g'ri hisoblash", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392005",
            "Biologiya",
            "2-Namunaviy Variant (Mock Sinov 2025)",
            json.dumps(keys_1_32_v2),
            json.dumps(keys_33_35_v2),
            json.dumps(keys_36_40_v2),
            json.dumps(rubrics_41_43_v2)
        ))
        conn.commit()

    # 3-VARIANTNI TEKSHIRISH VA KIRITISH (8392006)
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392006'")
    if not cur.fetchone():
        keys_1_32_v3 = {
            "1": "C", "2": "A", "3": "D", "4": "B", "5": "C", "6": "A", "7": "D",
            "8": "B", "9": "C", "10": "A", "11": "D", "12": "B", "13": "C", "14": "A",
            "15": "D", "16": "B", "17": "C", "18": "A", "19": "D", "20": "B", "21": "C",
            "22": "A", "23": "D", "24": "B", "25": "C", "26": "A", "27": "D", "28": "B",
            "29": "C", "30": "A", "31": "D", "32": "B"
        }
        keys_33_35_v3 = {"33": "A", "34": "C", "35": "D"}
        keys_36_40_v3 = {
            "36": "250",
            "37": "9:3:3:1",
            "38": "12.5",
            "39": "CcDd",
            "40": "288000"
        }
        rubrics_41_43_v3 = {
            "41": {
                "title": "Kaputsin maymunlarida uch nuqtali krossingover (A, B, L)",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Keng qo'llar, yirik bosh va uzun oyoqlar genotiplarini yozish", "points": 2.0},
                    {"step": 2, "desc": "F1 duragaylarining tahliliy chatishtirish natijalarini guruhlash", "points": 2.0},
                    {"step": 3, "desc": "Yakka va qo'sh krossingover avlodlarini aniqlash", "points": 2.0},
                    {"step": 4, "desc": "Genlar xromosomadagi ketma-ketligi va masofalarini topish", "points": 2.0},
                    {"step": 5, "desc": "Interferensiya koeffitsientini hisoblash", "points": 2.0}
                ]
            },
            "42": {
                "title": "G'o'zada polimer irsiylanish va tola hosildorligi",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Polimer genlar (A1A1A2A2) ifodasini belgilash", "points": 2.5},
                    {"step": 2, "desc": "F2 da fenotipik nisbatlar va ajralishlarni hisoblash", "points": 2.5},
                    {"step": 3, "desc": "Geterozigota genotipli o'simliklar ulushini aniqlash", "points": 2.5},
                    {"step": 4, "desc": "Nazariy hosildorlik ko'rsatkichlarini hisoblash", "points": 2.5}
                ]
            },
            "43": {
                "title": "Aholi populyatsiyasida rezus omil va qon guruhlari taqsimoti",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "Rh+ va Rh- allellarining populyatsiyadagi chastotasini topish", "points": 3.0},
                    {"step": 2, "desc": "ABO tizimi bo'yicha p, q, r chastotalarini aniqlash", "points": 3.0},
                    {"step": 3, "desc": "Rezus-manfiy 1-qon guruhli insonlar sonini hisoblash", "points": 3.0},
                    {"step": 4, "desc": "Geterozigota Rh+ insonlar sonini hisoblash", "points": 3.0},
                    {"step": 5, "desc": "Yakuniy genetik tahlil va xulosani ifodalash", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392006",
            "Biologiya",
            "3-Namunaviy Variant (Diagnostik 2025)",
            json.dumps(keys_1_32_v3),
            json.dumps(keys_33_35_v3),
            json.dumps(keys_36_40_v3),
            json.dumps(rubrics_41_43_v3)
        ))
        conn.commit()

    # 4-VARIANT (8392007)
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392007'")
    if not cur.fetchone():
        keys_1_32_v4 = {
            "1": "A", "2": "B", "3": "C", "4": "D", "5": "A", "6": "B", "7": "C",
            "8": "D", "9": "A", "10": "B", "11": "C", "12": "D", "13": "A", "14": "B",
            "15": "C", "16": "D", "17": "A", "18": "B", "19": "C", "20": "D", "21": "A",
            "22": "B", "23": "C", "24": "D", "25": "A", "26": "B", "27": "C", "28": "D",
            "29": "A", "30": "B", "31": "C", "32": "D"
        }
        keys_33_35_v4 = {"33": "B", "34": "E", "35": "A"}
        keys_36_40_v4 = {"36": "8000", "37": "9:3:3:1", "38": "60000", "39": "AaBb", "40": "3600"}
        rubrics_41_43_v4 = {
            "41": {
                "title": "Populyatsiyada oyoq uzunligi va tana genetikasi",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "F va f genlari, ota-ona genotiplarini to'g'ri ifodalash", "points": 2.5},
                    {"step": 2, "desc": "Populyatsiyadagi genotipik sinflar va avlodlar taqsimoti", "points": 2.5},
                    {"step": 3, "desc": "Amaliy va nazariy ko'rsatkichlarni solishtirish", "points": 2.5},
                    {"step": 4, "desc": "Yakuniy xulosani to'g'ri yozish", "points": 2.5}
                ]
            },
            "42": {
                "title": "Tovuqlarda toj shaklining komplementar irsiylanishi",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "A-B (yong'oqsimon), A-bb (atirgul), aaB- (no'xat), aabb (oddiy) genotiplari", "points": 2.5},
                    {"step": 2, "desc": "Chatishtirish sxemasi va Panet katagini tuzish", "points": 2.5},
                    {"step": 3, "desc": "Avlodlar fenotipik nisbatlarini aniqlash (9:3:3:1)", "points": 2.5},
                    {"step": 4, "desc": "So'ralgan toj shakllari foizini hisoblash", "points": 2.5}
                ]
            },
            "43": {
                "title": "Aholi genetikasi: ko'z shakli (Hardy-Weinberg qonuniyati)",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "60000 kishilik aholidan q^2 (aa) chastotasini aniqlash", "points": 3.0},
                    {"step": 2, "desc": "q (retsessiv) va p (dominant) allellar chastotasini topish", "points": 3.0},
                    {"step": 3, "desc": "Geterozigota (Aa) insonlar sonini hisoblash (2pq * N)", "points": 3.0},
                    {"step": 4, "desc": "Gomozigota (AA) insonlar sonini hisoblash (p^2 * N)", "points": 3.0},
                    {"step": 5, "desc": "Yakuniy populyatsion xulosani asoslash", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392007",
            "Biologiya",
            "4-Namunaviy Variant (Shernazarov & Azimov)",
            json.dumps(keys_1_32_v4),
            json.dumps(keys_33_35_v4),
            json.dumps(keys_36_40_v4),
            json.dumps(rubrics_41_43_v4)
        ))
        conn.commit()

    # 5-VARIANT (8392008)
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392008'")
    if not cur.fetchone():
        keys_1_32_v5 = {
            "1": "D", "2": "C", "3": "B", "4": "A", "5": "D", "6": "C", "7": "B",
            "8": "A", "9": "D", "10": "C", "11": "B", "12": "A", "13": "D", "14": "C",
            "15": "B", "16": "A", "17": "D", "18": "C", "19": "B", "20": "A", "21": "D",
            "22": "C", "23": "B", "24": "A", "25": "D", "26": "C", "27": "B", "28": "A",
            "29": "D", "30": "C", "31": "B", "32": "A"
        }
        keys_33_35_v5 = {"33": "F", "34": "B", "35": "E"}
        keys_36_40_v5 = {"36": "120", "37": "50%", "38": "1:2:1", "39": "XDY", "40": "25000"}
        rubrics_41_43_v5 = {
            "41": {
                "title": "Zebralarda birikkan holda irsiylanish (D, E genlari)",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Katta oyoq (D) va katta peshona (E) genotiplarini yozish", "points": 2.5},
                    {"step": 2, "desc": "Gametalar va birikish guruhlarini tahlil qilish", "points": 2.5},
                    {"step": 3, "desc": "Krossingover foizi va masofani aniqlash", "points": 2.5},
                    {"step": 4, "desc": "F2 fenotipik nisbatlarini hisoblash", "points": 2.5}
                ]
            },
            "42": {
                "title": "Daltonizm, gemofiliya (jinsiy xromosoma) va braxidaktiliya",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "X^dH va X^Dh genotiplarini to'g'ri belgilash", "points": 2.5},
                    {"step": 2, "desc": "Ota-ona fenotipi va nikoh sxemasini tuzish", "points": 2.5},
                    {"step": 3, "desc": "Farzandlarda kasalliklar namoyon bo'lish ehtimolini hisoblash", "points": 2.5},
                    {"step": 4, "desc": "Sog'lom va tashuvchi qizlar nisbatini aniqlash", "points": 2.5}
                ]
            },
            "43": {
                "title": "Garvy formulasi bo'yicha populyatsiyada kasallik tarqalishi",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "Populyatsiya ko'rsatkichlari va Garvy formulasi qoidasi", "points": 3.0},
                    {"step": 2, "desc": "Vaksina qilinishi lozim bo'lgan qatlamni hisoblash", "points": 3.0},
                    {"step": 3, "desc": "Kasallik tarqalish darajasi va koeffitsientini topish", "points": 3.0},
                    {"step": 4, "desc": "Jami himoyalangan organizmlar foizini aniqlash", "points": 3.0},
                    {"step": 5, "desc": "Epifitologik/epidemiologik xulosa berish", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392008",
            "Biologiya",
            "5-Namunaviy Variant (Milliy Sertifikat 2025)",
            json.dumps(keys_1_32_v5),
            json.dumps(keys_33_35_v5),
            json.dumps(keys_36_40_v5),
            json.dumps(rubrics_41_43_v5)
        ))
        conn.commit()

    # 6-VARIANT (8392009)
    cur.execute("SELECT test_code FROM milliy_test_keys WHERE test_code = '8392009'")
    if not cur.fetchone():
        keys_1_32_v6 = {
            "1": "B", "2": "C", "3": "A", "4": "D", "5": "B", "6": "C", "7": "A",
            "8": "D", "9": "B", "10": "C", "11": "A", "12": "D", "13": "B", "14": "C",
            "15": "A", "16": "D", "17": "B", "18": "C", "19": "A", "20": "D", "21": "B",
            "22": "C", "23": "A", "24": "D", "25": "B", "26": "C", "27": "A", "28": "D",
            "29": "B", "30": "C", "31": "A", "32": "D"
        }
        keys_33_35_v6 = {"33": "C", "34": "F", "35": "B"}
        keys_36_40_v6 = {"36": "16", "37": "256", "38": "800", "39": "AaBbCc", "40": "320"}
        rubrics_41_43_v6 = {
            "41": {
                "title": "Sut emizuvchilarda poligen va polimer genotiplar tahlili",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "AaBbCcDE genotipidan 16 xil gameta hosil bo'lishini ko'rsatish", "points": 2.5},
                    {"step": 2, "desc": "Ota-ona chatishtirishidagi genotipik sinflar soni (2^n)", "points": 2.5},
                    {"step": 3, "desc": "Retsessiv gomozigotalar va geterozigotalar nisbati", "points": 2.5},
                    {"step": 4, "desc": "F1 avlod tahlilini yakunlash", "points": 2.5}
                ]
            },
            "42": {
                "title": "Interferon oqsili hosil bo'lishi va irsiylanish",
                "max_score": 10.0,
                "descriptors": [
                    {"step": 1, "desc": "Interferon (A) va hosil bo'lmaslik (a) genotiplarini yozish", "points": 2.5},
                    {"step": 2, "desc": "Autosoma bo'yicha ajralishlar va ehtimolliklar", "points": 2.5},
                    {"step": 3, "desc": "Serologik tahlillar va avlodlar sog'lomlik darajasi", "points": 2.5},
                    {"step": 4, "desc": "Nazariy xulosa chiqarish", "points": 2.5}
                ]
            },
            "43": {
                "title": "Tropik o'rmon populyatsiyasi: pat ranglari (R/r)",
                "max_score": 15.0,
                "descriptors": [
                    {"step": 1, "desc": "800 ta qushdan dominant (R) va retsessiv (r) pat chastotasini topish", "points": 3.0},
                    {"step": 2, "desc": "Tillarang va havorang patli organizmlar sonini hisoblash", "points": 3.0},
                    {"step": 3, "desc": "Geterozigota (Rr) organizmlar sonini aniqlash", "points": 3.0},
                    {"step": 4, "desc": "Populyatsion muvozanatni tahlil qilish", "points": 3.0},
                    {"step": 5, "desc": "Biogeotsenotik xulosa berish", "points": 3.0}
                ]
            }
        }
        cur.execute("""
            INSERT INTO milliy_test_keys 
            (test_code, subject, title, keys_1_32, keys_33_35, keys_36_40, rubrics_41_43)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "8392009",
            "Biologiya",
            "6-Namunaviy Variant (Murakkab Sinov 2025)",
            json.dumps(keys_1_32_v6),
            json.dumps(keys_33_35_v6),
            json.dumps(keys_36_40_v6),
            json.dumps(rubrics_41_43_v6)
        ))
        conn.commit()


def get_all_variants() -> list:
    """Bazadagi barcha Milliy Sertifikat variantlari ro'yxatini qaytaradi."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT test_code, title, subject FROM milliy_test_keys ORDER BY test_code ASC")
    rows = cur.fetchall()
    conn.close()
    return [{"test_code": r[0], "title": r[1], "subject": r[2]} for r in rows]


def get_variant_rubrics(test_code: str) -> dict:
    """Variantning rasmiy mezonlari va sarlavhasini qaytaradi."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT rubrics_41_43, title FROM milliy_test_keys WHERE test_code = ?", (test_code,))
    row = cur.fetchone()
    conn.close()
    if row and row[0]:
        try:
            return {"title": row[1], "rubrics": json.loads(row[0])}
        except Exception:
            pass
    return {}


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


def build_titul_prompt(expected_code: Optional[str] = None) -> str:
    """Variant kodi asosida dinamik va 100% aniq prompt tuzadi."""
    prompt = MASTER_TITUL_PROMPT
    if expected_code:
        v_info = get_variant_rubrics(expected_code)
        if v_info and v_info.get("rubrics"):
            r_dict = v_info.get("rubrics", {})
            rubrics_desc = f"\n\nDIQQAT! Foydalanuvchi aynan {expected_code} ({v_info.get('title')}) variantini topshirmoqda!\n"
            rubrics_desc += "Agar rasm 41, 42 yoki 43-savollarning yozma ishi bo'lsa, qat'iy ravishda quyidagi rasmiy mezonlar va to'g'ri yechim bo'yicha bahola:\n"
            for q_num, q_data in r_dict.items():
                rubrics_desc += f"\nSavol {q_num}: {q_data.get('title')} (Maksimal: {q_data.get('max_score')} ball):\n"
                for step in q_data.get("descriptors", []):
                    rubrics_desc += f"  - {step.get('step')}-qadam: {step.get('desc')} ({step.get('points')} ball)\n"
            prompt += rubrics_desc
    return prompt


# ==========================================================
# 5. UNIVERSAL RASM TEKSHIRUV ENTRYPOINTI
# ==========================================================

def process_titul_image(image_bytes: bytes, expected_test_code: Optional[str] = None) -> Tuple[str, str, dict]:
    """
    Rasm qabul qilib, bitta tezkor Vision so'rovi orqali uning 1-bet (OMR) yoki
    Yozma ish (41-43) ekanligini aniqlaydi va tayyor natijani beradi.
    Agar expected_test_code berilsa, aynan o'sha variant mezonlari bilan tekshiradi.
    """
    logger.info(f"Rasm Gemini 3 Flash orqali tahlil qilinmoqda (Variant: {expected_test_code or 'Avtomatik'})...")
    custom_prompt = build_titul_prompt(expected_test_code)
    extracted = call_gemini_vision(image_bytes, custom_prompt)
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
        if expected_test_code:
            extracted["test_code"] = expected_test_code
        msg_text = format_written_result_message(extracted)
        return "written_work", msg_text, extracted
    else:
        logger.info("Titul 1-bet natijasi solishtirilmoqda...")
        if expected_test_code and not extracted.get("booklet_number"):
            extracted["booklet_number"] = expected_test_code
        grade_res = grade_titul_submission(extracted)
        msg_text = format_titul_result_message(grade_res)
        return "titul_page_1", msg_text, grade_res


# ==========================================================
# 6. ADMIN MONITORING VA STATISTIKA FUNKSIYALARI
# ==========================================================

def get_milliy_stats() -> dict:
    """Milliy sertifikat bo'yicha umumiy statistika va so'nggi topshiriqlar."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute("SELECT count(*) FROM milliy_submissions")
    total = cur.fetchone()[0] or 0
    
    cur.execute("SELECT count(*) FROM milliy_submissions WHERE submission_type = 'titul_page_1'")
    titul_count = cur.fetchone()[0] or 0
    
    cur.execute("SELECT count(*) FROM milliy_submissions WHERE submission_type = 'written_work'")
    written_count = cur.fetchone()[0] or 0

    cur.execute("SELECT tier, count(*) FROM milliy_submissions WHERE tier IS NOT NULL AND tier != '' GROUP BY tier")
    tier_counts = dict(cur.fetchall())
    
    cur.execute("""
        SELECT user_id, user_full_name, test_code, submission_type, score, max_score, percentage, tier, created_at
        FROM milliy_submissions
        ORDER BY id DESC LIMIT 10
    """)
    recent = cur.fetchall()
    conn.close()

    return {
        "total": total,
        "titul_count": titul_count,
        "written_count": written_count,
        "tier_counts": tier_counts,
        "recent": [
            {
                "user_id": r[0],
                "user_name": r[1] or "Talabgor",
                "test_code": r[2] or "Noma'lum",
                "type": r[3] or "titul",
                "score": r[4] or 0.0,
                "max_score": r[5] or 100.0,
                "percentage": r[6] or 0.0,
                "tier": r[7] or "-",
                "date": str(r[8])[:16] if r[8] else ""
            }
            for r in recent
        ]
    }


def get_milliy_submissions_by_user(user_id: int) -> list:
    """Muayyan o'quvchining barcha topshiriqlari tarixi."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT test_code, submission_type, score, max_score, percentage, tier, created_at
        FROM milliy_submissions
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [
        {
            "test_code": r[0],
            "type": r[1],
            "score": r[2],
            "max_score": r[3],
            "percentage": r[4],
            "tier": r[5],
            "date": str(r[6])[:16] if r[6] else ""
        }
        for r in rows
    ]


if __name__ == "__main__":
    init_milliy_db()
    print("Milliy DB initialized.")
