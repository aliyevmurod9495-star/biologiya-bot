"""
Biologiya o'quv materiallari: Mavzu ma'ruzalari, video darslar va 3D animatsiyalar.
8-sinf va boshqa sinflar uchun boyitilgan darslik konspektlari.
"""

from typing import Dict, List, Any

# Mavzular ma'ruzalari (Konspektlar)
TOPICS_CONTENT: Dict[str, List[Dict[str, Any]]] = {
    "8": [
        {
            "id": "1",
            "title": "1-mavzu: Odam anatomiyasi va fiziologiyasi fanining maqsadi",
            "text": (
                "📖 <b>1-MAVZU: ODAM ANATOMIYASI VA FIZIOLOGIYASI FANINING MAQSADI VA VAZIFALARI</b>\n\n"
                "🔹 <b>Anatomiya</b> (yunoncha <i>'anatome'</i> — yorish, kesish) — odam organizmining, "
                "uning a'zolari va tizimlarining shakli, tuzilishi hamda rivojlanishini o'rganadigan fandir.\n\n"
                "🔹 <b>Fiziologiya</b> (yunoncha <i>'fisis'</i> — tabiat, <i>'logos'</i> — ta'limot) — tirik organizm, "
                "uning alohida to'qima, a'zo va tizimlari qanday ishlashini (hayotiy jarayonlar va funksiyalarni) o'rganadi.\n\n"
                "🔹 <b>Gigiyena</b> (yunoncha <i>'gigiyenos'</i> — sog'lom) — tashqi muhit omillarining inson salomatligiga "
                "ta'sirini o'rganib, kasalliklarning oldini olish va sog'lom turmush tarzi qoidalarini ishlab chiqadi.\n\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🌟 <b>Tarixiy ma'lumotlar va allomalar:</b>\n"
                "• <b>Abu Ali ibn Sino</b> — 'Tib qonunlari' asari bilan jahon tibbiyoti va anatomiyasiga asos solgan buyuk mutafakkir.\n"
                "• <b>Uilyam Garvey</b> (1628) — odamda qon aylanish doirasini kashf qilgan.\n"
                "• <b>I.I. Mechnikov</b> — leykotsitlarning fagotsitoz (himoya) xususiyatini ochib, Nobel mukofotiga sazovor bo'lgan.\n"
                "• <b>I.P. Pavlov</b> — shartli va shartsiz reflekslar ta'limotini yaratgan.\n\n"
                "💡 <i>Ushbu mavzu bo'yicha bilimlaringizni sinash uchun quyidagi 'Test ishlash' tugmasini bosing!</i>"
            )
        },
        {
            "id": "2",
            "title": "2-mavzu: Odam organizmining hujayraviy tuzilishi va to'qimalar",
            "text": (
                "📖 <b>2-MAVZU: HUJAYRAVIY TUZILISH VA TO'QIMALAR</b>\n\n"
                "🔹 <b>Hujayra</b> — organizmning eng kichik tuzilish va tiriklik birligidir. "
                "Odamning somatik hujayralari yadrosida <b>23 juft (46 ta)</b> xromosoma bo'ladi.\n\n"
                "🧬 <b>Asosiy organoidlar va vazifalari:</b>\n"
                "• <b>Plazmatik membrana</b> — himoya va tanlab o'tkazuvchanlik vazifasi.\n"
                "• <b>Mitoxondriya</b> — ATF sintez qiluvchi energetik stansiya.\n"
                "• <b>Ribosoma</b> — oqsillarni biosintez qiladi.\n"
                "• <b>Golji majmuasi</b> — moddalarni to'playdi, shakllantiradi va lizosomalarni hosil qiladi.\n"
                "• <b>Lizosoma</b> — ichki hazm qilish fermentlariga ega bo'lib, yot moddalarni parchalaydi.\n\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🔬 <b>Odam organizmidagi 4 xil to'qima:</b>\n"
                "1️⃣ <b>Epiteliy to'qimasi</b> — terining ustki qavati (epidermis), ichki a'zolar shilliq pardasi va bezlarni hosil qiladi.\n"
                "2️⃣ <b>Biriktiruvchi to'qima</b> — suyak, tog'ay, paylar, qon, limfa va yog' to'qimalari kiradi. Hujayralararo moddasi ko'p bo'ladi.\n"
                "3️⃣ <b>Muskul to'qimasi</b> — qo'zg'aluvchanlik va qisqaruvchanlik xususiyatiga ega. Skelet (ko'ndalang-targ'il), yurak va silliq muskullarga bo'linadi.\n"
                "4️⃣ <b>Nerv to'qimasi</b> — neyronlar (tana, dendrit va akson) hamda oraliq yordamchi neyrogliya hujayralaridan tashkil topgan.\n\n"
                "💡 <i>Ushbu mavzu bo'yicha 25 ta test savolini ishlash uchun quyidagi tugmani bosing!</i>"
            )
        },
        {
            "id": "3",
            "title": "3-mavzu: Organlar va organlar sistemasi",
            "text": (
                "📖 <b>3-MAVZU: ORGANLAR VA ORGANLAR SISTEMASI</b>\n\n"
                "🔹 <b>Organ (a'zo)</b> — tananing ma'lum shakli, tuzilishi, o'rni va vazifasiga ega bo'lgan qismidir (masalan: yurak, jigar, o'pka).\n"
                "Organ bir necha to'qimadan tuzilgan bo'lib, ulardan biri yetakchi hisoblanadi.\n\n"
                "🔹 <b>Organlar sistemasi</b> — umumiy vazifani bajarish uchun birlashgan a'zolar guruhi:\n"
                "• <b>Tayanch-harakat:</b> Skelet (suyaklar) va muskullar;\n"
                "• <b>Qon aylanish:</b> Yurak va tomirlar (arteriya, vena, kapillyarlar);\n"
                "• <b>Nafas olish:</b> Burun bo'shlig'i, hiqildoq, kekirdak, bronxlar va o'pka;\n"
                "• <b>Hazm qilish:</b> Og'iz bo'shlig'i, qizilo'ngach, oshqozon, ichaklar, jigar, me'da osti bezi;\n"
                "• <b>Ayirish:</b> Buyraklar, siydik naylari, siydik pufagi, siydik chiqarish kanali;\n"
                "• <b>Nerv sistemasi:</b> Bosh miya, orqa miya va periferik nervlar;\n"
                "• <b>Endokrin:</b> Ichki sekretsiya bezlari (gipofiz, qalqonsimon bez, buyrakusti bezi va h.k.)."
            )
        },
        {
            "id": "4",
            "title": "4-mavzu: Qon va organizmning ichki muhiti",
            "text": (
                "📖 <b>4-MAVZU: QON VA ORGANIZMNING ICHKI MUHITI</b>\n\n"
                "🔹 <b>Ichki muhit:</b> Qon, to'qima suyuqligi va limfadan iborat. Ichki muhit doimiyligi <b>gomeostaz</b> deb ataladi.\n"
                "Odam organizmida o'rtacha <b>4.5–5 litr qon</b> bo'lib, u tana vaznining 7–8 foizini tashkil etadi.\n\n"
                "🩸 <b>Qon tarkibi:</b>\n"
                "• <b>Plazma (55%):</b> 90-92% suv, 7-8% oqsillar (albumin, globulin, fibrinogen), 0.9% tuzlar, 0.1% glyukoza.\n"
                "• <b>Shaklli elementlar (45%):</b>\n"
                "  1. <b>Eritrotsitlar</b> — qizil qon tanachalari (1 mm³ qonda 4.5–5 mln). Yadrosiz, ikki tomoni botiq disk. Gemoglobin orqali O₂ va CO₂ tashiydi.\n"
                "  2. <b>Leykotsitlar</b> — oq qon tanachalari (1 mm³ qonda 6–8 ming). Yadroli, himoya vazifasini bajaradi (fagotsitoz va antitanalar).\n"
                "  3. <b>Trombotsitlar</b> — qon plastinkalari (1 mm³ qonda 200–400 ming). Qon ivishida ishtirok etadi."
            )
        },
        {
            "id": "5",
            "title": "5-mavzu: Yurak va qon tomirlar sistemasi",
            "text": (
                "📖 <b>5-MAVZU: YURAK VA QON AYLANISH SISTEMASI</b>\n\n"
                "🫀 <b>Yurak:</b> Ko'krak qafasida joylashgan 4 kamerali muskul a'zosi:\n"
                "• 2 ta bo'lmacha (o'ng va chap) hamda 2 ta qorincha (o'ng va chap).\n"
                "• Chap qorincha devori eng qalin (10-15 mm), chunki u qonni butun tanaga haydaydi.\n"
                "• Bo'lmachalar va qorinchalar o'rtasida <b>tavaqali klapanlar</b>, tomirlar chiqishida esa <b>yarimoysimon klapanlar</b> joylashgan.\n\n"
                "🔄 <b>Qon aylanish doiralari:</b>\n"
                "1️⃣ <b>Katta qon aylanish doirasi:</b> Chap qorinchadan aortaga boshlanadi ➔ barcha to'qima va a'zolarga tarqaladi ➔ yuqori va pastki kovak venalar orqali o'ng bo'lmachaga keladi (20-23 soniya).\n"
                "2️⃣ <b>Kichik qon aylanish doirasi:</b> O'ng qorinchadan o'pka arteriyasi orqali boshlanadi ➔ o'pkada gazlar almashinib kislorodga to'yinadi ➔ 4 ta o'pka venasi orqali chap bo'lmachaga quyiladi (4-5 soniya)."
            )
        }
    ]
}

