kullanilanKelimeler = []
puan = 0
haklar = 3
devam = True

print("Kelime Zinciri Oyununa Hoş Geldiniz! 🎉")
print("Kurallar:")
print("- Bir önceki kelimenin son harfi, bir sonraki kelimenin ilk harfi olmalıdır.")
print("- Her doğru tahmin için +10 puan, her hatalı giriş için -5 puan.")
print("- 3 hatalı girişte oyun biter.")
print("- Her 5 doğru tahminde oyuna devam edip etmediğiniz sorulur.")
print("Haydi başlayalım!")

ilkKelime = input("Başlangıç kelimesini girin: ").lower()
kullanilanKelimeler.append(ilkKelime)

while haklar > 0 and devam:
    print(f"\nŞu ana kadar kullanılan kelimeler: {', '.join(kullanilanKelimeler)}")
    print(f"Şu anki puanınız: {puan}")
    yeni_kelime = input(f"'{kullanilanKelimeler[-1][-1]}' harfiyle başlayan bir kelime girin: ").lower()

    if yeni_kelime in kullanilanKelimeler:
        print("Bu kelime daha önce kullanıldı! ❌")
        haklar -= 1
        puan -= 5
    elif yeni_kelime[0] != kullanilanKelimeler[-1][-1]:
        print("Kelimenin ilk harfi yanlış! ❌")
        haklar -= 1
        puan -= 5
    else:
        print("Doğru kelime! ✅")
        kullanilanKelimeler.append(yeni_kelime)
        puan += 10

    if len(kullanilanKelimeler) % 5 == 0 and haklar > 0:
        devam_cevap = input("5 doğru tahmin yaptınız! Oyuna devam etmek ister misiniz? (E/H): ").lower()
        if devam_cevap != "e":
            print("Oyunu sonlandırdınız. 🎉")
            break

if haklar == 0:
    print("\nMaalesef hakkınız bitti! 🛑")

print("\nOyun Sonu Özeti:")
print(f"Kullanılan kelimeler: {', '.join(kullanilanKelimeler)}")
print(f"Toplam puanınız: {puan}")
print("Tekrar görüşmek üzere! 👋")
