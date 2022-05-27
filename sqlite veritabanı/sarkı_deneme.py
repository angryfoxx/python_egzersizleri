from sarkı_proje import *

print("""\t\t\t\t\t!-iPod/Your Playlist-!
*****************************************
1- Şarkı ekleme

2- Şarkı silme

3- Tüm şarkıları öğrenme

4- Şarkı bulma

5- Şarkıların toplam uzunluğu

Çıkmak için 'q'ya basınız...
*****************************************
""")
ipod = iPod()
while True:
    a = input("Yapmak istediğiniz işlemi seçiniz:")
    if not a:
        print("Lütfen boş bırakmayınız...")
    elif a == "q" or a == "Q":
        print("Program kapatılıyor")
        time.sleep(2)
        ipod.c_connection()
        break
    elif a == "1":
        isim = input("Şarkı ismi:")
        sanatci = input("Sanatçı ismi:")
        album = input("Albüm ismi:")
        sirket = input("Plak şirketinin ismi:")
        sure = int(input("Şarkının süresi(saniye cinsinden):"))
        eklenecek = Sarki(isim,sanatci,album,sirket,sure)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        ipod.add_songs(eklenecek)
        print("şarkı eklendi")
    elif a == "2":
        isim = input("Silmek istediğiniz şarkının ismini giriniz:")
        print("Şarkı siliniyor...")
        time.sleep(2)
        ipod.del_songs(isim)
        print("Şarkı silindi...")
    elif a == "3":
        print("Playlist yazdırılıyor...")
        time.sleep(3)
        ipod.data()
    elif a == "4":
        isim = input("Tüm verilerine ulaşmak istediğiniz şarkıyı giriniz:")
        print("Şarkı aranıyor...")
        time.sleep(1)
        ipod.select_data(isim)
    elif a == "5":
        print("Hesaplanıyor...")
        time.sleep(2)
        ipod.plus_len()
    else:
        print("Lütfen hatalı değer girmeyiniz...")