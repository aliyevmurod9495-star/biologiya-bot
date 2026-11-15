"""
BioMaster - Milliy Sertifikat Natijalar Kartasi va Sertifikat Generatori
Talabgorlar uchun yuqori sifatli rasmiy sertifikat kartasini avtomatik yasab beradi.
"""

import io
import os
import random
import datetime
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

def get_font(size: int, bold: bool = False):
    """Platformaga mos shriftni xavfsiz yuklaydi."""
    font_candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/timesbd.ttf" if bold else "C:/Windows/Fonts/times.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "arialbd.ttf" if bold else "arial.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
    ]
    for font_path in font_candidates:
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def generate_certificate_image(
    student_name: str,
    test_code: str,
    total_score: float,
    max_score: float,
    percentage: float,
    tier: str,
    tier_desc: str,
    date_str: Optional[str] = None
) -> bytes:
    """
    Milliy sertifikat natija kartasini (PNG) generatsiya qiladi va baytlarni qaytaradi.
    Hajmi: 1200 x 800 px.
    """
    W, H = 1200, 800
    
    # 1. Asosiy fon (To'q zumrad va quyuq ko'k gradient)
    img = Image.new("RGB", (W, H), color=(10, 20, 30))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(10 + (16 - 10) * (y / H))
        g = int(24 + (38 - 24) * (y / H))
        b = int(36 + (50 - 36) * (y / H))
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # 2. Naqshdor oltin hoshiyalar (Borders)
    gold_outer = (212, 175, 55)
    gold_inner = (180, 140, 40)
    gold_subtle = (120, 95, 30)

    # Tashqi hoshiya
    draw.rectangle([25, 25, W - 25, H - 25], outline=gold_outer, width=3)
    # Ichki nozik hoshiya
    draw.rectangle([35, 35, W - 35, H - 35], outline=gold_subtle, width=1)
    draw.rectangle([42, 42, W - 42, H - 42], outline=gold_inner, width=2)

    # Burchaklardagi naqshlar (Corner accents)
    for cx, cy in [(42, 42), (W - 42, 42), (42, H - 42), (W - 42, H - 42)]:
        dx = 25 if cx == 42 else -25
        dy = 25 if cy == 42 else -25
        draw.rectangle([cx - 4, cy - 4, cx + 4, cy + 4], fill=gold_outer)
        draw.line([(cx, cy), (cx + dx, cy)], fill=gold_outer, width=2)
        draw.line([(cx, cy), (cx, cy + dy)], fill=gold_outer, width=2)

    # 3. Shriftlar
    font_title = get_font(28, bold=True)
    font_sub = get_font(16, bold=False)
    font_name = get_font(42, bold=True)
    font_body = get_font(18, bold=False)
    font_badge = get_font(48, bold=True)
    font_metric_num = get_font(26, bold=True)
    font_metric_lbl = get_font(14, bold=False)
    font_small = get_font(14, bold=False)

    # 4. Sarlavha qismi (Header)
    header_org = "BIOMASTER ACADEMY • MILLIY BAHOLASH TIZIMI"
    draw.text((W // 2, 75), header_org, fill=(160, 200, 220), font=font_sub, anchor="mm")

    main_title = "MALAKA SERTIFIKATI"
    draw.text((W // 2, 120), main_title, fill=gold_outer, font=font_title, anchor="mm")

    subtitle = "BIOLOGIYA FANI BO'YICHA 43 TALIK TEST SINOVI NATIJASI"
    draw.text((W // 2, 160), subtitle, fill=(200, 220, 235), font=font_sub, anchor="mm")

    # Oltin chiziq
    draw.line([(W // 2 - 250, 185), (W // 2 + 250, 185)], fill=gold_outer, width=2)

    # 5. Talabgor qismi
    draw.text((W // 2, 220), "Ushbu sertifikat tasdiqlaydiki, rasmiy sinov ishtirokchisi:", fill=(170, 185, 200), font=font_body, anchor="mm")

    clean_name = (student_name or "TALABGOR").upper()
    if len(clean_name) > 35:
        clean_name = clean_name[:32] + "..."
    draw.text((W // 2, 275), clean_name, fill=(255, 255, 255), font=font_name, anchor="mm")

    draw.text((W // 2, 330), "Milliy sertifikat talablari asosidagi barcha test va yozma topshiriqlarni topshirdi.", fill=(180, 200, 215), font=font_body, anchor="mm")

    # 6. Ko'rsatkichlar paneli (3 ta kartochka)
    # Kartochkalar o'lchami
    box_y = 370
    box_h = 130
    box_w = 230
    gap = 25
    total_w = 3 * box_w + 2 * gap
    start_x = (W - total_w) // 2

    # 1-box: Variant
    b1_x = start_x
    draw.rounded_rectangle([b1_x, box_y, b1_x + box_w, box_y + box_h], radius=12, fill=(18, 32, 48), outline=(50, 80, 110), width=1)
    draw.text((b1_x + box_w // 2, box_y + 35), "VARIANT KODI", fill=(140, 170, 200), font=font_metric_lbl, anchor="mm")
    draw.text((b1_x + box_w // 2, box_y + 80), str(test_code), fill=(100, 220, 255), font=font_metric_num, anchor="mm")

    # 2-box: Ball & Foiz
    b2_x = b1_x + box_w + gap
    draw.rounded_rectangle([b2_x, box_y, b2_x + box_w, box_y + box_h], radius=12, fill=(18, 32, 48), outline=(50, 80, 110), width=1)
    draw.text((b2_x + box_w // 2, box_y + 35), "TO'PLANGAN BALL", fill=(140, 170, 200), font=font_metric_lbl, anchor="mm")
    draw.text((b2_x + box_w // 2, box_y + 75), f"{total_score:g} / {max_score:g}", fill=(255, 255, 255), font=font_metric_num, anchor="mm")
    draw.text((b2_x + box_w // 2, box_y + 105), f"Ko'rsatkich: {percentage:.1f}%", fill=(110, 230, 180), font=font_metric_lbl, anchor="mm")

    # 3-box: Rasmiy Daraja
    b3_x = b2_x + box_w + gap
    tier_bg_color = (25, 50, 45) if "A" in tier else ((25, 45, 60) if "B" in tier else (45, 35, 40))
    tier_border = (50, 200, 140) if "A" in tier else ((80, 150, 240) if "B" in tier else (220, 100, 80))
    tier_text_color = (70, 240, 160) if "A" in tier else ((100, 180, 255) if "B" in tier else (255, 120, 100))

    draw.rounded_rectangle([b3_x, box_y, b3_x + box_w, box_y + box_h], radius=12, fill=tier_bg_color, outline=tier_border, width=2)
    draw.text((b3_x + box_w // 2, box_y + 30), "SERTIFIKAT DARAJASI", fill=(200, 220, 230), font=font_metric_lbl, anchor="mm")
    draw.text((b3_x + box_w // 2, box_y + 80), tier, fill=tier_text_color, font=font_badge, anchor="mm")

    # 7. Izoh va imtiyoz matni
    if tier_desc:
        clean_desc = tier_desc
        if len(clean_desc) > 90:
            clean_desc = clean_desc[:87] + "..."
        draw.text((W // 2, 535), f"🏅 Imtiyoz: {clean_desc}", fill=gold_outer, font=font_sub, anchor="mm")

    # 8. Quyi qism (Footer, ID, Sana, Muhr)
    if not date_str:
        now = datetime.datetime.now()
        date_str = now.strftime("%d.%m.%Y")

    cert_serial = f"BM-{test_code}-{random.randint(1000, 9999)}"

    # Chapda: Sertifikat ID va Sana
    footer_y = 670
    draw.text((80, footer_y), f"Sertifikat raqami: {cert_serial}", fill=(150, 175, 200), font=font_small)
    draw.text((80, footer_y + 24), f"Tekshirilgan sana: {date_str}", fill=(150, 175, 200), font=font_small)
    draw.text((80, footer_y + 48), "Tekshiruv tizimi: BioMaster AI Vision & OMR Engine", fill=(110, 140, 170), font=font_small)

    # O'ngda: Muhr va Tasdiq
    seal_x = W - 180
    seal_y = footer_y + 15
    draw.ellipse([seal_x - 55, seal_y - 55, seal_x + 55, seal_y + 55], outline=gold_outer, width=2)
    draw.ellipse([seal_x - 50, seal_y - 50, seal_x + 50, seal_y + 50], outline=gold_subtle, width=1)
    draw.text((seal_x, seal_y - 12), "BIOMASTER", fill=gold_outer, font=get_font(12, bold=True), anchor="mm")
    draw.text((seal_x, seal_y + 4), "★ ★ ★", fill=gold_outer, font=get_font(10, bold=True), anchor="mm")
    draw.text((seal_x, seal_y + 18), "VERIFIED", fill=(100, 220, 255), font=get_font(11, bold=True), anchor="mm")

    # Baytlar ko'rinishida saqlaymiz
    buffer = io.BytesIO()
    img.save(buffer, format="PNG", quality=95)
    return buffer.getvalue()


if __name__ == "__main__":
    # Test qilib ko'ramiz
    data = generate_certificate_image(
        student_name="Murod Aliyev",
        test_code="8392004",
        total_score=62.5,
        max_score=66.5,
        percentage=94.0,
        tier="A+",
        tier_desc="OTMga kirishda biologiya fanidan 100% maksimal ball beriladi",
        date_str="15.11.2026"
    )
    with open("test_certificate.png", "wb") as f:
        f.write(data)
    print("Sertifikat yaratildi, hajmi:", len(data), "bayt")