# Video darslar ro'yxati
VIDEO_LESSONS: Dict[str, List[Dict[str, str]]] = {
    "8": [
        {
            "id": "v1",
            "title": "Ko'zning tuzilishi va ko'rish mexanizmi",
            "duration": "10 daqiqa",
            "desc": "Ko'z soqqasi, to'r parda, shox parda, ko'z gavhari va yorug'lik sinishi tahlili."
        },
        {
            "id": "v2",
            "title": "Eshitish sistemasi va quloq anatomiyasi",
            "duration": "8 daqiqa",
            "desc": "Tashqi, o'rta va ichki quloq, chig'anoq, Kortiy a'zosi va tovush to'lqinlari o'tishi."
        },
        {
            "id": "v3",
            "title": "Yurak anatomiyasi va fiziologiyasi",
            "duration": "14 daqiqa",
            "desc": "Yurak kameralari, miokard qisqarishi, avtomatizm va qon tomirlar tizimi (lotincha atamalari bilan)."
        },
        {
            "id": "v4",
            "title": "Qonning shaklli elementlari va eritrotsitlar",
            "duration": "12 daqiqa",
            "desc": "Eritrotsitlar, leykotsitlar va trombotsitlar tuzilishi, mikroskop ostidagi ko'rinishi."
        },
        {
            "id": "v5",
            "title": "Nerv sistemasi va bosh miya bo'limlari",
            "duration": "15 daqiqa",
            "desc": "Bosh miya katta yarim sharlari, miyacha, uzunchoq miya va neyronlararo sinapslar."
        },
        {
            "id": "v6",
            "title": "Odamning ichki organlari joylashuvi",
            "duration": "11 daqiqa",
            "desc": "Ko'krak va qorin bo'shlig'i a'zolarining o'zaro topografik joylashuvi."
        },
        {
            "id": "v7",
            "title": "Nafas olish va oziq yo'li: Hiqildoq qopqog'i",
            "duration": "5 daqiqa",
            "desc": "Ovqat nima uchun nafas yo'liga o'tmaydi? Hiqildoq qopqog'ining reflektor harakati."
        }
    ]
}

# 3D Animatsiyalar ro'yxati
ANIMATIONS_3D: Dict[str, List[Dict[str, str]]] = {
    "8": [
        {
            "id": "a1",
            "title": "Buyrak transplantatsiyasi (3D Animatsiya)",
            "desc": "Buyrak ko'chirib o'tkazish jarayoni, qon tomirlar va siydik yo'llarini ulashning to'liq 3D tasviri."
        },
        {
            "id": "a2",
            "title": "Yurakning ishlash mexanizmi (3D)",
            "desc": "Yurak klapanlarining ochilib-yopilishi, sistola va diastola bosqichlarining dinamik 3D animatsiyasi."
        },
        {
            "id": "a3",
            "title": "Tuxum, sperma va urug'lanish (3D)",
            "desc": "Jinsiy hujayralar uchrashishi, urug'lanish va zigota hosil bo'lish jarayonining mikroskopik 3D ko'rinishi."
        },
        {
            "id": "a4",
            "title": "Aorta va magistral qon tomirlari (3D)",
            "desc": "Yurakdan chiquvchi yirik aorta raqami va tomirlar pulsatsiyasining vizual 3D modeli."
        }
    ]
}
