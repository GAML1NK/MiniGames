import random

kelime_listesi = ["python", "yazılım", "bilgisayar", "oyun", "veritabanı"]

dogru_kelime = random.choice(kelime_listesi)
karisik_kelime = ''.join(random.sample(dogru_kelime, len(dogru_kelime)))

print("Karışık kelime:", karisik_kelime)

haklar = 3
while haklar > 0:
    tahmin = input(f"Tahmininizi girin ({haklar} hakkınız kaldı): ").lower()
    if tahmin == dogru_kelime:
        print("Tebrikler! Doğru tahmin ettiniz 🎉")
        break
    else:
        haklar -= 1
        if haklar > 0:
            print("Yanlış tahmin. Tekrar deneyin.")
        else:
            print(f"Hakkınız bitti! Doğru kelime: {dogru_kelime}")