from proje import *

print("""Kütüphane programına hoşgeldiniz...
1-Veri ekleme

2-Veri silme

4-Verileri öğrenme

5-Veri sorgulama

6-Baskı sayısını yükseltme

Çıkmak için 'q'ya basınız...
""")
kutuphane = kutuphane()
while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz:")
    if islem == "q" or islem == "Q":
        print("Program kapatılıyor...")
        kutuphane.baglantikes()
        time.sleep(2)
        break
    elif not islem:
        print("Lütfen boş bırakmayınız...")
    elif islem == "1":
        isim = input("Kitabın ismini giriniz:")
        yazar = input("Yazarın ismini giriniz:")
        tur = input("Tür'ü giriniz:")
        yayinevi = input("Yayınevi ismini giriniz:")
        baski = int(input("Baskı sayısını giriniz:"))
        if not isim or not yazar or not tur or not yayinevi or not baski:
            print("Lütfen boş bırakmayınız...")
        else:
            print("Veriler ekleniyor...")
            time.sleep(2)
            kutuphane.veriekleme(isim, yazar, tur, yayinevi, baski)
            print("Veriler başarıyla eklendi.")
    elif islem == "2":
        dataone0 = input("Silinecek kitabın ismi:")
        if not dataone0:
            print("Lütfen boş bırakmayınız...")
        else:
            print("Veri siliniyor...")
            time.sleep(2)
            kutuphane.verisilme(dataone0)
            print("Veri silindi")
    elif islem == "4":
        print("Veriler yazdırılıyor...")
        time.sleep(3)
        kutuphane.bilgilerigoster()
    elif islem == "5":
        dataone2 = input("Sorgulanacak kitap ismi:")
        if not dataone2:
            print("Lütfen boş bırakmayınız...")
        else:
            print("Veriler yazdırılıyor")
            time.sleep(1.5)
            kutuphane.verisorgulama(dataone2)
    elif islem == "6":
        dataone3 = input("Baskı sayısını yükseltmek istediğiniz kitabı giriniz:")
        if not dataone3:
            print("Lütfen boş bırakmayınız...")
        else:
            print("Baskı yükseltiliyor...")
            time.sleep(1)
            kutuphane.baskiyukselt(dataone3)
            print("Baskı yükseltildi...")
    else:
        print("Hatalı tuşlama lütfen tekrar deneyiniz")