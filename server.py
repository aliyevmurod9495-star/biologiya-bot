# -*- coding: utf-8 -*-
"""
BioMaster Pro — Telegram Mini App (TMA) API va Veb Serveri.
100% mustaqil, aiohttp asosida yozilgan: mavjud bot_database.sqlite, materials.py va questions.json bilan
100% xavfsiz ishlaydi, qo'shimcha tashqi kutubxonalarsiz ishlaydi.
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

from aiohttp import web

# biologiya_test_bot yo'lini qo'shish
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if BOT_DIR not in sys.path:
    sys.path.insert(0, BOT_DIR)

import materials

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BioMasterWebApp")

# Ma'lumotlarni yuklash
QUESTIONS_FILE = os.path.join(BOT_DIR, "questions.json")
YOPIQ_FILE = os.path.join(BOT_DIR, "yopiq_tests.json")

def load_json(filepath: str) -> Any:
    if not os.path.exists(filepath):
        logger.warning(f"Fayl topilmadi: {filepath}")
        return {}
    with open(filepath, "r", encoding="utf-8-sig") as f:
        return json.load(f)

QUESTIONS_DATA = load_json(QUESTIONS_FILE)
YOPIQ_DATA = load_json(YOPIQ_FILE)

# 7 ta sinf ma'lumotlari (pastdan yuqoriga qat'iy tartibda)
GRADES_METADATA = [
    {
        "id": "5",
        "name": "5-sinf: Botanika boshlang‘ich",
        "badge": "Boshlang‘ich kurs",
        "desc": "O‘simliklar dunyosi bilan tanishuv, tabiat bilan uyg‘unlik",
        "icon": "🌿",
        "color": "emerald"
    },
    {
        "id": "6",
        "name": "6-sinf: Botanika",
        "badge": "Gulli o‘simliklar",
        "desc": "Vegetativ va generativ organlar, o‘simliklar oilalari",
        "icon": "🌻",
        "color": "yellow"
    },
    {
        "id": "7",
        "name": "7-sinf: Zoologiya",
        "badge": "2026 Yangi Darslik",
        "desc": "Sodda bir hujayralilar, umurtqasizlar va xordalilar",
        "icon": "🐾",
        "color": "blue"
    },
    {
        "id": "8",
        "name": "8-sinf: Odam anatomiyasi",
        "badge": "2026 Yangi Darslik",
        "desc": "Odam organizmi, qon aylanish, nerv va endokrin tizim",
        "icon": "🫀",
        "color": "rose"
    },
    {
        "id": "9",
        "name": "9-sinf: Sitologiya",
        "badge": "2026 Yangi Darslik",
        "desc": "Hujayra darajasidagi hayot, to‘qimalar, ko‘payish",
        "icon": "🔬",
        "color": "purple"
    },
    {
        "id": "10",
        "name": "10-sinf: Biologiya",
        "badge": "2025 Yangi Darslik",
        "desc": "Molekulyar biologiya, Biokimyo, Sitologiya, Genetika",
        "icon": "🧬",
        "color": "emerald"
    },
    {
        "id": "11",
        "name": "11-sinf: Biologiya",
        "badge": "DTM Asosiy Bazasi",
        "desc": "Evolyutsiya ta’limoti, Ekologiya, Biosfera va biogeotsenoz",
        "icon": "🌍",
        "color": "cyan"
    }
]

# NATIVE CORS MIDDLEWARE
@web.middleware
async def cors_middleware(request: web.Request, handler):
    if request.method == "OPTIONS":
        response = web.Response()
    else:
        response = await handler(request)
    
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
    return response

# API HANDLERS

async def api_get_grades(request: web.Request) -> web.Response:
    """Barcha 7 ta sinf ro'yxati va statistikasini qaytaradi"""
    grades = []
    for g in GRADES_METADATA:
        gid = g["id"]
        topics_count = len(materials.TOPICS_CONTENT.get(gid, []))
        q_topics = QUESTIONS_DATA.get(gid, {}).get("topics", [])
        total_questions = sum(len(t.get("questions", [])) for t in q_topics)
        
        grades.append({
            **g,
            "topics_count": topics_count,
            "questions_count": total_questions
        })
    return web.json_response({"ok": True, "grades": grades})


async def api_get_grade_topics(request: web.Request) -> web.Response:
    """Tanlangan sinfning barcha mavzulari ro'yxatini qaytaradi"""
    grade_id = request.match_info.get("grade_id")
    raw_topics = materials.TOPICS_CONTENT.get(grade_id, [])
    
    # Savollar sonini hisoblash
    q_topics = {str(t.get("id")): len(t.get("questions", [])) for t in QUESTIONS_DATA.get(grade_id, {}).get("topics", [])}
    
    topics = []
    for idx, t in enumerate(raw_topics, 1):
        tid = str(t.get("id", idx))
        topics.append({
            "id": tid,
            "number": idx,
            "title": t.get("title", f"{idx}-mavzu"),
            "guide": t.get("guide", ""),
            "has_media": bool(t.get("media")),
            "questions_count": q_topics.get(tid, 0)
        })
        
    return web.json_response({
        "ok": True, 
        "grade_id": grade_id,
        "total": len(topics),
        "topics": topics
    })


