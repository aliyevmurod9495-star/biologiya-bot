"""
Biologiya masalalari va amaliy topshiriqlar moduli:
DNK, oqsil, ATF, mitoz/meyoz va genetika masalalarini yechish qoidalari,
interaktiv mashqlar va uyga vazifalar to'plami.
"""

from typing import Dict, List, Any, Optional

# 1. Masalalarning mavzulashtirilgan nazariy qoidalari va formulalari
PROBLEM_GUIDES: Dict[str, Dict[str, Any]] = {
    "dnk": {
        "title": "🧬 DNK va RNK tuzilishiga oid masalalar",
        "description": "Nukleotidlar soni, uzunligi, massasi, vodorod bog'lari va Chargaff qoidalari.",
        "rules": (
            "📌 <b>DNK VA RNK MASALALARINI YECHISH FORMULALARI:</b>\n\n"
            "1. <b>Chargaff qoidalari:</b>\n"
            "• Adenin (A) = Timin (T)\n"
            "• Guanin (G) = Sitozin (Ts)\n"
            "• A + G = T + Ts = 50% (Purin = Pirimidin asoslari)\n"
            "• A + T + G + Ts = 100% (Umumiy nukleotidlar)\n\n"
            "2. <b>DNK zanjiri uzunligi (L):</b>\n"
            "• Qo'sh spiral bo'lgani uchun bitta zanjirdagi nukleotidlar soniga ko'paytiriladi:\n"
            "  <code>L = (N_jami / 2) × 0.34 nm</code>\n"
            "  <i>(1 ta nukleotid uzunligi = 0.34 nm yoki 3.4 Å)</i>\n\n"
            "3. <b>Molekulyar massasi (M):</b>\n"
            "• <code>M = N_jami × 345 Da</code> (yoki masalada berilsa 300 Da)\n\n"
            "4. <b>Vodorod bog'lari soni (H):</b>\n"
            "• A va T o'rtasida 2 ta, G va Ts o'rtasida 3 ta vodorod bog'i hosil bo'ladi:\n"
            "  <code>H = 2A + 3G</code> (yoki <code>H = 2T + 3Ts</code>)\n"
            "• <code>H = N_jami + G</code> (chunki har bir juftda kamida 2 ta bog' bor)"
        )
    },
    "protein": {
        "title": "🥩 Oqsil biosintezi va translyatsiya masalalari",
        "description": "Aminokislotalar soni, kodonlar, iRNK nukleotidlari va molekulyar massa.",
        "rules": (
            "📌 <b>OQSIL BIOSINTEZI FORMULALARI:</b>\n\n"
            "1. <b>Kodon va nukleotidlar bog'liqligi:</b>\n"
            "• 1 ta aminokislotani <b>3 ta nukleotid</b> (1 ta triplet / kodon) kodlaydi:\n"
            "  <code>N_nukleotid = N_aminokislota × 3</code>\n"
            "• Agar DNK qo'sh zanjiri so'ralsa: <code>N_dnk = N_aminokislota × 6</code>\n\n"
            "2. <b>Oqsilning molekulyar massasi:</b>\n"
            "• 1 ta aminokislotaning o'rtacha massasi = <b>110 Da</b> (ba'zi darsliklarda 120 Da):\n"
            "  <code>M_oqsil = N_aminokislota × 110 Da</code>\n\n"
            "3. <b>tRNK antikodonlari:</b>\n"
            "• Har bir aminokislotani ribosomaga 1 ta tRNK tashiydi:\n"
            "  <code>N_tRNK = N_aminokislota</code>"
        )
    },
    "atf": {
        "title": "⚡️ Energetik almashinuv va ATF masalalari",
        "description": "Glikoliz, nafas olish, to'liq parchalanish va ajralgan energiya hisobi.",
        "rules": (
            "📌 <b>METABOLIZM VA ENERGIYA FORMULALARI:</b>\n\n"
            "1. <b>1-bosqich: Tayyorgarlik</b>\n"
            "• Murakkab moddalar monomerlarga parchalanadi, energiya faqat issiqlik sifatida tarqaladi (ATF sintezlanmaydi).\n\n"
            "2. <b>2-bosqich: Chala (kislorodsiz) parchalanish — Glikoliz</b>\n"
            "• 1 mol glyukoza → 2 mol sut kislota + <b>2 mol ATF</b> + 200 kJ energiya (80 kJ ATFda, 120 kJ issiqlik).\n\n"
            "3. <b>3-bosqich: Kislorodli (mitoxondriyada) parchalanish</b>\n"
            "• 2 mol sut kislota + 6O₂ → 6CO₂ + 6H₂O + <b>36 mol ATF</b> + 2600 kJ energiya.\n\n"
            "4. <b>To'liq parchalanish tenglamasi:</b>\n"
            "• 1 mol glyukoza → 6CO₂ + 6H₂O + <b>38 mol ATF</b> + 2800 kJ energiya (1520 kJ ATFda, 1280 kJ issiqlik)."
        )
    },
    "mitoz": {
        "title": "🔬 Mitoz va Meyozda xromosomalar (n va c) hisobi",
        "description": "Interfaza, profaza, metafaza, anafaza va telofazada n va c miqdori.",
        "rules": (
            "📌 <b>XROMOSOMA (n) VA DNK (c) HISOBI:</b>\n\n"
            "1. <b>Mitoz bosqichlarida:</b>\n"
            "• <b>Interfaza G1:</b> 2n 2c (diplod to'plam, 1 xromatidli)\n"
            "• <b>Interfaza S va G2:</b> 2n 4c (DNK replikatsiyasi o'tgan)\n"
            "• <b>Profaza:</b> 2n 4c\n"
            "• <b>Metafaza:</b> 2n 4c (xromosomalar ekvatorda)\n"
            "• <b>Anafaza:</b> <b>4n 4c</b> (xromatidalar ajralib har biri mustaqil xromosomaga aylanadi!)\n"
            "• <b>Telofaza:</b> 2n 2c (2 ta qiz hujayra)\n\n"
            "2. <b>Meyoz bosqichlarida:</b>\n"
            "• <b>Profaza I:</b> 2n 4c (konyugatsiya va krossingover)\n"
            "• <b>Anafaza I:</b> 2n 4c (gomologik xromosomalar qutblarga tarqaladi)\n"
            "• <b>Telofaza I:</b> 1n 2c (reduksion bo'linish)\n"
            "• <b>Anafaza II:</b> 2n 2c (xromatidalar ajraladi)\n"
            "• <b>Gametalar:</b> <b>1n 1c</b> (gaploid to'plam)"
        )
    },
    "genetika": {
        "title": "🌿 Genetika masalalari (Mendel, Noallel, Jins)",
        "description": "Monoduragay, diduragay, komplementar, epistaz, polimeriya va jinsga birikkan irsiylanish.",
        "rules": (
            "📌 <b>GENETIKA MASALALARINING ASOSIY NISBATLARI:</b>\n\n"
            "1. <b>Mendel qonunlari:</b>\n"
            "• <b>Monoduragay (Aa × Aa):</b>\n"
            "  - Fenotip bo'yicha: <b>3 : 1</b>\n"
            "  - Genotip bo'yicha: <b>1 AA : 2 Aa : 1 aa</b>\n"
            "  - To'liqsiz dominantlikda: <b>1 : 2 : 1</b> (fenotip = genotip)\n"
            "• <b>Diduragay (AaBb × AaBb):</b>\n"
            "  - Fenotip bo'yicha: <b>9 : 3 : 3 : 1</b>\n\n"
            "2. <b>Noallel genlarning o'zaro ta'siri:</b>\n"
            "• <b>Komplementar:</b> 9:7 (shirin no'xat guli), 9:6:1 (qovoq shakli), 9:3:4\n"
            "• <b>Epistaz:</b> 12:3:1 (dominant epistaz), 13:3, 9:3:4 (retsessiv epistaz)\n"
            "• <b>Polimeriya:</b> 15:1 (bug'doy doni rangi)\n\n"
            "3. <b>Jins bilan bog'liq irsiylanish:</b>\n"
            "• Odamda X-xromosomaga birikkan retsessiv: Gemofiliya (Xʰ), Daltonizm (Xᵈ)\n"
            "• Erkak kishi (XY) faqat onasidan X xromosomani oladi va bitta retsessiv gen bo'lsa ham kasallanadi."
        )
    }
}

