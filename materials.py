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
            "title": "2-mavzu: Hujayra, to'qimalar va a'zolar",
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
                "💡 <i>Ushbu mavzu bo'yicha test ishlab bilimlaringizni sinab ko'ring!</i>"
            )
        },
        {
            "id": "3",
            "title": "3-mavzu: Gormonlar va ichki sekretsiya bezlari",
            "text": (
                "📖 <b>3-MAVZU: GORMONLAR VA ICHKI SEKRETSIYA BEZLARI</b>\n\n"
                "🔹 <b>Ichki sekretsiya bezlari (Endokrin bezlar):</b> Maxsus chiqaruv naylariga ega emas, "
                "o'z mahsulotlarini (gormonlarni) bevosita qon va limfaga chiqaradi.\n\n"
                "🧪 <b>Asosiy endokrin bezlar va ularning gormonlari:</b>\n"
                "• <b>Gipofiz:</b> Bosh miya asosida joylashgan boshqaruvchi bez. Somatotrop (o'sish), tireotrop, gonadotrop gormonlar ishlab chiqaradi.\n"
                "• <b>Qalqonsimon bez:</b> Bo'yin sohasida joylashgan. Tiroksin gormoni (tarkibida yod bor) ishlab chiqaradi. Yetishmovchiligida endemik buqoq, kretinizm; ko'payganda bazedov kasalligi yuzaga keladi.\n"
                "• <b>Qalqonoldi bezlari:</b> Paratgormon ishlab chiqaradi, kalsiy va fosfor almashinuvini boshqaradi.\n"
                "• <b>Epifiz:</b> Melatonin gormoni (kun-tun ritmlari va pigmentatsiyani boshqaradi).\n"
                "• <b>Ayrisimon bez (Timus):</b> Timozin gormoni (yoshlikda immunitet T-limfotsitlarini shakllantiradi).\n"
                "• <b>Buyrakusti bezlari:</b> Po'stloq qavatidan kortikosteroidlar, miya qavatidan adrenalin va noradrenalin (stress va xavf gormonlari).\n"
                "• <b>Aralash bezlar:</b> Me'da osti bezi (insulin va glyukagon — qonda qand miqdorini boshqaradi) hamda jinsiy bezlar (testosteron, estrogen)."
            )
        },
        {
            "id": "4",
            "title": "4-mavzu: Tayanch-harakat sistemasi: Suyaklar va skelet",
            "text": (
                "📖 <b>4-MAVZU: TAYANCH-HARAKAT SISTEMASI: SUYAKLAR VA SKELET</b>\n\n"
                "🔹 Odam skeleti <b>200 dan ortiq</b> suyakdan tashkil topgan bo'lib, tayanch, himoya va harakat vazifalarini bajaradi.\n\n"
                "🦴 <b>Skelet bo'limlari:</b>\n"
                "1️⃣ <b>Kalla skeleti:</b> Miya qutisi (peshana, tepa, ensa, chakka) va yuz qismi (yuqori va pastki jag', burun suyaklari).\n"
                "2️⃣ <b>Tana skeleti:</b> Umurtqa pog'onasi (33-34 ta umurtqa: 7 bo'yin, 12 ko'krak, 5 bel, 5 dumg'aza, 4-5 dum) va ko'krak qafasi (12 juft qovurg'a va to'sh suyagi).\n"
                "3️⃣ <b>Qo'l-oyoq (Kamar) skeleti:</b> Yelka kamari (o'mrov va kurak), erkin qo'l (yelka, bilak, tirsak, qo'l panjasi); Chanoq kamari va erkin oyoq (son, tizza qopqog'i, boldir, tovon, oyoq panjasi).\n\n"
                "⚙️ <b>Suyaklarning birikishi:</b>\n"
                "• Harakatsiz (choklar orqali, masalan kalla suyagi);\n"
                "• Yarim harakatli (tog'aylar orqali, masalan umurtqalar);\n"
                "• Harakatli (bo'g'imlar orqali: tirsak, tizza, yelka bo'g'imlari)."
            )
        },
        {
            "id": "5",
            "title": "5-mavzu: Muskullar sistemasi va jismoniy mehnat gigiyenasi",
            "text": (
                "📖 <b>5-MAVZU: MUSKULLAR SISTEMASI VA ISHLASHI</b>\n\n"
                "🔹 Odam tanasida <b>600 dan ortiq</b> muskul mavjud bo'lib, umumiy tana massasining 40% ini tashkil qiladi.\n\n"
                "💪 <b>Muskul turlari:</b>\n"
                "• <b>Skelet (ko'ndalang-targ'il) muskullari:</b> Ixtiyoriy qisqaradi, suyaklarga paylar yordamida birikadi (ikki boshli, uch boshli, to'rt boshli son muskuli).\n"
                "• <b>Silliq muskullar:</b> Ichki organlar (oshqozon, qon tomirlar, siydik pufagi) devorida joylashgan, noixtiyoriy ishlaydi.\n"
                "• <b>Yurak muskuli (Miokard):</b> Ko'ndalang-targ'il tuzilishga ega, ammo avtomatik ravishda noixtiyoriy qisqaradi.\n\n"
                "🏃 <b>Muskul ishi va charchoq:</b>\n"
                "• Dinamik ish (harakat bilan bog'liq) va statik ish (tanani bir holatda ushlab turish);\n"
                "• Charchoq — ATF zaxirasining kamayishi va sut kislotasi to'planishi natijasida yuzaga keladi. I.M. Sechenov faol dam olish charchoqni tezroq yo'qotishini isbotlagan."
            )
        },
        {
            "id": "6",
            "title": "6-mavzu: Organizmning ichki muhiti: Qon va immunitet",
            "text": (
                "📖 <b>6-MAVZU: QON VA ORGANIZMNING ICHKI MUHITI</b>\n\n"
                "🔹 <b>Ichki muhit:</b> Qon, to'qima suyuqligi va limfadan iborat. Odamda 4.5–5 litr qon bo'ladi.\n\n"
                "🩸 <b>Qon tarkibi:</b>\n"
                "• <b>Plazma (55%):</b> Suv (90-92%), oqsillar (albumin, globulin, fibrinogen), tuzlar, glyukoza.\n"
                "• <b>Eritrotsitlar (4.5–5 mln/mm³):</b> Yadrosiz, gemoglobin oqsili orqali O₂ va CO₂ tashiydi. Suyak qizil iligida hosil bo'ladi (yashash muddati 120 kun).\n"
                "• <b>Leykotsitlar (6–8 ming/mm³):</b> Yadroli, himoya vazifasini bajaradi (fagotsitoz — yot mikroblarni yutish).\n"
                "• <b>Trombotsitlar (200–400 ming/mm³):</b> Qon ivishini ta'minlaydi (fibrin tolalari hosil qiladi).\n\n"
                "🛡 <b>Immunitet:</b>\n"
                "• Tug'ma (tabiiy) va orttirilgan (sun'iy — vaksina va davolash zardobi orqali).\n"
                "• Qon guruhlari: I(0), II(A), III(B), IV(AB) va Rezus omil (Rh+ / Rh-)."
            )
        },
        {
            "id": "7",
            "title": "7-mavzu: Qon aylanish sistemasi: Yurak va qon tomirlar",
            "text": (
                "📖 <b>7-MAVZU: YURAK VA QON AYLANISH SISTEMASI</b>\n\n"
                "🫀 <b>Yurak tuzilishi:</b>\n"
                "• 4 kamerali muskul a'zosi: 2 bo'lmacha va 2 qorincha.\n"
                "• Chap qorincha devori eng baquvvat (10-15 mm), chunki qonni butun tanaga haydaydi.\n"
                "• Tavaqali va yarimoysimon klapanlar qonning faqat bir yo'nalishda oqishini ta'minlaydi.\n\n"
                "🔄 <b>Qon aylanish doiralari:</b>\n"
                "1️⃣ <b>Katta qon aylanish doirasi:</b> Chap qorinchadan aortaga boshlanadi ➔ to'qimalarga kislorod beradi ➔ vena tomirlari orqali o'ng bo'lmachaga quyiladi (20-23 soniya).\n"
                "2️⃣ <b>Kichik qon aylanish doirasi:</b> O'ng qorinchadan o'pka arteriyasiga boshlanadi ➔ o'pkada O₂ ga to'yinadi ➔ o'pka venalari orqali chap bo'lmachaga quyiladi (4-5 soniya).\n\n"
                "💓 Qon bosimi: Normal ko'rsatkich 110-120 / 70-80 mm simob ustuni."
            )
        },
        {
            "id": "8",
            "title": "8-mavzu: Nafas olish organlari va gazlar almashinuvi",
            "text": (
                "📖 <b>8-MAVZU: NAFAS OLISH SISTEMASI VA GAZLAR ALMASHINUVI</b>\n\n"
                "🔹 <b>Nafas a'zolari:</b>\n"
                "• <b>Nafas yo'llari:</b> Burun bo'shlig'i ➔ hiqildoq ➔ kekirdak (traxeya) ➔ bronxlar.\n"
                "• <b>Nafas organi:</b> O'pka (o'ng o'pka 3 bo'lakli, chap o'pka 2 bo'lakli).\n\n"
                "🫁 <b>Alveolalar (O'pka pufakchalari):</b>\n"
                "• Odam o'pkasida 300–400 million alveola bo'lib, umumiy nafas yuzasi 100 m² ga yetadi.\n"
                "• Alveolalarda kapillyarlar bilan gaz almashinuvi diffuziya yo'li bilan amalga oshadi: qonga O₂ o'tadi, qondan esa CO₂ chiqadi.\n\n"
                "🌬 Nafas olish va chiqarish qovurg'alararo muskullar va diafragmaning qisqarishi hisobiga ro'y beradi. Boshqaruv markazi uzunchoq miyada joylashgan."
            )
        },
        {
            "id": "9",
            "title": "9-mavzu: Ovqat hazm qilish sistemasi va moddalar almashinuvi",
            "text": (
                "📖 <b>9-MAVZU: OVQAT HAZM QILISH VA MODDALAR ALMASHINUVI</b>\n\n"
                "🔹 <b>Hazm qilish yo'li (8-10 metr):</b>\n"
                "• <b>Og'iz bo'shlig'i:</b> Tishlar (32 ta doimiy tish), til, so'lak bezlari (amilaza fermenti uglevodlarni parchalaydi).\n"
                "• <b>Qizilo'ngach</b> orqali ovqat oshqozonga tushadi.\n"
                "• <b>Oshqozon:</b> Me'da shirasi (xlorid kislota va pepsin fermenti) oqsillarni parchalaydi.\n"
                "• <b>Ingichka ichak (O'n ikki barmoqli ichak):</b> Jigar ishlab chiqargan o't suyuqligi yog'larni emulsiyalaydi, me'da osti bezi shirasi (tripsin, lipaza, amilaza) barcha moddalarni parchalaydi. Ichak vorsinkalari orqali ozuqa qonga so'riladi.\n"
                "• <b>Yo'g'on ichak:</b> Suv qayta so'riladi, axlat massasi shakllanadi.\n\n"
                "🧪 Vitaminlar: Suvda eruvchan (C, B guruh) va yog'da eruvchan (A, D, E, K)."
            )
        },
        {
            "id": "10",
            "title": "10-mavzu: Ayirish sistemasi: Buyraklar va teri gigiyenasi",
            "text": (
                "📖 <b>10-MAVZU: AYIRISH SISTEMASI VA TERI TUZILISHI</b>\n\n"
                "🔹 <b>Buyraklar:</b> Bel sohasida joylashgan juft loviyasimon a'zo. Asosiy funktsional birligi — <b>nefron</b> (har bir buyrakda 1 milliondan ortiq).\n\n"
                "💧 <b>Siydik hosil bo'lishi:</b>\n"
                "1️⃣ <b>Birlamchi siydik (Filtratsiya):</b> Buyrak koptokchalarida kuniga 150–180 litr filtrlanadi (oqsil va hujayralardan xoli plazma).\n"
                "2️⃣ <b>Ikkilamchi siydik (Reabsorbtsiya):</b> Buyrak naychalarida suv va foydali moddalar qayta so'rilib, kuniga 1.5 litr ikkilamchi siydik hosil bo'ladi va chiqariladi.\n\n"
                "🧖 <b>Teri tuzilishi:</b>\n"
                "• Epidermis (ustki ko'p qavatli epiteliy);\n"
                "• Derma (chin teri — qon tomirlar, retseptorlar, yog' va ter bezlari, soch ildizlari);\n"
                "• Teriosti yog' kletchatkasi (termoregulyatsiya va zaxira energiya)."
            )
        },
        {
            "id": "11",
            "title": "11-mavzu: Nerv sistemasi: Bosh miya va orqa miya",
            "text": (
                "📖 <b>11-MAVZU: NERV SISTEMASI VA REFLEKSLAR</b>\n\n"
                "🔹 <b>Nerv sistemasi:</b>\n"
                "• <b>Markaziy:</b> Bosh miya va orqa miya;\n"
                "• <b>Periferik:</b> Nerv tugunlari, nerv tolalari va retseptorlar.\n\n"
                "🧠 <b>Bosh miya bo'limlari:</b>\n"
                "1. <b>Uzunchoq miya:</b> Nafas olish, yurak urishi, yutinish, yo'tal, aksirish markazlari.\n"
                "2. <b>Ko'prik va O'rta miya:</b> Ko'rish va eshitishga qaratilgan yo'naltiruvchi reflekslar, muskul tonusi.\n"
                "3. <b>Miyacha:</b> Harakatlar koordinatsiyasi va muvozanatni boshqaradi.\n"
                "4. <b>Oraliq miya:</b> Talamus (sezgi stansiyasi) va gipotalamus (termoregulyatsiya, ochlik, to'qlik, uyqu markazlari).\n"
                "5. <b>Katta yarim sharlar po'stlog'i:</b> Oliy asab faoliyati, fikrlash, nutq va xotira."
            )
        },
        {
            "id": "12",
            "title": "12-mavzu: Sezgi a'zolari: Ko'rish, eshitish va boshqa analizatorlar",
            "text": (
                "📖 <b>12-MAVZU: SEZGI ORGANLARI (ANALIZATORLAR)</b>\n\n"
                "🔹 <b>Analizator</b> (I.P. Pavlov kiritgan) 3 qismdan iborat: Retseptor ➔ O'tkazuvchi nerv yo'li ➔ Bosh miya po'stlog'idagi markaz.\n\n"
                "👁 <b>Ko'rish organi (Ko'z):</b>\n"
                "• Odam tashqi olam ma'lumotlarining 90% ini ko'rish orqali oladi.\n"
                "• Shox parda, qorachiq, ko'z gavhari va shishasimon tana yorug'likni sindiradi.\n"
                "• <b>To'r parda (Retina):</b> Yorug'likni sezuvchi tayoqchalar (oq-qora, tungi ko'rish) va kolbachalar (rangli ko'rish).\n\n"
                "👂 <b>Eshitish organi (Quloq):</b>\n"
                "• Tashqi quloq (quloq suprasi va eshitish yo'li), O'rta quloq (nog'ora parda, bolg'acha, sandon, uzangi), Ichki quloq (chig'anoq va Kortiy a'zosi).\n"
                "• Ichki quloqdagi yarimhalqa naylar — muvozanat (vestibulyar) apparatini hosil qiladi."
            )
        },
        {
            "id": "13",
            "title": "13-mavzu: Oliy asab faoliyati va psixika",
            "text": (
                "📖 <b>13-MAVZU: OLIY ASAB FAOLIYATI VA PSIXIKA</b>\n\n"
                "🔹 I.M. Sechenov va I.P. Pavlov odamning bosh miya yarim sharlari po'stlog'i faoliyatini ilmiy tadqiq qilgan.\n\n"
                "🔄 <b>Reflekslar:</b>\n"
                "• <b>Shartsiz reflekslar:</b> Tug'ma, irsiy, turning barcha vakillarida bo'ladi (yutinish, emish, ko'zni pirpiratish).\n"
                "• <b>Shartli reflekslar:</b> Hayot davomida orttiriladi, vaqtincha bog'lanishlar hosil qiladi, o'zgaruvchan sharoitga moslashtiradi.\n\n"
                "🗣 <b>Signallar sistemalari:</b>\n"
                "• <b>1-signal sistemasi:</b> Hayvonlar va odamlarda umumiy (tovush, rang, hid kabi bevosita ta'sirotlar).\n"
                "• <b>2-signal sistemasi:</b> Faqat odamga xos (so'z, nutq, yozuv, mavhum tafakkur).\n\n"
                "💤 Uyqu va tush ko'rish — bosh miya hujayralarining himoyalanish va tiklanish jarayonidir."
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
            "title": "Odam skeleti va suyaklarning tuzilishi",
            "duration": "11 daqiqa",
            "desc": "Kalla, umurtqa pog'onasi, ko'krak qafasi va erkin qo'l-oyoq suyaklarining anatomik atlas ko'rinishi."
        },
        {
            "id": "v7",
            "title": "Nafas olish va gazlar almashinuvi",
            "duration": "9 daqiqa",
            "desc": "O'pka alveolalarida kislorod va karbonat angidrid gazining kapillyarlar bilan diffuziyasi."
        },
        {
            "id": "v8",
            "title": "Ovqat hazm qilish va ichki fermentlar",
            "duration": "13 daqiqa",
            "desc": "Oshqozon va o'n ikki barmoqli ichakda oziq moddalarning fermentativ parchalanishi va so'rilishi."
        }
    ]
}