async def api_get_topic_detail(request: web.Request) -> web.Response:
    """Mavzuning to'liq konspekti va test savollarini qaytaradi"""
    grade_id = request.match_info.get("grade_id")
    topic_id = request.match_info.get("topic_id")
    
    # 1. Konspekt
    raw_topics = materials.TOPICS_CONTENT.get(grade_id, [])
    topic_info = next((t for t in raw_topics if str(t.get("id")) == str(topic_id)), None)
    
    # 2. Savollar
    q_topics = QUESTIONS_DATA.get(grade_id, {}).get("topics", [])
    q_info = next((t for t in q_topics if str(t.get("id")) == str(topic_id)), None)
    questions = q_info.get("questions", []) if q_info else []
    
    return web.json_response({
        "ok": True,
        "grade_id": grade_id,
        "topic_id": topic_id,
        "title": topic_info.get("title") if topic_info else (q_info.get("title") if q_info else "Mavzu"),
        "text": topic_info.get("text") if topic_info else "",
        "guide": topic_info.get("guide") if topic_info else "",
        "media": topic_info.get("media") if topic_info else "",
        "questions": questions
    })


async def api_get_yopiq_tests(request: web.Request) -> web.Response:
    """10-sinf yopiq testlar toifalarini qaytaradi"""
    categories = []
    for c in YOPIQ_DATA:
        categories.append({
            "id": c.get("id"),
            "name": c.get("name"),
            "questions_count": len(c.get("questions", []))
        })
    return web.json_response({"ok": True, "categories": categories})


async def api_get_yopiq_category(request: web.Request) -> web.Response:
    """Kategoriya bo'yicha yopiq savollarni qaytaradi"""
    cat_id = request.match_info.get("cat_id")
    cat = next((c for c in YOPIQ_DATA if str(c.get("id")) == str(cat_id)), None)
    if not cat:
        return web.json_response({"ok": False, "error": "Kategoriya topilmadi"}, status=404)
        
    return web.json_response({
        "ok": True,
        "category": {
            "id": cat.get("id"),
            "name": cat.get("name"),
            "questions": cat.get("questions", [])
        }
    })


async def api_attestation_mock(request: web.Request) -> web.Response:
    """Pedagoglar attestatsiyasi uchun 40 ta biologiya + 10 ta pedagogika savollari simulyatori"""
    import random
    
    all_q = []
    # 8, 9, 10, 11-sinflardan tasodifiy savollar terish
    for gid in ["8", "9", "10", "11"]:
        for t in QUESTIONS_DATA.get(gid, {}).get("topics", []):
            for q in t.get("questions", []):
                all_q.append({
                    **q,
                    "grade": gid,
                    "topic": t.get("title")
                })
                
    sampled_bio = random.sample(all_q, min(40, len(all_q))) if all_q else []
    
    pedagogy_q = [
        {
            "id": "ped_1",
            "question": "Formativ (shakllantiruvchi) baholashning asosiy maqsadi nima?",
            "options": [
                "O‘quvchining o‘zlashtirishdagi bo‘shliqlarini aniqlash va o‘z vaqtida tuzatish",
                "Choraklik yakuniy bahoni qo‘yish",
                "Sinf jurnali uchun rasmiy ball yozish",
                "O‘quvchini boshqa o‘quvchilar bilan solishtirib jazolash"
            ],
            "correct_option_id": 0,
            "explanation": "Formativ baholash o‘rganish jarayonini yaxshilash va kamchiliklarni bartaraf etishga qaratilgan."
        },
        {
            "id": "ped_2",
            "question": "Blum taksonomiyasining 'Qo‘llash' (Application) bosqichiga qaysi fe’l mos keladi?",
            "options": ["Hisoblaydi / Tajribada sinab ko‘radi", "Yoddan aytadi", "Baho beradi", "Ta’riflaydi"],
            "correct_option_id": 0,
            "explanation": "Qo‘llash bosqichida o‘quvchi olingan bilimlarni yangi vaziyatlarda amalda qo‘llaydi."
        }
    ]
    
    return web.json_response({
        "ok": True,
        "exam_type": "attestation_mock_100",
        "duration_minutes": 100,
        "biology_questions": sampled_bio,
        "pedagogy_questions": pedagogy_q
    })


# Asosiy HTML sahifani uzatish
async def serve_index(request: web.Request) -> web.FileResponse:
    index_path = os.path.join(CURRENT_DIR, "index.html")
    if not os.path.exists(index_path):
        return web.Response(text="<h1>BioMaster WebApp yuklanmoqda...</h1>", content_type="text/html")
    return web.FileResponse(index_path)


def create_app() -> web.Application:
    app = web.Application(middlewares=[cors_middleware])
    
    # Yo'nalishlar (Routes)
    app.router.add_get("/", serve_index)
    app.router.add_get("/api/grades", api_get_grades)
    app.router.add_get("/api/grade/{grade_id}/topics", api_get_grade_topics)
    app.router.add_get("/api/grade/{grade_id}/topic/{topic_id}", api_get_topic_detail)
    app.router.add_get("/api/yopiq_tests", api_get_yopiq_tests)
    app.router.add_get("/api/yopiq_tests/{cat_id}", api_get_yopiq_category)
    app.router.add_get("/api/attestation/mock", api_attestation_mock)
    
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"BioMaster Pro Mini App serveri ishga tushmoqda: http://localhost:{port}")
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=port)
