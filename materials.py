"""
Biologiya o'quv materiallari: Mavzu ma'ruzalari, qisqa qo'llanmalar, video darslar va 3D animatsiyalar.
8-sinf va boshqa sinflar uchun boyitilgan darslik konspektlari.
"""

from typing import Dict, List, Any

# Mavzular ma'ruzalari, qo'llanmalar va multimedia
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
                "• <b>Gippokrat:</b> 4 xil mizoj va organizmning bir butunligi ta'limotini yaratgan.\n"
                "• <b>Klavdiy Galen:</b> Dastlab murdani yorib ko'rish va hayvonlar ustida tajribalar (viviseksiya) o'tkazgan.\n"
                "• <b>Andrey Vezaliy:</b> 1543-yilda 'Odam tanasining tuzilishi to'g'risida' fundamental ilmiy asar yozgan.\n"
                "• <b>Abu Ali ibn Sino:</b> 'Tib qonunlari' asari bilan jahon tibbiyotiga tamal toshini qo'ygan.\n"
                "• <b>Uilyam Garvey (1628):</b> Odamda qon aylanish doirasini kashf qilgan.\n"
                "• <b>I.I. Mechnikov:</b> Leykotsitlarning fagotsitoz (himoya) xususiyatini ochib, Nobel mukofotiga sazovor bo'lgan.\n"
                "• <b>I.P. Pavlov:</b> Shartli va shartsiz reflekslar ta'limotini yaratgan.\n"
                "• <b>O'zbek olimlari:</b> Vosid Vohidov (jarrohlik), O'ktam Aripov (buyrak ko'chirish), Komiljon Zufarov (hujayraviy so'rilish), Adham Yunusov (suv-tuz balansi), Yolqin To'raqulov (endokrinologiya)."
            ),
            "guide": (
                "📘 <b>1-MAVZU BO'YICHA QISQA QO'LLANMA VA MUHIM FAKTLAR:</b>\n\n"
                "• <b>Anatomiya</b> — tuzilishini o'rganadi.\n"
                "• <b>Fiziologiya</b> — qanday ishlashini (funksiyasini) o'rganadi.\n"
                "• <b>Gigiyena</b> — salomatlikni saqlash qoidalarini o'rganadi.\n"
                "• <b>Ibn Sino:</b> 'Tib qonunlari' asari muallifi.\n"
                "• <b>Uilyam Garvey:</b> 1628-yilda qon aylanish doirasini kashf etgan.\n"
                "• <b>Mechnikov:</b> Fagotsitoz hodisasi asoschisi, Nobel mukofoti laureati.\n"
                "• <b>Pavlov:</b> 'Fiziologiya otasi' deb I.M. Sechenovni atagan."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Odam organizmi topografiyasi va a'zolar joylashuvi (11 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Inson tanasining umumiy anatomik tuzilishi"
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
                "• <b>Plazmatik membrana:</b> Himoya va tanlab o'tkazuvchanlik vazifasi.\n"
                "• <b>Mitoxondriya:</b> ATF sintez qiluvchi energetik stansiya.\n"
                "• <b>Ribosoma:</b> Oqsillarni biosintez qiladi.\n"
                "• <b>Golji majmuasi:</b> Moddalarni to'playdi, shakllantiradi va lizosomalarni hosil qiladi.\n"
                "• <b>Lizosoma:</b> Ichki hazm fermentlariga ega bo'lib, yot moddalarni parchalaydi.\n\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🔬 <b>Odam organizmidagi 4 xil to'qima:</b>\n"
                "1️⃣ <b>Epiteliy to'qimasi:</b> Terining ustki qavati (epidermis), ichki a'zolar shilliq pardasi va bezlarni hosil qiladi.\n"
                "2️⃣ <b>Biriktiruvchi to'qima:</b> Suyak, tog'ay, paylar, qon, limfa va yog' to'qimalari kiradi. Hujayralararo moddasi ko'p bo'ladi.\n"
                "3️⃣ <b>Muskul to'qimasi:</b> Qo'zg'aluvchanlik va qisqaruvchanlik xususiyatiga ega. Skelet, yurak va silliq muskullarga bo'linadi.\n"
                "4️⃣ <b>Nerv to'qimasi:</b> Neyronlar (tana, dendrit va akson) hamda oraliq neyrogliya hujayralaridan tashkil topgan."
            ),
            "guide": (
                "📘 <b>2-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Xromosoma:</b> Somatik hujayrada 46 ta (23 juft), jinsiy hujayrada 23 ta.\n"
                "• <b>Fagotsitoz:</b> Qattiq zarralarni yutish; <b>Pinotsitoz:</b> Suyuqlik tomchilarini yutish.\n"
                "• <b>Osmotik bosim:</b> Qonda 7.6 - 8.1 atm ga teng.\n"
                "• <b>4 to'qima:</b> Epiteliy (qoplovchi), Biriktiruvchi (tayanch-oziq), Muskul (harakat), Nerv (boshqaruv)."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> To'qimalarning mikroskopik tuzilishi (10 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Hujayra organoidlarining ishlashi va moddalar transporti"
            )
        },
        {
            "id": "3",
            "title": "3-mavzu: Gormonlar va ichki sekretsiya bezlari",
            "text": (
                "📖 <b>3-MAVZU: GORMONLAR VA ICHKI SEKRETSIYA BEZLARI</b>\n\n"
                "🔹 <b>Ichki sekretsiya bezlari:</b> Maxsus chiqaruv naylariga ega emas, "
                "o'z mahsulotlarini (gormonlarni) bevosita qon va limfaga chiqaradi.\n\n"
                "🧪 <b>Asosiy endokrin bezlar:</b>\n"
                "• <b>Gipofiz:</b> Bosh miya asosida joylashgan boshqaruvchi bez. Somatotrop (o'sish gormoni). Yetishmasa pakanalik, oshsa gigantizm va akromegaliya.\n"
                "• <b>Qalqonsimon bez:</b> Bo'yinda joylashgan. Tiroksin gormoni (tarkibida yod bor). Oshsa bazedov kasalligi, kamaysa endemik buqoq va kretinizm.\n"
                "• <b>Qalqonoldi bezlari:</b> Paratgormon ishlab chiqaradi, kalsiy va fosfor almashinuvini boshqaradi.\n"
                "• <b>Epifiz:</b> Melatonin (kun-tun ritmlari va pigmentatsiyani boshqaradi).\n"
                "• <b>Ayrisimon bez (Timus):</b> Timozin (yoshlikda immunitet T-limfotsitlarini rivojlantiradi).\n"
                "• <b>Buyrakusti bezlari:</b> Po'stlog'idan kortikoidlar, mag'zidan adrenalin va noradrenalin (stress gormonlari).\n"
                "• <b>Aralash bezlar:</b> Me'da osti bezi (insulin — qandni kamaytiradi, glyukagon — qandni oshiradi) va jinsiy bezlar."
            ),
            "guide": (
                "📘 <b>3-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Gipofiz:</b> Somatotrop (o'sish). Balog'atdan keyin ko'paysa — <i>Akromegaliya</i>.\n"
                "• <b>Qalqonsimon bez:</b> Tiroksin. Yod yetishmasa — <i>Endemik buqoq</i>.\n"
                "• <b>Me'da osti bezi:</b> Insulin yetishmasa — <i>Qandli diabet</i>.\n"
                "• <b>Paratgormon oshsa:</b> Suyaklar mo'rtlashadi, kalsiy qonga chiqadi.\n"
                "• <b>Adrenalin:</b> Yurak urishini tezlashtiradi, qon bosimini oshiradi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Endokrin tizim va gormonlarning ahamiyati (12 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Qandli diabet va insulin ta'sir mexanizmi"
            )
        },
        {
            "id": "4",
            "title": "4-mavzu: Tayanch-harakat sistemasi: Suyaklar va skelet",
            "text": (
                "📖 <b>4-MAVZU: TAYANCH-HARAKAT SISTEMASI: SUYAKLAR VA SKELET</b>\n\n"
                "🔹 Odam skeleti <b>200 dan ortiq</b> suyakdan tashkil topgan bo'lib, tayanch, himoya va harakat vazifalarini bajaradi.\n\n"
                "🦴 <b>Skelet bo'limlari:</b>\n"
                "1️⃣ <b>Kalla skeleti:</b> Miya qutisi (peshana, tepa, ensa, chakka) va yuz qismi (jag', burun suyaklari).\n"
                "2️⃣ <b>Tana skeleti:</b> Umurtqa pog'onasi (33-34 ta umurtqa: 7 bo'yin, 12 ko'krak, 5 bel, 5 dumg'aza, 4-5 dum) va ko'krak qafasi (12 juft qovurg'a va to'sh suyagi).\n"
                "3️⃣ <b>Qo'l-oyoq skeleti:</b> Yelka kamari (o'mrov va kurak), erkin qo'l (yelka, bilak, tirsak, qo'l panjasi); Chanoq kamari va erkin oyoq (son, tizza qopqog'i, boldir, tovon, oyoq panjasi).\n\n"
                "⚙️ <b>Suyaklarning birikishi:</b>\n"
                "• Harakatsiz (choklar orqali: kalla suyagi);\n"
                "• Yarim harakatli (tog'aylar orqali: umurtqalar);\n"
                "• Harakatli (bo'g'imlar orqali: tirsak, tizza, yelka bo'g'imlari)."
            ),
            "guide": (
                "📘 <b>4-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Suyaklar soni:</b> 200 dan ortiq.\n"
                "• <b>Umurtqalar:</b> 7 bo'yin, 12 ko'krak, 5 bel, 5 dumg'aza, 4-5 dum.\n"
                "• <b>Ko'krak qafasi:</b> 12 juft qovurg'a + 1 to'sh suyagi.\n"
                "• <b>Suyak tarkibi:</b> Organik moddalar (essein — elastiklik) va mineral tuzlar (kalsiy, fosfor — qattiqlik).\n"
                "• <b>Bo'g'im:</b> Bo'g'im yuzasi, bo'g'im xaltasi, bo'g'im suyuqligi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Odam skeleti va suyaklarning tuzilishi (11 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Tirsak va tizza bo'g'imlari harakati 3D modeli"
            )
        },
        {
            "id": "5",
            "title": "5-mavzu: Muskullar sistemasi va jismoniy mehnat gigiyenasi",
            "text": (
                "📖 <b>5-MAVZU: MUSKULLAR SISTEMASI VA ISHLASHI</b>\n\n"
                "🔹 Odam tanasida <b>600 dan ortiq</b> muskul mavjud bo'lib, tana massasining 40% ini tashkil qiladi.\n\n"
                "💪 <b>Muskul turlari:</b>\n"
                "• <b>Skelet (ko'ndalang-targ'il):</b> Ixtiyoriy qisqaradi, suyaklarga paylar orqali birikadi.\n"
                "• <b>Silliq muskullar:</b> Ichki organlar devorida, noixtiyoriy ishlaydi.\n"
                "• <b>Yurak muskuli (Miokard):</b> Ko'ndalang-targ'il, avtomatik ravishda noixtiyoriy qisqaradi.\n\n"
                "🏃 <b>Muskul ishi va charchoq:</b>\n"
                "• Charchoq — ATF kamayishi va sut kislotasi to'planishi tufayli ro'y beradi.\n"
                "• I.M. Sechenov faol dam olish charchoqni passiv dam olishga qaraganda tezroq yo'qotishini isbotlagan."
            ),
            "guide": (
                "📘 <b>5-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Muskullar:</b> 600 dan ortiq.\n"
                "• <b>Sinaps:</b> Nerv va muskul tutashgan joy.\n"
                "• <b>Bosh muskullari:</b> Chaynov va mimika muskullari.\n"
                "• <b>Sechenov effekti:</b> Ishlayotgan a'zoning toliqishini ikkinchi a'zo harakati orqali tezda tiklash (faol dam olish)."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Muskullarning tuzilishi va qisqarish kuchi (10 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Aktin va miozin oqsillarining ATF sarflab qisqarishi"
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
                "• <b>Eritrotsitlar (4.5–5 mln/mm³):</b> Yadrosiz, gemoglobin orqali O₂ va CO₂ tashiydi. 120 kun yashaydi.\n"
                "• <b>Leykotsitlar (6–8 ming/mm³):</b> Yadroli, himoya vazifasini bajaradi (fagotsitoz).\n"
                "• <b>Trombotsitlar (200–400 ming/mm³):</b> Qon ivishini ta'minlaydi.\n\n"
                "🛡 <b>Qon guruhlari:</b> I(0), II(A), III(B), IV(AB) va Rezus omil (Rh+ / Rh-)."
            ),
            "guide": (
                "📘 <b>6-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Qon hajmi:</b> 4.5 - 5.0 litr.\n"
                "• <b>Gemoglobin:</b> Temir moddasi tutadi, o'pkada oksi-gemoglobin hosil qiladi.\n"
                "• <b>Fagotsitoz:</b> I.I. Mechnikov kashf qilgan (leykotsitlar mikrobni yutishi).\n"
                "• <b>Vaksina:</b> Zaiflashtirilgan mikrob (faol immunitet);\n"
                "• <b>Zardob:</b> Tayyor antitanalar (sust immunitet)."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Qon shaklli elementlari va eritrotsitlar (12 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Fagotsitoz — leykotsitlar mikrobni yo'q qilish jarayoni"
            )
        },
        {
            "id": "7",
            "title": "7-mavzu: Qon aylanish sistemasi: Yurak va qon tomirlar",
            "text": (
                "📖 <b>7-MAVZU: YURAK VA QON AYLANISH SISTEMASI</b>\n\n"
                "🫀 <b>Yurak tuzilishi:</b>\n"
                "• 4 kamerali muskul a'zosi: 2 bo'lmacha va 2 qorincha.\n"
                "• Chap qorincha devori eng qalin (10-15 mm).\n"
                "• Tavaqali va yarimoysimon klapanlar qonning faqat bir yo'nalishda oqishini ta'minlaydi.\n\n"
                "🔄 <b>Qon aylanish doiralari:</b>\n"
                "1️⃣ <b>Katta qon aylanish:</b> Chap qorincha ➔ Aorta ➔ Barcha to'qimalar ➔ Venalar ➔ O'ng bo'lmacha (20-23 soniya).\n"
                "2️⃣ <b>Kichik qon aylanish:</b> O'ng qorincha ➔ O'pka arteriyasi ➔ O'pka ➔ O'pka venalari ➔ Chap bo'lmacha (4-5 soniya)."
            ),
            "guide": (
                "📘 <b>7-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Yurak sikli:</b> 0.8 soniya (0.1 s bo'lmacha qisqarishi, 0.3 s qorincha qisqarishi, 0.4 s umumiy tinchlik).\n"
                "• <b>Klapanlar:</b> Bo'lmacha va qorincha o'rtasida tavaqali, tomirlar chiqishida yarimoysimon klapanlar.\n"
                "• <b>Qon bosimi:</b> Normal 110-120 / 70-80 mm simob ustuni.\n"
                "• <b>Puls:</b> Tinch holatda daqiqasiga 60-80 marta uradi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Yurak anatomiyasi va qon tomirlar tizimi (14 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Yurak klapanlarining dinamik ochilib-yopilishi"
            )
        },
        {
            "id": "8",
            "title": "8-mavzu: Nafas olish organlari va gazlar almashinuvi",
            "text": (
                "📖 <b>8-MAVZU: NAFAS OLISH SISTEMASI VA GAZLAR ALMASHINUVI</b>\n\n"
                "🔹 <b>Nafas a'zolari:</b>\n"
                "• Burun bo'shlig'i ➔ Hiqildoq ➔ Kekirdak (traxeya) ➔ Bronxlar ➔ O'pka.\n"
                "• O'ng o'pka 3 bo'lakli, chap o'pka 2 bo'lakli.\n\n"
                "🫁 <b>Alveolalar:</b> O'pkada 300–400 million alveola bo'lib, umumiy nafas yuzasi 100 m² ga yetadi.\n"
                "Gazlar almashinuvi diffuziya yo'li bilan kechadi: qonga O₂ o'tadi, qondan esa CO₂ chiqadi.\n"
                "Nafas markazi uzunchoq miyada joylashgan."
            ),
            "guide": (
                "📘 <b>8-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Hiqildoq qopqog'i:</b> Ovqat yutilganda nafas yo'lini yopib turadi.\n"
                "• <b>O'pkaning tiriklik sig'imi:</b> 3500 - 4500 ml (spirometr bilan o'lchanadi).\n"
                "• <b>Havoda:</b> Nafas olinadigan havoda 21% O₂, 0.03% CO₂; chiqariladigan havoda 16% O₂, 4% CO₂.\n"
                "• <b>Nafas harakati:</b> Diafragma va qovurg'alararo muskullar qisqaradi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Nafas olish va gazlar almashinuvi (9 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Alveola va kapillyar devorida gazlar diffuziyasi"
            )
        },
        {
            "id": "9",
            "title": "9-mavzu: Ovqat hazm qilish sistemasi va moddalar almashinuvi",
            "text": (
                "📖 <b>9-MAVZU: OVQAT HAZM QILISH VA MODDALAR ALMASHINUVI</b>\n\n"
                "🔹 <b>Hazm qilish yo'li (8-10 metr):</b>\n"
                "• <b>Og'iz bo'shlig'i:</b> Tishlar (32 ta doimiy), so'lak bezlari (amilaza fermenti uglevodlarni parchalaydi).\n"
                "• <b>Qizilo'ngach</b> orqali ovqat oshqozonga tushadi.\n"
                "• <b>Oshqozon:</b> Xlorid kislota va pepsin fermenti oqsillarni parchalaydi.\n"
                "• <b>Ingichka ichak:</b> Jigar ishlab chiqargan o't suyuqligi yog'larni emulsiyalaydi, me'da osti bezi shirasi (tripsin, lipaza, amilaza) barcha moddalarni parchalaydi. Ichak vorsinkalari orqali so'riladi.\n"
                "• <b>Yo'g'on ichak:</b> Suv qayta so'riladi, axlat massasi shakllanadi."
            ),
            "guide": (
                "📘 <b>9-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Tishlar:</b> 8 ta kurak, 4 ta qoziq, 8 ta kichik oziq, 12 ta katta oziq = jami 32 ta.\n"
                "• <b>Jigar:</b> O't suyuqligi ishlab chiqaradi, yog'larni parchalanishga tayyorlaydi.\n"
                "• <b>Pepsin:</b> Faqat nordon muhitda (xlorid kislota borligida) ishlaydi.\n"
                "• <b>Vitaminlar:</b> C (singa kasalligi), D (raxit), A (shabko'rlik), B1 (beri-beri)."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Ovqat hazm qilish va fermentlar faoliyati (13 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Ingichka ichak vorsinkalarida ozuqa so'rilishi"
            )
        },
        {
            "id": "10",
            "title": "10-mavzu: Ayirish sistemasi: Buyraklar va teri gigiyenasi",
            "text": (
                "📖 <b>10-MAVZU: AYIRISH SISTEMASI VA TERI TUZILISHI</b>\n\n"
                "🔹 <b>Buyraklar:</b> Bel sohasida joylashgan juft loviyasimon a'zo. Asosiy funktsional birligi — <b>nefron</b> (har bir buyrakda 1 milliondan ortiq).\n\n"
                "💧 <b>Siydik hosil bo'lishi:</b>\n"
                "1️⃣ <b>Birlamchi siydik (Filtratsiya):</b> Koptokchalarda kuniga 150–180 litr filtrlanadi.\n"
                "2️⃣ <b>Ikkilamchi siydik (Qayta so'rilish):</b> Buyrak naychalarida suv va foydali moddalar qayta so'rilib, kuniga 1.5 litr ikkilamchi siydik hosil bo'ladi va chiqariladi.\n\n"
                "🧖 <b>Teri:</b> Epidermis (ustki), Derma (chin teri: retseptorlar, yog' va ter bezlari), Teriosti yog' kletchatkasi."
            ),
            "guide": (
                "📘 <b>10-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Nefron:</b> Buyrakning strukturaviy birligi.\n"
                "• <b>Birlamchi siydik:</b> Kuniga 150-180 litr (oqsil va hujayralardan xoli plazma).\n"
                "• <b>Ikkilamchi siydik:</b> Kuniga 1.5 litr (mochevina, siydik kislotasi va tuzlar).\n"
                "• <b>Teri:</b> Termoregulyatsiya markazi, kuniga 500-1000 ml ter chiqaradi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Buyrak tuzilishi va siydik hosil bo'lishi (11 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Buyrak koptokchalarida filtratsiya va nefron ishlashi"
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
                "2. <b>Ko'prik va O'rta miya:</b> Ko'rish va eshitishga yo'naltiruvchi reflekslar, muskul tonusi.\n"
                "3. <b>Miyacha:</b> Harakatlar koordinatsiyasi va muvozanat.\n"
                "4. <b>Oraliq miya:</b> Talamus va gipotalamus (termoregulyatsiya, ochlik, to'qlik markazlari).\n"
                "5. <b>Katta yarim sharlar:</b> Oliy asab faoliyati, tafakkur, nutq va xotira."
            ),
            "guide": (
                "📘 <b>11-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Refleks yoyi:</b> Retseptor ➔ Sezuvchi neyron ➔ Markaz ➔ Harakatlantiruvchi neyron ➔ Ishchi organ.\n"
                "• <b>Bosh miya og'irligi:</b> Katta odamda o'rtacha 1300 - 1400 gramm.\n"
                "• <b>Miyacha zararlansa:</b> Odam chayqalib yuradi, aniq harakatlar bajara olmaydi.\n"
                "• <b>Simpatik nerv:</b> Yurakni tezlashtiradi; <b>Parasimpatik:</b> Sekinlashtiradi."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Nerv sistemasi va bosh miya bo'limlari (15 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Neyronlararo sinaps orqali elektr impulsi uzatilishi"
            )
        },
        {
            "id": "12",
            "title": "12-mavzu: Sezgi a'zolari: Ko'rish, eshitish va boshqa analizatorlar",
            "text": (
                "📖 <b>12-MAVZU: SEZGI ORGANLARI (ANALIZATORLAR)</b>\n\n"
                "🔹 <b>Analizator:</b> Retseptor ➔ O'tkazuvchi nerv yo'li ➔ Bosh miya po'stlog'i markazi.\n\n"
                "👁 <b>Ko'rish organi (Ko'z):</b>\n"
                "• Shox parda, qorachiq, ko'z gavhari va shishasimon tana yorug'likni sindiradi.\n"
                "• <b>To'r parda:</b> Tayoqchalar (oq-qora, tungi ko'rish) va kolbachalar (rangli ko'rish).\n\n"
                "👂 <b>Eshitish organi (Quloq):</b>\n"
                "• Tashqi quloq (quloq suprasi, eshitish yo'li), O'rta quloq (nog'ora parda, bolg'acha, sandon, uzangi), Ichki quloq (chig'anoq, Kortiy a'zosi).\n"
                "• Yarimhalqa naylar — muvozanat apparatini hosil qiladi."
            ),
            "guide": (
                "📘 <b>12-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>Axborot:</b> Tashqi olam ma'lumotining 90% ini ko'rish orqali olamiz.\n"
                "• <b>Yaqindan ko'rish:</b> Tasvir to'r parda oldiga tushadi (botiq linza kerak).\n"
                "• <b>Uzoqdan ko'rish:</b> Tasvir to'r parda orqasiga tushadi (qabariq linza kerak).\n"
                "• <b>Kortiy a'zosi:</b> Eshitish retseptorlari joylashgan a'zo."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Ko'z va quloq tuzilishi, eshitish mexanizmi (10 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Ko'z gavhari akkomodatsiyasi va yorug'lik sinishi"
            )
        },
        {
            "id": "13",
            "title": "13-mavzu: Oliy asab faoliyati va psixika",
            "text": (
                "📖 <b>13-MAVZU: OLIY ASAB FAOLIYATI VA PSIXIKA</b>\n\n"
                "🔹 I.M. Sechenov va I.P. Pavlov bosh miya yarim sharlari po'stlog'i faoliyatini ilmiy asoslab bergan.\n\n"
                "🔄 <b>Reflekslar:</b>\n"
                "• <b>Shartsiz reflekslar:</b> Tug'ma, irsiy, butun turga xos (emish, yutinish, ko'z pirpiratish).\n"
                "• <b>Shartli reflekslar:</b> Hayot davomida orttiriladi, vaqtinchalik bog'lanishlar hosil qiladi.\n\n"
                "🗣 <b>Signallar sistemalari:</b>\n"
                "• <b>1-signal:</b> Hayvon va odamda umumiy (bevosita tovush, rang, hid).\n"
                "• <b>2-signal:</b> Faqat odamga xos (so'z, nutq, yozuv, fikrlash)."
            ),
            "guide": (
                "📘 <b>13-MAVZU BO'YICHA QISQA QO'LLANMA:</b>\n\n"
                "• <b>I.P. Pavlov:</b> Shartli reflekslar ta'limotiga asos solgan (Nobel mukofoti).\n"
                "• <b>2-signal sistemasi:</b> Inson tafakkuri va nutqiga xos.\n"
                "• <b>Temperament turlari:</b> Sangvinik (chaqqon), Xolerik (tez qizishuvchi), Flegmatik (bosiq), Melanxolik (hissiyotchan).\n"
                "• <b>Uyqu:</b> Miya hujayralarining himoyalanish va o'zini tiklash jarayoni."
            ),
            "media": (
                "🎥 <b>Mavzuga oid Video va 3D modellar:</b>\n\n"
                "🎬 <b>Video dars:</b> Shartli va shartsiz reflekslar mexanizmi (11 daqiqa)\n"
                "🧬 <b>3D Animatsiya:</b> Bosh miyada xotira va yangi refleks yoyi hosil bo'lishi"
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
            "desc": "Yurak kameralari, miokard qisqarishi, avtomatizm va qon tomirlar tizimi."
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