# 3D Animatsiyalar ro'yxati
ANIMATIONS_3D: Dict[str, List[Dict[str, str]]] = {
    "8": [
        {
            "id": "a1",
            "title": "Buyrak va Nefron ishlash mexanizmi (3D)",
            "desc": "Buyrak koptokchalarida qon filtratsiyasi, birlamchi va ikkilamchi siydik hosil bo'lishining 3D modeli."
        },
        {
            "id": "a2",
            "title": "Yurakning ishlash mexanizmi va klapanlar (3D)",
            "desc": "Yurak tavaqali va yarimoysimon klapanlarining dinamik ochilib-yopilishi, sistola va diastola davri."
        },
        {
            "id": "a3",
            "title": "Alveola va kapillyar gaz almashinuvi (3D)",
            "desc": "O'pka pufakchalarida qizil qon tanachalari — eritrotsitlar kislorod bilan to'yinishining mikroskopik 3D ko'rinishi."
        },
        {
            "id": "a4",
            "title": "Neyronlar aro sinaps va impuls uzatilishi (3D)",
            "desc": "Nerv tolalari bo'ylab mediatorlar ajralishi va elektr impulslarining o'tish jarayoni 3D animatsiyasi."
        },
        {
            "id": "a5",
            "title": "Muskul tolasining qisqarishi (Aktin va miozin 3D)",
            "desc": "Ko'ndalang-targ'il muskullarda aktin va miozin oqsillarining ATF sarflab sirg'alish mexanizmi."
        }
    ]
}
