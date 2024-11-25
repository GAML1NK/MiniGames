import random
import time

def yarısFonk():

    araba_sayisi = int(input("Yarışa kaç araba katılacak? "))
    arabalar = []
    for i in range(araba_sayisi):
        isim = input(f"{i+1}. arabanın ismini girin: ")
        arabalar.append({"isim": isim, "mesafe": 0})

    sahaMesafesi = int(input("Yarışın uzunluğu nedir? (ör: 50): "))

    print("\nYarış başlıyor! 🚗💨\n")

    kazanan = None
    while not kazanan:
        for araba in arabalar:

            araba["mesafe"] += random.randint(1, 10)
            if araba["mesafe"] >= sahaMesafesi:
                kazanan = araba["isim"]
                break


        print("\nYarış Durumu:")
        for araba in arabalar:
            print(f"{araba['isim']}: {'-' * araba['mesafe']} ({araba['mesafe']})")

        time.sleep(1)

    print(f"\n🏆 Yarışı kazanan araba: {kazanan}! Tebrikler! 🎉")

yarısFonk()
