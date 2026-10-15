"""
Biologiya o'quv materiallari: Mavzu ma'ruzalari, qisqa qo'llanmalar, video darslar va 3D animatsiyalar.
8-sinf va boshqa sinflar uchun boyitilgan darslik konspektlari (Barcha 61 ta mavzu to'liq kiritilgan).
"""

from typing import Dict, List, Any

# Mavzular ma'ruzalari, qo'llanmalar va multimedia
TOPICS_CONTENT: Dict[str, List[Dict[str, Any]]] = {
    "8": [
        {
            "id":  "1",
            "title":  "1-mavzu: Odam organizmi haqidagi fanlar",
            "text":  "📖 <b>1-MAVZU: ODAM ORGANIZMI HAQIDAGI FANLAR</b>\n\n🔹 Odam biologiyasi bir-biri bilan uzviy bog'liq uch fanni o'z ichiga oladi:\n• <b>Anatomiya:</b> Tana, organlar tuzilishi va joylashuvini o'rganadi.\n• <b>Fiziologiya:</b> Organlar va butun organizmning hayotiy faoliyati va vazifalarini o'rganadi.\n• <b>Gigiyena:</b> Sog'liqni saqlash va kasalliklarning oldini olish qoidalarini ishlab chiqadi.\n\n🏛 <b>Buyuk allomalar:</b> Abu Ali ibn Sino («Tib qonunlari»), Gippokrat, Abu Rayhon Beruniy.",
            "guide":  "📘 <b>1-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Anatomiya:</b> Shakl va tuzilish fani.\n• <b>Fiziologiya:</b> Jarayon va funksiyalar fani.\n• <b>Gigiyena:</b> Salomatlikni asrash va profilaktika.",
            "media":  "🎥 <b>Video dars:</b> Odam anatomiyasi va allomalar ta'limoti (10 daqiqa)"
        },
        {
            "id":  "2",
            "title":  "2-mavzu: Odam tanasining umumiy tuzilishi va hujayra organoidlari",
            "text":  "📖 <b>2-MAVZU: ODAM TANASINING UMUMIY TUZILISHI VA HUJAYRA</b>\n\n🔹 Hujayra — organizmning eng kichik tirik tuzilish va funksional birligidir.\n• <b>Yadro:</b> Irsiyat markazi, xromosoma va DNK saqlanadi.\n• <b>Mitoxondriya:</b> Energiya (ATF) hosil qiluvchi organoid.\n• <b>Ribosoma:</b> Oqsil sintezlaydi.\n• <b>Lizosoma:</b> Hujayra ichki hazm a'zosi.\n• <b>Golji majmuasi:</b> Moddalarni to'plash va saralash markazi.",
            "guide":  "📘 <b>2-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Yadro:</b> Boshqaruv va irsiyat.\n• <b>Mitoxondriya:</b> Hujayra elektrostansiyasi.\n• <b>Ribosoma:</b> Oqsil fabrikasi.",
            "media":  "🎥 <b>3D Animatsiya:</b> Hujayra organoidlarining 3D tuzilishi va harakati"
        },
        {
            "id":  "3",
            "title":  "3-mavzu: Hujayraning kimyoviy tarkibi va moddalar almashinuvi",
            "text":  "📖 <b>3-MAVZU: HUJAYRANING KIMYOVIY TARKIBI VA METABOLIZM</b>\n\n🔹 Hujayrada suv (70-80%), oqsillar (10-20%), yog'lar (1-5%), uglevodlar (0.2-2%) mavjud.\n• <b>Assimilatsiya (Anabolizm):</b> Moddalar sintezlanishi va to'planishi (energiya sarflanadi).\n• <b>Dissimilyatsiya (Katabolizm):</b> Murakkab moddalarning parchalanishi va ATF ajralishi.",
            "guide":  "📘 <b>3-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Anabolizm:</b> Oddiydan murakkab modda sintezi.\n• <b>Katabolizm:</b> Parchalanish va energiya hosil bo'lishi.",
            "media":  "🎥 <b>Video dars:</b> Hujayradagi kimyoviy reaksiyalar va ATF aylanishi"
        },
        {
            "id":  "4",
            "title":  "4-mavzu: To'qimalar (epiteliy, biriktiruvchi, muskul, nerv)",
            "text":  "📖 <b>4-MAVZU: TO'QIMALAR VA ULARNING TURLARI</b>\n\n🔹 To'qima — kelib chiqishi, tuzilishi va vazifasi o'xshash hujayralar to'plamidir.\n1. <b>Epiteliy:</b> Teri usti, ichki organlar shilliq pardasini qoplovchi himoya to'qimasi.\n2. <b>Biriktiruvchi:</b> Qon, limfa, suyak, tog'ay, yog' to'qimalari (hujayralararo moddasi ko'p).\n3. <b>Muskul:</b> Silliq, ko'ndalang-targ'il skelet va yurak muskuli.\n4. <b>Nerv:</b> Neyronlar va neyrogliya (qo'zg'aluvchanlik va o'tkazuvchanlik).",
            "guide":  "📘 <b>4-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Epiteliy:</b> Himoya va ajratish.\n• <b>Biriktiruvchi:</b> Suyak, qon, pay (tayanch).\n• <b>Muskul:</b> Qisqaruvchanlik.\n• <b>Nerv:</b> Impuls o'tkazish.",
            "media":  "🎥 <b>Video dars:</b> Mikroskop ostida to'qimalar tahlili (8 daqiqa)"
        },
        {
            "id":  "5",
            "title":  "5-mavzu: Gumoral boshqarilish va gormonlar haqida tushuncha",
            "text":  "📖 <b>5-MAVZU: GUMORAL BOSHQARILISH VA GORMONLAR</b>\n\n🔹 Organizm boshqarilishida nerv va gumoral (suyuqlik orqali) tizimlar hamkorlik qiladi.\n• <b>Endokrin bezlar:</b> Chiqaruv nayisiz, gormonlarini to'g'ridan-to'g'ri qonga chiqaradi.\n• <b>Gormonlar:</b> Yuqori biologik faol moddalar, moddalar almashinuvini, o'sishni va rivojlanishni boshqaradi.",
            "guide":  "📘 <b>5-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Gumor:</b> Qon, limfa, to'qima suyuqligi.\n• <b>Gormon xususiyati:</b> Kichik konsentratsiyada ham kuchli ta'sir ko'rsatadi.",
            "media":  "🎥 <b>Video dars:</b> Endokrin tizim va gormonlar ishlash mexanizmi"
        },
        {
            "id":  "6",
            "title":  "6-mavzu: Gipofiz va qalqonsimon bez",
            "text":  "📖 <b>6-MAVZU: GIPOFIZ VA QALQONSIMON BEZ</b>\n\n🔹 <b>Gipofiz:</b> Bosh miya ostida joylashgan boshliq bez (0.5 g). Somatotrop (o'sish gormoni) ishlab chiqaradi.\n• Giperfunsiyasi: <b>Gigantizm</b> (bolalarda), <b>Akromegaliya</b> (kattalarda).\n• Gipofunsiyasi: <b>Mittilik (nanizm)</b>.\n\n🔹 <b>Qalqonsimon bez:</b> Tiroksin (yodli) gormoni.\n• Gipofunsiyasi: <b>Kretinizm</b> (bolalarda), <b>Miksedema</b> (kattalarda), <b>Endemik buqoq</b> (yod tanqisligida).\n• Giperfunsiyasi: <b>Bazedov kasalligi</b>.",
            "guide":  "📘 <b>6-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Somatotrop:</b> Gipofiz o'sish gormoni.\n• <b>Tiroksin:</b> Yodli gormon (qalqonsimon bez).\n• <b>Kretinizm:</b> Aqliy va jismoniy zaiflik.",
            "media":  "🎥 <b>3D Animatsiya:</b> Gipofiz va qalqonsimon bezning anatomik tuzilishi"
        },
        {
            "id":  "7",
            "title":  "7-mavzu: Qalqonoldi, ayrisimon va buyrakusti bezlari",
            "text":  "📖 <b>7-MAVZU: QALQONOLDI, TIMUS VA BUYRAKUSTI BEZLARI</b>\n\n🔹 <b>Qalqonoldi bezlari (4 ta):</b> <b>Paratgormon</b> — qonda kalsiy va fosfor almashinuvini boshqaradi.\n🔹 <b>Ayrisimon bez (Timus):</b> T-limfotsitlarni yetiltirib, immunitetni shakllantiradi.\n🔹 <b>Buyrakusti bezlari:</b>\n• Po'stloq qavati: Kortikosteroidlar (tuz-suv balansi).\n• Mag'iz qavati: <b>Adrenalin va noradrenalin</b> (yurakni tezlashtiradi, bosimni oshiradi).",
            "guide":  "📘 <b>7-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Paratgormon:</b> Kalsiy miqdori.\n• <b>Timus:</b> Immunitet va T-hujayralar.\n• <b>Adrenalin:</b> 'Qo'rquv va kurash' gormoni.",
            "media":  "🎥 <b>Video dars:</b> Adrenalinning stress holatidagi ta'siri (7 daqiqa)"
        },
        {
            "id":  "8",
            "title":  "8-mavzu: Me'daosti bezi va jinsiy bezlar",
            "text":  "📖 <b>8-MAVZU: ME'DAOSTI BEZI VA JINSIY BEZLAR</b>\n\n🔹 <b>Me'daosti bezi (Aralash bez):</b>\n• Tashqi sekretsiya: Hazm shirasi (tripsin, amilaza, lipaza).\n• Ichki sekretsiya: <b>Insulin</b> (qondagi glyukozani kamaytiradi) va <b>Glyukagon</b> (oshiradi).\n• Insulin yetishmasa — <b>qandli diabet</b>.\n\n🔹 <b>Jinsiy bezlar:</b> Urug'donlar (testosteron) va tuxumdonlar (estrogen).",
            "guide":  "📘 <b>8-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Insulin:</b> Qondagi qandni normallashtiradi.\n• <b>Qandli diabet:</b> Insulin tanqisligi oqibati.\n• <b>Testosteron va estrogen:</b> Jinsiy gormonlar.",
            "media":  "🎥 <b>Video dars:</b> Oshqozonosti bezi va qandli diabet tahlili"
        },
        {
            "id":  "9",
            "title":  "9-mavzu: Skeletning ahamiyati va suyaklarning tuzilishi",
            "text":  "📖 <b>9-MAVZU: SKELET VA SUYAKLARNING TUZILISHI</b>\n\n🔹 Skelet tayanch, himoya va harakat funksiyalarini bajaradi (206 dan ortiq suyak).\n• <b>Ossein (organik):</b> Suyakka elastiklik va qayishqoqlik beradi.\n• <b>Mineral tuzlar (anorganik):</b> Kalsiy va fosfor suyakka qattiqlik beradi.\n• <b>Suyakusti pardasi (periost):</b> Suyakning eniga o'sishi va sinishda bitishini ta'minlaydi. Bo'yiga o'sish tog'aylar hisobiga kechadi.",
            "guide":  "📘 <b>9-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Ossein:</b> Egiluvchanlik.\n• <b>Kalsiy/fosfor:</b> Mustahkamlik.\n• <b>Periost:</b> Eniga o'sish va oziqlanish.",
            "media":  "🎥 <b>3D Animatsiya:</b> Suyak to'qimasi osteonlari va periost qavati"
        },
        {
            "id":  "10",
            "title":  "10-mavzu: Suyaklarning birikishi: bo'g'imlar va tog'aylar",
            "text":  "📖 <b>10-MAVZU: SUYAKLARNING BIRIKISHI: BO'G'IMLAR</b>\n\n🔹 Suyaklar 3 xil birikadi:\n1. <b>Harakatsiz:</b> Kalla suyagi choklari, chanoq suyaklari.\n2. <b>Yarim harakatchan:</b> Umurtqalararo tog'ay disklari, qovurg'a-to'sh birikishi.\n3. <b>Harakatchan (Bo'g'imlar):</b> Yelka, tirsak, tizza bo'g'imlari.\n• Bo'g'im qismlari: Bo'g'im boshi, chuqurchasi, tog'ayi, bo'g'im xaltasi va bo'g'im suyuqligi (ishqalanishni kamaytiradi).",
            "guide":  "📘 <b>10-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Harakatsiz:</b> Kalla choklari.\n• <b>Yarim harakatchan:</b> Umurtqa disklari.\n• <b>Bo'g'im:</b> Harakatchan birikish.",
            "media":  "🎥 <b>Video dars:</b> Bo'g'imlar biomexanikasi va bo'g'im suyuqligi roli"
        },
        {
            "id":  "11",
            "title":  "11-mavzu: Kalla, tana va qo'l-oyoq skeleti",
            "text":  "📖 <b>11-MAVZU: KALLA, TANA VA QO'L-OYOQ SKELETI</b>\n\n🔹 <b>Kalla skeleti:</b> Miya bo'limi (peshona, ensa, tepa, chakka) va yuz bo'limi (jag'lar, burun, yonoq).\n🔹 <b>Tana skeleti:</b>\n• Umurtqa pog'onasi (33-34 ta umurtqa): Bo'yin (7), ko'krak (12), bel (5), dumg'aza (5), dum (4-5).\n• Ko'krak qafasi: 12 juft qovurg'a va to'sh suyagi.\n🔹 <b>Qo'l va oyoq skeleti:</b> Kamar (yelka, chanoq) va erkin suyaklar.",
            "guide":  "📘 <b>11-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Bo'yin umurtqalari:</b> Barcha sutemizuvchilarda 7 ta.\n• <b>Qovurg'alar:</b> 12 juft (7 chin, 3 soxta, 2 yetim).",
            "media":  "🎥 <b>3D Animatsiya:</b> Odam skeletining 3D interaktiv modeli"
        },
        {
            "id":  "12",
            "title":  "12-mavzu: Muskullarning tuzilishi va turlari",
            "text":  "📖 <b>12-MAVZU: MUSKULLARNING TUZILISHI VA TURLARI</b>\n\n🔹 Muskullar tana vaznining 40% ini tashkil qiladi (600 dan ortiq muskul).\n• Qisqaruvchi oqsillar: <b>Aktin</b> va <b>Miozin</b>.\n• Tuzilishi: Muskul qorinchasi (tutamlar) va paylar (suyakka birikadi).\n• Muskul turlari: <b>Skelet</b> (ko'ndalang-targ'il, ixtiyoriy), <b>Silliq</b> (ichki organlarda, ixtiyorsiz), <b>Yurak muskuli</b> (avtomatizmga ega).",
            "guide":  "📘 <b>12-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Aktin va miozin:</b> Qisqarish oqsillari.\n• <b>Sinergistlar:</b> Birgalikda ishlovchi muskullar.\n• <b>Antagonistlar:</b> Qarama-qarshi ishlovchi (bukuvchi/yozuvchi).",
            "media":  "🎥 <b>Video dars:</b> Muskul tolalari va mushak kuchi fizikasi"
        },
        {
            "id":  "13",
            "title":  "13-mavzu: Muskullar ishi, toliqishi va qaddi-qomat gigiyenasi",
            "text":  "📖 <b>13-MAVZU: MUSKULLAR ISHI VA QADDI-QOMAT GIGIYENASI</b>\n\n🔹 <b>Muskul ishi:</b> Dinamik (harakatli) va Statik (yukni ushlab turish).\n• <b>I.M. Sechenov:</b> Faol dam olish toliqishni tez yo'qotishini isbotlagan.\n🔹 <b>Qad-qomat:</b> Noto'g'ri o'tirishdan <b>skolioz</b> (umurtqaning yon tomonga qiyshayishi), tor poyabzal kiyishdan <b>yassioyoqlik</b> kelib chiqadi.",
            "guide":  "📘 <b>13-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Sechenov:</b> Faol dam olish qoidasi.\n• <b>Skolioz:</b> Umurtqa egriligi.\n• <b>Yassioyoqlik:</b> Oyoq gumbazi yassilanishi.",
            "media":  "🎥 <b>Video dars:</b> Skolioz profilaktikasi va qad-qomat mashqlari"
        },
        {
            "id":  "14",
            "title":  "14-mavzu: Organizmning ichki muhiti va gomeostaz",
            "text":  "📖 <b>14-MAVZU: ORGANIZMNING ICHKI MUHITI VA GOMEOSTAZ</b>\n\n🔹 Organizmning ichki muhiti: <b>Qon, limfa va to'qima suyuqligi</b>.\n• Qon tomirlar orqali oqadi, to'qima suyuqligi hujayralarni o'rab turadi, limfa limfa tomirlarida harakatlanadi.\n• <b>Gomeostaz:</b> Ichki muhit ko'rsatkichlarining (harorat, bosim, pH) turg'unligi va doimiyligidir.",
            "guide":  "📘 <b>14-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Ichki muhit:</b> Qon + Limfa + To'qima suyuqligi.\n• <b>Gomeostaz:</b> Turg'unlik saqlanishi.",
            "media":  "🎥 <b>Video dars:</b> Gomeostaz va organizm ichki suyuqliklari balansi"
        },
        {
            "id":  "15",
            "title":  "15-mavzu: Qonning tarkibi va qon plazmasi",
            "text":  "📖 <b>15-MAVZU: QONNING TARKIBI VA PLAZMASI</b>\n\n🔹 Odamda 4.5-5 litr qon bo'ladi.\n• Qon 2 qismdan iborat: <b>Plazma (55%)</b> va <b>Shaklli elementlar (45%)</b>.\n• <b>Plazma:</b> 90-92% suv, 7-8% oqsillar (albumin, globulin, fibrinogen), 0.9% tuzlar, 0.1% glyukoza.\n• Fibrinogensiz plazma — <b>qon zardobi (serum)</b> deyiladi.",
            "guide":  "📘 <b>15-MAVZU QISQA QO'LLANMASI:</b>\n• <b>Plazma:</b> 55% suyuq qism.\n• <b>Qon zardobi:</b> Fibrinogensiz plazma.\n• <b>Glyukoza:</b> 0.1% (normada).",
            "media":  "🎥 <b>Video dars:</b> Qon plazmasi va gematologik tahlillar"
        },
        {
            "id":  "16",
            "title":  "16-mavzu: Qonning shaklli elementlari: Eritrotsitlar va gemoglobin",
            "text":  "📖 <b>16-MAVZU: ERITROTSITLAR VA GEMOGLOBIN</b>\n\n🔹 <b>Eritrotsitlar:</b> Ikki tomoni botiq disk shaklidagi yadrosiz qizil qon hujayralari.\n• 1 mm³ qonda: Erkaklarda 4.5-5 mln, ayollarda 4-4.5 mln.\n• Yashash davri: 120 kun (suyak qizil iligida hosil bo'ladi, taloq va jigarda parchalanadi).\n• <b>Gemoglobin:</b> Kislorod bilan <b>oksigemoglobin</b>, is gazi bilan <b>karboksigemoglobin</b> hosil qiladi.",
            "guide":  "📘 <b>16-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Eritrotsit:</b> 120 kun, yadrosiz disk.\n• <b>Gemoglobin:</b> Temirli oqsil.\n• <b>Anemiya:</b> Gemoglobin yoki eritrotsitlar kamayishi.",
            "media":  "🎥 <b>3D Animatsiya:</b> Eritrotsitlar harakati va gazlar almashinuvi"
        },
        {
            "id":  "17",
            "title":  "17-mavzu: Leykotsitlar, immunitet, trombotsitlar va qon guruhlari",
            "text":  "📖 <b>17-MAVZU: LEYKOTSITLAR, IMMUNITET VA QON GURUHLARI</b>\n\n🔹 <b>Leykotsitlar:</b> Yadroli oq qon tanachalari (1 mm³ qonda 6 000 - 8 000 ta). <b>Fagotsitoz</b> orqali mikroblarni yutadi (I.I. Mechnikov).\n🔹 <b>Trombotsitlar:</b> Qon plastinkalari, qon ivishini ta'minlaydi.\n🔹 <b>Qon guruhlari:</b> I(0), II(A), III(B), IV(AB). Rezus-faktor (Rh+ va Rh-).",
            "guide":  "📘 <b>17-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Mechnikov:</b> Fagotsitoz nazariyasi.\n• <b>I guruh:</b> Universal donor.\n• <b>IV guruh:</b> Universal retsipiyent.\n• <b>Trombotsit:</b> Qon ivishi.",
            "media":  "🎥 <b>Video dars:</b> Qon guruhlari va rezus-konflikt sabablari"
        },
        {
            "id":  "18",
            "title":  "18-mavzu: Yurakning joylashuvi, tuzilishi va kameralari",
            "text":  "📖 <b>18-MAVZU: YURAKNING JOYLAHSHUVI VA TUZILISHI</b>\n\n🔹 Yurak ko'krak qafasining chap tomonida joylashgan to'rt kamerali muskulli a'zodir (250-300 g).\n• Kameralar: 2 ta bo'lmacha va 2 ta qorincha.\n• O'ng qismida venoz qon, chap qismida arterial qon bo'ladi.\n• Klapanlar: Bo'lmacha-qorincha o'rtasida <b>tabaqali</b> (o'ngda 3, chapda 2 tabaqali), tomirlar chiqishida <b>yarimoysimon</b> klapanlar.",
            "guide":  "📘 <b>18-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>4 kamera:</b> 2 bo'lmacha + 2 qorincha.\n• <b>Chap qorincha devori:</b> Eng qalin muskul qavatiga ega.\n• <b>Klapanlar:</b> Qonni faqat bir tomonga yo'naltiradi.",
            "media":  "🎥 <b>3D Animatsiya:</b> Yurak kameralari va klapanlarining 3D anatomiyasi"
        },
        {
            "id":  "19",
            "title":  "19-mavzu: Yurakning ishlash davri va avtomatizmi",
            "text":  "📖 <b>19-MAVZU: YURAKNING ISHLASH DAVRI VA AVTOMATIZMI</b>\n\n🔹 Yurak sikli tinch holatda <b>0.8 sekund</b> davom etadi:\n1. Bo'lmachalar qisqarishi (sistola): 0.1 sekund.\n2. Qorinchalar qisqarishi (sistola): 0.3 sekund.\n3. Umumiy dam olish (diastola): 0.4 sekund.\n• <b>Avtomatizm:</b> Yurakning o'zida paydo bo'luvchi impulslar hisobiga ritmik qisqarish xususiyati.",
            "guide":  "📘 <b>19-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>0.8 sekund:</b> 0.1 s bo'lmacha + 0.3 s qorincha + 0.4 s pauza.\n• <b>Puls normada:</b> 70-75 marta minutiga.",
            "media":  "🎥 <b>Video dars:</b> Yurak avtomatizmi va elektr o'tkazuvchi tizimi"
        },
        {
            "id":  "20",
            "title":  "20-mavzu: Qon tomirlari: arteriyalar, venalar, kapillyarlar",
            "text":  "📖 <b>20-MAVZU: QON TOMIRLARI: ARTERIYALAR, VENALAR, KAPILLYARLAR</b>\n\n🔹 <b>Arteriyalar:</b> Qonni yurakdan a'zolarga tashiydi. Devori qalin, elastik (yuqori bosimga chidamli).\n🔹 <b>Venalar:</b> Qonni a'zolardan yurakka olib keladi. Klapanlarga ega (qon orqaga oqmasligi uchun).\n🔹 <b>Kapillyarlar:</b> Bir qavat yassi epiteliydan iborat mikroskopik tomirlar. Aynan shu yerda moddalar va gazlar almashinadi.",
            "guide":  "📘 <b>20-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Arteriya:</b> Qalin devorli, yurakdan chiquvchi.\n• <b>Vena:</b> Klapanli, yurakka keluvchi.\n• <b>Kapillyar:</b> Bir qavatli, moddalar almashinuvi.",
            "media":  "🎥 <b>Video dars:</b> Qon tomirlar tizimi va mikrosirkulyatsiya"
        },
        {
            "id":  "21",
            "title":  "21-mavzu: Katta va kichik qon aylanish doiralari",
            "text":  "📖 <b>21-MAVZU: KATTA VA KICHIK QON AYLANISH DOIRALARI</b>\n\n🔹 <b>Katta doira:</b>\n• Boshlanadi: <b>Chap qorinchadan</b> (aorta orqali).\n• Tugaydi: <b>O'ng bo'lmachada</b> (kovak venalar orqali).\n• Vaqti: 20-23 sekund. Butun tanani oziqlantiradi.\n🔹 <b>Kichik (o'pka) doirasi:</b>\n• Boshlanadi: <b>O'ng qorinchadan</b> (o'pka arteriyasi orqali venoz qon ketadi).\n• O'pkada O₂ ga to'yinadi.\n• Tugaydi: <b>Chap bo'lmachada</b> (o'pka venalari orqali arterial qon keladi).\n• Vaqti: 4-5 sekund.",
            "guide":  "📘 <b>21-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Katta doira:</b> Chap qorincha ➡️ Butun tana ➡️ O'ng bo'lmacha (23 s).\n• <b>Kichik doira:</b> O'ng qorincha ➡️ O'pka ➡️ Chap bo'lmacha (4-5 s).",
            "media":  "🎥 <b>3D Animatsiya:</b> Qon aylanish doiralarining to'liq 3D harakati"
        },
        {
            "id":  "22",
            "title":  "22-mavzu: Qon harakati, qon bosimi, puls va birinchi yordam",
            "text":  "📖 <b>22-MAVZU: QON BOSIMI, PULS VA BIRINCHI YORDAM</b>\n\n🔹 <b>Qon bosimi:</b> Normada 120/80 mm sim.ust. Sistolik (maksimal) va diastolik (minimal) bosim.\n🔹 <b>Puls:</b> Arteriya devorining tebranishi (60-80 marta/min).\n🔹 <b>Birinchi yordam:</b>\n• <b>Arterial qon ketganda:</b> Qip-qizil favvora. Jgut jarohatdan <b>yuqoriga</b> qo'yiladi (yozda 1.5-2 soat, qishda 1 soat).\n• <b>Venoz qon ketganda:</b> To'q qizil qon sizib oqadi. Bosuvchi bog'lam qo'yiladi.",
            "guide":  "📘 <b>22-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Norma:</b> 120/80 mm sim.ust.\n• <b>Arterial qon:</b> Jgut yuqoriga bog'lanadi.\n• <b>Venoz qon:</b> Bosuvchi bog'lam qo'yiladi.",
            "media":  "🎥 <b>Video dars:</b> Qon bosimini o'lchash va jgut bog'lash qoidalari"
        },
        {
            "id":  "23",
            "title":  "23-mavzu: Nafas olish a'zolari tuzilishi",
            "text":  "📖 <b>23-MAVZU: NAFAS OLISH A'ZOLARI TUZILISHI</b>\n\n🔹 Nafas yo'llari: <b>Burun bo'shlig'i ➡️ Halqum ➡️ Hiqildoq ➡️ Kekirdak ➡️ Bronxlar ➡️ O'pka</b>.\n• Burunda havo isitiladi, namlanadi va changlardan filtrlanadi.\n• Hiqildoq: Ovoz boylamlari joylashgan a'zo. Yutinganda hiqildoq usti tog'ayi nafas yo'lini yopadi.\n• Kekirdak: 16-20 ta tog'ay yarimhalqasidan iborat nay.",
            "guide":  "📘 <b>23-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Burun:</b> Isitadi, namlaydi, changdan tozalaydi.\n• <b>Hiqildoq:</b> Ovoz hosil qilish a'zosi.\n• <b>Kekirdak:</b> Tog'ay yarimhalqalari.",
            "media":  "🎥 <b>Video dars:</b> Nafas yo'llari anatomiyasi va ovoz apparati"
        },
        {
            "id":  "24",
            "title":  "24-mavzu: O'pkaning tuzilishi va alveolalar",
            "text":  "📖 <b>24-MAVZU: O'PKANING TUZILISHI VA ALVEOLALAR</b>\n\n🔹 O'pka ko'krak qafasida joylashgan juft a'zo. O'ng o'pka 3 bo'lakli, chap o'pka 2 bo'lakli.\n• Tashqaridan plevra pardasi bilan o'ralgan.\n• O'pkada 300-400 millionta <b>alveola (pufakcha)</b> bor. Ularning umumiy yuzasi 100 m² ga yetadi.\n• Alveola devori bir qavat yassi epiteliydan iborat bo'lib, kapillyarlar bilan o'ralgan.",
            "guide":  "📘 <b>24-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>O'pka:</b> O'ngda 3 bo'lak, chapda 2 bo'lak.\n• <b>Alveolalar:</b> 300-400 mln ta (yuzasi 100 m²).\n• <b>Plevra:</b> Ichida manfiy bosimli parda.",
            "media":  "🎥 <b>3D Animatsiya:</b> Alveola va kapillyar o'rtasida kislorod o'tishi"
        },
        {
            "id":  "25",
            "title":  "25-mavzu: Nafas olish mexanizmi va gazlar almashinuvi",
            "text":  "📖 <b>25-MAVZU: NAFAS HARAKATLARI VA GAZLAR ALMASHINUVI</b>\n\n🔹 <b>Nafas olish:</b> Qovurg'alararo tashqi muskullar va diafragma qisqaradi ➡️ Ko'krak qafasi kengayadi ➡️ Havo o'pkaga kiradi (faol jarayon).\n🔹 <b>Nafas chiqarish:</b> Muskullar bo'shashadi, ko'krak torayadi (passiv jarayon).\n🔹 <b>O'pkaning hayotiy sig'imi (O'HS):</b> Chuqur nafas olib, chuqur chiqarilgan havo hajmi (3.5-4.5 litr). Spirometr bilan o'lchanadi.",
            "guide":  "📘 <b>25-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Diafragma:</b> Nafas olishda pastga tushadi.\n• <b>Nafas soni:</b> 16-18 marta minutiga.\n• <b>Spirometr:</b> Hayotiy sig'imni o'lchaydi.",
            "media":  "🎥 <b>Video dars:</b> Nafas olish mexanikasi va spirometriya amaliyoti"
        },
        {
            "id":  "26",
            "title":  "26-mavzu: Hazm qilishning ahamiyati va hazm kanali tuzilishi",
            "text":  "📖 <b>26-MAVZU: HAZM SISTEMASI REJASI VA AHAMIYATI</b>\n\n🔹 Hazm qilish — oziq moddalarni qon va limfaga so'riladigan holatga keltirish.\n• <b>Hazm kanali (8-10 m):</b> Og'iz ➡️ Halqum ➡️ Qizilo'ngach (25 sm) ➡️ Oshqozon ➡️ Ingichka ichak ➡️ Yo'g'on ichak ➡️ To'g'ri ichak.\n• Devor qavatlari: Ichki shilliq, o'rta muskul, tashqi biriktiruvchi parda.",
            "guide":  "📘 <b>26-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Hazm kanali:</b> 8-10 metr.\n• <b>Qizilo'ngach:</b> 25 sm nay.\n• <b>Bosqichlar:</b> Mexanik maydalash va kimyoviy parchalash.",
            "media":  "🎥 <b>Video dars:</b> Hazm qilish sistemasi umumiy anatomik tuzilishi"
        },
        {
            "id":  "27",
            "title":  "27-mavzu: Og'iz bo'shlig'ida hazm bo'lishi (tishlar, so'lak bezlari)",
            "text":  "📖 <b>27-MAVZU: OG'IZ BO'SHLIG'IDA HAZM BO'LISHI</b>\n\n🔹 <b>Tishlar (32 ta):</b> 8 kurak, 4 qoziq, 8 kichik oziq, 12 katta oziq. Tuzilishi: toj, bo'yin, ildiz. Emal — tanadagi eng qattiq to'qima.\n🔹 <b>So'lak bezlari:</b> 3 juft yirik (quloqoldi, jag'osti, tilosti).\n• So'lak fermenti: <b>Amilaza (ptialin)</b> — uglevodlarni kraxmaldan glyukozagacha parchalaydi. <b>Lizotsim</b> mikroblarni o'ldiradi.",
            "guide":  "📘 <b>27-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>32 ta tish:</b> Emal, dentin, pulpa.\n• <b>Amilaza (ptialin):</b> Uglevodlarni parchalaydi.\n• <b>Lizotsim:</b> Bakteritsid (himoya).",
            "media":  "🎥 <b>3D Animatsiya:</b> Tish anatomiyasi va og'izda kraxmal parchalanishi"
        },
        {
            "id":  "28",
            "title":  "28-mavzu: Oshqozonda hazm bo'lishi va me'da shirasi",
            "text":  "📖 <b>28-MAVZU: OSHQOZONDA HAZM BO'LISHI</b>\n\n🔹 Oshqozon sig'imi 1.5-3 litr.\n• <b>Me'da shirasi:</b> 1.5-2 litr/sutka. Nordon muhit (pH 1.5-2.0).\n• <b>Xlorid kislota (HCl):</b> Pepsinni faollashtiradi, mikroblarni o'ldiradi.\n• <b>Pepsin:</b> Oqsillarni polipeptidlargacha parchalovchi asosiy ferment.\n• I.P. Pavlov 'soxta ovqatlantirish' tajribasida me'da sekretsiyasini o'rgangan.",
            "guide":  "📘 <b>28-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Pepsin:</b> Oqsillarni parchalaydi.\n• <b>HCl:</b> Nordon muhit (pH 1.5-2).\n• <b>Pavlov:</b> Me'da shirasi ajralish qonuniyatlari.",
            "media":  "🎥 <b>Video dars:</b> Oshqozonda kimyoviy hazm jarayoni"
        },
        {
            "id":  "29",
            "title":  "29-mavzu: Ichaklarda hazm bo'lishi. Jigar va o't suyuqligi",
            "text":  "📖 <b>29-MAVZU: ICHAKLARDA HAZM BO'LISHI VA JIGAR</b>\n\n🔹 <b>12 barmoqli ichak:</b> Ingichka ichakning boshlanish qismi (25-30 sm).\n• <b>Jigar (1.5 kg):</b> O't suyuqligi ishlab chiqaradi. O't yog'larni emulsiyalaydi va lipazani faollashtiradi.\n• <b>Me'daosti bezi:</b> Ishqoriy shira chiqaradi (tripsin — oqsil, amilaza — uglevod, lipaza — yog'ni parchalaydi).",
            "guide":  "📘 <b>29-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Jigar:</b> O't suyuqligi (yog'larni emulsiyalash).\n• <b>Me'daosti shirasi:</b> Tripsin, amilaza, lipaza.\n• <b>Ichak muhiti:</b> Ishqoriy.",
            "media":  "🎥 <b>Video dars:</b> Jigar vazifalari va ichakdagi hazm jarayoni"
        },
        {
            "id":  "30",
            "title":  "30-mavzu: Oziq moddalarning so'rilishi va hazm gigiyenasi",
            "text":  "📖 <b>30-MAVZU: SO'RILISH VA HAZM GIGIYENASI</b>\n\n🔹 <b>So'rilish:</b> Ingichka ichakdagi millionlab <b>vorsinkalar</b> orqali amalga oshadi.\n• <b>Qonga:</b> Aminokislotalar va glyukoza so'riladi.\n• <b>Limfaga:</b> Yog' kislotalari va glitserin so'riladi.\n🔹 <b>Yo'g'on ichak:</b> Suv qayta so'riladi, kletchatka bakteriyalar yordamida parchalanadi, B va K vitaminlari sintezlanadi, najas shakllanadi.",
            "guide":  "📘 <b>30-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Vorsinkalar:</b> So'rilish yuzasini oshiradi.\n• <b>Qonga:</b> Oqsil va uglevodlar.\n• <b>Limfaga:</b> Yog'lar.\n• <b>Yo'g'on ichak:</b> Suv so'rilishi va najas.",
            "media":  "🎥 <b>3D Animatsiya:</b> Ichak vorsinkalarida oziq moddalarning so'rilishi"
        },
        {
            "id":  "31",
            "title":  "31-mavzu: Oqsillar, yog'lar va uglevodlar almashinuvi",
            "text":  "📖 <b>31-MAVZU: OQSILLAR, YOG'LAR VA UGLEVODLAR ALMASHINUVI</b>\n\n🔹 <b>Oqsillar:</b> Tananing qurilish materiali. 1 g oqsil — <b>4.1 kkal (17.2 kJ)</b>. 8 ta aminokislota almashtirib bo'lmaydigan hisoblanadi.\n🔹 <b>Uglevodlar:</b> Asosiy energiya manbai. 1 g uglevod — <b>4.1 kkal</b>. Jigarda glikogen holida saqlanadi.\n🔹 <b>Yog'lar:</b> Eng yuqori energiya manbai. 1 g yog' — <b>9.3 kkal (38.9 kJ)</b> energiya beradi.",
            "guide":  "📘 <b>31-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>1 g Oqsil:</b> 4.1 kkal.\n• <b>1 g Uglevod:</b> 4.1 kkal.\n• <b>1 g Yog':</b> 9.3 kkal (eng ko'p energiya).\n• <b>Glikogen:</b> Jigardagi zaxira uglevod.",
            "media":  "🎥 <b>Video dars:</b> Oziq moddalarining energetik qiymati va masalalar"
        },
        {
            "id":  "32",
            "title":  "32-mavzu: Suv va mineral tuzlar almashinuvi. Energiya sarfi",
            "text":  "📖 <b>32-MAVZU: SUV VA MINERAL TUZLAR ALMASHINUVI</b>\n\n🔹 Odam kuniga 2-2.5 litr suv iste'mol qiladi. Suv erituvchi, harorat boshqaruvchisi va transport vositasidir.\n• <b>Kalsiy va fosfor:</b> Suyak va tish to'qimasi, qon ivishi va muskul qisqarishi.\n• <b>Temir (Fe):</b> Gemoglobin tarkibida kislorod tashiydi.\n• <b>Yod (I):</b> Qalqonsimon bez tiroksin gormoni uchun zarur.\n• <b>Kaliy va natriy:</b> Nerv impulsi o'tishi va osmotik bosim.",
            "guide":  "📘 <b>32-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Suv:</b> Kuniga 2-2.5 litr.\n• <b>Kalsiy:</b> Suyak va qon ivishi.\n• <b>Temir:</b> Qon gemoglobini.\n• <b>Yod:</b> Qalqonsimon bez.",
            "media":  "🎥 <b>Video dars:</b> Suv-tuz balansi va minerallar vazifasi"
        },
        {
            "id":  "33",
            "title":  "33-mavzu: Vitaminlar va ularning ahamiyati (A, B guruhi, C, D)",
            "text":  "📖 <b>33-MAVZU: VITAMINLAR VA ULARNING AHAMIYATI</b>\n\n🔹 Vitaminlar fermentlar tarkibiga kiradi (N.I. Lunin 1881-yilda kashf etgan).\n• <b>A vitamini:</b> Ko'rish. Yetishmasa — <b>shabko'rlik</b>.\n• <b>D vitamini:</b> Suyak mustahkamligi. Yetishmasa — bolalarda <b>raxit</b>.\n• <b>C vitamini:</b> Immunitet va tomirlar. Yetishmasa — <b>singa (tsinga)</b>.\n• <b>B1 vitamini:</b> Yetishmasa — <b>beri-beri</b> (asab falaji).\n• <b>B12 vitamini:</b> Qon yaratilishi.",
            "guide":  "📘 <b>33-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>A:</b> Shabko'rlik.\n• <b>D:</b> Raxit.\n• <b>C:</b> Singa (milklarning qonashi).\n• <b>B1:</b> Beri-beri kasalligi.",
            "media":  "🎥 <b>Video dars:</b> Vitaminlar dunyosi va gipovitaminoz oqibatlari"
        },
        {
            "id":  "34",
            "title":  "34-mavzu: Terining tuzilishi va qavatlari",
            "text":  "📖 <b>34-MAVZU: TERINING TUZILISHI VA QAVATLARI</b>\n\n🔹 Teri butun tanani qoplaydi (yuzasi 1.5-2 m²). 3 qavatdan iborat:\n1. <b>Epidermis (Ustki qavat):</b> Ko'p qavatli yassi epiteliy. Shoxlangan qavat va tirik o'suvchi qavat (melanin pigmenti teriga rang beradi). Qon tomiri yo'q.\n2. <b>Derma (Chin teri):</b> Biriktiruvchi to'qima. Retseptorlar, qon tomirlar, ter va yog' bezlari joylashgan.\n3. <b>Gipoderma (Teriosti yog' qavati):</b> Issiqlikni saqlash, zarbalarni yumshatish.",
            "guide":  "📘 <b>34-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Epidermis:</b> Melanin pigmenti, qon tomirsiz.\n• <b>Derma:</b> Retseptorlar, bezlar, tomirlar.\n• <b>Gipoderma:</b> Yog' zaxirasi.",
            "media":  "🎥 <b>3D Animatsiya:</b> Terining 3 qavati mikroskopik tuzilishi"
        },
        {
            "id":  "35",
            "title":  "35-mavzu: Terining funksiyalari va termoregulyatsiya",
            "text":  "📖 <b>35-MAVZU: TERI FUNKSIYALARI VA TERMOREGULYATSIYA</b>\n\n🔹 <b>Teri vazifalari:</b> Himoya, sezish, nafas (1-2%), ayirish (ter), termoregulyatsiya.\n• <b>Termoregulyatsiya:</b> Tana haroratini (36.6°C) doimiy saqlash.\n• Issiqda: Teri tomirlari kengayadi, ter ko'p ajraladi va bug'lanib tanani sovitadi.\n• Sovuqda: Tomirlar torayadi, muskullar qaltirab issiqlik hosil qiladi.",
            "guide":  "📘 <b>35-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Markaz:</b> Gipotalamusda.\n• <b>Terlash:</b> Issiqlik chiqarishning asosiy mexanizmi.\n• <b>Chiniqish:</b> Tomirlarning haroratga tez moslashuvi.",
            "media":  "🎥 <b>Video dars:</b> Tana haroratini boshqarish va chiniqish"
        },
        {
            "id":  "36",
            "title":  "36-mavzu: Ayirish organlari: buyraklar tuzilishi",
            "text":  "📖 <b>36-MAVZU: AYIRISH ORGANLARI: BUYRAKLAR</b>\n\n🔹 Ayirish organlari: <b>Buyraklar (juft), siydik yo'li naylari, qovuq va siydik chiqarish kanali</b>.\n• <b>Buyraklar:</b> Bel sohasida joylashgan loviyasimon a'zo (har biri 150 g).\n• Kesimida: Tashqi to'qroq <b>po'stloq qavat</b> va ichki ochroq <b>mag'iz qavat</b> (piramidalar) hamda buyrak jomi mavjud.",
            "guide":  "📘 <b>36-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Buyrak:</b> Juft a'zo (har biri 150 g).\n• <b>Tuzilishi:</b> Po'stloq, mag'iz, jom.\n• <b>Vazifasi:</b> Qonni tozalash va siydik hosil qilish.",
            "media":  "🎥 <b>Video dars:</b> Buyraklar anatomiyasi va qon ta'minoti"
        },
        {
            "id":  "37",
            "title":  "37-mavzu: Nefron tuzilishi. Birlamchi va ikkilamchi siydik",
            "text":  "📖 <b>37-MAVZU: NEFRON VA SIYDIK HOSIL BO'LISHI</b>\n\n🔹 <b>Nefron:</b> Buyrakning mikroskopik birligi (1-1.2 millionta). Bovmen kapsulasi (kapillyar kalavasi) va egri-bugri naychalardan iborat.\n💧 <b>2 bosqich:</b>\n1. <b>Filtratsiya:</b> Kapsulada qon plazmasi filtrlanib, <b>birlamchi siydik (150-170 litr/sutka)</b> hosil bo'ladi.\n2. <b>Reabsorbsiya:</b> Naychalarda suv va foydali moddalar qonga qayta so'riladi. Natijada <b>ikkilamchi siydik (1.5 litr)</b> hosil bo'ladi.",
            "guide":  "📘 <b>37-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Nefron:</b> Buyrak filtri.\n• <b>Birlamchi siydik:</b> 150-170 l (filtratsiya).\n• <b>Ikkilamchi siydik:</b> 1.5 l (reabsorbsiya).",
            "media":  "🎥 <b>3D Animatsiya:</b> Nefronda filtratsiya va reabsorbsiya jarayoni"
        },
        {
            "id":  "38",
            "title":  "38-mavzu: Siydik chiqarish a'zolari va ayirish gigiyenasi",
            "text":  "📖 <b>38-MAVZU: SIYDIK CHIQARISH VA AYIRISH GIGIYENASI</b>\n\n🔹 Ikkilamchi siydik naylar orqali <b>qovuqqa</b> tushadi (sig'imi 500 ml). 200-300 ml to'planganda chiqarish refleksi uyg'onadi.\n⚠️ <b>Kasalliklar:</b>\n• <b>Nefrit:</b> Buyrak yallig'lanishi (angina asorati).\n• <b>Urolitiaz:</b> Buyrakda tosh paydo bo'lishi (sho'r, achchiq ovqatlar, qattiq suv ta'sirida).",
            "guide":  "📘 <b>38-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Qovuq:</b> 500 ml sig'imli muskulli xalta.\n• <b>Nefrit:</b> Yallig'lanish kasalligi.\n• <b>Profilaktika:</b> Shamollashni davolash, spirtli ichimlikdan tiyilish.",
            "media":  "🎥 <b>Video dars:</b> Buyrak toshlari hosil bo'lishi va profilaktika"
        },
        {
            "id":  "39",
            "title":  "39-mavzu: Nerv sistemasining ahamiyati va tuzilish rejasi",
            "text":  "📖 <b>39-MAVZU: NERV SISTEMASINING AHAMIYATI VA REJASI</b>\n\n🔹 Nerv sistemasi barcha a'zolar ishini o'zaro bog'laydi va organizmni tashqi muhitga moslashtiradi.\n• <b>MNS (Markaziy):</b> Bosh miya va orqa miya.\n• <b>PNS (Periferik):</b> Nervlar (12 juft kalla, 31 juft orqa miya), tugunlar va retseptorlar.\n• <b>Somatik:</b> Skelet muskullari (ixtiyoriy).\n• <b>Vegetativ:</b> Ichki a'zolar (ixtiyorsiz).",
            "guide":  "📘 <b>39-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>MNS:</b> Bosh miya + Orqa miya.\n• <b>PNS:</b> Nervlar va tugunlar.\n• <b>Somatik:</b> Harakat muskullari.\n• <b>Vegetativ:</b> Ichki a'zolar.",
            "media":  "🎥 <b>Video dars:</b> Nerv sistemasining umumiy tuzilishi"
        },
        {
            "id":  "40",
            "title":  "40-mavzu: Neyron, sinaps va refleks yoyi",
            "text":  "📖 <b>40-MAVZU: NEYRON, SINAPS VA REFLEKS YOYI</b>\n\n🔹 <b>Neyron:</b> Tana, dendritlar (impulsni keltiradi) va bitta akson (impulsni olib ketadi).\n• <b>Sinaps:</b> Neyronlar tutashgan joy (mediatorlar orqali impuls o'tadi).\n🔄 <b>Refleks yoyi 5 qismdan iborat:</b>\n1. Retseptor ➡️ 2. Sezuvchi nerv ➡️ 3. Markaz (MNS) ➡️ 4. Harakatlantiruvchi nerv ➡️ 5. Ishchi a'zo (muskul/bez).",
            "guide":  "📘 <b>40-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Dendrit:</b> Qabul qiladi.\n• <b>Akson:</b> Uzatadi.\n• <b>Sinaps:</b> Aloqa nuqtasi.\n• <b>Refleks yoyi:</b> 5 ta zanjir.",
            "media":  "🎥 <b>3D Animatsiya:</b> Neyron bo'ylab elektr impulsi va sinaps ishlashi"
        },
        {
            "id":  "41",
            "title":  "41-mavzu: Orqa miyaning tuzilishi va funksiyalari",
            "text":  "📖 <b>41-MAVZU: ORQA MIYANING TUZILISHI VA VAZIFALARI</b>\n\n🔹 Orqa miya umurtqa kanalida joylashgan (42-45 sm, 30 g).\n• Kesimida: Ichkarida <b>kulrang modda</b> (kapalak shaklida) va tashqarida <b>oq modda</b> (o'tkazuvchi yo'llar).\n• Orqa miyadan <b>31 juft nerv</b> chiqadi.\n• Vazifalari: <b>Reflektor</b> (tizza refleksi, siydik chiqarish) va <b>O'tkazuvchi</b> (miya bilan aloqa).",
            "guide":  "📘 <b>41-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Uzunligi:</b> 42-45 sm, 31 juft nerv.\n• <b>Kulrang modda:</b> Ichkarida (neyron tanalari).\n• <b>Oq modda:</b> Tashqarida (tolalar).",
            "media":  "🎥 <b>Video dars:</b> Orqa miya anatomiyasi va tizza refleksi"
        },
        {
            "id":  "42",
            "title":  "42-mavzu: Bosh miya poyasi: uzunchoq miya, miyacha va o'rta miya",
            "text":  "📖 <b>42-MAVZU: BOSHM MIYA POYASI VA MIYACHA</b>\n\n🔹 Bosh miya og'irligi 1300-1400 g.\n• <b>Uzunchoq miya:</b> Hayotiy markazlar joylashgan: <b>nafas, yurak, qon bosimi, himoya reflekslari (yo'tal, aksa, qusish)</b>. Zararlansa odam darhol halok bo'ladi.\n• <b>Miyacha:</b> Harakatlar koordinatsiyasi, muvozanat va muskul tonusi markazi.\n• <b>O'rta miya:</b> Ko'rish va eshitishga burilish birlamchi reflekslari markazi.",
            "guide":  "📘 <b>42-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Uzunchoq miya:</b> Nafas, yurak, yutish (hayotiy markaz).\n• <b>Miyacha:</b> Muvozanat va koordinatsiya.\n• <b>O'rta miya:</b> Ko'rish-eshitish yo'naltiruvchi refleksi.",
            "media":  "🎥 <b>3D Animatsiya:</b> Bosh miya poyasi va miyacha tuzilishi"
        },
        {
            "id":  "43",
            "title":  "43-mavzu: Oraliq miya va bosh miya yarim sharlari po'stlog'i",
            "text":  "📖 <b>43-MAVZU: ORALIQ MIYA VA KATTA YARIM SHARLAR</b>\n\n🔹 <b>Oraliq miya:</b>\n• <b>Talamus:</b> Barcha sezgi impulslari saralanadigan markaz.\n• <b>Gipotalamus:</b> Vegetativ markaz (harorat, ochlik, to'qlik, chanqoq, gormonlar).\n🧠 <b>Katta yarim sharlar po'stlog'i (burmali, 2200-2500 sm²):</b>\n• Peshona: Tafakkur, iroda, xulq, nutq.\n• Tepa: Teri va muskul sezgilari.\n• Ensa: Ko'rish markazi.\n• Chakka: Eshitish va hid markazi.",
            "guide":  "📘 <b>43-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Gipotalamus:</b> Tana harorati va gomeostaz.\n• <b>Ensa bo'lagi:</b> Ko'rish.\n• <b>Chakka bo'lagi:</b> Eshitish.\n• <b>Peshona bo'lagi:</b> Tafakkur va iroda.",
            "media":  "🎥 <b>Video dars:</b> Katta yarim sharlar xaritasi va po'stloq zonalari"
        },
        {
            "id":  "44",
            "title":  "44-mavzu: Vegetativ (simpatik va parasimpatik) nerv sistemasi",
            "text":  "📖 <b>44-MAVZU: VEGETATIV NERV SISTEMASI</b>\n\n🔹 Ichki organlar, qon tomirlar va bezlar ishini boshqaruvchi ixtiyorsiz sistema. 2 qismdan iborat:\n1. <b>Simpatik sistema (Stress va xavf):</b> Yurakni tezlashtiradi, bosimni oshiradi, bronxlarni kengaytiradi, hazmni sekinlashtiradi.\n2. <b>Parasimpatik sistema (Dam olish):</b> Yurakni sekinlashtiradi, bosimni pasaytiradi, hazm shirasi ajralishini kuchaytiradi.",
            "guide":  "📘 <b>44-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Simpatik:</b> Yurakni tezlatadi, hazmni to'xtatadi.\n• <b>Parasimpatik:</b> Yurakni sekinlatadi, hazmni kuchaytiradi.\n• <b>Markaz:</b> Gipotalamusda.",
            "media":  "🎥 <b>Video dars:</b> Simpatik va parasimpatik sistemalar qarama-qarshiligi"
        },
        {
            "id":  "45",
            "title":  "45-mavzu: Nerv sistemasi gigiyenasi va kasalliklari",
            "text":  "📖 <b>45-MAVZU: NERV SISTEMASI GIGIYENASI VA KASALLIKLARI</b>\n\n🔹 <b>Kasalliklar:</b>\n• <b>Insult:</b> Miya qon tomirining uzilishi yoki tromblanishi oqibatida qon aylanishining buzilishi.\n• <b>Meningit:</b> Miya pardalarining infeksion yallig'lanishi.\n• <b>Nevrozlar:</b> Surunkali stress, ruhiy charchoq tufayli asab buzilishi.\n• <b>Radikulit:</b> Orqa miya nerv ildizlarining siqilishi.\n🛡 <b>Gigiyena:</b> Uyqu rejimi (7-8 soat), aqliy va jismoniy mehnatni navbatlash.",
            "guide":  "📘 <b>45-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Insult:</b> Miya qon aylanishi o'tkir buzilishi.\n• <b>Meningit:</b> Miya pardasi yallig'lanishi.\n• <b>Gigiyena:</b> Muntazam toza havoda sayr va uyqu.",
            "media":  "🎥 <b>Video dars:</b> Insult alomatlari va asabni asrash qoidalari"
        },
        {
            "id":  "46",
            "title":  "46-mavzu: I.P. Pavlov ta'limoti. Shartsiz va shartli reflekslar",
            "text":  "📖 <b>46-MAVZU: I.P. PAVLOV TA'LIMOTI. REFLEKSLAR</b>\n\n🔹 Oliy asab faoliyatiga I.M. Sechenov va I.P. Pavlov asos solgan.\n• <b>Shartsiz reflekslar:</b> Tug'ma, irsiy, turning barcha vakillariga xos, o'zgarmas (emish, yutish, ko'z pirpiratish). Markazi — miya poyasi va orqa miyada.\n• <b>Shartli reflekslar:</b> Hayot davomida orttiriladi, individual, vaqtinchalik bog'lanishlar. Markazi — miya katta yarim sharlari po'stlog'ida.",
            "guide":  "📘 <b>46-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Shartsiz:</b> Tug'ma, butun turga xos.\n• <b>Shartli:</b> Hayotda orttirilgan, po'stloqda hosil bo'ladi.",
            "media":  "🎥 <b>Video dars:</b> Pavlovning klassik shartli refleks tajribalari"
        },
        {
            "id":  "47",
            "title":  "47-mavzu: Shartli reflekslarning hosil bo'lishi va tormozlanishi",
            "text":  "📖 <b>47-MAVZU: SHARTLI REFLEKSLAR TORMOZLANISHI</b>\n\n🔹 <b>Tormozlanish — refleksning to'xtatilishi:</b>\n1. <b>Tashqi (shartsiz) tormozlanish:</b> Yangi kuchli begona ta'sir paydo bo'lganda (masalan qattiq shovqin) mavjud refleks darhol to'xtaydi.\n2. <b>Ichki (shartli) tormozlanish:</b> Agar shartli qo'zg'atuvchi shartsiz bilan mustahkamlanmasa, vaqtinchalik bog'lanish asta-sekin <b>so'nadi</b>.",
            "guide":  "📘 <b>47-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Tashqi tormozlanish:</b> Begona qo'zg'atuvchi ta'sirida.\n• <b>Ichki tormozlanish:</b> Mustahkamlanmaganda so'nishi.",
            "media":  "🎥 <b>Video dars:</b> Miya po'stlog'ida qo'zg'alish va tormozlanish balansi"
        },
        {
            "id":  "48",
            "title":  "48-mavzu: Birinchi va ikkinchi signal sistemalari. Nutq va tafakkur",
            "text":  "📖 <b>48-MAVZU: BIRINCHI VA IKKINCHI SIGNAL SISTEMALARI</b>\n\n🔹 <b>1-signal sistemasi:</b>\n• Tashqi muhitning bevosita ta'sirlari: rang, tovush, hid, shakl, harorat.\n• Hayvon va odamda umumiy mavjud.\n🔹 <b>2-signal sistemasi:</b>\n• <b>So'z, nutq va yozuv</b> orqali ifodalanadigan signallar.\n• Faqat insoniyatga xos bo'lib, umumlashtirish, mavhum fikrlash va tafakkur asosidir.",
            "guide":  "📘 <b>48-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>1-signal:</b> Aniq narsalar (rang, tovush) — hayvon va odamda.\n• <b>2-signal:</b> So'z, nutq, mavhum tafakkur — faqat insonda.",
            "media":  "🎥 <b>Video dars:</b> Nutq markazlari va tafakkur fiziologiyasi"
        },
        {
            "id":  "49",
            "title":  "49-mavzu: Xotira, diqqat va o'rganish jarayonlari",
            "text":  "📖 <b>49-MAVZU: XOTIRA, DIQQAT VA O'RGANISH</b>\n\n🔹 <b>Xotira:</b> Axborotni qabul qilish, esda saqlash va qayta tiklash qobiliyati.\n• Muddatiga ko'ra: Qisqa muddatli (tezkor) va uzoq muddatli xotira.\n• Turiga ko'ra: Ko'rish, eshitish, harakat va emotsional xotira.\n🔹 <b>Diqqat:</b> Ongning ma'lum ob'ektga qaratilishi. Ixtiyorsiz (kutilmagan shovqin) va Ixtiyoriy (iroda kuchi bilan maqsadli).",
            "guide":  "📘 <b>49-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Xotira:</b> Neyronlararo yangi sinapslar.\n• <b>Ixtiyoriy diqqat:</b> Maqsadli iroda kuchi bilan boshqariladi.",
            "media":  "🎥 <b>Video dars:</b> Xotirani kuchaytirish va diqqatni jamlash usullari"
        },
        {
            "id":  "50",
            "title":  "50-mavzu: Uyqu va uning fiziologik ahamiyati. Tush ko'rish",
            "text":  "📖 <b>50-MAVZU: UYQU VA UNING AHAMIYATI. TUSH KO'RISH</b>\n\n🔹 Uyqu — miya hujayralarining himoyalanishi, toliqishdan saqlanishi va o'zini qayta tiklashidir.\n🌙 <b>Fazalari (har 90 minutda takrorlanadi):</b>\n1. <b>Sekin uyqu (75-80%):</b> Nafas, puls sekinlashadi, muskullar bo'shashadi.\n2. <b>Tez uyqu (20-25%):</b> Ko'z soqqalari tez harakatlanadi. Aynan shu fazada <b>tush ko'riladi</b> va axborotlar xotirada tartibga solinadi.",
            "guide":  "📘 <b>50-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Sekin uyqu:</b> Tana tiklanishi.\n• <b>Tez uyqu:</b> Tush ko'rish, axborotlarni saralash.\n• <b>Uyqu normasi:</b> 7-8 soat.",
            "media":  "🎥 <b>Video dars:</b> Uyqu fazalari va tush ko'rish mexanizmi"
        },
        {
            "id":  "51",
            "title":  "51-mavzu: Hissiyotlar, temperament turlari va inson fe'l-atvori",
            "text":  "📖 <b>51-MAVZU: TEMPERAMENT VA XULQ-ATVOR</b>\n\n🔹 Asab tizimi xususiyatlariga ko'ra 4 xil temperament turi ajratiladi:\n1. <b>Sangvinik:</b> Kuchli, vazmin, chaqqon. Kirishimli, xushchaqchaq, tez moslashadi.\n2. <b>Xolerik:</b> Kuchli, muvozanatsiz, tez qizishuvchi. Qat'iyatli, hissiyotga beriluvchan.\n3. <b>Flegmatik:</b> Kuchli, vazmin, harakatsiz (bosiq). Sabrli, kamgap, vazmin.\n4. <b>Melanxolik:</b> Kuchsiz asab tizimi. Tez ranjiydigan, nozik tabiatli, ta'sirchan.",
            "guide":  "📘 <b>51-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Sangvinik:</b> Chaqqon, kuchli, vazmin.\n• <b>Xolerik:</b> Muvozanatsiz, tez qizishuvchi.\n• <b>Flegmatik:</b> Bosiq, sabrli.\n• <b>Melanxolik:</b> Kuchsiz, nozik tabiatli.",
            "media":  "🎥 <b>Video dars:</b> 4 xil temperament va xarakter psixologiyasi"
        },
        {
            "id":  "52",
            "title":  "52-mavzu: Analizatorlar haqida umumiy tushuncha",
            "text":  "📖 <b>52-MAVZU: ANALIZATORLAR HAQIDA TUSHUNCHA</b>\n\n🔹 Analizator (sezgi a'zosi) tashqi muhitdan axborotni qabul qilib, tahlil qiladi (I.P. Pavlov).\n🔗 <b>3 qismdan iborat:</b>\n1. <b>Periferik qism:</b> Retseptor (ta'sirni nerv impulsiga aylantiradi).\n2. <b>O'tkazuvchi qism:</b> Sezuvchi nerv tolalari (impulsni miyaga tashiydi).\n3. <b>Markaziy qism:</b> Miya katta yarim sharlari po'stlog'idagi maxsus zona (sezgi hosil qiladi).",
            "guide":  "📘 <b>52-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Pavlov:</b> Analizator ta'limoti.\n• <b>3 qism:</b> Retseptor ➡️ Nerv ➡️ Miya po'stlog'i markazi.",
            "media":  "🎥 <b>Video dars:</b> Sezgi a'zolari va analizatorlar arxitekturasi"
        },
        {
            "id":  "53",
            "title":  "53-mavzu: Ko'rish organi: ko'zning tuzilishi va optikasi",
            "text":  "📖 <b>53-MAVZU: KO'ZNING TUZILISHI VA OPTIKASI</b>\n\n🔹 Inson axborotning 80-90% ini ko'rish orqali oladi. Ko'z soqqasi 3 qavatdan iborat:\n1. <b>Sklera (oqsil parda):</b> Oldingi shaffof qismi — <b>shox parda (kornea)</b>.\n2. <b>Tomirli parda:</b> Rangdor parda (iris), o'rtasida <b>qorachiq</b> joylashgan.\n3. <b>To'r parda (retina):</b> Fotoretseptorlar joylashgan.\n🔍 <b>Optik tizim:</b> Shox parda ➡️ Ko'z gavhari (qavariq linza) ➡️ Shishasimon tana. To'r pardada teskari va kichraygan tasvir tushadi.",
            "guide":  "📘 <b>53-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Shox parda:</b> Oldingi shaffof qism.\n• <b>Ko'z gavhari:</b> Yorug'likni sindiruvchi linza.\n• <b>Tasvir:</b> To'r pardada teskari va kichraygan.",
            "media":  "🎥 <b>3D Animatsiya:</b> Ko'z soqqasi va nurlarning sinish optikasi"
        },
        {
            "id":  "54",
            "title":  "54-mavzu: To'r parda fotoretseptorlari va ko'rish gigiyenasi",
            "text":  "📖 <b>54-MAVZU: TO'R PARDA VA KO'RISH GIGIYENASI</b>\n\n🔹 <b>Fotoretseptorlar:</b>\n• <b>Tayoqchalar (130 mln):</b> Oq-qora ko'rish, qorong'ida ko'rish (rodopsin oqsili, A vitamini).\n• <b>Kolbachalar (7 mln):</b> Rang ajratish, kunduzgi yorug'likda ko'rish (yodopsin). Rang ajrata olmaslik — <b>daltonizm</b>.\n• <b>Sariq dog':</b> Eng o'tkir ko'rish joyi (faqat kolbachalar bor).\n• <b>Ko'r dog':</b> Ko'rish nervi chiquvchi joy (retseptorlar yo'q).\n👓 <b>Nuqsonlar:</b> Yaqindan ko'rish (miopiya — botiq linza), uzoqdan ko'rish (gipermetropiya — qavariq linza).",
            "guide":  "📘 <b>54-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Tayoqchalar:</b> 130 mln (oq-qora, rodopsin).\n• <b>Kolbachalar:</b> 7 mln (rangli ko'rish).\n• <b>Sariq dog':</b> Eng o'tkir ko'rish joyi.\n• <b>Miopiya:</b> Botiq linza.",
            "media":  "🎥 <b>Video dars:</b> Daltonizm, miopiya va ko'rish gigiyenasi"
        },
        {
            "id":  "55",
            "title":  "55-mavzu: Eshitish organi: quloq tuzilishi va Kortiy a'zosi",
            "text":  "📖 <b>55-MAVZU: ESHITISH ORGANINING TUZILISHI</b>\n\n🔹 <b>1. Tashqi quloq:</b> Quloq suprasi va tashqi eshitish yo'li. Nog'ora parda bilan chegaralanadi.\n🔹 <b>2. O'rta quloq:</b> 3 ta eshitish suyakchasi: <b>bolg'acha, sandon, uzangicha</b> (tebranishni 50 barobar kuchaytiradi). Yevstaxiy nayi bilan tutashadi.\n🔹 <b>3. Ichki quloq:</b> <b>Chig'anoq</b> ichida joylashgan <b>Kortiy a'zosi</b> retseptor tukchalari tovush to'lqinlarini nerv impulsiga aylantiradi ➡️ Eshitish nervi ➡️ Chakka bo'lagiga uzatadi.",
            "guide":  "📘 <b>55-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Suyakchalar:</b> Bolg'acha, sandon, uzangicha.\n• <b>Kortiy a'zosi:</b> Chig'anoqdagi eshitish retseptorlari.\n• <b>Markaz:</b> Miya chakka bo'lagida.",
            "media":  "🎥 <b>3D Animatsiya:</b> Tovush to'lqinining Kortiy a'zosigacha o'tishi"
        },
        {
            "id":  "56",
            "title":  "56-mavzu: Muvozanat, hid bilish, ta'm bilish va teri sezgilari",
            "text":  "📖 <b>56-MAVZU: MUVOZANAT, HID, TA'M VA TERI SEZGILARI</b>\n\n🔹 <b>Muvozanat (Vestibulyar apparat):</b> Ichki quloqdagi 3 ta yarim doira naylari va dahliz xaltachalari (fazoviy holat va tezlanishni aniqlaydi).\n🔹 <b>Hid bilish:</b> Burun bo'shlig'i yuqori qismidagi hidlovchi retseptorlar.\n🔹 <b>Ta'm bilish:</b> Til so'rg'ichlari: uchi — shirinni, orqasi — achchiqni, yonlari — nordon va sho'rni sezadi.\n🔹 <b>Teri sezgisi:</b> Bosim, og'riq, issiq va sovuq retseptorlari.",
            "guide":  "📘 <b>56-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Vestibulyar:</b> Yarim doira naylari (muvozanat).\n• <b>Til uchi:</b> Shirin; <b>Orqasi:</b> Achchiq.\n• <b>Og'riq:</b> Himoya sezgisi.",
            "media":  "🎥 <b>Video dars:</b> Vestibulyar apparat va sezgi a'zolari"
        },
        {
            "id":  "57",
            "title":  "57-mavzu: Jinsiy organlarning tuzilishi va jinsiy hujayralar",
            "text":  "📖 <b>57-MAVZU: JINSIY ORGANLAR VA GAMETALAR</b>\n\n🔹 <b>Erkaklik jinsiy organlari:</b>\n• Urug'donlar (moyaklar): Spermatozoidlar va testosteron ishlab chiqariladi (34-35°C da).\n• Spermatozoid: Boshcha, bo'yincha, dumcha. 23 ta xromosoma.\n🔹 <b>Ayollik jinsiy organlari:</b>\n• Tuxumdonlar: Follikulalarda tuxum hujayralar yetiladi.\n• Tuxum hujayra: Yirik (0.15-0.2 mm), harakatsiz, oziqqa boy. 23 ta xromosoma.",
            "guide":  "📘 <b>57-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Urug'don:</b> Spermatozoidlar (23 xromosoma, harakatchan).\n• <b>Tuxumdon:</b> Tuxum hujayra (23 xromosoma, harakatsiz).\n• <b>Harorat:</b> Moyaklar 34-35°C da ishlaydi.",
            "media":  "🎥 <b>Video dars:</b> Jinsiy hujayralar va ularning yetilishi"
        },
        {
            "id":  "58",
            "title":  "58-mavzu: Urug'lanish va homilaning bachadonda rivojlanishi",
            "text":  "📖 <b>58-MAVZU: URUG'LANISH VA EMBRION TARAQQIYOTI</b>\n\n🔹 <b>Urug'lanish:</b> Bachadon nayining yuqori qismida spermatozoid va tuxum hujayra qo'shilib, <b>zigota (46 ta xromosoma)</b> hosil qiladi.\n• Zigota bo'linib bachadonga o'tadi va 6-7 kunda bachadon devoriga <b>implantatsiya</b> bo'ladi.\n🌱 <b>Homiladorlik davri (270-280 kun, 40 hafta):</b>\n• <b>Yo'ldosh (Plasenta):</b> Homila va ona o'rtasida moddalar almashinuvini ta'minlaydi (qonlari aralashmaydi!).\n• Homila <b>kindik tizimchasi</b> orqali yo'ldosh bilan tutashadi.",
            "guide":  "📘 <b>58-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Urug'lanish joyi:</b> Bachadon nayi.\n• <b>Zigota:</b> 46 xromosoma.\n• <b>Homiladorlik:</b> 280 kun (9 oy).\n• <b>Plasenta:</b> Oziqlanish to'sig'i.",
            "media":  "🎥 <b>3D Animatsiya:</b> Urug'lanishdan tug'ilishgacha 9 oylik rivojlanish"
        },
        {
            "id":  "59",
            "title":  "59-mavzu: Bolalik, o'smirlik va balog'atga yetish davrlari",
            "text":  "📖 <b>59-MAVZU: ONTOGENEZ BOSHQICHLARI VA BALOG'AT</b>\n\n🔹 <b>Postembrional davrlar:</b> Chaqaloqlik (1-10 kun), go'daklik (1 yoshgacha), yasli (1-3 yosh), bog'cha (3-7 yosh), kichik maktab (7-11 yosh).\n• <b>O'smirlik (balog'at davri):</b> Qizlarda 11-13 yosh, o'g'il bolalarda 12-14 yosh.\n⚧ <b>Jinsiy belgilar:</b>\n• Birlamchi: Jinsiy organlarning o'zi.\n• Ikkilamchi: O'g'illarda ovoz do'rillashi, mo'ylov-soqol; qizlarda ko'krak bezi o'sishi, chanoq kengayishi.",
            "guide":  "📘 <b>59-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Balog'at davri:</b> 11-14 yoshlar.\n• <b>Birlamchi belgilar:</b> Jinsiy a'zolar.\n• <b>Ikkilamchi belgilar:</b> Ovoz, qad-qomat o'zgarishlari.",
            "media":  "🎥 <b>Video dars:</b> O'smirlik davri fiziologiyasi va psixologiyasi"
        },
        {
            "id":  "60",
            "title":  "60-mavzu: Jismoniy tarbiya va zararli odatlarning organizmga ta'siri",
            "text":  "📖 <b>60-MAVZU: ZARARLI ODAMLAR VA GIPODINAMIYA</b>\n\n🔹 <b>Gipodinamiya:</b> Kamharakatlilik (yurak-qon tomir va semizlikka olib keladi).\n☠️ <b>Zararli omillar ta'siri:</b>\n• <b>Alkogol:</b> Jigar sirrozi, miya hujayralari nobud bo'lishi va jinsiy hujayralar mutatsiyasi.\n• <b>Nikotin:</b> Tomirlar spazmi (infarkt), o'pka saratoni xavfini 20 barobar oshiradi.\n• <b>Giyohvandlik:</b> Butun nerv sistemasining yemirilishi.",
            "guide":  "📘 <b>60-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Nikotin:</b> Tomirlar torayishi va nafas saratoni.\n• <b>Alkogol:</b> Jigar va asab zahari.\n• <b>Faollik:</b> Sog'lom turmush asosi.",
            "media":  "🎥 <b>Video dars:</b> Chekish va spirtli ichimliklarning organlarga zarari"
        },
        {
            "id":  "61",
            "title":  "61-mavzu: Odam va biosfera. Sog'lom turmush tarzi asoslari",
            "text":  "📖 <b>61-MAVZU: ODAM VA BIOSFERA. SOG'LOM TURMUSH TARZI</b>\n\n🔹 Inson tabiatning ajralmas qismi bo'lib, biosfera bilan uzviy bog'langan.\n🍏 <b>Sog'lom turmush tarzi tamoyillari:</b>\n1. Kun tartibiga qat'iy rioya qilish;\n2. Rasionallik va muvozanatli ovqatlanish;\n3. Doimiy jismoniy tarbiya va mehnat;\n4. Zararli odatlardan (tamaki, spirt) butunlay voz kechish;\n5. Ruhiy xotirjamlik va tabiat bilan hamohang yashash.",
            "guide":  "📘 <b>61-MAVZU QISQA QO'LLANMASI:</b>\n\n• <b>Sog'lom turmush tarzi:</b> To'g'ri ovqatlanish + harakat + rejim.\n• <b>Ibn Sino vasiyati:</b> O'z vaqtida ovqatlanish, toza suv va jismoniy harakat — eng yaxshi dori.",
            "media":  "🎥 <b>Video dars:</b> 8-sinf anatomiyasi xulosasi va sog'lom turmush tarzi"
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