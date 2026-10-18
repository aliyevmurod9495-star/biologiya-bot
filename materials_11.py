"""
11-sinf Biologiya (Ekologiya va Filogenez) o'quv materiallari:
Mavzu ma'ruzalari, qisqa qo'llanmalar, video darslar va 3D animatsiyalar.
Barcha 44 ta mavzu O'zbekiston maktab darsligi rasmiy mundarijasi va dasturi bo'yicha to'liq kiritilgan.
"""

from typing import Dict, List, Any

TOPICS_11: List[Dict[str, Any]] = [
    # -------------------------------------------------------------
    # I QISM. EKOLOGIYA VA HAYOT
    # 1-bob. Biologik tizimlar va ekologiya fani asoslari
    # -------------------------------------------------------------
    {
        "id": "1",
        "title": "1-§. Biologik tizimlar. Ekologiya — biologik tizimlar haqidagi fan",
        "text": (
            "📖 <b>1-§. BIOLOGIK TIZIMLAR. EKOLOGIYA — BIOLOGIK TIZIMLAR HAQIDAGI FAN</b>\n\n"
            "🔹 <b>Biologik tizim (sistema)</b> — o‘zaro uzviy bog‘langan, muayyan funksiyani bajaruvchi, "
            "rivojlanish, o‘z-o‘zini barpo etish va tashqi muhitga moslashish qobiliyatiga ega bo‘lgan "
            "tirik komponentlar yig‘indisidir.\n\n"
            "🧬 <b>Tirik materiyaning tashkiliy darajalari:</b>\n"
            "1. <b>Molekula darajasi:</b> Hayotning eng quyi kimyoviy darajasi (DNK, RNK, oqsillar, ATF, uglevodlar).\n"
            "2. <b>Hujayra darajasi:</b> Barcha tirik organizmlarning tuzilish, vazifa va ko‘payish birligi.\n"
            "3. <b>To‘qima darajasi:</b> Kelib chiqishi, tuzilishi va vazifasi bir xil hujayralar to‘plami.\n"
            "4. <b>Organ darajasi:</b> Muayyan shakl va fiziologik vazifaga ega tana qismi.\n"
            "5. <b>Organizm darajasi:</b> Mustaqil yashovchi yaxlit tirik mavjudot (individ).\n"
            "6. <b>Populyatsiya-tur darajasi:</b> Muayyan hududda erkin chatishib yashovchi bir tur individlari guruhi.\n"
            "7. <b>Biogeotsenoz (Ekotizim) darajasi:</b> Muayyan hududdagi tirik organizmlar va anorganik muhit birligi.\n"
            "8. <b>Biosfera darajasi:</b> Sayyoramizdagi barcha ekotizimlarni qamrab oluvchi eng oliy global tizim.\n\n"
            "🌿 <b>Ekologiya fanining predmeti va vazifalari:</b>\n"
            "• <b>«Ekologiya»</b> atamasi yunoncha <i>«oikos»</i> — uy, maskan, vatan va <i>«logos»</i> — fan, ta'limot so‘zlaridan olingan bo‘lib, "
            "fanga 1866-yilda nemis olimi <b>Ernst Gekkel</b> tomonidan kiritilgan.\n"
            "• Ekologiya tirik organizmlarning bir-biri bilan hamda o‘zlarini o‘rab turgan tashqi muhit bilan "
            "o‘zaro aloqalari va munosabatlarini o‘rganadi."
        ),
        "guide": (
            "📘 <b>1-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Ekologiya atamasi:</b> 1866-yil, Ernst Gekkel («oikos» — uy, «logos» — ta'limot).\n"
            "• <b>Tiriklik darajalari:</b> Molekula ➔ Hujayra ➔ To‘qima ➔ Organ ➔ Organizm ➔ Populyatsiya ➔ Biogeotsenoz ➔ Biosfera.\n"
            "• <b>Biologik tizim:</b> O‘z-o‘zini boshqaruvchi ochiq tirik tuzilma."
        ),
        "media": "🎥 <b>Video dars:</b> Biologik tizimlar iyerarxiyasi va ekologiya fanining mohiyati (12 daqiqa)"
    },
    {
        "id": "2",
        "title": "2-§. Ekologiyaning rivojlanishi, bo'limlari va metodlari",
        "text": (
            "📖 <b>2-§. EKOLOGIYANING RIVOJLANISHI, BO‘LIMLARI VA METODLARI</b>\n\n"
            "🔹 <b>Ekologik bilimlarning shakllanish tarixi:</b>\n"
            "• Antik davr olimlari (Gippokrat, Arastu, Teofrast) organizmlarning tashqi muhitga bog‘liqligini qayd etganlar.\n"
            "• Sharq allomalari: <b>Abu Ali ibn Sino</b> («Tib qonunlari»), <b>Abu Rayhon Beruniy</b> («Saydana») va "
            "<b>Zahiriddin Muhammad Bobur</b> («Boburnoma») o‘simlik va hayvonlarning yashash sharoitlarini tavsiflaganlar.\n"
            "• XIX asr: <b>Aleksandr Gumboldt</b> o‘simliklar geografiyasi va iqlimga moslashuvini o‘rgandi. "
            "<b>Charlz Darvin</b>ning evolutsion ta'limoti ekologiyaning nazariy poydevori bo‘ldi.\n\n"
            "🌿 <b>Ekologiyaning asosiy bo‘limlari:</b>\n"
            "1. <b>Autekologiya (organizm ekologiyasi):</b> Alohida olingan turning muhit bilan munosabatlari va moslashuvlarini o‘rganadi.\n"
            "2. <b>Demekologiya (populyatsiyalar ekologiyasi):</b> Populyatsiyalarning soni, zichligi, strukturasi va dinamikasini tadqiq etadi.\n"
            "3. <b>Sinekologiya (jamoalar ekologiyasi):</b> Turli turlardan iborat jamoalar (biotsenozlar)ning shakllanishi va qonuniyatlarini o‘rganadi.\n"
            "4. <b>Biogeotsenologiya:</b> Biogeotsenozlarning modda va energiya aylanmasini o‘rganadi.\n"
            "5. <b>Global ekologiya:</b> Biosferadagi umumiy sayyoraviy jarayonlarni tadqiq qiladi.\n\n"
            "🔬 <b>Ekologik metodlar:</b> Dala kuzatuvlari, eksperiment, ekologik monitoring va matematik-kompyuter modellashtirish."
        ),
        "guide": (
            "📘 <b>2-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Autekologiya:</b> Alohida organizm/tur ekologiyasi.\n"
            "• <b>Demekologiya:</b> Populyatsiyalar ekologiyasi.\n"
            "• <b>Sinekologiya:</b> Biotsenozlar (jamoalar) ekologiyasi.\n"
            "• <b>Metodlar:</b> Dala kuzatuvi, laboratoriya tajribasi, monitoring, modellashtirish."
        ),
        "media": "🎥 <b>Video dars:</b> Ekologiya fanining rivojlanish bosqichlari va zamonaviy tadqiqot metodlari"
    },
    {
        "id": "3",
        "title": "3-§. Hayotning ekosistema darajasi xususiyatlari. Biogeotsenoz — biologik sistema",
        "text": (
            "📖 <b>3-§. HAYOTNING EKOSISTEMA DARAJASI XUSUSIYATLARI. BIOGEOTSENOZ — BIOLOGIK SISTEMA</b>\n\n"
            "🔹 <b>Biogeotsenoz ta'limoti:</b>\n"
            "1942-yilda atoqli rus biologi <b>V.N.Sukachyov</b> tomonidan biogeotsenoz tushunchasi fanga kiritildi.\n\n"
            "🌿 <b>Biogeotsenoz tuzilishi ikkita uzviy qismdan iborat:</b>\n"
            "1. <b>Ekotop (Biotop):</b> Anorganik (jonsiz) tabiat sharoitlari majmui:\n"
            "   • <i>Klimatop:</i> quyosh nuri, harorat, namlik, havo tarkibi.\n"
            "   • <i>Edafotop:</i> tuproqning mexanik va kimyoviy tarkibi.\n"
            "2. <b>Biotsenoz:</b> Muayyan hududda birgalikda yashovchi barcha tirik organizmlar majmui:\n"
            "   • <i>Fitotsenoz:</i> o‘simliklar jamoasi (biotsenozning asosiy o‘zagi).\n"
            "   • <i>Zootsenoz:</i> hayvonlar jamoasi.\n"
            "   • <i>Mikobiototsenoz:</i> zamburug‘lar jamoasi.\n"
            "   • <i>Mikrobotsenoz:</i> mikroorganizmlar jamoasi.\n\n"
            "⚡ <b>Biogeotsenoz xususiyatlari:</b>\n"
            "Yaxlitlik, ochiqlik, o‘z-o‘zini boshqarish (gomeostaz) va dinamik muvozanatga ega bo‘lish."
        ),
        "guide": (
            "📘 <b>3-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Biogeotsenoz muallifi:</b> V.N.Sukachyov (1942).\n"
            "• <b>Biogeotsenoz = Ekotop (abiotik) + Biotsenoz (biotik).</b>\n"
            "• <b>Biotsenoz qismlari:</b> Fitotsenoz (o‘simlik), Zootsenoz (hayvon), Mikobiototsenoz (zamburug‘), Mikrobotsenoz (bakteriya)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Biogeotsenozning tarkibiy qismlari va fazoviy tuzilishi"
    },
    {
        "id": "4",
        "title": "4-§. Ekosistemalarning tarkibiy qismlari",
        "text": (
            "📖 <b>4-§. EKOSISTEMALARNING TARKIBIY QISMLARI</b>\n\n"
            "🔹 <b>Ekotizim (Ekosistema)</b> tushunchasi 1935-yilda ingliz ekologi <b>Artur Tensli</b> tomonidan fanga kiritilgan.\n"
            "• <i>Ekotizim</i> — tirik organizmlar va ularning yashash muhitining o‘zaro bog‘langan ixtiyoriy o‘lchamdagi tizimidir "
            "(tomchi suvdan tortib ulkan okeangacha).\n"
            "• <i>Biogeotsenoz</i> esa aniq quruqlik chegarasiga (fitotsenozga) ega bo‘lgan ekotizimdir.\n\n"
            "🌱 <b>Ekotizimdagi funksional guruhlar:</b>\n"
            "1. <b>Produsentlar (ishlab chiqaruvchilar):</b> Quyosh energiyasi yordamida anorganik moddalardan organik modda hosil qiluvchi avtotrof organizmlar (yashil o‘simliklar, sianobakteriyalar).\n"
            "2. <b>Konsumentlar (iste'molchilar):</b> Tayyor organik moddalar bilan oziqlanuvchi geterotroflar:\n"
            "   • <i>1-tartib konsumentlar:</i> o‘txo‘r hayvonlar (fitofaglar).\n"
            "   • <i>2-tartib konsumentlar:</i> o‘txo‘rlar bilan oziqlanuvchi yirtqichlar.\n"
            "   • <i>3- va undan yuqori tartib konsumentlar:</i> yirtqichlar bilan oziqlanuvchi yirtqichlar va parazitlar.\n"
            "3. <b>Redusentlar (parchalovchilar / destruktorlar):</b> O‘lik organik qoldiqlarni anorganik moddalargacha parchalovchi saprofit mikroorganizmlar va zamburug‘lar."
        ),
        "guide": (
            "📘 <b>4-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Ekotizim atamasi:</b> A.Tensli (1935).\n"
            "• <b>Produsentlar:</b> Avtotroflar (organika yaratuvchilar).\n"
            "• <b>Konsumentlar:</b> Geterotroflar (iste'molchilar: o‘txo‘r, yirtqich).\n"
            "• <b>Redusentlar:</b> Destruktorlar (organikani minerallarga parchalovchilar)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Produsent, konsument va redusentlarning modda aylanishidagi o‘rni"
    },
    # 2-bob
    {
        "id": "5",
        "title": "5-§. Organizmlarning yashash muhiti. Suv muhiti",
        "text": (
            "📖 <b>5-§. ORGANIZMLARNING YASHASH MUHITI. SUV MUHITI</b>\n\n"
            "🔹 <b>Yashash muhiti</b> — organizm yoki tur yashaydigan, unga bevosita yoki bilvosita ta'sir ko‘rsatadigan "
            "abiotik va biotik sharoitlar majmuasidir.\n\n"
            "🌊 <b>Suv muhiti (Gidrosfera) xususiyatlari:</b>\n"
            "• Zichligi yuqori (havodan 800 marta zich), gidrostatik bosim chuqurlik sari har 10 metrda 1 atmosferaga ortadi.\n"
            "• Yuqori issiqlik sig‘imi tufayli haroratning keskin tebranishi kuzatilmaydi.\n"
            "• Yorug‘lik chuqurlashgan sari tez yutiladi (200 m dan chuqurda qorong‘ulik).\n"
            "• Kislorod miqdori havoga nisbatan kam (suv harorati ko‘tarilganda erigan kislorod kamayadi).\n\n"
            "🐟 <b>Gidrobiontlar ekologik guruhlari:</b>\n"
            "1. <b>Plankton:</b> Suv oqimi bilan passiv suzuvchi mayda organizmlar (fitoplankton: bir hujayrali suvo‘tlar; zooplankton: dafniya, siklop, mayda qisqichbaqasimonlar).\n"
            "2. <b>Nekton:</b> Suv oqimiga qarshi faol suzuvchi yirik hayvonlar (baliqlar, kitlar, delfinlar, tyulenlar, kalmarlar).\n"
            "3. <b>Bentos:</b> Suv havzasi tubida yashovchi organizmlar (marjon poliplari, mollyuskalar, dengiz yulduzlari, chuvalchanglar).\n"
            "4. <b>Neyston:</b> Suvning sirt pardasida yoki unga yopishib yashovchi organizmlar (suvchilar, suzuvchi qurtlar)."
        ),
        "guide": (
            "📘 <b>5-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Suv muhiti:</b> Zich, bosim yuqori, harorat barqaror, kislorod cheklangan.\n"
            "• <b>Plankton:</b> Oqim bilan passiv suzuvchilar (dafniya).\n"
            "• <b>Nekton:</b> Faol suzuvchilar (baliq, kit).\n"
            "• <b>Bentos:</b> Tubda yashovchilar (marjon, ustritsa)."
        ),
        "media": "🎥 <b>Video dars:</b> Suv muhitining ekologik zonalari va gidrobiontlar moslashuvlari"
    },
    {
        "id": "6",
        "title": "6-§. Quruqlik-havo, tuproq, tirik organizmlar yashash muhitlari sifatida",
        "text": (
            "📖 <b>6-§. QURUQLIK-HAVO, TUPROQ VA TIRIK ORGANIZMLAR YASHASH MUHITLARI SIFATIDA</b>\n\n"
            "🦅 <b>1. Quruqlik-havo muhiti:</b>\n"
            "• Kislorodga nihoyatda boy (21%), zichligi va bosimi past.\n"
            "• Harorat sutka va fasllar bo‘yicha keskin o‘zgaradi.\n"
            "• Suv va namlik asosiy cheklovchi omil hisoblanadi.\n"
            "• Hayvonlarda skelet mustahkamligi, o‘pka orqali nafas olish va terida himoya qavatlari rivojlangan.\n\n"
            "🪱 <b>2. Tuproq muhiti (Edafotop):</b>\n"
            "• Qattiq, suyuq va gaz fazalarining murakkab qorishmasi.\n"
            "• Yorug‘lik tushmaydi, harorat chuqurlashgan sari barqarorlashadi, karbonat angidrid miqdori yuqori.\n"
            "• Edafobiontlar: yomg‘ir chuvalchangi, ko‘rsichqon, buzoqbosh, tuproq nematodalari va mikroblar.\n\n"
            "🦠 <b>3. Tirik organizmlar yashash muhiti sifatida (Endobiontlar):</b>\n"
            "• Oziq moddalar doimiy va mo‘l bo‘ladi.\n"
            "• Noqulay tashqi iqlim ta'siridan himoyalangan.\n"
            "• Xo‘jayin organizmning immunitet reaksiyalariga qarshilik ko‘rsatish va kislorod tanqisligiga (anaerobozga) moslashuv talab etiladi (parazit chuvalchanglar, ichak bakteriyalari)."
        ),
        "guide": (
            "📘 <b>6-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Quruqlik-havo:</b> Kislorod ko‘p, past zichlik, harorat o‘zgaruvchan.\n"
            "• <b>Tuproq:</b> Yorug‘liksiz, harorat mo‘tadil, CO2 ko‘p.\n"
            "• <b>Organizm muhiti:</b> Oziq mo‘l, kislorod kam, xo‘jayin qarshiligi."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Yashash muhitlarining solishtirma ekologik tavsifi"
    },
    {
        "id": "7",
        "title": "7-§. Muhit omillari va ularning tasnifi",
        "text": (
            "📖 <b>7-§. MUHIT OMILLARI VA ULARNING TASNIFI</b>\n\n"
            "🔹 <b>Ekologik omillar</b> — tirik organizmlarning hayotiga, o‘sishi, rivojlanishi va tarqalishiga bevosita yoki bilvosita ta'sir ko‘rsatuvchi muhit sharoitlaridir.\n\n"
            "📊 <b>Ekologik omillar 3 guruhga bo‘linadi:</b>\n"
            "1. <b>Abiotik omillar:</b> Anorganik (jonsiz) tabiat omillari: harorat, yorug‘lik, namlik, bosim, tuproq tarkibi, shamol, relyef.\n"
            "2. <b>Biotik omillar:</b> Tirik organizmlarning bir-biriga ko‘rsatadigan barcha o‘zaro ta'sirlari.\n"
            "3. <b>Antropogen omillar:</b> Inson faoliyati bilan bog‘liq bo‘lgan barcha ta'sirlar.\n\n"
            "⚖️ <b>Ekologik omillar ta'sirining asosiy qonuniyatlari:</b>\n"
            "• <b>Optimum qoidasi:</b> Har bir omilning organizm uchun eng qulay (optimum), cheklovchi (pessimum) va halokatli (minimum/maksimum) doirasi mavjud.\n"
            "• <b>Y.Libixning minimum qoidasi (1840):</b> Organizmning yashashi va hosildorligi miqdori me'yordan eng ko‘p chetga chiqqan (minimumda turgan) omilga bog‘liq («Libix bochkasi»).\n"
            "• <b>V.Shelfordning tolerantlik qoidasi (1913):</b> Organizmning chidamlilik chegarasi omilning nafaqat yetishmasligi, balki ortiqchaligi bilan ham belgilanadi.\n"
            "• <b>Stenobiontlar:</b> Omilning tor o‘zgarishiga chidamli turlar (masalan, forel balig‘i).\n"
            "• <b>Evribiontlar:</b> Omilning keng doiradagi tebranishiga chidamli turlar (masalan, kalamush, suvarak, qamish)."
        ),
        "guide": (
            "📘 <b>7-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Omillar:</b> Abiotik (jonsiz), Biotik (tirik), Antropogen (inson).\n"
            "• <b>Libix qoidasi:</b> Cheklovchi omil minimumda turgan omildir.\n"
            "• <b>Shelford qoidasi:</b> Tolerantlik chegarasi minimum va maksimum bilan belgilanadi.\n"
            "• <b>Steno-:</b> Tor doiraga chidamli; <b>Evri-:</b> Keng doiraga chidamli."
        ),
        "media": "🎥 <b>Video dars:</b> Ekologik omillar ta'siri egri chizig‘i va Libix bochkasi tajribasi"
    },
    {
        "id": "8",
        "title": "8-§. Yorug'lik — muhitning ekologik omili",
        "text": (
            "📖 <b>8-§. YORUG‘LIK — MUHITNING EKOLOGIK OMILI</b>\n\n"
            "☀️ <b>Quyosh nurlanishining biologik spektri:</b>\n"
            "1. <b>Ultrabinafsha nurlar (to‘lqin uzunligi <400 nm):</b>\n"
            "   • Qisqa to‘lqinli (<290 nm): halokatli, ozon qatlami tutib qoladi.\n"
            "   • O‘rta to‘lqinli (290–380 nm): bakteritsid ta'sirga ega, teri pigmenti (melanin) va D vitamini sintezini qo‘zg‘atadi.\n"
            "2. <b>Ko‘rinadigan nurlar (380–750 nm):</b> Yerga yetib keladigan nurlarning qariyb 50% ini tashkil etadi. Fotosintez uchun asosiy energiya manbai va hayvonlarning ko‘rish a'zolarini qo‘zg‘atuvchisi.\n"
            "3. <b>Infraqizil nurlar (>750 nm):</b> Yerga tushadigan nurlarning 45% dan ortig‘i. Asosiy issiqlik manbai bo‘lib, organizmlarni isitadi.\n\n"
            "🌿 <b>O‘simliklarning yorug‘likka munosabati:</b>\n"
            "• <b>Geliofitlar (yorug‘sevar):</b> Paxta, makkajo‘xori, oq jo‘xori, terak, shuvoq.\n"
            "• <b>Stsiofitlar (soyasevar):</b> O‘rmon qoplami ostidagi qirqquloqlar, moxlar, zangori marvaridgul.\n"
            "• <b>Soyaga chidamli:</b> Olma, nok, qoraqarag‘ay, ligustrum.\n\n"
            "⏰ <b>Fotoperiodizm va biologik soatlar:</b>\n"
            "• <i>Fotoperiodizm</i> — organizmlarning kun uzunligiga nisbatan reaksiyasi.\n"
            "• <b>Uzun kun o‘simliklari (kun >12 soat):</b> Bug‘doy, arpa, suli, karam, qorabug‘doy.\n"
            "• <b>Qisqa kun o‘simliklari (kun <12 soat):</b> G‘o‘za, sholi, soya, makkajo‘xori, tariq.\n"
            "• <b>Neytral o‘simliklar:</b> Pomidor, loviya, no‘xat, kungaboqar."
        ),
        "guide": (
            "📘 <b>8-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Spektr:</b> Ultrabinafsha (D vitamin), Ko‘rinadigan (fotosintez), Infraqizil (issiqlik).\n"
            "• <b>Geliofit:</b> Yorug‘sevar; <b>Stsiofit:</b> Soyasevar.\n"
            "• <b>Uzun kun:</b> Bug‘doy, arpa; <b>Qisqa kun:</b> G‘o‘za, sholi, soya.\n"
            "• <b>Fotoperiodizm:</b> Kun uzunligining mavsumiy biologik signali."
        ),
        "media": "🎥 <b>Video dars:</b> O‘simlik va hayvonlarda fotoperiodizm hodisasi"
    },
    {
        "id": "9",
        "title": "9-§. Harorat — muhitning abiotik omili",
        "text": (
            "📖 <b>9-§. HARORAT — MUHITNING ABIOTIK OMILI</b>\n\n"
            "🔹 Harorat hujayralardagi barcha biokimyoviy reaksiyalar va fermentlar faolligini belgilaydi.\n\n"
            "🌡 <b>Organizmlarning tana haroratini boshqarish guruhlari:</b>\n"
            "1. <b>Poykiloterm (sovuqqonli) organizmlar:</b> Tana harorati atrof-muhit haroratiga bog‘liq bo‘lib, doimiy emas (barcha o‘simliklar, umurtqasizlar, baliqlar, suvda ham quruqlikda yashovchilar, sudralib yuruvchilar).\n"
            "2. <b>Gomoyoterm (issiqqonli) organizmlar:</b> Tana harorati tashqi muhitdan qat'i nazar doimiy saqlanadi (qushlar va sutemizuvchilar).\n\n"
            "📏 <b>Ekogeografik qoidalar:</b>\n"
            "• <b>Bergmann qoidasi:</b> Bir turga yoki yaqin turlarga mansub gomoyoterm hayvonlarning sovuq iqlimda yashovchi vakillari issiq hududdagilarga qaraganda yirikroq gavda o‘lchamiga ega bo‘ladi (tana hajmi ortib, nisbiy sirt kamayadi va issiqlik saqlanadi).\n"
            "• <b>Allen qoidasi:</b> Sovuq iqlimda yashovchi sutemizuvchilarning gavdasidan chiqib turuvchi a'zolari (quloq suprasi, oyoqlar, quyruq, tumshuq) issiq hududdagi qardoshlariga nisbatan kalta bo‘ladi (masalan, arktika tulkisi vs sahro tulkisi fenek).\n\n"
            "❄️ <b>Noqulay haroratga moslashuvlar:</b> Anabioz (yashirin hayot), qishki uyqu (ayiq, tipratikan, bo‘rsiq) va yozgi uyqu (cho‘l toshbaqasi, sariq yumronqoziq)."
        ),
        "guide": (
            "📘 <b>9-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Poykiloterm:</b> Sovuqqonli (baliq, sudralib yuruvchi).\n"
            "• <b>Gomoyoterm:</b> Issiqqonli (qush, sutemizuvchi).\n"
            "• <b>Bergmann qoidasi:</b> Sovuqda tana yirikroq bo‘ladi.\n"
            "• <b>Allen qoidasi:</b> Sovuqda quloq, quyruq va oyoqlar kalta bo‘ladi."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Gomoyoterm va poykiloterm hayvonlarning issiqlik almashinuvi"
    },
    {
        "id": "10",
        "title": "10-§. Namlik ekologik omil sifatida",
        "text": (
            "📖 <b>10-§. NAMLIK EKOLOGIK OMIL SIFATIDA</b>\n\n"
            "🔹 Suv protoplazmaning 70–90% ini tashkil etadi va hayotning ajralmas asosi hisoblanadi.\n\n"
            "🌿 <b>O‘simliklarning namlikka bo‘lgan ekologik guruhlari:</b>\n"
            "1. <b>Gidatofitlar:</b> To‘liq suvga botib o‘suvchi o‘simliklar (elodeya, vallisneriya).\n"
            "2. <b>Gidrofitlar:</b> Quruqlik-suv o‘simliklari, pastki qismi suvda (qamish, nilufar).\n"
            "3. <b>Gigrofitlar:</b> Havosi va tuprog‘i doimiy o‘ta nam yerlarda o‘suvchilar (sholi, papirus, qirqbo‘g‘im).\n"
            "4. <b>Mezofitlar:</b> O‘rtacha namlik sharoitida o‘suvchi o‘simliklar (olma, nok, bug‘doy, beda, g‘o‘za).\n"
            "5. <b>Kserofitlar:</b> Qurg‘oqchil sharoitga moslashgan o‘simliklar:\n"
            "   • <i>Sukulentlar:</i> o‘z a'zolarida suv to‘plovchi seret o‘simliklar (kaktus, aloe, semizo‘t).\n"
            "   • <i>Sklerofitlar:</i> quruq, qattiq, barglari tikanga aylangan yoki mayda o‘simliklar (saksovul, yantoq, shuvoq).\n\n"
            "🐫 <b>Hayvonlarning suv tanqisligiga moslanishlari:</b>\n"
            "• Tana qoplamalari orqali bug‘lanishni keskin kamaytirish.\n"
            "• Quyuq siydik ajratish (qushlar va reptiliyalarda siydik kislotasi).\n"
            "• <b>Metabolik suv:</b> Yog‘ zaxiralarini oksidlab suv olish (tuyaning o‘rkachi, yumronqoziqlar)."
        ),
        "guide": (
            "📘 <b>10-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Gidrofit:</b> Suv o‘simligi (nilufar).\n"
            "• <b>Gigrofit:</b> O‘ta namsevar (sholi).\n"
            "• <b>Mezofit:</b> Mo‘tadil namsevar (bug‘doy, olma).\n"
            "• <b>Kserofit:</b> Qurg‘oqchil (Sukulent — kaktus; Sklerofit — yantoq, saksovul).\n"
            "• <b>Metabolik suv:</b> 100 g yog‘ oksidlanganda 107 g suv ajraladi."
        ),
        "media": "🎥 <b>Video dars:</b> Qurg‘oqchilikka o‘simlik va hayvonlarning moslashuv strategiyalari"
    },
    {
        "id": "11",
        "title": "11-§. Tuproq va topografik omillar",
        "text": (
            "📖 <b>11-§. TUPROQ VA TOPOGRAFIK OMILLAR</b>\n\n"
            "🔹 <b>Tuproq (Edafik omillar):</b>\n"
            "• Tuproq — litozferaning ustki unumdor qatlami bo‘lib, o‘simliklar uchun mineral oziq va suv manbaidir.\n"
            "• Tuproq unumdorligini <b>gumus (chirindi)</b> miqdori belgilaydi.\n"
            "• Tuproq reaksiyasi (pH): kislotali (sfagnumli botqoqlar), neytral (qora tuproqlar) va ishqoriy (sho‘rxoklar).\n\n"
            "🏔 <b>Topografik (orografik) omillar:</b>\n"
            "• Dengiz sathidan balandlik, relyef shakli, qiyalikning tikligi va yo‘nalishi (ekspozitsiyasi).\n"
            "• <b>Qiyalik ekspozitsiyasi:</b> Janubiy qiyaliklar ko‘proq quyosh nuri oladi, issiq va quruq bo‘ladi. Shimoliy qiyaliklar sovuqroq va sernamroq bo‘ladi.\n"
            "• <b>Balandlik mintaqalanishi:</b> Balandlikka ko‘tarilgan sari havo harorati har 100 metrda o‘rtacha 0.6°C ga pasayadi, bosim kamayadi va UB nurlanish ortadi."
        ),
        "guide": (
            "📘 <b>11-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tuproq omili:</b> Gumus, mexanik tarkib, pH.\n"
            "• <b>Orografik omillar:</b> Balandlik, qiyalik tikligi va ekspozitsiyasi.\n"
            "• <b>Janubiy qiyalik:</b> Issiq, yorug‘; <b>Shimoliy qiyalik:</b> Salqin, sernam.\n"
            "• <b>Harorat gradiyenti:</b> Har 100 m da 0.6°C pasayadi."
        ),
        "media": "🎥 <b>Video dars:</b> Tog‘ mintaqalanishi va tuproq turlarining o‘simliklarga ta'siri"
    },
    {
        "id": "12",
        "title": "12-§. Muhitning biotik omillari. Tirik organizmlar o'rtasidagi munosabatlar",
        "text": (
            "📖 <b>12-§. MUHITNING BIOTIK OMILLARI. TIRIK ORGANIZMLAR O‘RTASIDAGI MUNOSABATLAR</b>\n\n"
            "🔹 <b>Biotik munosabatlarning asosiy shakllari:</b>\n\n"
            "1. <b>Simbioz (birgalikda yashash):</b>\n"
            "   • <b>Mutualizm (+/+):</b> Har ikki tur uchun majburiy foydali hamkorlik (zamburug‘ va suvo‘t — lixenlar; tugunak bakteriyasi va dukkaklilar; termitlar va xivchinlilar).\n"
            "   • <b>Protokooperatsiya (+/+):</b> Ixtiyoriy foydali hamkorlik (zohid qisqichbaqa va aktiniya; qushlar va timsoh).\n"
            "   • <b>Kommensalizm (+/0):</b> Bir turga foydali, ikkinchisiga befarq:\n"
            "     - <i>Hamsoyalik (sinoykiya):</i> birovning inida boshpana topish (baliqchalar dengiz bodringi ichida).\n"
            "     - <i>Oshnalik (epioykiya):</i> yirtqich ortidan oziqlanish (akula va yondosh baliqlar).\n"
            "     - <i>Foreziya:</i> boshqa hayvon orqali tarqalish (kana hasharotlar ustida).\n\n"
            "2. <b>Antagonistik munosabatlar:</b>\n"
            "   • <b>Yirtqichlik (+/-):</b> Bir tur ikkinchisini tutib o‘ldiradi va oziqlanadi (bo‘ri va quyon).\n"
            "   • <b>Parazitizm (+/-):</b> Parazit xo‘jayin hisobiga yashaydi, lekin uni darhol o‘ldirmaydi.\n"
            "   • <b>Amensalizm (-/0):</b> Bir tur boshqasining yashashiga to‘sqinlik qiladi, o‘zi foyda ham zarar ham ko‘rmaydi (penitsill zamburug‘i bakteriyalarni o‘ldiradi).\n"
            "   • <b>Raqobat (-/-):</b> O‘xshash ehtiyojli turlar orasidagi cheklangan resurslar (oziq, joy) uchun kurash. <b>Gauzening raqobatli istisno qoidasi:</b> Ekologik ehtiyojlari bir xil bo‘lgan ikki tur bitta ekologik tokchada uzoq vaqt birga yashay olmaydi."
        ),
        "guide": (
            "📘 <b>12-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Mutualizm (+/+):</b> Majburiy foyda (lixen, tugunak bakteriya).\n"
            "• <b>Kommensalizm (+/0):</b> Biriga foyda, ikkinchisiga befarq.\n"
            "• <b>Yirtqichlik / Parazitizm (+/-):</b> Biriga foyda, ikkinchisiga zarar.\n"
            "• <b>Raqobat (-/-):</b> Ikkisiga ham zararli kurash.\n"
            "• <b>Gauze qoidasi:</b> 1 ta tokchada 2 ta raqobatchi tur uzoq qololmaydi."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Biotsenozdagi biotik munosabatlar turlari va Gauze qoidasi"
    },
    {
        "id": "13",
        "title": "13-§. Antropogen omillar",
        "text": (
            "📖 <b>13-§. ANTROPOGEN OMILLAR</b>\n\n"
            "🔹 <b>Antropogen omillar</b> — insonning tabiatga, tirik organizmlarning yashash muhitiga ko‘rsatadigan "
            "barcha shakldagi ta'sirlari yig‘indisidir.\n\n"
            "⚙️ <b>Ta'sir turlari:</b>\n"
            "1. <b>Bevosita ta'sir:</b> O‘simliklarni yig‘ish, ov qilish, daraxtlarni kesish, baliq ovlash, begona turlarni introduksiya qilish.\n"
            "2. <b>Bilvosita ta'sir:</b> Muhit sharoitlarini o‘zgartirish orqali (shaharlar qurish, kanallar qazish, suv omborlari barpo etish, havoni va suvni ifloslantirish).\n\n"
            "🌍 <b>Antropogen o‘zgarishlar oqibatlari:</b>\n"
            "• Bioxilma-xillikning qisqarishi va turlarning yo‘qolib ketishi.\n"
            "• Tabiiy landshaftlarning sun'iy landshaftlarga (agroekotizimlar, shaharlar) aylanishi.\n"
            "• Biosfera biogeokimyoviy sikllarining buzilishi."
        ),
        "guide": (
            "📘 <b>13-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Antropogen omil:</b> Inson faoliyati bilan bog‘liq ta'sirlar.\n"
            "• <b>Bevosita:</b> Ov, kesish, terish.\n"
            "• <b>Bilvosita:</b> Iqlim o‘zgarishi, sanoat chiqindilari, landshaft o‘zgarishi."
        ),
        "media": "🎥 <b>Video dars:</b> Inson faoliyatining global ekotizimlarga ta'siri"
    },
    # 3-bob
    {
        "id": "14",
        "title": "14-§. Turning populatsion strukturasi",
        "text": (
            "📖 <b>14-§. TURNING POPULATSION STRUKTURASI</b>\n\n"
            "🔹 <b>Populyatsiya</b> — muayyan hududda (arealda) uzoq vaqt yashovchi, bir-biri bilan erkin chatishib "
            "nasldor zurriyot beradigan bitta turning individlari guruhidir.\n\n"
            "📊 <b>Populyatsiyaning statik ko‘rsatkichlari:</b>\n"
            "1. <b>Populyatsiya soni:</b> Muayyan hududdagi individlarning umumiy miqdori.\n"
            "2. <b>Populyatsiya zichligi:</b> Maydon yoki hajm birligiga to‘g‘ri keladigan individlar (yoki biomassa) soni (masalan, 1 ga yerda 500 tup terak, 1 m³ suvda 10 000 ta dafniya).\n"
            "3. <b>Fazoviy strukturasi:</b> Individlarning maydon bo‘ylab taqsimlanishi:\n"
            "   • <i>Tekis:</i> kuchli raqobatda (yirtqich qushlar uyalari).\n"
            "   • <i>Tasodifiy:</i> muhit bir xil bo‘lganda.\n"
            "   • <i>Guruhli (to‘p-to‘p):</i> eng keng tarqalgan (poda, suruv, to‘da).\n"
            "4. <b>Jinsiy strukturasi:</b> Erkak va urg‘ochi individlar nisbati:\n"
            "   • <i>Birlamchi:</i> urug‘lanish paytidagi nisbat (odatda 1:1).\n"
            "   • <i>Ikkilamchi:</i> tug‘ilish paytidagi nisbat.\n"
            "   • <i>Uchlamchi:</i> voyaga yetgan jinsiy yetuk individlar nisbati.\n"
            "5. <b>Yosh strukturasi:</b> Yosh (generatsiyagacha), voyaga yetgan (reproduktiv) va qari (postreproduktiv) guruhlar nisbati."
        ),
        "guide": (
            "📘 <b>14-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Populyatsiya:</b> Turning erkin chatishuvchi elementar guruhi.\n"
            "• <b>Statik parametrlar:</b> Soni, zichligi, fazoviy, jinsiy va yosh strukturasi.\n"
            "• <b>Fazoviy:</b> Tekis, tasodifiy, guruhli (eng ko‘p).\n"
            "• <b>Jinsiy nisbat:</b> Birlamchi (urug‘lanishda 1:1), Ikkilamchi (tug‘ilishda), Uchlamchi (voyaga yetganda)."
        ),
        "media": "🎥 <b>Video dars:</b> Populyatsiya strukturasi va yosh piramidalari tahlili"
    },
    {
        "id": "15",
        "title": "15-§. Turning populatsion strukturasi (davomi)",
        "text": (
            "📖 <b>15-§. TURNING POPULATSION STRUKTURASI (DAVOMI)</b>\n\n"
            "🔹 <b>Populyatsiyaning dinamik ko‘rsatkichlari:</b>\n"
            "1. <b>Tug‘ilish (natalnost):</b> Muayyan vaqt birligi ichida yangi tug‘ilgan (unib chiqqan) individlar soni.\n"
            "2. <b>O‘lim (mortalnost):</b> Muayyan vaqt ichida nobud bo‘lgan individlar soni.\n"
            "3. <b>O‘sish sur'ati:</b> Tug‘ilish va o‘lim ko‘rsatkichlari orasidagi farq.\n\n"
            "📈 <b>Populyatsiya o‘sish modellari:</b>\n"
            "• <b>Eksponentsial o‘sish (J-simon egri chiziq):</b> Resurslar cheklanmagan ideal sharoitda sonning geometrik progressiyada shiddatli ortishi.\n"
            "• <b>Logistik o‘sish (S-simon egri chiziq):</b> Muhit sig‘imi (K) cheklangan real sharoitda resurslar kamayishi bilan o‘sishning barqarorlashishi.\n\n"
            "🌊 <b>Populyatsiya to‘lqinlari («hayot to‘lqinlari»):</b>\n"
            "1905-yilda <b>S.S.Chetverikov</b> tomonidan fanga kiritilgan. Populyatsiya sonining oziq miqdori, iqlim va yirtqichlar ta'sirida davriy yoki nodavriy ko‘payishi va kamayishi."
        ),
        "guide": (
            "📘 <b>15-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Dinamik parametrlar:</b> Tug‘ilish, o‘lim, migratsiya, o‘sish sur'ati.\n"
            "• <b>J-simon o‘sish:</b> Cheksiz resurslarda (eksponentsial).\n"
            "• <b>S-simon o‘sish:</b> Muhit sig‘imi cheklangan real sharoitda (logistik).\n"
            "• <b>Populyatsiya to‘lqinlari:</b> S.S.Chetverikov kashf etgan son tebranishlari."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Populyatsiya dinamikasi modellari (J va S egri chiziqlari)"
    },
    # 4-bob
    {
        "id": "16",
        "title": "16-§. Ekotizimlarning trofik strukturasi",
        "text": (
            "📖 <b>16-§. EKOTIZIMLARNING TROFIK STRUKTURASI</b>\n\n"
            "🔹 <b>Trofik struktura (Oziq aloqalari):</b>\n"
            "Ekotizimda moddalar va energiya bitta organizmdan ikkinchisiga oziqlanish aloqalari orqali uzatiladi.\n\n"
            "⛓ <b>Oziq zanjirlari 2 xil bo‘ladi:</b>\n"
            "1. <b>Yaylov (iste'mol) zanjiri:</b>\n"
            "   • Yashil o‘simliklardan (produsentlardan) boshlanadi.\n"
            "   • <i>Sxema:</i> O‘simlik ➔ O‘txo‘r hayvon ➔ Yirtqich hayvon ➔ Yirik yirtqich.\n"
            "   • <i>Misol:</i> Beda ➔ Chigirtka ➔ Qoplonbaqa ➔ Ilon ➔ Burgut.\n"
            "2. <b>Detrit (chirindixo‘r) zanjiri:</b>\n"
            "   • O‘lik organik moddalar (xazon, o‘laksalar, chiqindilar)dan boshlanadi.\n"
            "   • <i>Sxema:</i> O‘lik barglar ➔ Yomg‘ir chuvalchangi ➔ Qoraqush.\n\n"
            "🕸 <b>Oziq to‘ri:</b> Bitta organizm bir nechta oziq zanjirining a'zosi bo‘lgani uchun ekotizimda murakkab <b>trofik to‘r</b> hosil bo‘ladi. Oziq to‘ri qancha murakkab va boy bo‘lsa, ekotizim shuncha barqaror bo‘ladi."
        ),
        "guide": (
            "📘 <b>16-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Yaylov zanjiri:</b> O‘simlikdan (produsentdan) boshlanadi.\n"
            "• <b>Detrit zanjiri:</b> O‘lik organik qoldiqdan boshlanadi.\n"
            "• <b>Trofik to‘r:</b> Zanjirlarning kesishuvidan hosil bo‘luvchi barqaror tizim."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Yaylov va detrit oziq zanjirlarining 3D fazoviy to‘ri"
    },
    {
        "id": "17",
        "title": "17-§. Ekotizimlarning mahsuldorligi",
        "text": (
            "📖 <b>17-§. EKOTIZIMLARNING MAHSULDORLIGI</b>\n\n"
            "🔹 <b>Biologik mahsuldorlik</b> — ekotizimda vaqt birligi ichida hosil qilinadigan biomassa miqdoridir.\n\n"
            "🌿 <b>Mahsuldorlik turlari:</b>\n"
            "1. <b>Birlamchi mahsuldorlik:</b> Fotosintez va xemosintez natijasida avtotroflar (produsentlar) hosil qilgan biomassa:\n"
            "   • <i>Yalpi birlamchi mahsulot (PG):</i> Fotosintezda sintezlangan barcha organik moddalar umumiy massasi.\n"
            "   • <i>Sof birlamchi mahsulot (PN):</i> O‘simlikning o‘z nafas olishi (R)ga sarflaganidan ortib qolgan va o‘sishga ketgan sof massasi: <b>PN = PG - R</b>.\n"
            "2. <b>Ikkilamchi mahsuldorlik:</b> Geterotrof organizmlar (konsumentlar va redusentlar) tomonidan hosil qilinadigan biomassa.\n\n"
            "🌍 <b>Yer yuzi ekotizimlari mahsuldorligi:</b>\n"
            "• Eng sermahsul: Nam tropik o‘rmonlar, marjon riflari va to‘qaylar (yiliga 2000–3000 g/m²).\n"
            "• O‘rtacha: Mo‘tadil o‘rmonlar, dashtlar, ekinzorlar.\n"
            "• Kam mahsuldor: Cho‘llar, tundra, ochiq okean suvlari (<100 g/m²)."
        ),
        "guide": (
            "📘 <b>17-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Yalpi mahsulot (PG):</b> Jami fotosintez mahsuli.\n"
            "• <b>Sof mahsulot (PN):</b> Nafas sarfidan ortgan sof biomassa: <b>PN = PG - R</b>.\n"
            "• <b>Ikkilamchi mahsulot:</b> Konsumentlar biomassasi.\n"
            "• <b>Eng yuqori:</b> Tropik o‘rmon va marjon rifi."
        ),
        "media": "🎥 <b>Video dars:</b> Biosferaning birlamchi va ikkilamchi mahsuldorligi hisob-kitoblari"
    },
    {
        "id": "18",
        "title": "18-§. Ekologik piramida qoidasi. Biomassa va energiya piramidasi",
        "text": (
            "📖 <b>18-§. EKOLOGIK PIRAMIDA QOIDASI. BIOMASSA VA ENERGIYA PIRAMIDASI</b>\n\n"
            "🔹 <b>Lindeman qoidasi (10% qoidasi — 1942-yil):</b>\n"
            "Bir trofik pog‘onadan keyingisiga energiyaning o‘rtacha atigi <b>10% qismi</b> o‘tadi. "
            "Qolgan 90% energiya organizmning hayotiy jarayonlarida (harakat, nafas olish) issiqlik sifatida tarqaladi.\n\n"
            "🔺 <b>Ekologik piramidalarning 3 ta asosiy turi:</b>\n"
            "1. <b>Sonlar piramidasi (Elton piramidasi):</b> Har bir pog‘onadagi individlar sonini aks ettiradi. Odatda yuqoriga torayadi. "
            "<i>Istisno:</i> Bitta yirik daraxtda minglab parazit hasharotlar yashaganda teskari piramida hosil bo‘ladi.\n"
            "2. <b>Biomassa piramidasi:</b> Har bir pog‘onadagi tirik moddaning quruq massasini ko‘rsatadi. Quruqlikda to‘g‘ri shaklda bo‘ladi. "
            "<i>Okeanda teskari bo‘lishi mumkin:</i> Fitoplankton massasi tez iste'mol qilingani uchun har lahzada zooplankton massasidan kam bo‘lib ko‘rinadi.\n"
            "3. <b>Energiya piramidasi:</b> Vaqt birligida trofik pog‘onalardan o‘tgan energiya oqimini ko‘rsatadi. "
            "<b>MUHIM QOIDA:</b> Energiya piramidasi hech qachon teskari bo‘lmaydi, har doim yuqoriga qarab torayadi!"
        ),
        "guide": (
            "📘 <b>18-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>10% qoidasi (Lindeman):</b> Keyingi bo‘g‘inga faqat 10% energiya o‘tadi (90% yo‘qotiladi).\n"
            "• <b>Sonlar piramidasi:</b> Individlar soni (Elton).\n"
            "• <b>Biomassa piramidasi:</b> Tirik modda og‘irligi.\n"
            "• <b>Energiya piramidasi:</b> Har doim to‘g‘ri piramida (teskari bo‘lmaydi!)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> 10% qoidasi va ekologik piramidalarning dinamik modeli"
    },
    {
        "id": "19",
        "title": "19-§. Tabiiy ekosistemalar",
        "text": (
            "📖 <b>19-§. TABIIY EKOSISTEMALAR</b>\n\n"
            "🔹 <b>Biom</b> — muayyan iqlimiy mintaqaga xos bo‘lgan ulkan tabiiy ekotizimlar majmuasidir.\n\n"
            "🌍 <b>Yer yuzining asosiy quruqlik biomalari:</b>\n"
            "1. <b>Tundra:</b> Shimoliy sovuq mintaqa, doimiy to‘nglik, mox va lixenlar, pakana tollar, bug‘ular, qutb tulkisi.\n"
            "2. <b>Tayga (ignabargli o‘rmonlar):</b> Qoraqarag‘ay, tilog‘och, qarag‘ay, o‘rmon qoploni, ayiq, los.\n"
            "3. <b>Keng bargli mo‘tadil o‘rmonlar:</b> Eman, qayin, jo‘ka, yong‘oqzorlar, boy o‘txo‘r va yirtqich fauna.\n"
            "4. <b>Dashtlar:</b> Boshbo‘liq, chalov, betaga kabi g‘alladosh o‘tlar, kemiruvchilar, sayg‘oqlar.\n"
            "5. <b>Cho‘llar:</b> Qurg‘oqchil iqlim, saksovul, yantoq, iloq, sudralib yuruvchilar va tuyalar.\n"
            "6. <b>Savannalar:</b> Tropik o‘tloqlar, baobablar, akatsiyalar, antilopalar, zebralar, sherlar.\n"
            "7. <b>Nam tropik o‘rmonlar (Gileyalar):</b> Dunyodagi eng yuqori bioxilma-xillik va qavatlilikka ega ekotizimlar."
        ),
        "guide": (
            "📘 <b>19-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Biom:</b> Yirik iqlimiy ekotizimlar mintaqasi.\n"
            "• <b>Sovuq bioma:</b> Tundra (to‘nglik, lixenlar), Tayga (ignabargli).\n"
            "• <b>Mo‘tadil:</b> Keng bargli o‘rmon, Dasht (g‘alladoshlar).\n"
            "• <b>Issiq:</b> Cho‘l (kserofitlar), Savanna (o‘tloq va yirik sutemizuvchilar), Tropik o‘rmon (eng boy)."
        ),
        "media": "🎥 <b>Video dars:</b> Sayyoramizning tabiiy zonalari va quruqlik biomalari"
    },
    {
        "id": "20",
        "title": "20-§. Markaziy Osiyo va O'zbekistonning tabiiy ekosistemalari",
        "text": (
            "📖 <b>20-§. MARKAZIY OSIYO VA O‘ZBEKISTONNING TABIIY EKOSISTEMALARI</b>\n\n"
            "🔹 O‘zbekiston Respublikasi o‘ziga xos relyef va iqlimiy zonalarga ega bo‘lib, asosan cho‘l, adir, tog‘ va yaylov mintaqalaridan iborat.\n\n"
            "🏜 <b>O‘zbekistonning asosiy ekotizimlari:</b>\n"
            "1. <b>Qumli cho‘l ekotizimi (Qizilqum):</b>\n"
            "   • Oq va qora saksovul, qandim, cherkez, qum quyonsuyagi, qum ilog‘i.\n"
            "   • Qum sichqoni, qo‘shoyoq, ingichka barmoqli yumronqoziq, bo‘z echkiemar, dasht toshbaqasi.\n"
            "2. <b>Gipsli va toshloq cho‘llar (Ustyurt platosi):</b> Biyurg‘un, bo‘yalishe, shuvoq, sayg‘oq, qoradum (jayron).\n"
            "3. <b>Sho‘rxoklar:</b> Sarosazan, qorasho‘ra, sho‘ra o‘tlar.\n"
            "4. <b>To‘qay ekotizimlari:</b> Amudaryo va Sirdaryo qirg‘oqlari bo‘ylab: turang‘il, jiyda, tol, yulg‘un, qamish; xonqul bug‘usi (kiyik), qamish mushugi, qirg‘ovul.\n"
            "5. <b>Tog‘ va tog‘oldi ekotizimlari:</b> Archazorlar, yong‘oqzorlar, pista va do‘lanazorlar; tog‘ echkisi (teke), qor qoploni (bars), Tyan-Shan qo‘ng‘ir ayig‘i."
        ),
        "guide": (
            "📘 <b>20-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Qumli cho‘l:</b> Saksovul, qandim, qum sichqoni, echkiemar.\n"
            "• <b>Gipsli cho‘l (Ustyurt):</b> Biyurg‘un, sayg‘oq, jayron.\n"
            "• <b>To‘qay:</b> Turang‘il, jiyda, xonqul bug‘usi, qirg‘ovul.\n"
            "• <b>Tog‘ ekotizimi:</b> Archazor, yong‘oqzor, qor qoploni, tog‘ echkisi."
        ),
        "media": "🎥 <b>Video dars:</b> O‘zbekistonning tabiiy cho‘l, to‘qay va tog‘ ekotizimlari"
    },
    {
        "id": "21",
        "title": "21-§. Sun'iy ekosistemalar",
        "text": (
            "📖 <b>21-§. SUN'IY EKOSISTEMALAR (AGROTSENOZLAR)</b>\n\n"
            "🔹 <b>Agrotsenoz (Agroekotizim)</b> — inson tomonidan qishloq xo‘jalik mahsulotlari olish maqsadida sun'iy yaratilgan va doimiy boshqarib turiladigan ekotizimdir (paxtazor, bug‘doyzor, bog‘, poliz, issiqxona).\n\n"
            "⚖️ <b>Tabiiy biogeotsenoz va Agrotsenozning qiyosiy farqlari:</b>\n"
            "1. <b>Bioxilma-xillik:</b> Tabiiyda yuksak; Agrotsenozda keskin kam, asosan monokultura (bitta tur ustun).\n"
            "2. <b>Tanlash shakli:</b> Tabiiyda tabiiy tanlanish; Agrotsenozda sun'iy tanlash ustun.\n"
            "3. <b>Energiya manbai:</b> Tabiiyda faqat quyosh energiyasi; Agrotsenozda quyoshdan tashqari qo‘shimcha energiya (inson mehnati, yoqilg‘i, o‘g‘itlar, sug‘orish).\n"
            "4. <b>Moddalar aylanmasi:</b> Tabiiyda to‘liq yopiq zanjir; Agrotsenozda ochiq (chunki mahsulot hosil bilan olib ketiladi, tuproqqa o‘g‘it solish talab etiladi).\n"
            "5. <b>Barqarorlik:</b> Tabiiy o‘z-o‘zini tiklaydi va juda barqaror; Agrotsenoz inson parvarishisiz tezda parchalanadi."
        ),
        "guide": (
            "📘 <b>21-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Agrotsenoz:</b> Inson yaratgan sun'iy tizim (dala, bog‘).\n"
            "• <b>Monokultura:</b> Bitta madaniy tur ustunligi.\n"
            "• <b>Moddalar aylanishi:</b> To‘liq emas (hosil bilan chiqariladi).\n"
            "• <b>Barqarorlik:</b> Past (inson nazoratisiz yo‘qoladi)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Agrotsenoz va tabiiy biotsenozning taqqoslama tahlili"
    },
    {
        "id": "22",
        "title": "22-§. Biogeotsenozlarning barqarorligi",
        "text": (
            "📖 <b>22-§. BIOGEOTSENOZLARNING BARQARORLIGI VA DINAMIKASI</b>\n\n"
            "🔹 <b>Suksessiya</b> (lotincha <i>«successio»</i> — ketma-ketlik, almashinish) — muayyan hududda tashqi yoki ichki omillar ta'sirida biotsenozlarning qonuniy ravishda bir-birini izchil almashtirishi jarayonidir.\n\n"
            "🔄 <b>Suksessiya turlari:</b>\n"
            "1. <b>Birlamchi suksessiya:</b>\n"
            "   • Ilgari hayot bo‘lmagan yalang‘och substratlarda boshlanadi (qoyalar, vulqon lavasi, qumtepalar).\n"
            "   • <i>Bosqichlar:</i> Bakteriyalar va lixenlar (pionerlar) ➔ Moxlar ➔ Bir yillik o‘tlar ➔ Ko‘p yillik o‘tlar ➔ Butalar ➔ O‘rmon.\n"
            "2. <b>Ikkilamchi suksessiya:</b>\n"
            "   • Ilgari mavjud bo‘lgan biotsenoz yo‘q qilingan, lekin tuproq qatlami va urug‘lar saqlangan joyda ro‘y beradi (o‘rmon yong‘ini, suv toshqini, kesilgan daraxtzor, tashlandiq shudgor).\n"
            "   • Birlamchi suksessiyaga qaraganda ancha tez (o‘nlab yillarda) kechadi.\n\n"
            "🌳 <b>Klimaks jamoa:</b> Suksessiyaning yakuniy, eng muvozanatli va barqaror holati (masalan, yetuk eman o‘rmoni yoki archazor)."
        ),
        "guide": (
            "📘 <b>22-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Suksessiya:</b> Biotsenozlarning ketma-ket almashinishi.\n"
            "• <b>Birlamchi suksessiya:</b> Hayotsiz substratda boshlanadi (qoya, lava).\n"
            "• <b>Ikkilamchi suksessiya:</b> Tuprog‘i saqlangan joyda (yong‘indan so‘ng).\n"
            "• <b>Klimaks:</b> Ekotizimning barqaror yakuniy holati."
        ),
        "media": "🎥 <b>Video dars:</b> Qoyalardan o‘rmongacha: Birlamchi va ikkilamchi suksessiya bosqichlari"
    },
    {
        "id": "23",
        "title": "23-§. Inson ekologiyasi",
        "text": (
            "📖 <b>23-§. INSON EKOLOGIYASI</b>\n\n"
            "🔹 <b>Inson ekologiyasi</b> — inson organizmining atrof-muhit (tabiiy va ijtimoiy-texnogen muhit) bilan o‘zaro aloqalari, "
            "moslashuv mexanizmlari va salomatligini saqlash qonuniyatlarini o‘rganuvchi fan tarmog‘idir.\n\n"
            "🏙 <b>Urbanizatsiya va inson muhiti:</b>\n"
            "• Shaharlarda aholining to‘planishi (urbanizatsiya) mikroiqlim, havo tozaligi va shovqin darajasining o‘zgarishiga olib keladi.\n"
            "• Shovqin ifloslanishi, elektromagnit to‘lqinlar va kimyoviy mutagenlar inson asab va yurak-qon tomir sistemasiga salbiy ta'sir ko‘rsatadi.\n\n"
            "🥗 <b>Ekologik xavfsizlik:</b>\n"
            "• Toza ichimlik suvi ta'minoti, pestitsidlarsiz oziq-ovqat mahsulotlari va yashil hududlarni saqlash inson genofondini asrashning muhim garovidir."
        ),
        "guide": (
            "📘 <b>23-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Inson ekologiyasi:</b> Inson va uning urbanizatsiyalashgan muhiti aloqalari.\n"
            "• <b>Antropogen omillar:</b> Shovqin, kimyoviy ifloslanish, stress.\n"
            "• <b>Maqsad:</b> Sog‘lom genofond va ekologik barqaror hayot muhitini ta'minlash."
        ),
        "media": "🎥 <b>Video dars:</b> Urbanizatsiya sharoitida inson salomatligi va ekologik madaniyat"
    },
    # 5-bob
    {
        "id": "24",
        "title": "24-§. Biosfera darajasining xususiyatlari. Biosfera haqida ta'limot",
        "text": (
            "📖 <b>24-§. BIOSFERA DARAJASINING XUSUSIYATLARI. BIOSFERA HAQIDA TA'LIMOT</b>\n\n"
            "🔹 <b>Biosfera</b> — Yer sayyorasining tirik organizmlar tarqalgan va ularning faoliyati ta'sirida o‘zgargan qobig‘idir.\n\n"
            "📜 <b>Biosfera ta'limotining yaratilishi:</b>\n"
            "• «Biosfera» atamasini birinchi marta 1875-yilda avstriyalik geolog <b>Eduard Zyuss</b> geologik qatlamlar tahlilida qo‘llagan.\n"
            "• Biosfera haqidagi yaxlit va fundamental ilmiy ta'limotni 1926-yilda buyuk olim <b>Vladimir Ivanovich Vernadskiy</b> o‘zining «Biosfera» nomli asarida asoslab berdi.\n\n"
            "🌍 <b>Vernadskiy ta'limotining asosiy qoidalari:</b>\n"
            "1. Tirik modda sayyoramizdagi eng qudratli geologik kuchdir.\n"
            "2. Yer yuzidagi barcha anorganik jarayonlar tirik organizmlar ta'sirida o‘zgaradi.\n"
            "3. Biosfera ochiq, dinamik, o‘z-o‘zini boshqaruvchi global biologik tizimdir."
        ),
        "guide": (
            "📘 <b>24-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Biosfera atamasi:</b> E.Zyuss (1875).\n"
            "• <b>Biosfera ta'limoti asoschisi:</b> V.I.Vernadskiy (1926, «Biosfera» kitobi).\n"
            "• <b>Asosiy xulosa:</b> Tirik modda — eng qudratli sayyoraviy geokimyoviy kuch."
        ),
        "media": "🎥 <b>Video dars:</b> V.I.Vernadskiyning biosfera haqidagi ta'limoti va uning ahamiyati"
    },
    {
        "id": "25",
        "title": "25-§. Biosfera chegaralari",
        "text": (
            "📖 <b>25-§. BIOSFERA CHEGARALARI</b>\n\n"
            "🔹 Biosferaning fazoviy chegaralari organizmlarning yashashi uchun zarur bo‘lgan sharoitlar (suv, harorat, yorug‘lik, himoya) bilan belgilanadi:\n\n"
            "🌌 <b>Biosferaning qobiqlar bo‘yicha chegaralari:</b>\n"
            "1. <b>Atmosferada:</b> Yuqori chegara <b>ozon ekrani</b> balandligigacha (20–25 km). Ozon qatlamidan yuqorida kuchli qisqa to‘lqinli ultrabinafsha nurlanish tiriklikni yo‘q qiladi. 20–22 km balandlikda faqat bakteriya va zamburug‘ sporalari aniqlangan.\n"
            "2. <b>Gidrosferada:</b> Dunyo okeanining butun chuqurligini qamrab oladi (eng chuqur nuqtasi — Mariana botig‘i, 11 022 m gacha maxsus bakteriyalar va chuqur suv baliqlari uchraydi).\n"
            "3. <b>Litosferada:</b> Qattiq yer po‘stining yuqori qatlami bo‘ylab 3–4 km chuqurlikkacha (neft qatlamlaridagi anaerob bakteriyalar). Pastki chegarani yuqori harorat (+100°C dan yuqori) cheklaydi.\n\n"
            "🌟 <b>«Hayot pardasi»:</b> Organizmlar biosferada bir tekis tarqalmagan. Eng qizg‘in hayot quruqlik va okean yuzasida, havo bilan tutashgan zonada to‘plangan."
        ),
        "guide": (
            "📘 <b>25-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Atmosferada:</b> Ozon qatlamigacha (20–25 km).\n"
            "• <b>Gidrosferada:</b> Butun chuqurlikda (Mariana botig‘i — 11 km).\n"
            "• <b>Litosferada:</b> 3–4 km gacha (neft bakteriyalari, +100°C chegara).\n"
            "• <b>Cheklovchilar:</b> Yuqorida — UB nurlar; Pastda — yuqori harorat."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Biosferaning sayyoraviy chegaralari va qobiqlari 3D da"
    },
    {
        "id": "26",
        "title": "26-§. Biosferaning tarkibi",
        "text": (
            "📖 <b>26-§. BIOSFERANING TARKIBI</b>\n\n"
            "🔹 V.I.Vernadskiy biosferani tashkil etuvchi moddalarni genetik kelib chiqishiga ko‘ra bir necha guruhga ajratgan:\n\n"
            "🧪 <b>Biosferadagi moddalar toifalari:</b>\n"
            "1. <b>Tirik modda:</b> Sayyoramizdagi barcha tirik organizmlar (o‘simliklar, hayvonlar, zamburug‘lar, mikroorganizmlar) yig‘indisi.\n"
            "2. <b>Biogen modda:</b> Tirik organizmlarning hayot faoliyati natijasida hosil bo‘lgan va to‘plangan moddalar: toshko‘mir, neft, torf, yonuvchi slaneslar, bo‘r, ohaktosh, atmosfera kislorodi.\n"
            "3. <b>Kosil modda:</b> Tirik organizmlar ishtirokisiz paydo bo‘lgan moddalar: magmatik tog‘ jinslari, birlamchi minerallar.\n"
            "4. <b>Biokosil modda:</b> Tirik organizmlar va anorganik tabiatning birgalikdagi ta'siri natijasida vujudga kelgan murakkab tuzilmalar: tuproq, cho‘kindi jinslar, loy, tabiiy suvlar.\n"
            "5. <b>Radioaktiv moddalar:</b> Radioaktiv elementlarning parchalanish mahsulotlari.\n"
            "6. <b>Kosmik modda:</b> Koinotdan tushuvchi meteorit moddalari va kosmik chang."
        ),
        "guide": (
            "📘 <b>26-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tirik modda:</b> Barcha tirik organizmlar.\n"
            "• <b>Biogen modda:</b> Organik kelib chiqishli (neft, ko‘mir, bo‘r, O2).\n"
            "• <b>Kosil modda:</b> Tirikliksiz hosil bo‘lgan (magma, granit).\n"
            "• <b>Biokosil modda:</b> Tirik + anorganik birligi (tuproq, balchiq)."
        ),
        "media": "🎥 <b>Video dars:</b> Biosferaning moddiy tarkibi va V.I.Vernadskiy tasnifi"
    },
    {
        "id": "27",
        "title": "27-§. Biosferadagi tirik moddaning xususiyatlari va funksiyalari",
        "text": (
            "📖 <b>27-§. BIOSFERADAGI TIRIK MODDANING XUSUSIYATLARI VA FUNKSIYALARI</b>\n\n"
            "🔹 <b>Tirik moddaning o‘ziga xos xususiyatlari:</b>\n"
            "Katta miqdorda erkin kimyoviy energiyaga egaligi, reaksiyalarning nihoyatda yuqori tezligi, o‘z-o‘zini yangilash va biosfera bo‘ylab faol tarqalish xususiyati.\n\n"
            "⚙️ <b>Tirik moddaning biosferadagi biogeokimyoviy funksiyalari:</b>\n"
            "1. <b>Gaz funksiyasi:</b> Gazlar almashinuvini ta'minlaydi. Fotosintez natijasida erkin kislorod (O2) hosil bo‘lishi, nafas olishda karbonat angidrid (CO2) ajralishi, bakteriyalar orqali azot (N2), metan (CH4) va vodorod sulfid (H2S) balansi boshqariladi.\n"
            "2. <b>Konsentratsion funksiya:</b> Tirik hujayralar atrof-muhitdagi tarqoq kimyoviy elementlarni tanlab o‘zida to‘playdi (suvo‘tlar yod to‘playdi; mollyuskalar kalsiy; qirqbo‘g‘imlar kremniy; qon eritrotsitlari temir).\n"
            "3. <b>Oksidlanish-qaytarilish funksiyasi:</b> Atomlarning valentligini o‘zgartiruvchi reaksiyalar (temir bakteriyalari, oltingugurt bakteriyalari, azot aylanishi).\n"
            "4. <b>Destruktiv (parchalash) funksiya:</b> O‘lik organik moddalarni mineral elementlargacha parchalab, tabiatga qaytarish (redusentlar faoliyati).\n"
            "5. <b>Energetik funksiya:</b> Quyosh nuri energiyasini fotosintez orqali organik moddalar kimyoviy bog‘lariga to‘plash va oziq zanjirlari bo‘ylab taqsimlash."
        ),
        "guide": (
            "📘 <b>27-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Gaz funksiyasi:</b> O2, CO2, N2 balansini saqlash.\n"
            "• <b>Konsentratsion:</b> Elementlarni to‘plash (yod, kalsiy, kremniy, temir).\n"
            "• <b>Oksidlanish-qaytarilish:</b> Xemotrof bakteriyalar faoliyati.\n"
            "• <b>Destruktiv:</b> Qoldiqlarni chirish va minerallash.\n"
            "• <b>Energetik:</b> Quyosh energiyasini to‘plash va uzatish."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Tirik moddaning biosferadagi biogeokimyoviy vazifalari"
    },
    {
        "id": "28",
        "title": "28-§. Biosfera biomassasi",
        "text": (
            "📖 <b>28-§. BIOSFERA BIOMASSASI</b>\n\n"
            "🔹 <b>Biomassa</b> — muayyan vaqtda biosferada mavjud bo‘lgan barcha tirik organizmlarning quruq modda og‘irligi yig‘indisidir. Sayyoramizdagi jami biomassa qariyb <b>2.4 × 10¹² tonna</b>ni tashkil etadi.\n\n"
            "⚖️ <b>Quruqlik va Dunyo okeani biomassasi nisbati:</b>\n"
            "1. <b>Quruqlikda:</b>\n"
            "   • Biosfera umumiy biomassasining <b>99.8% qismi</b> quruqlikka to‘g‘ri keladi.\n"
            "   • Quruqlikda <b>fitomassa (o‘simliklar)</b> mutlaq ustunlik qiladi (99.2%), hayvonlar va mikroblar esa 1% dan kamroq.\n"
            "2. <b>Dunyo okeanida:</b>\n"
            "   • Biosfera biomassasining atigi <b>0.2% qismi</b> okeanlarga to‘g‘ri keladi.\n"
            "   • Okeanda <b>zoomassa (hayvonlar)</b> fitomassadan ko‘p (90% dan ortig‘i hayvonlar va mikroblar). Fitoplankton nihoyatda tez ko‘payadi va zudlik bilan iste'mol qilinadi."
        ),
        "guide": (
            "📘 <b>28-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Umumiy biomassa:</b> ~2.4 × 10¹² tonna.\n"
            "• <b>Quruqlikda:</b> 99.8% biomassa to‘plangan (Fitomassa 99%).\n"
            "• <b>Okeanda:</b> 0.2% biomassa (Zoomassa ustun — 90%).\n"
            "• <b>Okean paradoksi:</b> Fitoplankton tez ko‘payib, tez yeyiladi."
        ),
        "media": "🎥 <b>Video dars:</b> Quruqlik va Dunyo okeani biomassasining taqsimlanish xaritasi"
    },
    {
        "id": "29",
        "title": "29-§. Biosferada modda va energiyaning davriy aylanishi",
        "text": (
            "📖 <b>29-§. BIOSFERADA MODDA VA ENERGIYANING DAVRIY AYLANISHI</b>\n\n"
            "🔹 Biosferadagi hayotning abadiyligi moddalarning doimiy davriy aylanishi va energiya oqimi bilan ta'minlanadi.\n\n"
            "🔄 <b>Ikki xil davriy aylanish mavjud:</b>\n"
            "1. <b>Katta (geologik) davriy aylanish:</b>\n"
            "   • Yuz minglab va millionlab yillar davom etadi.\n"
            "   • Tog‘ jinslarining yemirilishi, daryolar orqali okeanga yuvilishi, cho‘kindi qatlamlar hosil bo‘lishi va tektonik harakatlar natijasida yana quruqlikka ko‘tarilishi.\n"
            "2. <b>Kichik (biologik) davriy aylanish:</b>\n"
            "   • Tirik organizmlar ishtirokida ro‘y beradi va nisbatan tez kechadi.\n"
            "   • Oziq moddalar tuproq va atmosferadan o‘simliklarga o‘tadi, konsumentlar orqali iste'mol qilinadi, redusentlar vositasida yana tuproq va atmosferaga qaytariladi.\n\n"
            "⚡ <b>Energiya oqimi qoidasi:</b> Moddalar biosferada berk halqa bo‘ylab aylanadi, lekin energiya aylanmaydi! Energiya quyoshdan kirib keladi va termodinamika qonunlariga binoan kosmosga qaytarilmas issiqlik bo‘lib tarqaladi."
        ),
        "guide": (
            "📘 <b>29-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Geologik aylanish:</b> Katta, millionlab yillik anorganik sikl.\n"
            "• <b>Biologik aylanish:</b> Kichik, tirik organizmlar ishtirokidagi tezkor sikl.\n"
            "• <b>Moddalar:</b> Davriy aylanadi (halqasimon).\n"
            "• <b>Energiya:</b> Qaytmas oqim shaklida o‘tadi (aylanmaydi)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Biosferadagi global biogeokimyoviy aylanma va energiya oqimi"
    },
    {
        "id": "30",
        "title": "30-§. Biogeokimyoviy sikl",
        "text": (
            "📖 <b>30-§. BIOGEOKIMYOVIY SIKL</b>\n\n"
            "🔹 <b>Biogeokimyoviy sikllar</b> — kimyoviy elementlarning anorganik tabiatdan tirik organizmlarga va ulardan yana anorganik tabiatga davriy ravishda o‘tib turishidir.\n\n"
            "💧 <b>Asosiy sikllar tavsifi:</b>\n"
            "1. <b>Suv sikli:</b> Quyosh nuri ostida Dunyo okeani va quruqlikdan suv bug‘lanadi, bulutlar hosil bo‘lib, yog‘in sifatida qaytadi. O‘simliklar transpiratsiyasi muhim rol o‘ynaydi.\n"
            "2. <b>Uglerod (C) sikli:</b> Atmosferadagi CO2 fotosintezda organik moddaga aylanadi. Tirik organizmlar nafas olganda va chiriganda CO2 yana atmosferaga ajraladi. Yoqilg‘ilar (ko‘mir, neft) yonganda ulkan CO2 chiqadi.\n"
            "3. <b>Azot (N) sikli:</b> Atmosferadagi erkin azotni (78%) faqat azot fiksatsiya qiluvchi bakteriyalar (tugunak va erkin bakteriyalar) o‘zlashtira oladi. Nitrifikatsiya va denitrifikatsiya jarayonlari azot balansini saqlaydi.\n"
            "4. <b>Fosfor (P) sikli:</b> Cho‘kindi jinslardan boshlanadi, o‘simliklar shimib oladi, oziq zanjiri bo‘ylab o‘tadi va suyak qoldiqlari orqali yana cho‘kindi hosil qiladi (gaz fazasi yo‘q)."
        ),
        "guide": (
            "📘 <b>30-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Uglerod sikli:</b> Fotosintez (yutilish) va Nafas/Yonish (ajralish).\n"
            "• <b>Azot sikli:</b> Azotfiksatsiya ➔ Nitrifikatsiya ➔ Denitrifikatsiya.\n"
            "• <b>Fosfor sikli:</b> Cho‘kindi sikli (gaz fazasiga ega emas)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Uglerod, azot va fosforning biosferadagi davriy aylanishi"
    },
    # 6-bob
    {
        "id": "31",
        "title": "31-§. Biosfera evolutsiyasi. Biogenez",
        "text": (
            "📖 <b>31-§. BIOSFERA EVOLUTSIYASI. BIOGENEZ</b>\n\n"
            "🔹 Biosfera rivojlanishi geologik davrlar mobaynida tirik organizmlarning murakkablashuvi bilan chambarchas bog‘liq.\n\n"
            "⏳ <b>Eralar bo‘yicha biosfera bosqichlari:</b>\n"
            "1. <b>Arxey va Proterozoy:</b> Dastlabki prokaryotlar, sianobakteriyalar paydo bo‘lishi, fotosintezning kelib chiqishi, erkin kislorod hosil bo‘lishi va ozon ekranining shakllanishi.\n"
            "2. <b>Paleozoy:</b> Hayotning quruqlikka chiqishi (psilofitlar, qadimgi qirqquloqlar, birinchi quruqlik bo‘g‘imoyoqlilari va steqotsefallar), toshko‘mir qatlamlarining to‘planishi.\n"
            "3. <b>Mezozoy:</b> Sudralib yuruvchilar hukmronligi, ochiq urug‘lilar davri, dastlabki gulli o‘simliklar, sutemizuvchilar va qushlarning paydo bo‘lishi.\n"
            "4. <b>Kaynozoy:</b> Gulli o‘simliklar, hasharotlar, qushlar va sutemizuvchilarning gullab-yashnashi. Antropogen davrda insonning paydo bo‘lishi."
        ),
        "guide": (
            "📘 <b>31-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Proterozoy:</b> Kislorod inqilobi, ozon qatlami.\n"
            "• <b>Paleozoy:</b> Quruqlikka chiqish (psilofit, steqotsefal).\n"
            "• <b>Mezozoy:</b> Reptiliyalar va ochiq urug‘lilar davri.\n"
            "• <b>Kaynozoy:</b> Gulli o‘simliklar va sutemizuvchilar davri, inson paydo bo‘lishi."
        ),
        "media": "🎥 <b>Video dars:</b> Biosferaning geologik davrlar bo‘yicha evolutsiyasi"
    },
    {
        "id": "32",
        "title": "32-§. Biosfera evolutsiyasi. Noogenez",
        "text": (
            "📖 <b>32-§. BIOSFERA EVOLUTSIYASI. NOOGENEZ</b>\n\n"
            "🔹 <b>Noosfera</b> (yunoncha <i>«noos»</i> — aql, ong va <i>«sphaira»</i> — shar) — biosferaning inson ongi, aqli va ilmiy mehnati boshqaruvchi yangi, oliy evolutsion bosqichidir.\n\n"
            "🧠 <b>Noosfera ta'limoti:</b>\n"
            "• Atama 1927-yilda fransuz olimlari <b>Eduard Lerua</b> va <b>Pyer Teyyar de Sharden</b> tomonidan ilgari surilgan.\n"
            "• <b>V.I.Vernadskiy</b> noosfera ta'limotini moddiy-ilmiy asoslab berdi: insoniyat o‘z faoliyati bilan biosferaning tabiiy o‘zgarishidan ham kuchliroq omilga aylandi.\n\n"
            "🌱 <b>Noosferaga o‘tish shartlari:</b>\n"
            "• Tabiiy resurslardan oqilona foydalanish va chiqindisiz texnologiyalarni joriy etish.\n"
            "• Urushlar va qirg‘in qurollaridan voz kechish.\n"
            "• Butun insoniyatning sayyora taqdiri uchun umumiy mas'uliyati."
        ),
        "guide": (
            "📘 <b>32-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Noosfera:</b> Aql va ong sohasi (E.Lerua, P.Teyyar de Sharden).\n"
            "• <b>Vernadskiy qarashi:</b> Inson aqli sayyoraviy geologik kuchga aylandi.\n"
            "• <b>Bosh maqsad:</b> Tabiat va jamiyatning uyg‘un hamkorligi (koevolyutsiya)."
        ),
        "media": "🎥 <b>Video dars:</b> Noosfera konsepsiyasi va kelajak ekologik sivilizatsiyasi"
    },
    {
        "id": "33",
        "title": "33-§. Inson biosfera omili sifatida. Inson faoliyatining biosferaga ta'siri",
        "text": (
            "📖 <b>33-§. INSON BIOSFERA OMILI SIFATIDA. INSON FAOLIYATINING BIOSFERAGA TA'SIRI</b>\n\n"
            "🔹 Hozirgi davrda inson faoliyati biosferada global miqyosdagi ekologik tangliklarni keltirib chiqarmoqda.\n\n"
            "⚠️ <b>Asosiy global ekologik muammolar:</b>\n"
            "1. <b>Issiqxona effekti va iqlim isishi:</b> Sanoat va transport tufayli CO2, CH4 gazlari atmosferada to‘planib, issiqlik nurlarini tutib qoladi.\n"
            "2. <b>Ozon qatlamining yemirilishi:</b> Freonlar (xlorftoruglerodlar) ta'sirida ozon ekrani siyraklashib, xavfli ultrabinafsha nurlarning yerga tushishi ortadi.\n"
            "3. <b>Kislotali yomg‘irlar:</b> Oltingugurt oksidi (SO2) va azot oksidlari (NOx) atmosferadagi namlik bilan qo‘shilib, sulfat va nitrat kislotalarni hosil qiladi.\n"
            "4. <b>Cho‘llanish va tuproq eroziyasi:</b> Noto‘g‘ri sug‘orish, sho‘rlanish va o‘rmonlarning kesilishi natijasida unumdor yerlarning yo‘qolishi.\n"
            "5. <b>Orol dengizi inqirozi:</b> Markaziy Osiyodagi eng yirik mintaqaviy fojia — suv sathining keskin pasayishi, tuzli chang bo‘ronlari va iqlimning keskinlashuvi."
        ),
        "guide": (
            "📘 <b>33-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Issiqxona effekti:</b> CO2, metan ko‘payishi ➔ Global isish.\n"
            "• <b>Ozon tuynugi:</b> Freonlar ta'sirida O3 yemirilishi.\n"
            "• <b>Kislotali yomg‘ir:</b> SO2 va NOx gazlari.\n"
            "• <b>Mintaqaviy inqiroz:</b> Orol dengizining qurishi."
        ),
        "media": "🎥 <b>Video dars:</b> Global ekologik muammolar va Orol fojiasining sabablari"
    },
    {
        "id": "34",
        "title": "34-§. O'simlik va hayvonot olamini muhofaza qilish",
        "text": (
            "📖 <b>34-§. O‘SIMLIK VA HAYVONOT OLAMINI MUHOFAZA QILISH</b>\n\n"
            "🔹 Bioxilma-xillikni saqlash — biosfera barqarorligining yagona garovidir.\n\n"
            "📕 <b>Qizil kitob:</b>\n"
            "• Xalqaro va milliy darajada noyob va yo‘qolib ketish xavfi ostida turgan turlar ro‘yxati.\n"
            "• <b>O‘zbekiston Qizil kitobi</b> ilk bor 1979-yilda ta'sis etilgan va davriy ravishda yangilanib boriladi.\n\n"
            "🛡 <b>Muhofaza etiladigan tabiiy hududlar:</b>\n"
            "1. <b>Davlat qo‘riqxonalari (qo‘riqxona rejimi eng qat'iy):</b> Har qanday xo‘jalik faoliyati mutlaqo taqiqlanadi (Zomin, Chotqol, Qizilqum, Surxon, Hisor, Nurota, Quyi Amudaryo).\n"
            "2. <b>Milliy tabiat bog‘lari:</b> Tabiatni muhofaza qilish bilan birga ilmiy turizm va dam olishga ruxsat beriladi (Zomin, Ugom-Chotqol milliy bog‘lari).\n"
            "3. <b>Buyurtmaxonalar (zakazniklar):</b> Muayyan hayvon yoki o‘simlik turini ko‘paytirish uchun vaqtincha yoki doimiy cheklangan hududlar."
        ),
        "guide": (
            "📘 <b>34-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Qizil kitob:</b> Yo‘qolish arafasidagi noyob turlar reyestri.\n"
            "• <b>Qo‘riqxona:</b> Barcha xo‘jalik faoliyati qat'iy taqiqlangan hudud.\n"
            "• <b>Milliy bog‘:</b> Muhofaza + sayohat (Zomin, Ugom-Chotqol).\n"
            "• <b>Qo‘riqxonalar:</b> Chotqol, Hisor, Surxon, Qizilqum, Zomin."
        ),
        "media": "🎥 <b>Video dars:</b> O‘zbekistonning qo‘riqxonalari va Qizil kitobga kiritilgan turlari"
    },
    # -------------------------------------------------------------
    # II QISM. ORGANIK OLAM FILOGENEZI
    # 7-bob. Organik olam va o'simliklar filogenezi
    # -------------------------------------------------------------
    {
        "id": "35",
        "title": "35-§. Organik olam filogenezining umumiy tavsifi",
        "text": (
            "📖 <b>35-§. ORGANIK OLAM FILOGENEZINING UMUMIY TAVSIFI</b>\n\n"
            "🔹 <b>Filogenez</b> (yunoncha <i>«phylon»</i> — qabila, urug‘ va <i>«genesis»</i> — kelib chiqish) — turlar, oilalar va umuman organik olamning Yer yuzidagi uzoq tarixiy rivojlanish jarayonidir. Atamani 1866-yilda <b>Ernst Gekkel</b> kiritgan.\n\n"
            "🔬 <b>Filogenezni o‘rganish usullari:</b>\n"
            "1. <b>Paleontologik usul:</b> Qazilma qoldiqlar, o‘tish shakllari va filogenetik qatorlarni o‘rganish (V.O.Kovalevskiyning ot filogenezi qatori).\n"
            "2. <b>Qiyosiy-anatomik usul:</b>\n"
            "   • <i>Gomologik organlar:</i> Kelib chiqishi va tuzilishi bir xil, lekin turli vazifani bajaruvchi a'zolar (odam qo‘li, qush qanoti, kit suzgichi — divergensiya natijasi).\n"
            "   • <i>Analogik organlar:</i> Kelib chiqishi har xil, ammo tashqi ko‘rinishi va vazifasi o‘xshash a'zolar (kapalak qanoti va qush qanoti — konvergensiya natijasi).\n"
            "   • <i>Rudimentlar:</i> Evolutsiya jarayonida o‘z ahamiyatini yo‘qotgan qoldiq a'zolar (odamda ko‘richak o‘simtasi, dum umurtqalari).\n"
            "   • <i>Atavizmlar:</i> Qadimgi ajdodlar belgilarining ayrim individlarda qayta paydo bo‘lishi (odamda quyruq, qalin jun, ko‘p emchaklik).\n"
            "3. <b>Embriologik usul:</b> <b>Biogenetik qonun (Gekkel-Myuller):</b> Ontogenez (individual rivojlanish) — filogenezning (tarixiy rivojlanishning) qisqa va tezkor takrorlanishidir."
        ),
        "guide": (
            "📘 <b>35-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Filogenez:</b> Tarixiy rivojlanish (E.Gekkel).\n"
            "• <b>Gomologik organ:</b> Kelib chiqishi bir, vazifasi har xil (qush qanoti va odam qo‘li).\n"
            "• <b>Analogik organ:</b> Kelib chiqishi har xil, vazifasi bir (kapalak va qush qanoti).\n"
            "• <b>Biogenetik qonun:</b> Ontogenez filogenezni takrorlaydi."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Gomologik va analogik a'zolar hamda filogenetik daraxt modeli"
    },
    {
        "id": "36",
        "title": "36-§. O'simliklar filogenezi. O'simliklarning vegetativ organlari filogenezi",
        "text": (
            "📖 <b>36-§. O‘SIMLIKLAR FILOGENEZI. VEGETATIV ORGANLAR FILOGENEZI</b>\n\n"
            "🔹 O‘simliklar evolyutsiyasi suv muhitidan quruqlik muhitiga chiqish va tana a'zolarining tabaqalanishi yo‘nalishida borgan.\n\n"
            "🌿 <b>Vegetativ organlar evolutsiyasi:</b>\n"
            "1. <b>Suvo‘tlar (Tuban o‘simliklar):</b> Haqiqiy ildiz, poya va barglari bo‘lmagan, tanasi qat-qat (tallom / qatron)dan iborat.\n"
            "2. <b>Dastlabki quruqlik o‘simliklari (Riniofitlar / Psilofitlar — Silur-Devon):</b> Tanasida poya va ildiz bo‘lmagan, shoxlangan yashil poyasimon o‘q (telom)lar va rizoidlar paydo bo‘lgan.\n"
            "3. <b>Telom nazariyasi (V.Tsimmerman):</b> Yuksak o‘simliklarning barcha vegetativ a'zolari (ildiz, poya, barg) psilofitlarning telom shoxchalarining o‘zgarishi (birlashishi va tabaqalanishi) natijasida shakllangan.\n"
            "4. <b>Ildizning paydo bo‘lishi:</b> Suv va minerallarni shimish uchun qirqquloqsimonlarda dastlab qo‘shimcha ildizlar, urug‘lilarda esa murtakdan asosiy ildiz shakllangan.\n"
            "5. <b>O‘tkazuvchi to‘qimalar:</b> Ksilema (naylar) va Floema (elaksimon naylar)ning takomillashuvi o‘simliklarning baland bo‘yga o‘sishiga imkon bergan."
        ),
        "guide": (
            "📘 <b>36-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Suvo‘t:</b> Tallom (ildiz va poyasiz).\n"
            "• <b>Psilofitlar (Riniofitlar):</b> Birinchi quruqlik o‘simliklari.\n"
            "• <b>Telom nazariyasi:</b> A'zolarning telomlardan kelib chiqishi (Tsimmerman).\n"
            "• <b>To‘qimalar:</b> O‘tkazuvchi naylar (ksilema, floema) poyani baquvvat qildi."
        ),
        "media": "🎥 <b>Video dars:</b> O‘simliklarning quruqlikka chiqishi va vegetativ organlar evolutsiyasi"
    },
    {
        "id": "37",
        "title": "37-§. O'simliklarning generativ organlari filogenezi",
        "text": (
            "📖 <b>37-§. O‘SIMLIKLARNING GENERATIV ORGANLARI FILOGENEZI</b>\n\n"
            "🔹 O‘simliklar ko‘payish organlari evolyutsiyasining bosh yo‘nalishi — jinsiy ko‘payish jarayonining suvga bo‘lgan bog‘liqligidan butunlay qutulish bo‘lgan.\n\n"
            "🌸 <b>Generativ organlarning taraqqiyot bosqichlari:</b>\n"
            "1. <b>Yo‘sinlar:</b> Nasllar gallanishida jinsiy bo‘g‘in — <b>gametofit</b> ustunlik qiladi. Urug‘lanish uchun mutlaqo tomchi suv zarur.\n"
            "2. <b>Qirqquloqlar, Plaunlar, Qirqbo‘g‘imlar:</b> Jinssiz bo‘g‘in — <b>sporofit</b> ustunlikka erishadi, gametofit murtakcha (o‘simtacha)ga aylanadi. Urug‘lanish hali ham suv orqali kechadi.\n"
            "3. <b>Ochiq urug‘lilar (Qarag‘ay, archa):</b> Suvga bog‘liqlik yo‘qoladi! Changlanish shamol orqali yuz beradi, urug‘kurtak qubba tangachalarida ochiq holda yetiladi.\n"
            "4. <b>Yopiq urug‘lilar (Gulli o‘simliklar):</b> Evolutsiyaning eng yuksak cho‘qqisi:\n"
            "   • <b>Gul</b> — maxsus ko‘payish organi paydo bo‘ldi.\n"
            "   • Urug‘kurtak tuguncha ichida himoyalangan (yopiq) bo‘ladi.\n"
            "   • <b>Qo‘sh urug‘lanish</b> (1898-yil, <b>S.G.Navashin</b>): 1-spermiy tuxum hujayra bilan (murtak 2n), 2-spermiy markaziy hujayra bilan qo‘shiladi (triploid endosperm 3n).\n"
            "   • Urug‘ni himoyalovchi va tarqatuvchi <b>meva</b> shakllanadi."
        ),
        "guide": (
            "📘 <b>37-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Yo‘sin:</b> Gametofit ustun, suv shart.\n"
            "• <b>Qirqquloq:</b> Sporofit ustun, suv shart.\n"
            "• <b>Ochiq urug‘li:</b> Urug‘ paydo bo‘ldi, suvga bog‘liq emas.\n"
            "• <b>Gulli o‘simlik:</b> Gul, meva va qo‘sh urug‘lanish (S.G.Navashin, 3n endosperm)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Gulli o‘simliklarda qo‘sh urug‘lanish va gul filogenezi"
    },
    # 8-bob
    {
        "id": "38",
        "title": "38-§. Hayvonot dunyosidagi evolutsion o'zgarishlar",
        "text": (
            "📖 <b>38-§. HAYVONOT DUNYOSIDAGI EVOLUTSION O‘ZGARISHLAR</b>\n\n"
            "🔹 Hayvonlar filogenezi bir hujayrali tuzilishdan to yuksak ixtisoslashgan ko‘p hujayrali murakkab organizmlargacha rivojlangan.\n\n"
            "🐾 <b>Asosiy evolutsion burilishlar (Aromorfozlar):</b>\n"
            "1. <b>Bir hujayralilikdan ko‘p hujayralilikka o‘tish:</b> Koloniya shakllari orqali (Gekkelning «Gastreya» va Mechnikovning «Fagotsitella» nazariyalari).\n"
            "2. <b>Murtak varaqlari:</b>\n"
            "   • 2 qavatli hayvonlar: Ektoderma va Entoderma (G‘ovaktanlilar, Bo‘shliqichlilar).\n"
            "   • 3 qavatli hayvonlar: Mezoderma (o‘rta varaqa) hosil bo‘lishi (Yassi chuvalchanglardan boshlab).\n"
            "3. <b>Simmetriya:</b> Nurlanuvchi (radial) simmetriyadan ikki tomonlama (bilateral) simmetriyaga o‘tish (faol harakatlanish natijasi).\n"
            "4. <b>Tana bo‘shlig‘i:</b>\n"
            "   • Bo‘shliqsiz (parenxima bilan to‘lgan — Yassi chuvalchanglar).\n"
            "   • Birlamchi tana bo‘shlig‘i (To‘garak chuvalchanglar).\n"
            "   • Ikkilamchi tana bo‘shlig‘i (Tselom — o‘z epiteliy qoplamiga ega: Halqali chuvalchanglar, Xordalilar).\n"
            "   • Aralash bo‘shliq (Miksotsel — Bo‘g‘imoyoqlilar).\n"
            "5. <b>Birlamchi va ikkilamchi og‘izlilar:</b>\n"
            "   • <i>Birlamchi og‘izlilar:</i> Murtak og‘zi (blastopor) katta organizmning og‘ziga aylanadi (Chuvalchanglar, Bo‘g‘imoyoqlilar, Mollyuskalar).\n"
            "   • <i>Ikkilamchi og‘izlilar:</i> Blastopor anal teshigiga aylanadi, og‘iz yangi teshikdan ochiladi (Ninaterililar, Xordalilar)."
        ),
        "guide": (
            "📘 <b>38-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>2 qavatli:</b> Bo‘shliqichlilar (radial simmetriya).\n"
            "• <b>3 qavatli:</b> Mezoderma paydo bo‘lishi (bilateral simmetriya).\n"
            "• <b>Tselom:</b> Ikkilamchi tana bo‘shlig‘i (Halqali chuvalchang, Xordalilar).\n"
            "• <b>Birlamchi og‘izli:</b> Chuvalchang, hasharot, mollyuska.\n"
            "• <b>Ikkilamchi og‘izli:</b> Ninaterili, Xordalilar (odam)."
        ),
        "media": "🎥 <b>Video dars:</b> Hayvonot olami filogenetik daraxti va yirik aromorfozlar"
    },
    {
        "id": "39",
        "title": "39-§. Tirik organizmlarda o'z-o'zini idora etish organlari: gumoral va nerv sistemasi evolutsiyasi",
        "text": (
            "📖 <b>39-§. GUMORAL VA NERV SISTEMASI EVOLUTSIYASI</b>\n\n"
            "🔹 Tirik organizmlarda boshqaruv va moslashuv dastlab kimyoviy (gumoral), keyinchalik nerv sistemasi orqali shakllangan.\n\n"
            "⚡ <b>Nerv sistemasining tarixiy tiplari:</b>\n"
            "1. <b>Diffuz (to‘rsimon) sistema:</b> Hayvonot olamidagi eng qadimgi nerv sistemasi (Gidra, meduzalar). Nerv hujayralari butun tana bo‘ylab to‘r hosil qiladi.\n"
            "2. <b>Zinasimon (ortogon) sistema:</b> Yassi chuvalchanglar (planariya). Boshda nerv tugunlari va bo‘ylama nerv ustunlari ko‘ndalang bog‘lamlar bilan tutashgan.\n"
            "3. <b>Tugunli (ganglionar) sistema:</b> Halqali chuvalchanglar va Bo‘g‘imoyoqlilar. Halqum usti va osti nerv tugunlari hamda qorin nerv zanjiridan iborat.\n"
            "4. <b>Naysimon sistema:</b> Faqat Xordalilarga xos. Tananing orqa tomonida xorda ustida nerv nayi joylashadi.\n\n"
            "🧠 <b>Umurtqalilarda bosh miya evolutsiyasi (5 ta bo‘lim):</b>\n"
            "• <b>Baliqlar:</b> Miyacha va o‘rta miya kuchli rivojlangan (suzish muvozanati va ko‘rish).\n"
            "• <b>Amfibiyalar:</b> Oldingi miya yarimsharlari ilk bor 2 ga ajraladi.\n"
            "• <b>Sudralib yuruvchilar:</b> Oldingi miya yarimsharlarida ilk bor kulrang po‘stloq kurtagi paydo bo‘ladi.\n"
            "• <b>Qushlar:</b> Miyacha nihoyatda yirik (uchish koordinatsiyasi) va ko‘rish bo‘rtiqlari kuchli.\n"
            "• <b>Sutemizuvchilar:</b> Bosh miya yarimsharlari po‘stlog‘i mukammal rivojlanib, burmalar va egatlar hosil qiladi (shartli reflekslar va aqliy faoliyat)."
        ),
        "guide": (
            "📘 <b>39-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Diffuz:</b> Gidra (to‘rsimon).\n"
            "• <b>Zinasimon:</b> Planariya.\n"
            "• <b>Tugunli:</b> Chuvalchang, hasharot (qorin nerv zanjiri).\n"
            "• <b>Naysimon:</b> Xordalilar.\n"
            "• <b>Miya 5 bo‘limi:</b> Oldingi, oraliq, o‘rta, miyacha, uzunchoq miya (Sutemizuvchilarda po‘stloq burmali)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Bosh miya bo‘limlarining baliqlardan sutemizuvchilargacha evolutsiyasi"
    },
    {
        "id": "40",
        "title": "40-§. Hayvonlarning tana qoplami va harakat organlari evolutsiyasi",
        "text": (
            "📖 <b>40-§. TANA QOPLAMI VA HARAKAT ORGANLARI EVOLUTSIYASI</b>\n\n"
            "🛡 <b>Tana qoplamalari evolutsiyasi:</b>\n"
            "• <b>Bir hujayralilar:</b> Plazmolemma yoki pellikula.\n"
            "• <b>Umurtqasizlar:</b> Bir qavatli epiteliy, gipoderma, kutikula, xitin qobiq (bo‘g‘imoyoqlilar).\n"
            "• <b>Umurtqalilar:</b> Ikki qavatli teri — <i>Epiderma</i> (tashqi) va <i>Derma</i> (ichki chin teri):\n"
            "  - <i>Baliqlar:</i> Suyak tangachalar va shilimshiq bezlar.\n"
            "  - <i>Suvda ham quruqlikda yashovchilar:</i> Yalang‘och, bezlarga boy doimiy nam teri (teri orqali nafas oladi).\n"
            "  - <i>Sudralib yuruvchilar:</i> Quruq, bezsiz, muguz tangachalar va qalqonlar (quruqlikda suv yo‘qotishdan asraydi).\n"
            "  - <i>Qushlar:</i> Quruq teri, pat qoplami, po‘stloqli oyoqlar, yog‘ ajratuvchi dumg‘aza bezi.\n"
            "  - <i>Sutemizuvchilar:</i> Jun qoplami (tuktosh), ter, yog‘, hid va sut bezlari; tirnoq, tuyoq, muguz shoxlar.\n\n"
            "🦴 <b>Skelet va harakat organlari evolutsiyasi:</b>\n"
            "• Tashqi skelet (xitin)dan ichki skeletga (xorda va umurtqa pog‘onasi) o‘tish.\n"
            "• Baliqlarning suzgich qanotlaridan quruqlik umurtqalilarining besh panjali bo‘g‘imli erkin oyoqlariga o‘tish."
        ),
        "guide": (
            "📘 <b>40-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Baliq:</b> Suyak tangacha.\n"
            "• <b>Amfibiya:</b> Yalang‘och nam teri.\n"
            "• <b>Reptiliya:</b> Muguz tangacha (quruqlikka moslashuv).\n"
            "• <b>Qush:</b> Pat qoplami + dumg‘aza bezi.\n"
            "• <b>Sutemizuvchi:</b> Jun, ter, yog‘ va sut bezlari."
        ),
        "media": "🎥 <b>Video dars:</b> Umurtqali hayvonlar skeleti va teri qoplamalari evolutsiyasi"
    },
    {
        "id": "41",
        "title": "41-§. Hayvonlarning nafas olish organlari evolutsiyasi",
        "text": (
            "📖 <b>41-§. NAFAS OLISH ORGANLARI EVOLUTSIYASI</b>\n\n"
            "🔹 Nafas olish sistemasi tanani kislorod bilan ta'minlash va karbonat angidridni chiqarish yuzasini oshirish tomonga rivojlangan.\n\n"
            "🫁 <b>Nafas olish apparatlarining taraqqiyoti:</b>\n"
            "1. <b>Tana yuzasi orqali diffuziya:</b> Maxsus organ yo‘q (Bir hujayralilar, Bo‘shliqichlilar, Chuvalchanglar).\n"
            "2. <b>Jabralar:</b> Suvda erigan kislorodni o‘zlashtiruvchi yupqa qon tomirlarga boy o‘simtalar (Qisqichbaqasimonlar, dengiz mollyuskalari, lansetnik, baliqlar, amfibiya lichinkalari).\n"
            "3. <b>Traxeyalar:</b> Butun tanaga kislorodni gaz holida tarqatuvchi tarmoqlangan havo naychalari (Hasharotlar, ko‘poyoqlilar).\n"
            "4. <b>O‘pkalar (Quruqlik umurtqalilari):</b>\n"
            "   • <i>Amfibiyalar:</i> Sodda xaltasimon silliq o‘pka (yuzasi kichik, 50% gaz almashinuvi teri orqali o‘tadi).\n"
            "   • <i>Sudralib yuruvchilar:</i> Kataksimon to‘siqli o‘pka, traxeya va bronxlar shakllangan.\n"
            "   • <i>Qushlar:</i> G‘ovaksimon zich o‘pka va <b>havo xaltachalari</b>. <b>Qo‘shaloq nafas olish:</b> havo o‘pkadan uchishda nafas olganda ham, nafas chiqarganda ham kislorod bilan boyitiladi.\n"
            "   • <i>Sutemizuvchilar:</i> Shoxlangan bronxlar va yuzlab millionlab mayda pufakchalar — <b>alveolalar</b> (katta so‘rish yuzasi), diafragma ishtirokida nafas olish."
        ),
        "guide": (
            "📘 <b>41-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Tana yuzasi:</b> Chuvalchanglar.\n"
            "• <b>Jabra:</b> Baliqlar, qisqichbaqalar.\n"
            "• <b>Traxeya:</b> Hasharotlar.\n"
            "• <b>Xaltasimon o‘pka:</b> Amfibiyalar (+teri).\n"
            "• <b>Kataksimon o‘pka:</b> Sudralib yuruvchilar.\n"
            "• <b>G‘ovaksimon o‘pka:</b> Qushlar (qo‘shaloq nafas olish).\n"
            "• <b>Alveolyar o‘pka:</b> Sutemizuvchilar (alveolalar, diafragma)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Qushlarda qo‘shaloq nafas olish va sutemizuvchilar alveolalari"
    },
    {
        "id": "42",
        "title": "42-§. Hayvonlarning qon aylanish organlari evolutsiyasi",
        "text": (
            "📖 <b>42-§. QON AYLANISH ORGANLARI EVOLUTSIYASI</b>\n\n"
            "🔹 Qon aylanish sistemasi to‘qimalarga oziq va kislorod yetkazish, parchalanish mahsulotlarini chiqarish vazifasini bajaradi.\n\n"
            "❤️ <b>Qon tomir sistemasi tiplari va yurak evolutsiyasi:</b>\n"
            "1. <b>Ochiq qon aylanish sistemasi:</b> Qon tomirlardan tana bo‘shlig‘iga (lakunalarga) quyiladi va to‘qimalarni bevosita yuvadi (Bo‘g‘imoyoqlilar, Mollyuskalar).\n"
            "2. <b>Yopiq qon aylanish sistemasi:</b> Qon faqat tomirlar bo‘ylab harakatlanadi (Halqali chuvalchanglar, Lansetnik, barcha Umurtqalilar).\n\n"
            "🩸 <b>Umurtqali hayvonlarda yurak tuzilishi:</b>\n"
            "• <b>Baliqlar:</b> 2 kamerali yurak (1 ta bo‘lmacha, 1 ta qorincha), 1 ta qon aylanish doirasi. Yurakda faqat venoz qon oqadi.\n"
            "• <b>Suvda ham quruqlikda yashovchilar:</b> 3 kamerali yurak (2 ta bo‘lmacha, 1 ta qorincha), 2 ta qon aylanish doirasi. Qorinchada aralash qon.\n"
            "• <b>Sudralib yuruvchilar:</b> 3 kamerali yurak, qorinchada <i>chala to‘siq</i> bor (aralashish kamayadi). Timsohlarda to‘liq 4 kamerali yurak.\n"
            "• <b>Qushlar:</b> To‘liq 4 kamerali yurak (2 bo‘lmacha, 2 qorincha), o‘ng aorta yoyi. Arterial va venoz qon butunlay ajralgan (gomoyotermlik/issiqqonlilik ta'minlandi).\n"
            "• <b>Sutemizuvchilar:</b> To‘liq 4 kamerali yurak, chap aorta yoyi. Qon mutlaqo aralashmaydi."
        ),
        "guide": (
            "📘 <b>42-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Ochiq sistema:</b> Hasharot, mollyuska (gemolimfa).\n"
            "• <b>Yopiq sistema:</b> Chuvalchang, baliq, qush, sutemizuvchi.\n"
            "• <b>Baliq:</b> 2 kamerali (1 doira, faqat venoz qon).\n"
            "• <b>Amfibiya:</b> 3 kamerali (2 doira, aralash qon).\n"
            "• <b>Reptiliya:</b> 3 kamerali (chala to‘siq; timsohda 4).\n"
            "• <b>Qush:</b> 4 kamerali (o‘ng aorta yoyi).\n"
            "• <b>Sutemizuvchi:</b> 4 kamerali (chap aorta yoyi)."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Yurak kameralari va qon aylanish doiralari evolutsiyasi"
    },
    {
        "id": "43",
        "title": "43-§. Hayvonlarning hazm qilish organlari evolutsiyasi",
        "text": (
            "📖 <b>43-§. HAZM QILISH ORGANLARI EVOLUTSIYASI</b>\n\n"
            "🔹 Hazm qilish sistemasi oziqni tutish, maydalash, kimyoviy parchalash va qonga so‘rish yo‘nalishida takomillashgan.\n\n"
            "🍽 <b>Hazm sistemasining asosiy evolutsion bosqichlari:</b>\n"
            "1. <b>Hujayra ichi hazmi:</b> Soxta oyoqlar orqali hazm vakuolalarida (Bir hujayralilar, G‘ovaktanlilar).\n"
            "2. <b>Berk hazm sistemasi:</b> Faqat og‘iz teshigi bor, anal teshigi yo‘q, hazm bo‘lmagan qoldiqlar yana og‘izdan chiqadi (Bo‘shliqichlilar, Yassi chuvalchanglar).\n"
            "3. <b>O‘tuvchi (orqali) hazm sistemasi:</b> Ilk bor <b>To‘garak chuvalchanglarda</b> paydo bo‘lgan: Og‘iz ➔ Qizilo‘ngach ➔ O‘rta ichak ➔ Orqa ichak ➔ Anal teshigi.\n"
            "4. <b>Hazm bezlarining shakllanishi:</b> Jigar va oshqozonosti bezi (Mollyuskalarda paydo bo‘lib, umurtqalilarda kuchli rivojlangan).\n\n"
            "🥩 <b>Umurtqali hayvonlar hazm traktining tabaqalanishi:</b>\n"
            "• Tishlar differensiallashuvi: Sutemizuvchilarda tishlar vazifasiga ko‘ra kurak, qoziq, kichik va katta oziq tishlarga ajralgan.\n"
            "• Qushlarda: Tishsiz muguz tumshuq, jig‘ildon, 2 bo‘limli oshqozon (bezli va muskulli tegirmon oshqozon).\n"
            "• Kavsh qaytaruvchi sutemizuvchilar: Murakkab 4 kamerali oshqozon (Qatqorin, To‘r qorin, Qat-qat qorin, Shirdon/haqiqiy oshqozon)."
        ),
        "guide": (
            "📘 <b>43-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Berk sistema:</b> Faqat og‘iz bor (gidra, planariya).\n"
            "• <b>Orqali sistema:</b> Anal teshigi paydo bo‘ldi (to‘garak chuvalchang).\n"
            "• <b>Bezlari:</b> Jigar va oshqozonosti bezi.\n"
            "• <b>Qushlar:</b> Jig‘ildon + Bezli va muskulli oshqozon.\n"
            "• <b>Kavsh qaytaruvchilar:</b> 4 kamerali (qatqorin, to‘rqorin, qat-qat, shirdon)."
        ),
        "media": "🎥 <b>Video dars:</b> Qushlar va kavsh qaytaruvchi hayvonlar hazm sistemasining anatomiyasi"
    },
    {
        "id": "44",
        "title": "44-§. Hayvonlarning ayirish va jinsiy organlari evolutsiyasi",
        "text": (
            "📖 <b>44-§. AYIRISH VA JINSIY ORGANLAR EVOLUTSIYASI</b>\n\n"
            "🚽 <b>Ayirish a'zolarining evolutsiyasi:</b>\n"
            "1. <b>Protonefridiylar:</b> Kiprikli «miltillovchi alangali» terminal hujayralar va tarmoqlangan naychalar (Yassi va to‘garak chuvalchanglar, lansetnik).\n"
            "2. <b>Metanefridiylar:</b> Har bir tana bo‘g‘imida voronkasimon tselomga ochiluvchi ayirish naychalari (Halqali chuvalchanglar).\n"
            "3. <b>Malpigi naychalari:</b> Tana bo‘shlig‘idan oqsil qoldiqlarini (siydik kislotani) quruq holda ichakka chiqaruvchi berk naychalar (O‘rgimchaksimonlar, Hasharotlar).\n"
            "4. <b>Buyraklarning umurtqalilardagi evolutsiyasi:</b>\n"
            "   • <i>Bosh (boshlang‘ich / bo‘yin) buyrak (Pronefros):</i> Lansetnik va umurtqalilar embrionida.\n"
            "   • <i>Tana (birlamchi) buyrak (Mezonefros):</i> Baliqlar va Amfibiyalarda (chala konsentratsiyalangan siydik).\n"
            "   • <i>Chanoq (ikkilamchi) buyrak (Metanefros):</i> Sudralib yuruvchilar, Qushlar va Sutemizuvchilarda (nefronlar, Genle halqasi, suvni qayta so‘rish — reabsorbsiya mexanizmi juda kuchli).\n\n"
            "🐣 <b>Jinsiy sistema va ko‘payish evolutsiyasi:</b>\n"
            "• Germafroditizmdan (bir jinslilikdan) ayrim jinslilikka o‘tish.\n"
            "• Tashqi urug‘lanishdan (suvda ro‘y beruvchi — baliq, amfibiya) ichki urug‘lanishga (quruqlikda — sudralib yuruvchi, qush, sutemizuvchi) o‘tish.\n"
            "• Tuxum qo‘yishdan tirik tug‘ish va platsenta orqali embrionni ona qornida oziqlantirishga o‘tish."
        ),
        "guide": (
            "📘 <b>44-§ QISQA QO‘LLANMASI:</b>\n"
            "• <b>Protonefridiylar:</b> Miltillovchi hujayrali naychalar (yassi chuvalchang).\n"
            "• <b>Metanefridiylar:</b> Voronkasimon naychalar (yomg‘ir chuvalchangi).\n"
            "• <b>Malpigi naychalari:</b> Hasharotlar (suvni tejovchi).\n"
            "• <b>Tana buyragi:</b> Baliq, amfibiya.\n"
            "• <b>Chanoq buyragi:</b> Sudralib yuruvchi, qush, sutemizuvchi (nefron).\n"
            "• <b>Ko‘payish:</b> Tashqi urug‘lanish ➔ Ichki urug‘lanish ➔ Tirik tug‘ish."
        ),
        "media": "🎥 <b>3D Animatsiya:</b> Umurtqali hayvonlar buyragi va nefron tuzilishining 3D modeli"
    }
]

# 11-sinf Video darslar ro'yxati
VIDEO_LESSONS_11: List[Dict[str, str]] = [
    {
        "id": "v11_1",
        "title": "Biologik tizimlar va ekologiya fanining predmeti",
        "duration": "12 daqiqa",
        "desc": "Tirik materiyaning tashkiliy darajalari va ekologiyaning asosiy vazifalari."
    },
    {
        "id": "v11_2",
        "title": "Biogeotsenoz va ekotizimlar: Produsent, konsument va redusentlar",
        "duration": "14 daqiqa",
        "desc": "Trofik zanjirlar, oziq to'rlari va biotsenoz tarkibiy qismlari."
    },
    {
        "id": "v11_3",
        "title": "Ekologik omillar: Yorug'lik, harorat va namlik qonuniyatlari",
        "duration": "15 daqiqa",
        "desc": "Libixning minimum qoidasi, Shelford qoidasi, Bergmann va Allen qoidalari."
    },
    {
        "id": "v11_4",
        "title": "Turning populatsion strukturasi va dinamikasi",
        "duration": "11 daqiqa",
        "desc": "Populyatsiya zichligi, yosh va jinsiy strukturasi, hayot to'lqinlari."
    },
    {
        "id": "v11_5",
        "title": "Ekologik piramidalar: Lindeman 10% qoidasi",
        "duration": "13 daqiqa",
        "desc": "Sonlar, biomassa va energiya piramidalari tahlili hamda masalalar."
    },
    {
        "id": "v11_6",
        "title": "Biosfera haqida V.I.Vernadskiy ta'limoti va chegaralari",
        "duration": "16 daqiqa",
        "desc": "Tirik modda xususiyatlari, biosferadagi biogeokimyoviy funksiyalar."
    },
    {
        "id": "v11_7",
        "title": "Biogeokimyoviy sikllar: Suv, uglerod va azot aylanishi",
        "duration": "14 daqiqa",
        "desc": "Katta va kichik aylanma, inson faoliyatining sikllarga ta'siri."
    },
    {
        "id": "v11_8",
        "title": "Organik olam filogenezi va dalillari",
        "duration": "12 daqiqa",
        "desc": "Gomologik va analogik a'zolar, rudimentlar, atavizmlar va biogenetik qonun."
    },
    {
        "id": "v11_9",
        "title": "O'simliklar vegetativ va generativ a'zolari filogenezi",
        "duration": "15 daqiqa",
        "desc": "Telom nazariyasi, urug' va gulning kelib chiqishi, qo'sh urug'lanish."
    },
    {
        "id": "v11_10",
        "title": "Hayvonlar qon aylanish va nerv sistemalari evolutsiyasi",
        "duration": "18 daqiqa",
        "desc": "Diffuzdan bosh miya po'stlog'igacha, 2 kamerali yurakdan 4 kamerali yurakkacha."
    }
]

# 11-sinf 3D Animatsiyalar ro'yxati
ANIMATIONS_3D_11: List[Dict[str, str]] = [
    {
        "id": "a11_1",
        "title": "Biogeotsenozning fazoviy 3D modeli",
        "desc": "Abiotik muhit (ekotop) va biotsenoz tarkibidagi modda oqimining 3D tasviri."
    },
    {
        "id": "a11_2",
        "title": "Yaylov va detrit oziq zanjirlari modeli (3D)",
        "desc": "Produsentdan yuqori tartib konsumentlargacha trofik pog'onalarning fazoviy o'zaro ta'siri."
    },
    {
        "id": "a11_3",
        "title": "Energiya piramidasi va 10% qoidasi (3D)",
        "desc": "Har bir pog'onada energiyaning 90% issiqlik bo'lib yo'qolishi va 10% o'tish dinamikasi."
    },
    {
        "id": "a11_4",
        "title": "Biosferaning global chegaralari (3D Yer modeli)",
        "desc": "Ozon ekrani, Dunyo okeani chuqurliklari va litosferadagi hayot chegaralari."
    },
    {
        "id": "a11_5",
        "title": "Uglerod va azotning biogeokimyoviy sikli (3D)",
        "desc": "Atmosfera, o'simliklar, hayvonlar va tuproq bakteriyalari orqali atomlar harakati."
    },
    {
        "id": "a11_6",
        "title": "Gulli o'simliklarda qo'sh urug'lanish (3D)",
        "desc": "Chang naychasining o'sishi, spermiylarning tuxum hujayra va markaziy hujayra bilan qo'shilishi."
    },
    {
        "id": "a11_7",
        "title": "Umurtqali hayvonlar yuragi va qon aylanish doiralari (3D)",
        "desc": "Baliq, baqa, kaltakesak, qush va sutemizuvchilar yuragi anatomiyasining qiyosiy evolutsiyasi."
    },
    {
        "id": "a11_8",
        "title": "Bosh miya bo'limlari evolutsiyasi (3D)",
        "desc": "Baliqlardan sutemizuvchilargacha bosh miya yarimsharlari po'stlog'i va burmalarining rivojlanishi."
    }
]
