'''
__Author__ = "FOX"


print("""*****************************************************
Mükemmel sayı hesaplama:'1'.
Armstrong sayısı hesaplama:'2'.
Çarpım tablosu:'3'.
Değişken toplama:'4'.
2'ye bölünen sayıları bulma:'5'.
3'e bölünen sayıları bulma:'6'
Çıkmak için 'q'ya basınız.
*****************************************************
""")
while True:
    baslangic_islemi = input("Yapmak istediğiniz işlemi seçiniz:")
    def mukemmel(): #Problem 1 "Mükemmel sayı"
        print("""*****************************************************          
    'Mükemmel sayı' hesaplama programına hoşgeldiniz.
    Bir sayının kendi hariç bölenlerinin toplamı 
    kendine eşitse bu sayıya "mükemmel sayı" denir. 
    Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
    Çıkmak için 'q'ya basınız.
    *****************************************************
        """)
        while True:
            muk_a = int(input("Bir sayı giriniz:"))
            liste_muk = 0
            for muki in range(1, muk_a):
                if muk_a % muki == 0:
                    liste_muk += muki
            if liste_muk == muk_a:
                print("Seçtiğiniz sayı bir 'Mükemmel sayı'!!!!!")
                res = input("""Yeni bir sayı denemek için 'e'ye,çıkmak için 'q'ya basınız:""")
                if res == "e":
                    continue
                elif res == "q":
                    break
                else:
                    print("Hatalı işlem yaptınız tekrar deneyin...")
                    rese = res
            else:
                print("Seçtiğiniz sayı maalesef mükemmel sayı değil...")
                res1 = input("""Yeni bir sayı denemek için 'e'ye,çıkmak için 'q'ya basınız:""")
                if res1 == "e":
                    continue
                elif res1 == "q":
                    break
                else:
                    print("Hatalı işlem yaptınız tekrar deneyin...")
        return baslangic_islemi


    def armstrong(): # Problem 2 "Armstrong"
        print("""*******************************************************          
    'Armstrong sayısı' hesaplama programına hoşgeldiniz.
    Bir sayını basamaklarındaki tüm rakamlarının,
    sayının basamak sayısı kadar kuvveti alınıp 
    toplanıldığında elde edilen sayı,
    sayının kendisine eşitse bu sayıya "Armstrong sayısı" denir.
    Örnek olarak :
    153 = 1^3 + 5^3 + 3^3
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    Çıkmak için 'q'ya basınız.
    *******************************************************
        """)
        armstrong_a = input("Bir sayı giriniz:")
        armstrong_ai = int(armstrong_a)
        arm_toplam = 0
        for armi in armstrong_a:
            rakam_arm = int(armi) ** len(armstrong_a)
            arm_toplam += rakam_arm
        if arm_toplam == armstrong_ai:
            print("Seçtiğiniz sayı armstrong sayısıdır")
        else:
            print("Seçtiğiniz sayı armstrong sayısı değildir")
        return baslangic_islemi

    def carpim():   #Problem 3 "çarpım tablosu"
        for carp in range(1,11):
            for carpi in range(1,11):
                print(f"{carp}x{carpi}={carp*carpi}")
        return baslangic_islemi

    def degisken(): #Problem 4 "değişken toplama"
        print("""*********************************************
        Girdiğiniz sayılar sürekli toplanarak artar.
        Ta ki siz çıkana kadar.
        Çıkmak için 'q'ya basınız.
        *********************************************""")
        degisken_toplam = 0
        print("Toplam",degisken_toplam)
        while True:
            degisken_a = input("Sayı giriniz:")
            if degisken_a == "q":
                print("Toplam Değişken:", degisken_toplam)
                print("Program sonlandırılıyor...")
                break
            degisken_a = int(degisken_a)
            degisken_toplam += degisken_a
        return baslangic_islemi

    def ucebolunen():
        auc = int(input("Başlangıç aralığı belirleyiniz:"))
        buc = int(input("Bitiş aralığı belirleyiniz:"))
        listeuc = range(auc,buc)
        listeuc1 = [uc for uc in listeuc if uc % 3 == 0]
        print(listeuc1)
        return baslangic_islemi

    def ikiyebolunen(): #Problem 6 "2 e bölünen sayılar l-comp"
        aikiye = int(input("Başlangıç aralığı belirleyiniz:"))
        bikiye = int(input("Bitiş aralığı belirleyiniz:"))
        listeikiye = range(aikiye,bikiye)
        listeikiye1 = [iki for iki in listeikiye if iki % 2 == 0]
        print(listeikiye1)
        return baslangic_islemi

    if baslangic_islemi == "1":
        mukemmel()
    elif baslangic_islemi == "2":
        armstrong()
    elif baslangic_islemi == "3":
        carpim()
    elif baslangic_islemi == "4":
        degisken()
    elif baslangic_islemi == "5":
        ikiyebolunen()
    elif baslangic_islemi == "6":
        ucebolunen()
    elif baslangic_islemi == "q":
        print("Program kapatılıyor...")
        break
    else:
        print("Hatalı işlem tekrar deneyin")
        continue
'''