# 2. Interaktiv amaliy masalalar to'plami (Mavzular bo'yicha mashqlar)
PRACTICE_PROBLEMS: List[Dict[str, Any]] = [
    {
        "id": "p1",
        "category": "dnk",
        "title": "DNK nukleotidlari va uzunligini topish",
        "question": (
            "DNK molekulasining bitta zanjirida 450 ta Adenin, 250 ta Timin, 300 ta Guanin va 200 ta Sitozin nukleotidlari bor.\n"
            "Ushbu DNK molekulasining umumiy uzunligini (nm) toping."
        ),
        "options": [
            "204 nm",
            "408 nm",
            "816 nm",
            "300 nm"
        ],
        "correct_option_id": 1,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. Bitta zanjirdagi nukleotidlar sonini topamiz:\n"
            "   N = 450 + 250 + 300 + 200 = 1200 ta nukleotid.\n"
            "2. DNK qo'sh zanjir uzunligi bitta zanjirdagi nukleotidlar uzunligiga teng:\n"
            "   L = 1200 × 0.34 nm = <b>408 nm</b>.\n"
            "To'g'ri javob: <b>408 nm</b>."
        )
    },
    {
        "id": "p2",
        "category": "dnk",
        "title": "DNKda vodorod bog'lari sonini hisoblash",
        "question": (
            "DNK fragmentida jami 2000 ta nukleotid bo'lib, ulardan 400 tasi Adenin.\n"
            "Ushbu DNK dagi umumiy vodorod bog'lari soni nechta?"
        ),
        "options": [
            "2400 ta",
            "2600 ta",
            "2800 ta",
            "2200 ta"
        ],
        "correct_option_id": 1,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. Chargaff qoidasiga ko'ra: A = T = 400 ta.\n"
            "   A + T = 400 + 400 = 800 ta.\n"
            "2. G + Ts = 2000 - 800 = 1200 ta → G = Ts = 600 ta.\n"
            "3. Vodorod bog'lari formulasi: H = 2A + 3G\n"
            "   H = (2 × 400) + (3 × 600) = 800 + 1800 = <b>2600 ta</b>.\n"
            "To'g'ri javob: <b>2600 ta</b>."
        )
    },
    {
        "id": "p3",
        "category": "protein",
        "title": "Oqsil biosintezida nukleotidlar sonini aniqlash",
        "question": (
            "Oqsil molekulasi 150 ta aminokislotadan tashkil topgan.\n"
            "Ushbu oqsilni kodlagan iRNK dagi nukleotidlar soni va uning sintezida ishtirok etgan tRNK lar sonini toping."
        ),
        "options": [
            "iRNK: 450 ta, tRNK: 150 ta",
            "iRNK: 300 ta, tRNK: 300 ta",
            "iRNK: 150 ta, tRNK: 450 ta",
            "iRNK: 900 ta, tRNK: 150 ta"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. 1 ta aminokislotani 3 ta nukleotid kodlaydi:\n"
            "   iRNK nukleotidlari = 150 × 3 = <b>450 ta</b>.\n"
            "2. Har bitta aminokislotani 1 ta tRNK tashiydi:\n"
            "   tRNK soni = <b>150 ta</b>.\n"
            "To'g'ri javob: <b>iRNK: 450 ta, tRNK: 150 ta</b>."
        )
    },
    {
        "id": "p4",
        "category": "atf",
        "title": "Energiya almashinuvi va ATF hosil bo'lishi",
        "question": (
            "Hujayrada 5 mol glyukoza to'liq (kislorodli) parchalanganda necha mol ATF sintezlanadi va jami necha kJ energiya ajraladi?"
        ),
        "options": [
            "190 mol ATF, 14 000 kJ",
            "180 mol ATF, 12 000 kJ",
            "100 mol ATF, 10 000 kJ",
            "190 mol ATF, 7 600 kJ"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. 1 mol glyukoza to'liq parchalanganda 38 mol ATF va 2800 kJ energiya ajraladi.\n"
            "2. 5 mol glyukoza uchun:\n"
            "   ATF = 5 × 38 = <b>190 mol ATF</b>.\n"
            "   Energiya = 5 × 2800 kJ = <b>14 000 kJ</b>.\n"
            "To'g'ri javob: <b>190 mol ATF, 14 000 kJ</b>."
        )
    },
    {
        "id": "p5",
        "category": "mitoz",
        "title": "Mitoz anafazasida xromosomalar soni",
        "question": (
            "Shimpanzening tana hujayrasida xromosomalar soni 2n = 48 ga teng.\n"
            "Mitozning anafaza bosqichida va meyozning anafaza II bosqichida xromosomalar soni qancha bo'ladi?"
        ),
        "options": [
            "Mitoz anafaza: 96 ta; Meyoz anafaza II: 48 ta",
            "Mitoz anafaza: 48 ta; Meyoz anafaza II: 24 ta",
            "Mitoz anafaza: 96 ta; Meyoz anafaza II: 24 ta",
            "Mitoz anafaza: 48 ta; Meyoz anafaza II: 48 ta"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. Mitoz anafazasida har bir xromosoma xromatidalari mustaqil xromosomaga aylanadi, formula: 4n 4c.\n"
            "   Xromosomalar = 2 × 48 = <b>96 ta</b>.\n"
            "2. Meyoz anafaza II da formula: 2n 2c.\n"
            "   Xromosomalar = <b>48 ta</b>.\n"
            "To'g'ri javob: <b>Mitoz anafaza: 96 ta; Meyoz anafaza II: 48 ta</b>."
        )
    },
    {
        "id": "p6",
        "category": "genetika",
        "title": "Monoduragay chatishtirishda ajralish",
        "question": (
            "Pomidorda mevaning qizil rangi (A) sariq rang (a) ustidan to'liq dominantlik qiladi.\n"
            "Ikkita geterozigota qizil mevali o'simlik chatishtirilganda, F1 avlodda 600 ta o'simlik olindi.\n"
            "Ularning nechtasi sariq mevali bo'ladi?"
        ),
        "options": [
            "150 ta",
            "200 ta",
            "300 ta",
            "450 ta"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. Chatishtirish: Aa × Aa → 1 AA : 2 Aa : 1 aa\n"
            "2. Fenotip bo'yicha ajralish: 3 qism qizil (75%) : 1 qism sariq (25%).\n"
            "3. Sariq mevali (aa) o'simliklar ulushi: 600 × 25% = <b>150 ta</b>.\n"
            "To'g'ri javob: <b>150 ta</b>."
        )
    },
    {
        "id": "p7",
        "category": "genetika",
        "title": "Jinsga birikkan irsiylanish (Gemofiliya)",
        "question": (
            "Sog'lom, lekin gemofiliya genini tashuvchi ayol (XᴴXʰ) sog'lom erkak (XᴴY) bilan turmush qurdi.\n"
            "Bu oilada tug'ilishi mumkin bo'lgan o'g'il bolalarning necha foizi kasal bo'ladi?"
        ),
        "options": [
            "50%",
            "25%",
            "100%",
            "0%"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>Yechilishi:</b>\n"
            "1. Ota-onalar genotipi: XᴴXʰ × XᴴY\n"
            "2. Avlodlar:\n"
            "   - Qizlar: XᴴXᴴ (sog'lom), XᴴXʰ (tashuvchi) — qizlar kasal bo'lmaydi.\n"
            "   - O'g'illar: XᴴY (sog'lom), XʰY (gemofiliya kasal).\n"
            "3. O'g'il bolalar orasida nisbat: 1 ta sog'lom : 1 ta kasal (ya'ni o'g'illarning <b>50%</b> qismi kasal).\n"
            "To'g'ri javob: <b>50%</b>."
        )
    }
]

