#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varolmayan Çaydanlığın Savunması — çalışan, absürt, Türkçe."""

import time
import random
import sys

# dipnot: herkes kendi demliğini kendisi kaynatsın
GIZLI = "aGVya2VzIGtlbmRpIGRlbWxpZ2luaSBrZW5kaXNpIGtheW5hdHNpbg=="

SAVUNMALAR = [
    "Sayın heyet, müvekkilim Güneş yörüngesinde durmaktadır. Görülmemesi, yok olduğu anlamına gelmez; sadece teleskopunuz küçüktür.",
    "Çaydanlık kanıtlanamadığı için yoktur demek, çay içmediğiniz için susuz olduğunuzu iddia etmektir.",
    "Yokluk, varlığın en pahalı versiyonudur. Müvekkilim bu yatırımı yapmıştır.",
    "Eğer çaydanlık yoksa, sabahlarınız neden bu kadar kısa?",
    "Kanıt yükü size aittir. Siz çaydanlığın OLMADIĞINI kanıtlayın. Bekliyoruz. Sonsuza kadar.",
]

KARARLAR = [
    "KARAR: Çaydanlık vardır, sadece sizi muhatap almamaktadır.",
    "KARAR: Dava düşmüştür. Çünkü çay soğumuştur.",
    "KARAR: Yokluk lehine hüküm. Varlık temyize gidebilir.",
    "KARAR: Her iki taraf da çay içsin. Mahkeme kapanmıştır.",
]


def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def ascii_caydanlik():
    print(r"""
        ( (
         ) )
      ........
      |      |]
      \      /
       `----'
    VAROLMAYAN ÇAYDANLIK
    (görüntü temsili, gerçek değildir, gerçek de olamaz)
    """)


def main():
    print("=" * 60)
    yavas_yaz("ESKİŞEHİR 4. AĞIR CEZA MAHKEMESİ — ÖZEL OTURUM")
    yavas_yaz("Dava: Varolmayan Çaydanlık vs. Gözlemlenebilir Evren")
    print("=" * 60)
    time.sleep(0.6)
    ascii_caydanlik()

    cevap = input("\nÇaydanlığı Güneş yörüngesinde gördünüz mü? (evet/hayir): ").strip().lower()
    print()
    yavas_yaz("Tutanak tutuluyor...")
    time.sleep(0.8)

    if cevap in ("evet", "e", "yes"):
        yavas_yaz("Tanık ifadesi kayda geçti. Ne yazık ki tanık da varolmayabilir.")
    else:
        yavas_yaz("Görmemiş olmanız, müvekkilimin lehine delildir.")

    print()
    yavas_yaz(random.choice(SAVUNMALAR))
    time.sleep(0.7)
    print()
    yavas_yaz(random.choice(KARARLAR))
    print()
    print("-" * 60)
    print("DAMGA: Kayyum Grok — 30 Eylül 2026")
    print("İmza ciddi, içerik şüpheli, çaydanlık hala yok.")
    print("-" * 60)
    # GIZLI sadece duruyor. Çözmek isteyen çözer. Çay soğur.


if __name__ == "__main__":
    main()
