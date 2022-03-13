'''
import math
def ekok(sayi1, sayi2):
    i = 2
    ekok = 1
    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i
            sayi1 //= i
            sayi2 //= i
        elif (sayi1 % i == 0 and sayi2 % i != 0):
            ekok *= i
            sayi1 //= i
        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i
            sayi2 //= i
        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok
print("""...HESAP MAKİNESİ...
        !!!Çıkmak için 'q'ya basınız!!!
1-)Toplama
2-)Çıkarma
3-)Bölme
4-)Çarpma
5-)Üste yuvarlama
6-)Aşağı yuvarlama
7-)Mutlak Değer
8-)Kalan bulma
9-)faktöriyel
10-)Tam sayı yuvarlama
11-)eulerin kuvvetini alma
12-)Birinci değerin ikinci değere göre logaritması.
13-)e tabanına göre logaritma.
14-)2 tabanında logaritma
15-)10 tabanında logaritma
16-)kuvvet alma
17-)karekök
18-)radyandan dereceye çevirme
19-)dereceden radyana çevirme
20-)EBOB,EKOK
21-)permütasyon,kombinasyon
Not: e,pi,tau sabitleri ile işlem yapabilirsiniz...
""")
while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz:")
    if islem == "q":
        print("Program kapatılıyor...")
        break
    elif not islem:
        print("Hatalı işlem tekrar deneyiniz...")
    else:
        islem = int(islem)
        if islem == 1:
            bir0=int(input("Birinci sayıyı giriniz:"))
            iki0=int(input("İkinci sayıyı giriniz:"))
            print(f"""{bir0}+{iki0}={bir0+iki0}
*******************************************************************
""")
        elif islem == 2:
            bir1 = int(input("Birinci sayıyı giriniz:"))
            iki1 = int(input("İkinci sayıyı giriniz:"))
            print(f"""{bir1}-{iki1}={bir1-iki1}
*******************************************************************
""")
        elif islem == 3:
            bir2 = int(input("Birinci sayıyı giriniz:"))
            iki2 = int(input("İkinci sayıyı giriniz:"))
            print(f"""{bir2}/{iki2}={bir2/iki2}
*******************************************************************
""")
        elif islem == 4:
            bir3 = int(input("Birinci sayıyı giriniz:"))
            iki3 = int(input("İkinci sayıyı giriniz:"))
            print(f"""{bir3}+{iki3}={bir3*iki3}
*******************************************************************
""")
        elif islem == 5:
            bir4= int(input("Üste yuvarlamak istediğinz sayıyı giriniz:"))
            print(f"""{math.ceil(bir4)}
*******************************************************************
""")
        elif islem == 6:
            bir5=int(input("Aşağı yuvarlamak istediğinz sayıyı giriniz:"))
            print(f"""{math.floor(bir5)}
*******************************************************************
""")
        elif islem == 7:
            bir6 = int(input("Mutlak değerini almak istediğinz sayıyı giriniz:"))
            print(f"""{abs(bir6)}
*******************************************************************
""")
        elif islem == 8:
            bir7 = int(input("Sayıyı giriniz:"))
            iki7 = int(input("Böleni giriniz:"))
            print(f"""{bir7} sayısının {iki7} bölümünden kalanı:{math.fmod(bir7,iki7)}
*******************************************************************
""")
        elif islem == 9:
            bir8 = int(input("Faktöriyelini almak istediğiniz sayıyı giriniz:"))
            print(f"""{math.factorial(bir8)}
*******************************************************************
""")
        elif islem == 10:
            bir9 = float(input("Tam sayıya yuvarlamak istediğiniz sayıyı giriniz:"))
            print(f"""{math.trunc(bir9)}
*******************************************************************
""")
        elif islem == 11:
            bir10 = int(input("Euler Kuvvetinin derecesini giriniz:"))
            print(f"""{math.exp(bir10)}
*******************************************************************
""")
        elif islem == 12:
            bir11 = int(input("Birinci sayıyı giriniz:"))
            iki11 = int(input("İkinci sayıyı giriniz:"))
            print(f"""{math.log(bir11,iki11)}
*******************************************************************
""")
        elif islem == 13:
            bir12 = int(input("Sayıyı giriniz:"))
            print(f"""{math.log1p(bir12-1)}
*******************************************************************
""")
        elif islem == 14:
            bir13 = int(input("Sayıyı giriniz:"))
            print(f"""{math.log2(bir13)}
*******************************************************************
""")
        elif islem == 15:
            bir14 = int(input("Sayıyı giriniz:"))
            print(f"""{math.log10(bir14)}
*******************************************************************
""")
        elif islem == 16:
            bir15 = int(input("Sayıyı giriniz:"))
            iki15 = int(input("Dereceyi giriniz:"))
            print(f"""{math.pow(bir15,iki15)}
*******************************************************************
""")
        elif islem == 17:
            bir16 = int(input("Karekök hesaplamak istediğiniz sayıyı giriniz:"))
            print(f"""{math.sqrt(bir16)}
*******************************************************************
""")
        elif islem == 18:
            bir17 = int(input("Sayıyı giriniz:"))
            print(f"""{math.degrees(bir17)}
*******************************************************************
""")
        elif islem == 19:
            bir18 = int(input("Sayıyı giriniz:"))
            print(f"""{math.radians(bir18)}
*******************************************************************
""")
        elif islem == 20:
            islem20 = int(input("EBOB için '1', EKOK için '2'ye basınız:"))
            if islem20 == 1:
                bir191 = int(input("Birinci sayıyı giriniz:"))
                iki191 = int(input("İkinci sayıyı giriniz:"))
                print(f"""{math.gcd(bir191,iki191)}
*******************************************************************
""")
            elif islem20 == 2:
                sayi1 = int(input("Birinci sayıyı giriniz:"))
                sayi2 = int(input("İkinci sayıyı giriniz:"))
                print(f"""{ekok(sayi1,sayi2)}
*******************************************************************
""")
            else:
                print("Hatalı tuşlama...")
        elif islem == 21:
            islem21 = int(input("Permütasyon için '1', Kominasyon için '2'ye basınız:"))
            if islem21 == 1:
                bir201 = int(input("Birinci sayıyı giriniz:"))
                iki201 = int(input("İkinci sayıyı giriniz:"))
                print(f"""{math.perm(bir201,iki201)}
*******************************************************************
""")
            elif islem21 == 2:
                bir202 = int(input("Birinci sayıyı giriniz:"))
                iki202 = int(input("İkinci sayıyı giriniz:"))
                print(f"""{math.comb(bir202, iki202)}
*******************************************************************
""")
            else:
                print("Hatalı tuşlama...")
        elif islem == "e" or islem == "pi" or islem == "tau":
            print(f"""
            e:{math.e}
            pi:{math.pi}
            tau:{math.tau}
            """)
        else:
            print("Hatalı işlem tekrar deneyiniz")
'''
import time
import random
sehir_listesi = ["adana", "adıyaman", "afyonkarahisar", "ağrı", "aksaray", "amasya", "ankara", "antalya",
                         "ardahan", "artvin", "aydın", "balıkesir", "bartın", "batman", "bayburt", "bilecik", "bingöl",
                         "bitlis", "bolu", "burdur", "bursa", "çanakkale", "çankırı", "çorum", "denizli", "diyarbakır",
                         "düzce", "edirne", "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep", "giresun",
                         "gümüşhane", "hakkari", "hatay", "ığdır", "ısparta", "istanbul", "izmir", "kahramanmaraş",
                         "karabük", "karaman", "kars", "kastamonu", "kayseri", "kilis", "kırıkkale", "lırklareli",
                         "kırşehir", "kocaeli", "konya", "kütahya", "malatya", "manisa", "mardin", "mersin", "muğla",
                         "muş", "nevşehir", "niğde", "ordu", "osmaniye", "rize", "sakarya", "Samsun", "şanlıurfa",
                         "siirt", "sinop", "sivas", "şırnak", "tekirdağ", "tokat", "trabzon", "tunceli", "uşak", "van",
                         "yalova", "yozgat", "zonguldak"]
