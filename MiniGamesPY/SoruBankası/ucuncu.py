import random

sorular = {
    "bilim": [
        {"soru": "Einstein'ın ünlü enerji denklemi nedir?", "cevap": "e=mc^2"},
        {"soru": "Güneş sistemindeki en büyük gezegen hangisidir?", "cevap": "jüpiter"},
        {"soru": "Bir atomun çevresinde dolanan negatif yüklü parçacıklara ne ad verilir?", "cevap": "elektron"}
    ],
    "sinema": [
        {"soru": "'Titanic' filmi hangi yılda vizyona girdi?", "cevap": "1997"},
        {"soru": "'Yüzüklerin Efendisi' serisinin yazarı kimdir?", "cevap": "j.r.r. tolkien"},
        {"soru": "Oscar ödüllerini veren kuruluşun adı nedir?", "cevap": "academy"}
    ],
    "müzik": [
        {"soru": "'Beatles' grubunun ünlü solisti kimdir?", "cevap": "john lennon"},
        {"soru": "Dünyanın en çok satan albümü hangisidir?", "cevap": "thriller"},
        {"soru": "'Bohemian Rhapsody' şarkısını hangi grup yapmıştır?", "cevap": "queen"}
    ],
    "sanat": [
        {"soru": "Leonardo da Vinci'nin ünlü eseri 'Mona Lisa' hangi müzededir?", "cevap": "louvre"},
        {"soru": "Van Gogh'un kesik kulağı ile ünlü tablosunun adı nedir?", "cevap": "otoportre"},
        {"soru": "'Çığlık' tablosunun ressamı kimdir?", "cevap": "edvard munch"}
    ]
}

def bilgi_yarismasi():
    toplamPuan = 0

    print("Bilgi Yarışmasına Hoş Geldiniz! 🎉")
    print("Kategoriler: Bilim, Sinema, Müzik, Sanat")

    while True:
        kategori = input("Bir kategori seçin (Çıkmak için 'çıkış' yazın): ").lower()

        if kategori == "çıkış":
            break
        elif kategori not in sorular:
            print("Geçerli bir kategori seçin!")
            continue

        print(f"\nSeçtiğiniz kategori: {kategori.capitalize()}")
        kategoriSoruları = random.sample(sorular[kategori], 3)  

        for i, soru in enumerate(kategoriSoruları, 1):
            print(f"\nSoru {i}: {soru['soru']}")
            cevap = input("Cevabınız: ").lower()
            if cevap == soru['cevap']:
                print("Doğru! ✅")
                toplamPuan += 10
            else:
                print(f"Yanlış! ❌ Doğru cevap: {soru['cevap']}")

        print(f"\nKategori '{kategori.capitalize()}' tamamlandı! Toplam puanınız: {toplamPuan}")
        devam = input("Başka bir kategori seçmek ister misiniz? (E/H): ").lower()
        if devam != "e":
            break

    print("\nYarışma sona erdi!")
    print(f"Toplam puanınız: {toplamPuan}")
    print("Tekrar görüşmek üzere! 👋")

bilgi_yarismasi()