# 3. Uyga vazifa masalalari (Darsdan so'ng beriladigan mustaqil topshiriqlar)
HOMEWORK_TASKS: List[Dict[str, Any]] = [
    {
        "id": "hw1",
        "topic": "DNK va oqsil sintezi",
        "title": "1-Uyga vazifa: DNK va oqsil massasini hisoblash",
        "task": (
            "📋 <b>1-UYGA VAZIFA:</b>\n\n"
            "Oqsil zanjiri 220 ta aminokislotadan iborat.\n\n"
            "<b>Savollar:</b>\n"
            "1. Ushbu oqsilni kodlagan iRNK necha nukleotiddan iborat?\n"
            "2. Uni sintezlagan DNK qo'sh zanjirining uzunligi necha nm?\n"
            "3. Agar 1 ta aminokislota massasi 110 Da bo'lsa, oqsilning massasi qancha?\n\n"
            "💡 <i>Yechimingizni qog'ozda ishlab, javobni quyidagi variantlardan tanlang:</i>"
        ),
        "options": [
            "1) 660 ta, 2) 224.4 nm, 3) 24 200 Da",
            "1) 440 ta, 2) 149.6 nm, 3) 22 000 Da",
            "1) 660 ta, 2) 448.8 nm, 3) 24 200 Da",
            "1) 220 ta, 2) 74.8 nm, 3) 12 100 Da"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>To'liq yechim:</b>\n"
            "1. iRNK nukleotidlari = 220 × 3 = 660 ta.\n"
            "2. DNK bitta zanjirida ham 660 ta nukleotid bor. Uzunlik = 660 × 0.34 nm = 224.4 nm.\n"
            "3. Oqsil massasi = 220 × 110 Da = 24 200 Da."
        )
    },
    {
        "id": "hw2",
        "topic": "Energiya almashinuvi (ATF)",
        "title": "2-Uyga vazifa: Glikoliz va to'liq parchalanish",
        "task": (
            "📋 <b>2-UYGA VAZIFA:</b>\n\n"
            "Hujayrada ma'lum miqdordagi glyukoza to'liq parchalandi va 114 mol ATF sintezlandi.\n\n"
            "<b>Savollar:</b>\n"
            "1. Necha mol glyukoza parchalangan?\n"
            "2. Glikoliz bosqichining o'zida necha mol ATF hosil bo'lgan?\n"
            "3. Jami necha kJ energiya ajralgan?\n\n"
            "💡 <i>Yechimingizni variantlardan tanlang:</i>"
        ),
        "options": [
            "1) 3 mol glyukoza, 2) 6 mol ATF, 3) 8 400 kJ",
            "1) 4 mol glyukoza, 2) 8 mol ATF, 3) 11 200 kJ",
            "1) 3 mol glyukoza, 2) 38 mol ATF, 3) 2 800 kJ",
            "1) 2 mol glyukoza, 2) 4 mol ATF, 3) 5 600 kJ"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>To'liq yechim:</b>\n"
            "1. 1 mol glyukoza to'liq parchalanganda 38 mol ATF beradi. Glyukoza = 114 / 38 = 3 mol.\n"
            "2. Glikolizda 1 mol glyukoza 2 mol ATF beradi: 3 × 2 = 6 mol ATF.\n"
            "3. Energiya = 3 mol × 2800 kJ = 8 400 kJ."
        )
    },
    {
        "id": "hw3",
        "topic": "Genetika (Diduragay chatishtirish)",
        "title": "3-Uyga vazifa: Diduragay chatishtirishda fenotiplar nisbati",
        "task": (
            "📋 <b>3-UYGA VAZIFA:</b>\n\n"
            "No'xatda sariq rang (A) yashil rang (a) ustidan, silliq shakl (B) burishgan shakl (b) ustidan dominantlik qiladi.\n"
            "Digeterozigota (AaBb) no'xatlar o'zaro chatishtirildi va F1 avlodda 3200 ta urug' olindi.\n\n"
            "<b>Savollar:</b>\n"
            "1. Sariq-silliq urug'lar soni nechta?\n"
            "2. Yashil-burishgan urug'lar soni nechta?"
        ),
        "options": [
            "Sariq-silliq: 1800 ta; Yashil-burishgan: 200 ta",
            "Sariq-silliq: 1600 ta; Yashil-burishgan: 400 ta",
            "Sariq-silliq: 2400 ta; Yashil-burishgan: 800 ta",
            "Sariq-silliq: 1200 ta; Yashil-burishgan: 600 ta"
        ],
        "correct_option_id": 0,
        "explanation": (
            "<b>To'liq yechim:</b>\n"
            "1. Diduragayda fenotip nisbati: 9 : 3 : 3 : 1 (jami 16 qism).\n"
            "2. Bitta qism = 3200 / 16 = 200 ta urug'.\n"
            "3. Sariq-silliq (9 qism) = 9 × 200 = 1800 ta.\n"
            "4. Yashil-burishgan (1 qism, aabb) = 1 × 200 = 200 ta."
        )
    }
]
