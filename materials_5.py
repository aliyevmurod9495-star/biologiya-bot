"""
5-sinf Biologiya o'quv materiallari:
Mavzu ma'ruzalari, qisqa qo'llanmalar, video darslar va 3D animatsiyalar.
Barcha 18 ta mavzu O'zbekiston umumta'lim maktablarining 5-sinf Biologiya darsligi rasmiy mundarijasi va dasturi bo'yicha to'liq kiritilgan.
"""

from typing import Dict, List, Any

TOPICS_5: List[Dict[str, Any]] = [
    # -------------------------------------------------------------
    # 1-BOB. BIOLOGIYA — TIRIK ORGANIZMLAR HAQIDAGI FAN
    # -------------------------------------------------------------
    {
        "id": "1",
        "title": "1-§. Biologiya — hayot haqidagi fan",
        "text": (
            "📖 <b>1-§. BIOLOGIYA — HAYOT HAQIDAGI FAN</b>\n\n"
            "🔹 <b>Biologiya</b> — tirik organizmlarning tuzilishi, hayotiy faoliyati, kelib chiqishi, "
            "rivojlanishi hamda ularning o‘zaro va atrof-muhit bilan munosabatlarini o‘rganuvchi fandir. "
            "«Biologiya» atamasi yunoncha <i>«bios»</i> — hayot va <i>«logos»</i> — fan, ta’limot so‘zlaridan olingan.\n\n"
            "🌿 <b>Biologiya fanining tarixi va allomalarning hissasi:</b>\n"
            "• Qadim zamonlardan insonlar o‘simlik va hayvonlarni oziq-ovqat, kiyim-kechak va dori-darmon sifatida o‘rganib kelishgan.\n"
            "• <b>Abu Rayhon Beruniy</b> o‘zining mashhur <i>«Saydana» («Dorivor o‘simliklar»)</i> asarida 1000 dan ortiq dorivor o‘simliklar, ularning shifobaxsh xususiyatlarini yozib qoldirgan.\n"
            "• <b>Abu Ali ibn Sino</b> o‘zining shoh asari <i>«Tib qonunlari»</i>da yuzlab dorivor vositalar, jarrohlik, yuqumli kasalliklar va sog‘lom turmush tarzi haqida qimmatli ma’lumotlar bergan.\n"
            "• <b>Zahiriddin Muhammad Bobur</b> o‘zining <i>«Boburnoma»</i> asarida O‘rta Osiyo, Afg‘oniston va Hindistonning o‘simlik va hayvonot dunyosi, ularning o‘ziga xos biologik xususiyatlarini batafsil tasvirlagan.\n\n"
            "🔬 <b>Biologiyaning asosiy tarmoqlari:</b>\n"
            "• <b>Botanika:</b> O‘simliklar olamini o‘rganadi.\n"
            "• <b>Zoologiya:</b> Hayvonot dunyosini tadqiq etadi.\n"
            "• <b>Mikologiya:</b> Zamburug‘lar dunyosini o‘rganadi.\n"
            "• <b>Mikrobiologiya:</b> Ko‘zga ko‘rinmas mikroorganizmlarni (bakteriyalar, viruslar) o‘rganadi.\n"
            "• <b>Sitologiya:</b> Hujayraning tuzilishi va vazifalarini tekshiradi.\n"
            "• <b>Anatomiya:</b> Tirik organizmlarning ichki tuzilishini o‘rganadi.\n"
            "• <b>Fiziologiya:</b> Organizmlarda boradigan hayotiy jarayonlar (oziqlanish, nafas olish, qon aylanish)ni tadqiq qiladi.\n"
            "• <b>Sistematika:</b> Tirik mavjudotlarni o‘xshashlik belgilariga ko‘ra guruhlarga ajratadi.\n"
            "• <b>Ekologiya:</b> Organizmlarning o‘zaro va tashqi muhit bilan bog‘lanish qonuniyatlarini o‘rganadi.\n"
            "• <b>Genetika:</b> Irsiyat va o‘zgaruvchanlik qonuniyatlarini o‘rganadi."
        ),
        "guide": (
            "📘 <b>1-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Biologiya:</b> «bios» — hayot, «logos» — ta’limot.\n"
            "• <b>Allomalar:</b> Beruniy («Saydana»), Ibn Sino («Tib qonunlari»), Bobur («Boburnoma»).\n"
            "• <b>Sohalar:</b> Botanika (o‘simlik), Zoologiya (hayvon), Mikologiya (zamburug‘), Sitologiya (hujayra), Anatomiya (ichki tuzilish), Fiziologiya (faoliyat)."
        ),
        "media": "🎥 <b>Video dars:</b> Biologiya faniga kirish va buyuk allomalar merosi (10 daqiqa)"
    },
    {
        "id": "2",
        "title": "2-§. Tirik organizmlarning xususiyatlari",
        "text": (
            "📖 <b>2-§. TIRIK ORGANIZMLARNING XUSUSIYATLARI</b>\n\n"
            "🔹 Tirik tabiat jonsiz tabiatdan o‘ziga xos fundamental hayotiy belgilari bilan tubdan farq qiladi:\n\n"
            "⚡ <b>Tiriklikning asosiy xususiyatlari:</b>\n"
            "1. <b>Hujayraviy tuzilish:</b> Hamma tirik mavjudotlar (viruslardan tashqari) hujayralardan tashkil topgan.\n"
            "2. <b>Moddalar va energiya almashinuvi:</b> Har qanday tirik organizm tashqi muhitdan zarur moddalarni qabul qiladi, o‘zlashtiradi va keraksiz qoldiqlarni tashqariga chiqaradi.\n"
            "3. <b>Oziqlanish:</b>\n"
            "   • <i>Avtotrof oziqlanish:</i> Quyosh nuri yordamida o‘z tanasida noorganik moddalardan organik modda hosil qiluvchilar (yashil o‘simliklar).\n"
            "   • <i>Geterotrof oziqlanish:</i> Tayyor organik moddalar bilan oziqlanuvchilar (hayvonlar, zamburug‘lar, ko‘pchilik bakteriyalar).\n"
            "4. <b>Nafas olish:</b> Kislorod yutib, karbonat angidrid chiqarish orqali oziq moddalardan yashash uchun kerakli energiyani ajratib olish.\n"
            "5. <b>O‘sish va rivojlanish:</b> O‘lcham va massaning ortishi (o‘sish) hamda sifat jihatdan yangi belgilarning shakllanishi (rivojlanish).\n"
            "6. <b>Ko‘payish:</b> O‘zidan nasl qoldirish, turning Yer yuzida saqlanib qolishini ta’minlash (jinsiy va jinssiz ko‘payish).\n"
            "7. <b>Ta’sirlanish:</b> Tashqi va ichki muhit o‘zgarishlariga javob qaytarish xususiyati (masalan, kishi qo‘lini issiqdan tortib olishi, mimoza barglarining teginishdan bukilishi).\n"
            "8. <b>Harakatlanish:</b> Hayvonlarda aktiv harakat (yugurish, uchish, suzish), o‘simliklarda esa sekin harakatlar (yorug‘likka tomon burilish — tropizm)."
        ),
        "guide": (
            "📘 <b>2-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tiriklik xususiyatlari:</b> Hujayra, moddalar almashinuvi, oziqlanish, nafas olish, o‘sish, ko‘payish, ta’sirlanish, harakat.\n"
            "• <b>Avtotrof:</b> O‘zi oziq yaratadi (o‘simlik).\n"
            "• <b>Geterotrof:</b> Tayyor oziq yeydi (hayvon, zamburug‘)."
        ),
        "media": "🎥 <b>Video dars:</b> Tirik organizmlarning umumiy xususiyatlari va tajribalar (8 daqiqa)"
    },
    {
        "id": "3",
        "title": "3-§. Biologiyaning o‘rganish usullari",
        "text": (
            "📖 <b>3-§. BIOLOGIYANING O‘RGANISH USULLARI VA LABORATORIYA JIHOZLARI</b>\n\n"
            "🔹 Biologiya fanida tabiat sirlarini o‘rganish uchun bir necha asosiy ilmiy usullardan foydalaniladi:\n\n"
            "🔬 <b>Asosiy o‘rganish usullari:</b>\n"
            "1. <b>Kuzatish usuli:</b> O‘rganilayotgan tirik ob’yektning tabiiy holatiga aralashmasdan, sezgi organlari yoki asboblar yordamida ma’lumot to‘plash.\n"
            "2. <b>Taqqoslash usuli:</b> Ikki yoki undan ortiq organizmning tuzilishi, belgilari va yashash tarzini o‘zaro solishtirish, o‘xshashlik va farqlarini aniqlash.\n"
            "3. <b>Tajriba (Eksperiment) usuli:</b> Organizmni maxsus sun’iy yaratilgan sharoitda sinovdan o‘tkazib o‘rganish (masalan, o‘simlikni rangli suvga solib poyada suv ko‘tarilishini tekshirish, F.Redi va L.Paster tajribalari).\n"
            "4. <b>Tarixiy usul:</b> Tirik tabiatning uzoq o‘tmishdagi rivojlanish bosqichlarini, qadimgi tosh qotgan qoldiqlarni tahlil qilish (paleontologiya).\n\n"
            "🔍 <b>Kattalashtiruvchi asboblar:</b>\n"
            "• <b>Qo‘l lupasi:</b> Ob’yektni 2 martadan 20 martagacha kattalashtiradi.\n"
            "• <b>Shtativli lupa:</b> Shtativga o‘rnatilgan bo‘lib, ob’yektni 20–25 martagacha kattalashtiradi.\n"
            "• <b>Yorug‘lik mikroskopi:</b> Ob’yektni 100 martadan 1500–2000 martagacha kattalashtirib ko‘rsatadi.\n"
            "  - <i>Mikroskopning asosiy qismlari:</i> <b>Okulyar</b> (ko‘z bilan qaraladigan linza), <b>Tubus</b> (ko‘rish trubkasi), <b>Obyektiv</b> (predmetga qaraladigan linzalar to‘plami), <b>Shtativ</b> (tayanch), <b>Buyum stoli</b> (preparat qo‘yiladigan o‘rin), <b>Ko‘zgu</b> (yorug‘lik yo‘naltiruvchi), <b>Makrovint</b> va <b>Mikrovint</b> (tasvirni aniqlashtiruvchi buragichlar).\n"
            "  - <i>Kattalashtirish darajasini hisoblash:</i> Okulyar soni × Obyektiv soni (masalan: 10 × 40 = 400 marta).\n\n"
            "🧪 <b>Laboratoriya asboblari:</b>\n"
            "• <b>Probirka:</b> Moddalarning xususiyatlarini o‘rganish va reaksiyalar o‘tkazish uchun shisha idish.\n"
            "• <b>Petri idishi:</b> Bakteriyalar va zamburug‘larni ozuqa muhitida o‘stirish uchun yassi shisha idishcha.\n"
            "• <b>Pinset:</b> Mayda ob’yektlarni ushlab olish va preparat tayyorlash uchun qisqich.\n"
            "• <b>Pipetka:</b> Suyuqliklarni tomizish uchun mo‘ljallangan shisha naycha.\n"
            "• <b>Skalpel:</b> Biologik ob’yektlarni kesish uchun o‘tkir tig‘li kichik jarrohlik pichog‘i.\n"
            "• <b>Buyum va qoplag‘ich oyna:</b> Mikroskop ostida preparat tayyorlash uchun tekis shishalar."
        ),
        "guide": (
            "📘 <b>3-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Usullar:</b> Kuzatish (aralashmaslik), Taqqoslash (solishtirish), Tajriba (sun’iy sharoit), Tarixiy (o‘tmishni tiklash).\n"
            "• <b>Lupa:</b> Qo‘l lupasi (2–20 marta), Shtativli lupa (20–25 marta).\n"
            "• <b>Mikroskop:</b> Okulyar × Obyektiv = Jami kattalashtirish.\n"
            "• <b>Jihozlar:</b> Pinset (qisish), Pipetka (tomizish), Petri idishi (bakteriya o‘stirish), Skalpel (kesish)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Yorug‘lik mikroskopining 3D modeli va preparat tayyorlash qoidalari"
    },
    {
        "id": "4",
        "title": "4-§. Hujayra — tiriklikning asosi",
        "text": (
            "📖 <b>4-§. HUJAYRA — TIRIKLIKNING ASOSI</b>\n\n"
            "🔹 <b>Hujayra</b> — barcha tirik organizmlarning eng kichik tuzilish, tiriklik va ko‘payish birligidir. "
            "U ilk bor 1665-yilda ingliz tabiatshunosi <b>Robert Guk</b> tomonidan po‘kak kesmasida kashf etilgan.\n\n"
            "🔬 <b>Hujayraning asosiy qismlari:</b>\n"
            "1. <b>Hujayra qobig‘i (po‘sti):</b> Hujayrani tashqi tomondan o‘rab, unga muayyan shakl va mustahkamlik beradi. O‘simliklarda u kletchatka (sellyuloza)dan iborat pishiq bo‘ladi. Hayvonlarda esa yupqa elastik membrana bo‘ladi.\n"
            "2. <b>Sitoplazma:</b> Hujayra ichidagi shaffof, rangsiz, yarim suyuq, doimiy harakatdagi tirik muhit. U barcha organoidlarni o‘zaro bog‘lab turadi.\n"
            "3. <b>Yadro va yadrocha:</b> Hujayraning markaziy boshqaruv organi. Unda xromosomalar joylashgan bo‘lib, irsiy belgilar saqlanadi va hujayra bo‘linishi boshqariladi.\n"
            "4. <b>Vakuola:</b> Hujayra shirasi bilan to‘lgan bo‘shliq. O‘simliklarda yirik bo‘lib, suv, qandlar, organik kislotalar va rang beruvchi moddalarni saqlaydi, turgor bosimini beradi.\n"
            "5. <b>Plastidalar (faqat o‘simliklarda):</b>\n"
            "   • <i>Xloroplastlar:</i> Yashil rangli (xlorofill pigmenti), quyosh nuri yordamida fotosintez qiladi.\n"
            "   • <i>Xromoplastlar:</i> Sariq, to‘q sariq, qizil rangli, gul va mevalarga rang beradi.\n"
            "   • <i>Leykoplastlar:</i> Rangsiz plastidalar, kraxmal va zaxira oziqlarni to‘playdi.\n\n"
            "🌱 <b>Hujayralarning xilma-xilligi:</b>\n"
            "• Qonning qizil hujayralari — <b>eritrotsitlar</b> ikki tomoni botiq disksimon bo‘lib, kislorod tashiydi.\n"
            "• Oq qon hujayralari — <b>leykotsitlar</b> soxta oyoqlar hosil qilib, mikroblarni yutadi.\n"
            "• Nerv hujayralari — <b>neyronlar</b> uzun va kalta o‘simtalarga ega bo‘lib, impulslarni o‘tkazadi.\n"
            "• Bargning <b>og‘izcha hujayralari</b> loviyasimon juft bo‘lib, gaz almashinuvi va bug‘latishni boshqaradi.\n\n"
            "🧩 <b>To‘qima</b> — kelib chiqishi, tuzilishi va bajaradigan vazifasi bir xil bo‘lgan hujayralar va hujayralararo moddalar yig‘indisidir."
        ),
        "guide": (
            "📘 <b>4-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Kashfiyotchi:</b> 1665-yil, Robert Guk.\n"
            "• <b>Asosiy qismlar:</b> Qobiq (sellyuloza), Sitoplazma (harakatdagi muhit), Yadro (irsiyat markazi), Vakuola (shira ombori).\n"
            "• <b>Plastidalar:</b> Xloroplast (yashil), Xromoplast (sariq-qizil), Leykoplast (rangsiz zaxira)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> O‘simlik va hayvon hujayrasining 3D qiyosiy anatomiyasi"
    },
    # -------------------------------------------------------------
    # 2-BOB. TIRIK ORGANIZMLARNING XILMA-XILLIGI
    # -------------------------------------------------------------
    {
        "id": "5",
        "title": "5-§. Tirik organizmlar haqida umumiy ma‘lumot",
        "text": (
            "📖 <b>5-§. TIRIK ORGANIZMLAR HAQIDA UMUMIY MA‘LUMOT VA ULARNING TASNIFI</b>\n\n"
            "🔹 Yer yuzida tirik mavjudotlarning millionlab turlari yashaydi. Ularni o‘rganish va tartibga solish uchun biologik tasnif (sistematika) qo‘llaniladi.\n\n"
            "🌐 <b>Tiriklik olamining katta guruhlari:</b>\n"
            "1. <b>Hujayrasiz organizmlar:</b> <b>Viruslar</b> — hayotning hujayrasiz shakli bo‘lib, faqat tirik xo‘jayin hujayrasi ichida ko‘paya oladi (tamaki mozaikasi virusi, gripp, quturish, bakteriofag — bakteriyani yemiruvchi virus).\n"
            "2. <b>Hujayrali organizmlar:</b>\n"
            "   • <b>Prokariotlar:</b> Shakllangan yadroga ega bo‘lmagan eng qadimgi sodda organizmlar (bakteriyalar, ko‘k-yashil suvo‘tlar).\n"
            "   • <b>Eukariotlar:</b> Haqiqiy yadro qobig‘i va yadrosi shakllangan organizmlar (zamburug‘lar, o‘simliklar, hayvonlar).\n\n"
            "🌿 <b>Tirik organizmlarning 4 ta asosiy dunyosi:</b>\n"
            "• <b>Bakteriyalar dunyosi:</b> Prokariot bir hujayrali mikroorganizmlar.\n"
            "• <b>Zamburug‘lar dunyosi:</b> Geterotrof oziqlanuvchi, o‘simlik va hayvon belgilarini o‘zida jamlagan eukariotlar.\n"
            "• <b>O‘simliklar dunyosi (Flora):</b> Avtotrof oziqlanuvchi, xloroplastlarga ega eukariotlar.\n"
            "• <b>Hayvonot dunyosi (Fauna):</b> Geterotrof oziqlanuvchi, faol harakatlanuvchi eukariotlar.\n\n"
            "🏷 <b>Sistematika va Karl Linney:</b>\n"
            "• Shved olimi <b>Karl Linney</b> tirik organizmlarni guruhlashning ilmiy asosini yaratdi va <b>qo‘shaloq (binar) lotincha nomlash</b> tizimini joriy qildi.\n"
            "• <i>Sistematik iyerarxiya:</i> Tur ➔ Urug‘ ➔ Oila ➔ Turkum (Tartib) ➔ Sinf ➔ Tip (Bo‘lim) ➔ Dunyo."
        ),
        "guide": (
            "📘 <b>5-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Hujayrasiz:</b> Viruslar (quturish, tamaki mozaikasi, bakteriofag).\n"
            "• <b>Prokariot:</b> Yadrosiz (bakteriyalar).\n"
            "• <b>Eukariot:</b> Haqiqiy yadroli (zamburug‘, o‘simlik, hayvon).\n"
            "• <b>4 dunyo:</b> Bakteriyalar, Zamburug‘lar, O‘simliklar (Flora), Hayvonlar (Fauna).\n"
            "• <b>Karl Linney:</b> Turlarni qo‘shaloq lotincha nomlash asoschisi."
        ),
        "media": "🎥 <b>Video dars:</b> Tirik dunyo shajarasi va Karl Linney tasnifi (9 daqiqa)"
    },
    {
        "id": "6",
        "title": "6-§. Bakteriyalar dunyosi",
        "text": (
            "📖 <b>6-§. BAKTERIYALAR DUNYOSI</b>\n\n"
            "🔹 <b>Bakteriyalar</b> — Yer yuzidagi eng qadimgi, bir hujayrali, mikroskopik prokariot organizmlardir. Ular tuproqda, suvda, havoda, muzliklarda va organizmlar ichida keng tarqalgan.\n\n"
            "🦠 <b>Bakteriyalarning shakllari:</b>\n"
            "• <b>Kokklar:</b> Sharsimon bakteriyalar.\n"
            "• <b>Batsillalar:</b> Tayoqchasimon bakteriyalar.\n"
            "• <b>Vibrionlar:</b> Vergulsimon buralgan bakteriyalar (masalan, vabo vibrioni).\n"
            "• <b>Spirillalar:</b> Spiral shaklidagi cho‘ziq bakteriyalar.\n\n"
            "🔬 <b>Bakteriya hujayrasining tuzilishi:</b>\n"
            "• Qalin po‘st va shilimshiq kapsula (himoya qiladi).\n"
            "• Sitoplazma va membranalar.\n"
            "• Yadro shakllanmagan — irsiy axborot halqasimon DNK ko‘rinishida sitoplazmada ochiq yotadi (nukleoid).\n"
            "• Xivchinlar yoki kiprikchalar (harakatlanish uchun).\n"
            "• <b>Spora hosil qilish:</b> Noqulay sharoit (qurg‘oqchilik, sovuq, issiq) boshlanganda bakteriya qalin qobiq hosil qilib sporaga aylanadi va o‘nlab yillar tirik saqlanadi.\n\n"
            "🌱 <b>Tabiatda va inson hayotidagi ahamiyati:</b>\n"
            "• <b>Chirish bakteriyalari:</b> O‘lik o‘simlik va hayvon qoldiqlarini parchalab, chirindiga va mineral tuzlarga aylantiradi (tabiat sanitarlari).\n"
            "• <b>Tugunak bakteriyalari:</b> Dukkakli o‘simliklar (beda, no‘xat) ildizida yashab, havodagi erkin azotni o‘zlashtirib tuproqni boyitadi (simbioz).\n"
            "• <b>Bijg‘ituvchi bakteriyalar:</b> Qatiq, pishloq, tvorog, sirka tayyorlashda va karam tuzlashda ishlatiladi.\n"
            "• <b>Zararli va kasallik qo‘zg‘atuvchi bakteriyalar:</b> Oziq-ovqatlarni buzadi, vabo, sil, bo‘g‘ma, ichburug‘ va kuydirgi kabi og‘ir kasalliklarni chaqiradi.\n"
            "• <b>Fitontsidlar:</b> Qarag‘ay, archa, sarimsoq va piyoz ajratadigan bakteritsid moddalar havoni bakteriyalardan tozalaydi."
        ),
        "guide": (
            "📘 <b>6-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Shakllar:</b> Kokk (shar), Batsilla (tayoqcha), Vibrion (vergul), Spirilla (spiral).\n"
            "• <b>Tuzilishi:</b> Yadrosiz (prokariot), halqasimon DNK, spora (noqulay sharoitdan saqlanish).\n"
            "• <b>Foydali:</b> Chirish (sanitar), Tugunak (azot to‘plovchi), Sut achituvchi (qatiq).\n"
            "• <b>Fitontsid:</b> Archadan ajralib bakteriyalarni o‘ldiruvchi modda."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Bakteriya hujayrasi tuzilishi va bo‘linishi 3D da"
    },
    {
        "id": "7",
        "title": "7-§. Zamburug‘lar dunyosi",
        "text": (
            "📖 <b>7-§. ZAMBURUG‘LAR DUNYOSI</b>\n\n"
            "🔹 <b>Zamburug‘lar</b> — o‘simlik va hayvonlarga xos belgilarni o‘zida mujassam etgan o‘ziga xos eukariot tirik mavjudotlar guruhidir.\n\n"
            "⚖️ <b>Zamburug‘larning o‘simlik va hayvonlarga o‘xshashligi:</b>\n"
            "• <i>O‘simliklarga o‘xshashligi:</i> Harakatsiz hayot kechirishi, cheksiz o‘sishi, oziqni shimib olishi, hujayra qobig‘iga egaligi.\n"
            "• <i>Hayvonlarga o‘xshashligi:</i> Xloroplast va xlorofillning yo‘qligi, tayyor organik moddalar bilan <b>geterotrof</b> oziqlanishi, qobig‘ida <b>xitin</b> moddasi bo‘lishi, zaxira oziq sifatida glikogen to‘plashi.\n\n"
            "🍄 <b>Zamburug‘larning asosiy guruhlari:</b>\n"
            "1. <b>Qalpoqchali (shlyapkali) zamburug‘lar:</b>\n"
            "   • Tana tuzilishi: Yer ostidagi ingichka oq iplar — <b>mitseliy (zamburug‘ tanasi)</b> va yer ustidagi <b>mevali tana (poyacha va qalpoqcha)</b>.\n"
            "   • <i>Iste’mol qilinadiganlar:</i> Oq qo‘ziqorin, qayinquloq, shampinion, moyqo‘ziqorin.\n"
            "   • <i>Zaharli zamburug‘lar:</i> Qizil muxomor, oq qurbaqasalla (pale toadstool). Ular o‘limga olib kelishi mumkin.\n"
            "2. <b>Mog‘or zamburug‘lari:</b>\n"
            "   • <i>Mukor:</i> Non va sabzavotlar ustida oq-kulrang momiq g‘ubor hosil qiladi, sporangiylarida qora sporalar yetiladi.\n"
            "   • <i>Penisill:</i> Yashil-moviy mog‘or zamburug‘i. 1928-yilda ingliz olimi <b>Aleksandr Fleming</b> undan dunyodagi birinchi antibiotik — <b>penitsillin</b>ni kashf qilgan.\n"
            "3. <b>Achitqi (xamirturush) zamburug‘lari:</b>\n"
            "   • Bir hujayrali, mikroskopik zamburug‘lar. Mitseliy hosil qilmaydi, <b>kurtaklanish</b> yo‘li bilan tez ko‘payadi.\n"
            "   • Qandni parchalab spirt va karbonat angidrid ajratadi, non yopishda xamirni ko‘pirtirish uchun ishlatiladi.\n"
            "4. <b>Parazit zamburug‘lar:</b>\n"
            "   • Qishloq xo‘jaligiga katta zarar yetkazadi: <i>qorakuya</i> (bug‘doy va makkajo‘xori boshog‘ini qoraytiradi), <i>zang zamburug‘i</i> (barglarda qizg‘ish dog‘lar), <i>vilt (vertitsillium)</i> (g‘o‘zani quritadi)."
        ),
        "guide": (
            "📘 <b>7-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Xususiyati:</b> Xlorofillsiz, geterotrof, xitin qobiqli, mitseliydan iborat.\n"
            "• <b>Qalpoqchali:</b> Shampinion, oq qo‘ziqorin (yeyiladigan); Qizil muxomor (zaharli).\n"
            "• <b>Mog‘or:</b> Mukor (oq g‘ubor), Penisill (penitsillin antibiotigi olinadi).\n"
            "• <b>Achitqi:</b> Bir hujayrali, kurtaklanadi, xamir ko‘pirtiradi.\n"
            "• <b>Parazitlar:</b> Qorakuya, zang, vilt."
        ),
        "media": "🎥 <b>Video dars:</b> Zamburug‘larning sirli olami va mog‘or turlari (10 daqiqa)"
    },
    {
        "id": "8",
        "title": "8-§. O‘simliklar dunyosi",
        "text": (
            "📖 <b>8-§. O‘SIMLIKLAR DUNYOSI (FLORA)</b>\n\n"
            "🔹 <b>O‘simliklar</b> — fotosintez qilish orqali butun sayyoramizni kislorod va organik moddalar bilan ta’minlovchi avtotrof organizmlardir.\n\n"
            "🌱 <b>O‘simliklarning asosiy hayotiy shakllari:</b>\n"
            "1. <b>Daraxtlar:</b> Bitta yo‘g‘on, mustahkam yog‘ochlashgan tanaga ega bo‘lgan ko‘p yillik yirik o‘simliklar (chinor, terak, eman, olma, yong‘oq).\n"
            "2. <b>Butalar:</b> Poyasi yer yuzasidanoq bir nechta teng yog‘ochlashgan novdalarga shoxlanadigan, balandligi 0.8–3 metr bo‘lgan ko‘p yillik o‘simliklar (anor, na’matak, zirk, ligustrum).\n"
            "3. <b>Yarimbutalar:</b> Poyasining faqat pastki qismi yog‘ochlashib, yuqori yashil qismi har yili qishda qurib qoladigan o‘simliklar (shuvoq, izen, keyreuk).\n"
            "4. <b>O‘tlar:</b> Poyasi yog‘ochlashmagan, yumshoq va shirali o‘simliklar:\n"
            "   • <i>Bir yillik o‘tlar:</i> Bir vegetatsiya davrida urug‘dan unib, gullab, hosil berib quriydi (bug‘doy, arpa, makkajo‘xori, paxta).\n"
            "   • <i>Ikki yillik o‘tlar:</i> Birinchi yili vegetativ organlar, ikkinchi yili poya, gul va urug‘ hosil qiladi (sabzi, lavlagi, sholg‘om, karam).\n"
            "   • <i>Ko‘p yillik o‘tlar:</i> Yerosti organlari (ildizpoya, piyozbosh, tugunak) orqali ko‘p yillar yashaydi (beda, ajriq, lola, qoqio‘t).\n\n"
            "🌿 <b>O‘simliklarning bo‘linishi:</b>\n"
            "• <b>Tuban o‘simliklar:</b> Haqiqiy ildiz, poya va barg kabi organlarga ajralmagan (suvo‘tlar).\n"
            "• <b>Yuksak o‘simliklar:</b> Tanasi to‘qima va a’zolarga (vegetativ va generativ organlarga) ixtisoslashgan."
        ),
        "guide": (
            "📘 <b>8-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Hayotiy shakllar:</b> Daraxt (1 ta yo‘g‘on tana), Buta (tubidan shoxlangan ko‘p tana), Yarimbuta (pastki qismi yog‘ochlashgan), O‘tlar (bir, ikki va ko‘p yillik).\n"
            "• <b>Tuban:</b> Tana a’zolarga bo‘linmagan (suvo‘tlar).\n"
            "• <b>Yuksak:</b> Ildiz, poya, bargga ega o‘simliklar."
        ),
        "media": "🎥 <b>Video dars:</b> O‘simliklarning hayotiy shakllari va xilma-xilligi (8 daqiqa)"
    },
    {
        "id": "9",
        "title": "9-§. Tuban o‘simliklar",
        "text": (
            "📖 <b>9-§. TUBAN O‘SIMLIKLAR (SUVO‘TLAR)</b>\n\n"
            "🔹 <b>Suvo‘tlar (Algologiya)</b> — asosan suv muhitida yashovchi, tanasi ildiz, poya va barglarga ajralmagan eng qadimgi tuban o‘simliklardir.\n\n"
            "🌿 <b>Suvo‘tlarning tuzilish xususiyatlari:</b>\n"
            "• Ularning tanasi <b>tallom (qatbatan)</b> deb ataladi.\n"
            "• Suv tubiga birikish uchun <b>rizoidlar</b> (ildizsimon o‘simtalar) xizmat qiladi.\n"
            "• Xlorofill va boshqa pigmentlar maxsus organoid — <b>xromatofor</b>da joylashgan bo‘lib, fotosintez qiladi.\n\n"
            "🌱 <b>Bir hujayrali yashil suvo‘tlar:</b>\n"
            "• <b>Xlamidamonada:</b> Noksimon shaklli, oldingi uchida 2 ta xivchini, yorug‘lik sezuvchi qizil ko‘zchasi (stigma), kosachasimon xromatofori va 2 ta qisqaruvchi vakuolasi bor. Faol suzadi.\n"
            "• <b>Xlorella:</b> Sharsimon shaklli, xivchinlari va qizil ko‘zchasi yo‘q, suvda muallaq suzadi. Oqsil va vitaminlarga juda boy bo‘lib, suvni tozalashda va kosmik tadqiqotlarda qo‘llaniladi.\n\n"
            "🌾 <b>Ko‘p hujayrali yashil suvo‘tlar:</b>\n"
            "• <b>Ulotriks:</b> Oqmas va sekin oqar chuchuk suvlarda toshlarga yopishib yashovchi bir qator hujayralardan iborat ipsimon suvo‘t. Xromatofori ochiq halqa (bilaguzuk) shaklida.\n"
            "• <b>Spirogira:</b> Suv yuzida yashil balchiq hosil qiluvchi silliq ipsimon suvo‘t. Xromatofori tasmaga o‘xshash spiral shaklda buralgan.\n\n"
            "🌊 <b>Dengiz suvo‘tlari:</b>\n"
            "• <b>Qo‘ng‘ir suvo‘tlar (Laminariya):</b> «Dengiz karami» deb ataladi, bo‘yi bir necha metrgacha yetadi, tarkibida yod moddasi ko‘p bo‘ladi.\n"
            "• <b>Qizil suvo‘tlar (Porfira):</b> «Dengiz salati» deb ataladi, chuqur dengizlarda o‘sadi, undan qandolatchilikda ishlatiladigan <b>agar-agar</b> moddasi olinadi."
        ),
        "guide": (
            "📘 <b>9-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tallom:</b> Suvo‘tning a’zolarga ajralmagan tanasi.\n"
            "• <b>Xlamidamonada:</b> 2 xivchinli, qizil ko‘zchali, harakatchan.\n"
            "• <b>Xlorella:</b> Xivchinsiz, oqsilga boy, sharsimon.\n"
            "• <b>Ulotriks:</b> Halqasimon xromatoforli ip.\n"
            "• <b>Spirogira:</b> Spiral lentasimon xromatofor.\n"
            "• <b>Laminariya:</b> Dengiz karami (yodga boy), <b>Porfira:</b> Agar-agar olinadi."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Xlamidamonada va Ulotriksning mikroskopik tuzilishi 3D da"
    },
    {
        "id": "10",
        "title": "10-§. Yuksak o‘simliklar",
        "text": (
            "📖 <b>10-§. YUKSAK O‘SIMLIKLAR</b>\n\n"
            "🔹 <b>Yuksak o‘simliklar</b> — quruqlikda yashashga moslashgan, tanasi ildiz, poya va barg kabi ixtisoslashgan a’zolarga hamda rivojlangan to‘qimalarga ega o‘simliklardir.\n\n"
            "🌿 <b>1. Yuksak sporali o‘simliklar:</b> Ko‘payishi suv bilan bog‘liq bo‘lib, urug‘ hosil qilmaydi, spora orqali ko‘payadi:\n"
            "• <b>Yo‘sinlar (Moxlar):</b> Eng sodda yuksak o‘simliklar. Ildizi bo‘lmaydi, o‘rniga rizoidlar bo‘ladi. Poyasi va mayda barglari bor (masalan, funariya, sfagnum). Sfagnum yo‘sini suvni ko‘p shimadi va vaqt o‘tishi bilan <b>torf</b> hosil qiladi.\n"
            "• <b>Qirqbo‘g‘imlar:</b> Poyasi bo‘g‘im va bo‘g‘im oraliqlariga bo‘lingan, barglari reduksiyalangan. Bahorda poya uchida spora yetiladigan boshoqcha hosil qiladi.\n"
            "• <b>Qirqquloqlar (Paporotniklar):</b> Kuchli ildizpoyaga va patsimon chiroyli yirik barglarga (vayyalarga) ega. Barglarining ostki tomonida sporalar to‘plami — <b>soruslar</b> yetiladi.\n\n"
            "🌲 <b>2. Urug‘li o‘simliklar:</b> Suvga bog‘liq bo‘lmagan holda urug‘ orqali ko‘payadi:\n"
            "• <b>Ochiq urug‘lilar:</b> Urug‘lari meva ichida emas, qubba (shishka) tangachalarida ochiq holda yetiladi. Guli va mevasi bo‘lmaydi. Barglari ninasimon (ignabargli) yoki tangachasimon bo‘ladi (qarag‘ay, archa, qoraqarag‘ay, pixta, kedr).\n"
            "• <b>Yopiq urug‘li (Gulli) o‘simliklar:</b> O‘simliklar olamining eng yuksak taraqqiy etgan guruhi. Gul, meva va urug‘ hosil qiladi. Urug‘ meva pallasi ichida ishonchli himoyalangan."
        ),
        "guide": (
            "📘 <b>10-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Sporali yuksak:</b> Yo‘sin (rizoidli, torf beradi), Qirqbo‘g‘im (bo‘g‘imli), Qirqquloq (vayya barg ostida sorus).\n"
            "• <b>Ochiq urug‘li:</b> Mevasiz, urug‘i qubbada ochiq (qarag‘ay, archa).\n"
            "• <b>Yopiq urug‘li:</b> Gul va mevaga ega eng yuksak guruh."
        ),
        "media": "🎥 <b>Video dars:</b> Qirqquloqlar va ignabargli o‘simliklar hayot sikli (9 daqiqa)"
    },
    {
        "id": "11",
        "title": "11-§. O‘zbekistonda keng tarqalgan dorivor va zaharli o‘simliklar",
        "text": (
            "📖 <b>11-§. O‘ZBEKISTONDA KENG TARQALGAN DORIVOR VA ZAHARLI O‘SIMLIKLAR</b>\n\n"
            "🔹 O‘zbekiston zamini shifobaxsh dorivor va o‘ziga xos biologik faol o‘simliklarga juda boydir.\n\n"
            "🌿 <b>Keng tarqalgan dorivor o‘simliklar:</b>\n"
            "• <b>Na’matak:</b> Sershox tikanli buta. Mevasi S vitamini, provitamin A va boshqa vitaminlarga nihoyatda boy. Choy damlamasi immunitetni ko‘taradi va jigar faoliyatini yaxshilaydi.\n"
            "• <b>Yalpiz va Kiyiko‘t:</b> Poyasi va barglarida efir moylari (mentol) bo‘lib, xushbo‘y hidga ega. Tinchlantiruvchi, nafas yo‘llari va hazm qilishni yaxshilovchi vosita.\n"
            "• <b>Isiriq:</b> Quruq adirlarda o‘suvchi ko‘p yillik o‘t. Tarkibidagi garmalin moddasi tufayli tutuni xonalarni mikrob va viruslardan zararsizlantiradi (dezinfeksiya qiladi).\n"
            "• <b>Zubturum (Bargizub):</b> Yo‘l yoqalarida o‘suvchi oddiy bargli o‘t. Bargi oshqozon-ichak yaralarini tuzatishda va jarohatlardan qon to‘xtatishda ishlatiladi.\n"
            "• <b>Qizilmiya (Chuchukmiya):</b> Ildizpoyasida shirin glitsirrizin moddasi bo‘lib, yo‘talga qarshi shifobaxsh sirop va dorilar tayyorlanadi.\n"
            "• <b>Bo‘ymadaron va Moychechak:</b> Yallig‘lanishga qarshi va qon to‘xtatuvchi xususiyatga ega.\n\n"
            "⚠️ <b>Zaharli o‘simliklar va ulardan saqlanish:</b>\n"
            "• <b>Bangidevona:</b> Bo‘yi 1 metr keladigan bir yillik o‘t. Guli yirik, oq voronkasimon, mevasi tikanli ko‘sakcha. Tarkibida o‘ta zaharli alkaloidlar (atropin) bor, asab tizimini falajlaydi.\n"
            "• <b>Mingdevona:</b> Yopishqoq tukli, qo‘lansa hidli o‘simlik. Mevasi ko‘sakcha, urug‘i va barglari qattiq zaharli.\n"
            "• <b>Kanakunjut:</b> Bo‘yi 2–3 metr keladigan bir yillik o‘t. Bargi yirik panjasimon. Urug‘ida eng xavfli zahar — <b>ritsin</b> moddasi bo‘ladi (lekin maxsus qayta ishlanib kanakunjut moyi olinadi).\n"
            "• <b>Zaharli ayiqtovon:</b> Sariq yaltiroq gulli o‘t. Sharbati teriga tegsa pufakchalar hosil qilib kuydiradi.\n"
            "• <i>Muhim qoida:</i> Notanish o‘simliklarning meva va barglarini aslo og‘izga solmaslik va qo‘l bilan ezmaslik shart!"
        ),
        "guide": (
            "📘 <b>11-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Dorivor:</b> Na’matak (C vitamini), Isiriq (mikroblarni o‘ldiradi), Yalpiz (mentol), Zubturum (yara tuzatish), Qizilmiya (yo‘talga qarshi).\n"
            "• <b>Zaharli:</b> Bangidevona (tikanli ko‘sak, atropin), Mingdevona (qo‘lansa hid), Kanakunjut (panjasimon barg, ritsin zahari), Ayiqtovon (terini kuydiradi)."
        ),
        "media": "🎥 <b>Video dars:</b> O‘zbekiston dorivor giyohlari va zaharli o‘simliklarni ajratish (8 daqiqa)"
    },
    {
        "id": "12",
        "title": "12-§. Hayvonot dunyosi",
        "text": (
            "📖 <b>12-§. HAYVONOT DUNYOSI (FAUNA)</b>\n\n"
            "🔹 <b>Hayvonlar</b> — tayyor organik moddalar bilan geterotrof oziqlanuvchi, erkin va faol harakatlanuvchi, sezgi a’zolari rivojlangan eukariot mavjudotlardir.\n\n"
            "🐾 <b>Hayvonlarning o‘ziga xos biologik belgilari:</b>\n"
            "• Hujayralarida sellyuloza qobiq va plastidalar bo‘lmaydi.\n"
            "• Muskul va nerv to‘qimasi yordamida tezkor harakatlanadi va tashqi ta’sirlarga chaqqon javob beradi.\n"
            "• Chegaralangan o‘sishga ega (voyaga yetgach ko‘pchiligi o‘sishdan to‘xtaydi).\n\n"
            "🦁 <b>Hayvonlarning asosiy guruhlari:</b>\n"
            "1. <b>Bir hujayralilar (Sodda hayvonlar):</b> Tana faqat bitta hujayradan iborat bo‘lib, u mustaqil yaxlit organizm vazifasini bajaradi (amyoba, evglena, tufelka).\n"
            "2. <b>Ko‘p hujayrali hayvonlar:</b> Tanasi ko‘plab ixtisoslashgan to‘qima va a’zolardan tashkil topgan:\n"
            "   • <b>Umurtqasiz hayvonlar:</b> Tanasi ichida tayanch o‘qi — umurtqa pog‘onasi bo‘lmaydi. Sayyoramizdagi hayvon turlarining 95% dan ortig‘ini tashkil qiladi (bo‘shliqichlilar, chuvalchanglar, mollyuskalar, bo‘g‘imoyoqlilar).\n"
            "   • <b>Umurtqali hayvonlar:</b> Tanasi ichida mustahkam ichki skelet (xorda yoki umurtqa pog‘onasi) mavjud bo‘lgan yuksak hayvonlar (baliqlar, amfibiyalar, sudralib yuruvchilar, qushlar, sutemizuvchilar).\n\n"
            "🌍 <b>Yashash muhitlari:</b> Suv muhiti, quruqlik-havo muhiti, tuproq muhiti va boshqa organizmlar tanasi (parazitlar)."
        ),
        "guide": (
            "📘 <b>12-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Hayvonlar belgisi:</b> Geterotrof, faol harakat, nerv va muskul sistemasi, plastidasiz hujayra.\n"
            "• <b>Guruhlar:</b> Bir hujayralilar (sodda hayvonlar) va Ko‘p hujayralilar.\n"
            "• <b>Ko‘p hujayralilar:</b> Umurtqasizlar (95% turlar) va Umurtqalilar (ichki skeletli)."
        ),
        "media": "🎥 <b>Video dars:</b> Hayvonot olami xilma-xilligi va evolyutsiyasi (9 daqiqa)"
    },
    {
        "id": "13",
        "title": "13-§. Umurtqasiz hayvonlar",
        "text": (
            "📖 <b>13-§. UMURTQASIZ HAYVONLAR</b>\n\n"
            "🔹 Umurtqasizlar — ichki suyakli umurtqa pog‘onasi bo‘lmagan hayvonlar bo‘lib, shakli va yashash tarziga ko‘ra nihoyatda rang-barangdir.\n\n"
            "🐛 <b>Umurtqasizlarning asosiy tiplari:</b>\n"
            "1. <b>Sodda hayvonlar (Bir hujayralilar):</b>\n"
            "   • <i>Oddiy amyoba:</i> Doimiy shaklga ega emas, <b>soxta oyoqlari</b> orqali oziqni o‘rab oladi (fagotsitoz) va harakatlanadi.\n"
            "   • <i>Yashil evglena:</i> Bitta xivchini va qizil ko‘zchasi bor. Yorug‘likda fotosintez qiladi (avtotrof), qorong‘ida tayyor oziq yeydi (geterotrof — miksotrof).\n"
            "   • <i>Infuzoriya tufelka:</i> Doimiy poyabzal tagcharmi shaklida, tanasi minglab kiprikchalar bilan qoplangan, 2 ta yadroga ega.\n"
            "2. <b>Bo‘shliqichlilar tipi:</b>\n"
            "   • <i>Chuchuk suv gidrasi:</i> Tanasi ikki qavat hujayralardan (tashqi — ektoderma va ichki — endoderma) iborat xaltasimon hayvon. Nurli simmetriyaga ega. Paypaslagichlarida <b>otuvchi hujayralar</b> bo‘lib, o‘ljasini falajlaydi. Kuchli <b>regeneratsiya</b> (yo‘qotilgan tana qismini qayta tiklash) qobiliyatiga ega.\n"
            "3. <b>Chuvalchanglar:</b>\n"
            "   • <i>Yassi chuvalchanglar:</i> Tana shakli yapaloq, tana bo‘shlig‘i yo‘q (oq planariya, jigar qurti).\n"
            "   • <i>To‘garak chuvalchanglar:</i> Ko‘ndalang kesimi dumaloq, birlamchi tana bo‘shlig‘i bor (odam askaridasi, bolalar gijjasi — parazitlar).\n"
            "   • <i>Halqali chuvalchanglar:</i> Tanasi halqalardan iborat, yopiq qon aylanish sistemasiga ega (yomg‘ir chuvalchangi — tuproq unumdorligini oshiradi).\n"
            "4. <b>Mollyuskalar (Yumshoqtanlilar):</b> Tanasi yumshoq, ko‘pchiligi ohak chig‘anoq bilan himoyalangan (baqachanoq, tok shilliqqurti, sakkizoyoq).\n"
            "5. <b>Bo‘g‘imoyoqlilar tipi:</b> Sayyoramizdagi eng ko‘p sonli guruh. Tanasi xitin qobiq bilan qoplangan, oyoqlari bo‘g‘imlardan iborat:\n"
            "   • <i>Qisqichbaqasimonlar:</i> 5 juft yurish oyog‘i, suvda jabra bilan nafas oladi.\n"
            "   • <i>O‘rgimchaksimonlar:</i> 4 juft yurish oyog‘i, mo‘ylovchalari bo‘lmaydi, o‘rgimchak to‘ri to‘qiydi.\n"
            "   • <i>Hasharotlar:</i> 3 juft (6 ta) oyog‘i, 1 juft mo‘ylovi va qanotlari bor. Rivojlanishi to‘liq (kapalak: tuxum ➔ qurt ➔ g‘umbak ➔ kapalak) yoki chala (suvarak, chigirtka: tuxum ➔ lichinka ➔ yetuk zot)."
        ),
        "guide": (
            "📘 <b>13-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Sodda hayvonlar:</b> Amyoba (soxta oyoq), Evglena (xivchin, aralash oziqlanish), Tufelka (kiprikchalar).\n"
            "• <b>Gidra:</b> Otuvchi hujayralar, nurli simmetriya, regeneratsiya.\n"
            "• <b>Chuvalchanglar:</b> Yassi, To‘garak (askarida — parazit), Halqali (yomg‘ir chuvalchangi).\n"
            "• <b>Bo‘g‘imoyoqlilar:</b> Qisqichbaqa (10 oyoq), O‘rgimchak (8 oyoq), Hasharot (6 oyoq, qanotlar)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Gidraning otuvchi hujayralari va hasharotlar metamorfozi"
    },
    {
        "id": "14",
        "title": "14-§. Umurtqali hayvonlar",
        "text": (
            "📖 <b>14-§. UMURTQALI HAYVONLAR (XORDALILAR)</b>\n\n"
            "🔹 <b>Umurtqali hayvonlar</b> — ichki o‘q skeletga (umurtqa pog‘onasiga va kalla suyagiga), yuksak rivojlangan bosh miya va nerv sistemasiga ega bo‘lgan mukammal jonzotlardir.\n\n"
            "🐟 <b>Umurtqali hayvonlarning asosiy sinflari:</b>\n"
            "1. <b>Baliqlar:</b> Suvda yashovchi umurtqalilar. Tanasi tangachalar bilan qoplangan, suzgich qanotlari yordamida suzadi. <b>Jabrasi</b> bilan nafas oladi. Yuragi <b>2 kamerali</b> (1 bo‘lmacha, 1 qorincha), bitta qon aylanish doirasi bor. Sovuqqonli hayvonlar.\n"
            "2. <b>Suvda va quruqlikda yashovchilar (Amfibiyalar):</b> Quruqlikka chiqqan dastlabki to‘rt oyoqli umurtqalilar (baqa, qurbaqa, triton, salamandra). Lichinkasi (itbaliq) suvda yashab jabra bilan nafas oladi, yetuk baqa esa <b>o‘pka va sernam terisi</b> orqali nafas oladi. Yuragi <b>3 kamerali</b>, 2 ta qon aylanish doirasi bor. Sovuqqonli.\n"
            "3. <b>Sudralib yuruvchilar (Reptiliyalar):</b> Quruqlikda to‘liq yashashga moslashgan (kaltakesak, ilon, toshbaqa, timsoh). Terisi quruq, muguz tangachalar bilan qoplangan (suv yo‘qotishdan asraydi). Faqat <b>o‘pka</b> orqali nafas oladi. Yuragi <b>3 kamerali</b> (qorinchasida chala to‘sig‘i bor, timsohda esa 4 kamerali). Quruqlikda qalin po‘stli tuxum qo‘yadi.\n"
            "4. <b>Qushlar:</b> Uchishga moslashgan issiqqonli umurtqalilar. Oldingi oyoqlari qanotga aylangan, tanasi pat bilan qoplangan, jag‘lari muguz tumshuqqa aylangan (tishsiz). Suyaklari g‘ovak, havoli. Yuragi <b>4 kamerali</b>, 2 qon aylanish doirasi to‘liq ajralgan. <b>Qo‘shaloq nafas olish</b> (havo xaltachalari) mavjud. Tana harorati doimiy yuqori (40–42 °C).\n"
            "5. <b>Sutemizuvchilar (Darrandalar):</b> Eng yuksak tuzilgan issiqqonli umurtqalilar. Tanasi jun (tivit) bilan qoplangan, terisida ter va yog‘ bezlari bor. Bolasini <b>tirik tug‘adi va sut bilan boqadi</b>. Tishlari turlarga ixtisoslashgan (kurak, qoziq, oziq tishlar). Bosh miya po‘stlog‘i kuchli rivojlangan, murakkab xatti-harakatlarga ega (bo‘ri, tulki, kiyik, yo‘lbars, ko‘rshapalak, kit, delfin)."
        ),
        "guide": (
            "📘 <b>14-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Baliqlar:</b> Tangacha, jabra, 2 kamerali yurak, 1 qon doirasi, sovuqqonli.\n"
            "• <b>Amfibiyalar:</b> Baqa, 3 kamerali yurak, o‘pka + teri orqali nafas, sovuqqonli.\n"
            "• <b>Reptiliyalar:</b> Quruq muguz teri, o‘pka, 3 kamerali (timsoh 4), quruqlikda tuxum qo‘yadi.\n"
            "• <b>Qushlar:</b> Patlar, qanotlar, 4 kamerali yurak, issiqqonli, havo xaltachalari.\n"
            "• <b>Sutemizuvchilar:</b> Jun, tirik tug‘ib sut emizish, 4 kamerali yurak, tishlar ixtisoslashgan."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Baliqdan sutemizuvchigacha yurak va qon aylanish evolyutsiyasi"
    },
    {
        "id": "15",
        "title": "15-§. Odam organlari sistemasi",
        "text": (
            "📖 <b>15-§. ODAM ORGANLARI SISTEMASI</b>\n\n"
            "🔹 Odam organizmi yuksak darajada ixtisoslashgan organlar sistemalarining o‘zaro uzviy muvofiqlashgan yaxlit tizimidir.\n\n"
            "🫀 <b>Asosiy organlar sistemalari va ularning vazifalari:</b>\n"
            "1. <b>Tayanch-harakat sistemasi:</b> Skelet suyaklari va muskullardan iborat. Tanaga tayanch beradi, ichki a’zolarni himoya qiladi va fazoda harakatlanishni ta’minlaydi (masalan, qo‘l bukilganda yelkaning <i>ikki boshli muskuli (biceps)</i> qisqaradi, <i>uch boshli muskuli (triceps)</i> bo‘shashadi).\n"
            "2. <b>Hazm qilish sistemasi:</b> Oziq-ovqatlarni maydalash, parchalash va qonga so‘rishni bajaradi. Qismlari: og‘iz bo‘shlig‘i, halqum, qizilo‘ngach, oshqozon, ingichka ichak, yo‘g‘on ichak, hazm bezlari (jigar, me’daosti bezi).\n"
            "3. <b>Nafas olish sistemasi:</b> To‘qimalarni kislorod bilan ta’minlash va karbonat angidridni chiqarish. Qismlari: burun bo‘shlig‘i, hiqildoq, kekirdak (traxeya), bronxlar va o‘pka (alveolalar).\n"
            "4. <b>Qon aylanish sistemasi:</b> Oziq moddalar, kislorod va gormonlarni to‘qimalarga yetkazish hamda parchalanish mahsulotlarini olib ketish. Qismlari: 4 kamerali <b>yurak</b> va qon tomirlar (arteriyalar, venalar, kapillarlar).\n"
            "5. <b>Ayirish sistemasi:</b> Moddalar almashinuvining zararli suyuq chiqindilarini tashqariga chiqarish. Qismlari: <b>buyraklar</b> (juft loviyasimon organ), siydik yo‘llari, siydik pufagi (qovuq).\n"
            "6. <b>Nerv sistemasi:</b> Barcha a’zolar faoliyatini boshqarish va organizmning tashqi muhit bilan aloqasini ta’minlash. Qismlari: Markaziy nerv sistemasi (bosh miya va orqa miya) hamda Periferik nervlar.\n"
            "7. <b>Sezgi organlari:</b> Tashqi dunyoni his qilish: ko‘rish (ko‘z), eshitish (quloq), hid bilish (burun), ta’m bilish (til) va teri sezgisi.\n"
            "8. <b>Ichki sekretsiya (Endokrin) sistemasi:</b> Maxsus bezlar (gipofiz, qalqonsimon bez, buyrakusti bezi) qonga <b>gormonlar</b> ishlab chiqarib gumoral boshqaruvni ta’minlaydi."
        ),
        "guide": (
            "📘 <b>15-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tayanch-harakat:</b> Skelet + muskullar (biceps va triceps).\n"
            "• <b>Hazm:</b> Og‘iz ➔ qizilo‘ngach ➔ oshqozon ➔ ichak + jigar va me’daosti bezi.\n"
            "• <b>Nafas:</b> Burun ➔ hiqildoq ➔ kekirdak ➔ bronxlar ➔ o‘pka.\n"
            "• <b>Qon aylanish:</b> 4 kamerali yurak + tomirlar (arteriya, vena, kapillar).\n"
            "• <b>Ayirish:</b> Buyraklar (chiqindi filtri) + qovuq.\n"
            "• <b>Nerv:</b> Bosh miya, orqa miya va nerv tolalari."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Odam anatomiyasi va ichki a’zolari sistemalarining 3D joylashuvi"
    },
    # -------------------------------------------------------------
    # 3-BOB. ORGANIZM VA TASHQI MUHIT
    # -------------------------------------------------------------
    {
        "id": "16",
        "title": "16-§. Ekologik omillar",
        "text": (
            "📖 <b>16-§. EKOLOGIK OMILLAR VA OZUQA ZANJIRI</b>\n\n"
            "🔹 <b>Ekologik omillar</b> — tirik organizmlarning yashashiga, rivojlanishiga va tarqalishiga ta’sir ko‘rsatuvchi tashqi muhit shart-sharoitlaridir.\n\n"
            "☀️ <b>Ekologik omillarning 3 ta asosiy guruhi:</b>\n"
            "1. <b>Abiotik omillar:</b> Jonsiz tabiat elementlarining ta’siri (quyosh yorug‘ligi, havo harorati, namlik, shamol, atmosfera bosimi, tuproqning minerallashuvi).\n"
            "2. <b>Biotik omillar:</b> Tirik organizmlarning bir-biriga ko‘rsatadigan har qanday o‘zaro ta’siri:\n"
            "   • <i>Yirtqichlik:</i> Bir organizm ikkinchisini tutib yeyishi (bo‘ri va quyon).\n"
            "   • <i>Parazitlik:</i> Boshqa organizm hisobiga yashash (askarida, zarpechak).\n"
            "   • <i>Simbioz (hamkorlik):</i> Bir-biriga o‘zaro foyda keltirish (dukkaklilar va tugunak bakteriyalari, zamburug‘ va daraxt ildizi — mikoriza).\n"
            "   • <i>Raqobat:</i> Bir xil ozuqa yoki yorug‘lik uchun kurashish.\n"
            "3. <b>Antropogen omillar:</b> Insonning tabiatga, tirik organizmlar va ularning yashash muhitiga bevosita yoki bilvosita ko‘rsatadigan ta’sirlari (yer haydash, o‘rmon kesish, sun’iy sug‘orish, sanoat chiqindilari).\n\n"
            "🔄 <b>Ekotizimda moddalar davranyasi va ozuqa zanjiri:</b>\n"
            "• <b>Produtsentlar (Hosil qiluvchilar):</b> Quyosh energiyasidan organik modda sintezlovchi avtotroflar (yashil o‘simliklar, suvo‘tlar).\n"
            "• <b>Konsumentlar (Iste’molchilar):</b> Tayyor organik modda bilan oziqlanuvchi geterotroflar:\n"
            "  - <i>1-tartib konsumentlar:</i> O‘txo‘r hayvonlar (quyon, qo‘y, kiyik, hasharotlar).\n"
            "  - <i>2- va 3-tartib konsumentlar:</i> Yirtqichlar (tulki, bo‘ri, burgut, yo‘lbars).\n"
            "• <b>Redutsentlar (Parchalovchilar):</b> O‘lik organik qoldiqlarni noorganik minerallarga parchalovchilar (chirindixo‘r bakteriyalar, zamburug‘lar).\n"
            "• <i>Ozuqa zanjiriga misol:</i> O‘t (produtsent) ➔ Chigirtka (1-tartib konsument) ➔ Baqa (2-tartib konsument) ➔ Ilon (3-tartib konsument) ➔ Burgut (yuksak yirtqich)."
        ),
        "guide": (
            "📘 <b>16-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Omillar:</b> Abiotik (jonsiz muhit — yorug‘lik, suv), Biotik (tiriklar aloqasi), Antropogen (inson ta’siri).\n"
            "• <b>Ozuqa zanjiri:</b> Produtsent (o‘simlik) ➔ Konsument (o‘txo‘r va yirtqich) ➔ Redutsent (bakteriya va zamburug‘)."
        ),
        "media": "🎥 <b>Video dars:</b> Ekologik omillar va ozuqa zanjiri piramidasi (9 daqiqa)"
    },
    {
        "id": "17",
        "title": "17-§. Inson va tabiat",
        "text": (
            "📖 <b>17-§. INSON VA TABIAT</b>\n\n"
            "🔹 Insoniyat paydo bo‘lganidan buyon tabiat bilan chambarchas bog‘liq holda yashab kelmoqda. Inson o‘ziga zarur barcha hayotiy ne’matlarni (kislorod, toza suv, oziq-ovqat, kiyim-kechak, dori-darmon, yoqilg‘i) tabiatdan oladi.\n\n"
            "⛏ <b>Tabiiy boyliklar (resurslar) tasnifi:</b>\n"
            "1. <b>Qayta tiklanadigan resurslar:</b> O‘simliklar olami, hayvonot dunyosi, toza chuchuk suv, atmosfera havosi, tuproq unumdorligi (oqilona foydalanilsa o‘z-o‘zini qayta tiklay oladi).\n"
            "2. <b>Qayta tiklanmaydigan resurslar:</b> Yer qa’ridan qazib olinadigan foydali qazilmalar (neft, tabiiy gaz, ko‘mir, temir, oltin, uran). Ular sarflangan sari kamayadi va tugaydi.\n\n"
            "⚠️ <b>Zamonaviy ekologik muammolar:</b>\n"
            "• <b>Atmosferaning ifloslanishi:</b> Zavod-fabrikalar va transport vositalaridan zaharli gazlarning havoga ko‘p chiqarilishi («issiqxona effekti», kislotali yomg‘irlar).\n"
            "• <b>Orol fojiasi:</b> Amudaryo va Sirdaryo suvlarining haddan tashqari ko‘p sug‘orishga olinishi oqibatida Orol dengizining qurishi, tuzli va changli bo‘ronlar maydonining kengayishi.\n"
            "• <b>Tuproqning yemirilishi (eroziya va sho‘rlanish):</b> O‘rmonlarning kesilishi va noto‘g‘ri sug‘orish oqibatida hosildor yerlarning cho‘llanishi.\n"
            "• <b>Biologik xilma-xillikning kamayishi:</b> Yovvoyi o‘simliklar va nodir hayvonlar yashash joylarining buzilishi va brakonyerlik (noqonuniy ov) natijasida ko‘plab turlarning qirilib ketish xavfi ostida qolishi."
        ),
        "guide": (
            "📘 <b>17-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Qayta tiklanadigan:</b> O‘simlik, hayvon, suv, havo, unumdor tuproq.\n"
            "• <b>Qayta tiklanmaydigan:</b> Neft, gaz, ko‘mir, ma’danlar.\n"
            "• <b>Muammolar:</b> Havo ifloslanishi, Orol dengizi fojiasi, yerlarning sho‘rlanishi, brakonyerlik."
        ),
        "media": "🎥 <b>Video dars:</b> Orol dengizi fojiasi va global ekologik muammolar (10 daqiqa)"
    },
    {
        "id": "18",
        "title": "18-§. Tabiatni muhofaza qilish",
        "text": (
            "📖 <b>18-§. TABIATNI MUHOFAZA QILISH VA QIZIL KITOB</b>\n\n"
            "🔹 Tabiatni muhofaza qilish — tabiiy boyliklarni asrab-avaylash, ulardan oqilona foydalanish, ifloslanishning oldini olish va biologik xilma-xillikni kelajak avlodga yetkazishga qaratilgan davlat va jamoat chora-tadbirlari tizimidir.\n\n"
            "📕 <b>«O‘zbekiston Respublikasi Qizil kitobi»:</b>\n"
            "• Qizil kitob — kamyob, yo‘qolib ketish xavfi ostida turgan o‘simlik va hayvon turlarining rasmiy davlat ro‘yxatidir. U ilk bor 1979-yilda ta’sis etilgan.\n"
            "• <i>Qizil kitobga kiritilgan hayvonlar:</i> <b>Xongul (Buxoro bug‘usi)</b> (to‘qaylarning qisqarishi tufayli kamayib ketgan), <b>Yo‘rg‘a tuvaloq</b> (cho‘l va adirlarda yashaydi, tuxumini yerga qo‘yadi), Tyanshan qo‘ng‘ir ayig‘i, Oq tirnoqli ayiq, Ilvirs (qor qoploni), Buxoro tog‘ qo‘yi.\n"
            "• <i>Qizil kitobga kiritilgan o‘simliklar:</i> <b>Safsan xurmosi</b> (15–20 metrli baland bo‘yli nodir daraxt), <b>Xolmon isirg‘aguli</b> (gullari qo‘ng‘iroqsimon, chiroyli bezak o‘simlik), Lolaning yovvoyi turlari (Greyg lolasi), Shirach, Zarafshon archasi.\n\n"
            "🛡 <b>Muhofaza etiladigan tabiiy hududlar:</b>\n"
            "1. <b>Qo‘riqxonalar:</b> Tabiat butun boyligi bilan asl holicha saqlanadigan, har qanday xo‘jalik faoliyati qat’iyan man etilgan hududlar (Chatqol biosfera qo‘riqxonasi, Zomin tog‘-archa qo‘riqxonasi, Qizilqum, Surxon, Nurota qo‘riqxonalari).\n"
            "2. <b>Milliy bog‘lar:</b> Tabiatni muhofaza qilish bilan birga ilmiy va sayyohlik (ekoturizm) maqsadlarida foydalaniladigan hududlar (Zomin milliy bog‘i, Ugom-Chotqol milliy bog‘i).\n"
            "3. <b>Buyurtmaxonalar (Zakazniklar):</b> Muayyan hayvon yoki o‘simlik turini ko‘paytirish va asrash uchun vaqtincha yoki doimiy belgilangan hududlar.\n"
            "4. <b>Botanika va hayvonot bog‘lari:</b> Tirik o‘simlik va hayvon kolleksiyalarini to‘plash va ko‘paytirish maskanlari.\n\n"
            "🇺🇿 <i>Har bir fuqaroning konstitutsiyaviy burchi — atrof-muhitni toza saqlash, bir dona nihol ekish va ona tabiatni asrashdir!</i>"
        ),
        "guide": (
            "📘 <b>18-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Qizil kitob:</b> Kamyob va yo‘qolayotgan turlar ro‘yxati (1979-yildan).\n"
            "• <b>Kamyob hayvonlar:</b> Xongul (Buxoro bug‘usi), Yo‘rg‘a tuvaloq, Ilvirs, Qorayg‘ir.\n"
            "• <b>Kamyob o‘simliklar:</b> Safsan xurmosi, Xolmon isirg‘aguli, Yovvoyi lolalar.\n"
            "• <b>Qo‘riqxona:</b> Xo‘jalik faoliyati butunlay taqiqlangan hudud (Chatqol, Zomin, Qizilqum)."
        ),
        "media": "🎥 <b>Video dars:</b> O‘zbekiston Qizil kitobi va qo‘riqxonalari bo‘ylab sayohat (12 daqiqa)"
    }
]

# -------------------------------------------------------------
# 5-SINF VIDEO DARSLARI KATALOGI
# -------------------------------------------------------------
VIDEO_LESSONS_5: List[Dict[str, Any]] = [
    {
        "id": "v5_1",
        "title": "1-dars: Biologiya fani va buyuk allomalar merosi",
        "desc": "Biologiyaning maqsad va vazifalari. Beruniy, Ibn Sino va Bobur asarlaridagi biologik ma’lumotlar.",
        "duration": "10 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_1"
    },
    {
        "id": "v5_2",
        "title": "2-dars: Tirik organizmlarning asosiy xususiyatlari",
        "desc": "Moddalar almashinuvi, oziqlanish, nafas olish, ta’sirlanish va harakatlanish.",
        "duration": "8 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_2"
    },
    {
        "id": "v5_3",
        "title": "3-dars: Biologiyaning o‘rganish usullari va mikroskop",
        "desc": "Kuzatish, taqqoslash, tajriba va tarixiy usul. Yorug‘lik mikroskopining tuzilishi.",
        "duration": "12 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_3"
    },
    {
        "id": "v5_4",
        "title": "4-dars: Hujayra tuzilishi va mikroskopik preparatlar",
        "desc": "Piyoz po‘sti preparatini tayyorlash, qobiq, sitoplazma, yadro, vakuola va plastidalar.",
        "duration": "11 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_4"
    },
    {
        "id": "v5_5",
        "title": "5-dars: Bakteriyalar va viruslar dunyosi",
        "desc": "Prokariotlar tuzilishi, shakllari, spora hosil qilishi. Foydali va kasallik qo‘zg‘atuvchi bakteriyalar.",
        "duration": "9 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_5"
    },
    {
        "id": "v5_6",
        "title": "6-dars: Zamburug‘lar: Shlyapkali, mog‘or va achitqilar",
        "desc": "Mitseliy, penitsillin kashfiyoti, xamirturush va parazit zamburug‘lar.",
        "duration": "10 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_6"
    },
    {
        "id": "v5_7",
        "title": "7-dars: Suvo‘tlar va yuksak o‘simliklar",
        "desc": "Xlamidamonada, Ulotriks, yo‘sinlar, qirqquloqlar va ignabargli o‘simliklar.",
        "duration": "10 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_7"
    },
    {
        "id": "v5_8",
        "title": "8-dars: Dorivor va zaharli o‘simliklar",
        "desc": "O‘zbekiston dorivor o‘simliklari va zaharli turlar (bangidevona, kanakunjut, mingdevona).",
        "duration": "8 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_8"
    },
    {
        "id": "v5_9",
        "title": "9-dars: Umurtqasiz va umurtqali hayvonlar",
        "desc": "Sodda hayvonlar, gidra, chuvalchanglar, hasharotlar hamda xordalilar sinflari.",
        "duration": "13 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_9"
    },
    {
        "id": "v5_10",
        "title": "10-dars: Ekologik omillar va tabiatni muhofaza qilish",
        "desc": "Abiotik, biotik va antropogen omillar. Ozuqa zanjiri, O‘zbekiston Qizil kitobi va qo‘riqxonalari.",
        "duration": "11 daqiqa",
        "url": "https://mover.uz/video/biologiya_5_10"
    }
]

# -------------------------------------------------------------
# 5-SINF 3D ANIMATSIYALAR KATALOGI
# -------------------------------------------------------------
ANIMATIONS_3D_5: List[Dict[str, Any]] = [
    {
        "id": "a5_1",
        "title": "Yorug‘lik mikroskopining 3D tuzilishi",
        "desc": "Okulyar, tubus, obyektivlar, buyum stoli, ko‘zgu va vintlar mexanizmining 3D modeli."
    },
    {
        "id": "a5_2",
        "title": "O‘simlik hujayrasining fazoviy 3D anatomiyasi",
        "desc": "Hujayra devori, plazmatik membrana, yadro, xloroplastlar va markaziy vakuola 3D da."
    },
    {
        "id": "a5_3",
        "title": "Bakteriya hujayrasi va xivchinlari 3D da",
        "desc": "Kapsula, qobiq, halqasimon DNK (nukleoid) va harakatlanish xivchini modeli."
    },
    {
        "id": "a5_4",
        "title": "Mog‘or zamburug‘i (Mukor va Penisill 3D)",
        "desc": "Mitseliy iplari, sporangiylar va sporalar tarqalishi 3D animatsiyasi."
    },
    {
        "id": "a5_5",
        "title": "Xlamidamonada va Ulotriksning mikroskopik 3D ko‘rinishi",
        "desc": "Bir hujayrali xivchinli suvo‘t va ipsimon suvo‘tning fazoviy tuzilishi."
    },
    {
        "id": "a5_6",
        "title": "Gidraning otuvchi hujayralari ishlash mexanizmi (3D)",
        "desc": "Kapsula ichidagi otuvchi ipchaning tashqariga otilib o‘ljani falajlash jarayoni."
    },
    {
        "id": "a5_7",
        "title": "Odam gavdasi va ichki organlar sistemasi (3D)",
        "desc": "Yurak, o‘pka, oshqozon, jigar va buyraklarning ko‘krak va qorin bo‘shlig‘idagi 3D joylashuvi."
    },
    {
        "id": "a5_8",
        "title": "Ekotizimdagi ozuqa zanjiri va energiya oqimi (3D)",
        "desc": "Produtsentlar, 1- va 2-tartib konsumentlar hamda redutsentlar o‘rtasidagi bog‘lanish 3D modeli."
    }
]