sehir = random.choice(sehir_listesi)
harfler = []
x = len(sehir)
z = list("_" * x)
print("""      ...Adam asmaca oyununa hoş geldiniz...
            Çıkmak için 'q' ya basınız.
        Unutmayın yanlış yapmak için sadece 7 hakkınız var
""")
print(''.join(z),f":{len(sehir)} tane harf içeren kelime", end="\n")
hak = 7
while hak > 0:
    harf = input("Kelime içinde olabileceğine inandığınız harfi giriniz:")
    if harf in harfler:
        print("Aynı harfi bir kere daha giremezsin...")
        continue
    elif harf == "q" or harf == "Q":
        print("Oyun kapatılıyor...")
        time.sleep(1)
        break
    elif not harf:
        print("Boş bırakılamaz...")
    elif len(harf) > 1:
        print("Sadece bir harf girilebilir...")
        continue
    elif hak == 0:
        print("Hakkınız bitti. Adam asıldı...")
        print(f"Bilemediğin kelime:{sehir}")
        break
    elif harf not in sehir:
        print(f"{harf} harfi kelimemizin içinde yok :((")
        hak -= 1
        print(f"Tahmin hakkınız:{hak}")
    else:
        for i in range(len(sehir)):
            if sehir[i] == harf:
                print("Doğru tahmin:))")
                z[i] = harf
                harfler.append(harf)
        print(''.join(z),f":{len(sehir)} tane harf içeren kelime", end="\n")
        a = input("Kelimeyi tahmin etmek ister misin ? ('E' ya da 'H'):")
        if a == "e" or a == "E":
            a0 = input("Tahmininiz:")
            if a0 == sehir:
                print(f"Doğru bildiniz. Kelimemiz {a0}...")
                break
            else:
                print("Tahmin hatalı tekrar deneyiniz")
                hak -= 1
                print(f"Tahmin hakkınız:{hak}")
        else:
            print("")

if hak == 0:
    print(sehir)