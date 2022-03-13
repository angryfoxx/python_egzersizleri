"""
ad = "Ömer Faruk"
soyad = "Korkmaz"
yas  = "18"
sinif = "12"
print("Adım",ad,",")
print("Soyadım",soyad,".")
print(yas,"yaşındayım,")
print(sinif,".sınıfa gidiyorum")

print("Şimdi size üstün işlem yeteneklerimi sergileyeceğim...")
a = 500+300
b = 8000-4000
c = 700/2
d = 500/3
print("500+300=",a)
print("8000-4000=",b)
print("700/2=",c)
print("500/3=",d)
"""
"""
def selamla():
    print("\t\tLise Yılsonu Başarı Puanı Hesaplama Aracına Hoşgeldiniz...")
selamla()
a = input("Öğrencinin adını ve soyadını giriniz:")
print("Sayın: {} \nLütfen ders notlarınızı ve saatlerini doğru şekilde giriniz.".format(a))
mat = int(input("Öğrencinin Matematik notunu giriniz:"))
mats = int(input("Öğrencinin Matematik dersi kaç saat:"))
bio = int(input("Öğrencinin Biyoloji notunu giriniz:"))
bios = int(input("Öğrencinin Biyoloji dersi kaç saat:"))
kim = int(input("Öğrencinin Kimya notunu giriniz:"))
kims = int(input("Öğrencinin Kimya dersi kaç saat:"))
fiz = int(input("Öğrencinin Fizik notunu giriniz:"))
fizs = int(input("Öğrencinin Fizik dersi kaç saat:"))
cog = int(input("Öğrencinin Coğrafya notunu giriniz:"))
cogs = int(input("Öğrencinin Coğrafya dersi kaç saat:"))
ydil = int(input("Öğrencinin Yabancı Dil notunu giriniz:"))
ydils = int(input("Öğrencinin Yabancı Dil dersi kaç saat:"))
tar = int(input("Öğrencinin İnkılap notunu giriniz:"))
tars = int(input("Öğrencinin İnkilap dersi kaç saat:"))
ds = mats+kims+fizs+cogs+ydils+tars+bios
apo = (mat*mats)+(kim*kims)+(fizs*fiz)+(cog*cogs)+(ydil*ydils)+(tar*tars)+(bio*bios)
ort = apo/ds
print("Öğrencinin ağırlıklı puan ortalaması: {}\nÖğrencinin Sene Sonu Ortalaması: {}\n"
      "Öğrencinin ağırlıklı puan ortalaması: {}".format(apo,ort,ds))
if ort >= 85:
    print("Sınıfı geçmeye ve Takdir belgesi almaya hak kazandınız.Tebrikler...")
elif ort >= 70 and ort <= 84.99:
    print("Sınıfı geçmeye ve Teşekkür belgesi almaya hak kazandınız.Tebrikler...")
elif ort >= 50 and ort <= 69.99:
    print("Sınıfı geçmeye hak kazandınız.Maalesef belge alabilecek kadar çalışkan değilsiniz...")
else:
    print("Sınıfı geçmeye hakkınız yok.Daha çok çalış aptal!")
"""
"""
print(""********************************
Hesap Makinesi...

İşlemler;

1.Toplama işlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4. Bölme işlemi


********************************
"")

a = float(input("Birinci sayıyı giriniz:"))
b = float(input("İkinci sayıyı giriniz:"))
islem = input("Yapmak istediğiniz işlemi seçiniz:")
if islem == "1":
    print("{} ile {} toplamı {} dur".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} farkı {} dur".format(a,b,a*b))
elif islem == "3":
    print("{} ile {} çarpımı {} dur".format(a,b,a*b))
elif islem == "4":
    print("{} ile {} bölümü {} dur".format(a,b,a/b))
else:
    print("İşlem geçersiz")
"""
"""
print("\t\t\tEn büyük sayıyı bulurum!xd")
a = int(input("Bir sayı giriniz:"))
b = int(input("Bir sayı daha giriniz:"))
c = int(input("Bir sayı daha giriniz:"))

if a > b and a > c:
    print("En büyük sayı {}'dır.".format(a))
elif b > c and b > a:
    print("En büyük sayı {}'dır.".format(b))
else:
    print("En büyük sayı {}'dır.".format(c))
"""
"""
vize1 = float(input("Birinci vize notunuzu giriniz:"))
vize2 = float(input("İkinci vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))

toplam_not = (vize1*0.3)+(vize2*0.3)+(final*0.4)

if toplam_not >=90:
    print("Notunuz AA")
elif toplam_not >=85:
    print("Notunuz BA")
elif toplam_not >=80:
    print("Notunuz BB")
elif toplam_not >=75:
    print("Notunuz CB")
elif toplam_not >=70:
    print("Notunuz CC")
elif toplam_not >=65:
    print("Notunuz DC")
elif toplam_not >=60:
    print("Notunuz DD")
elif toplam_not >=55:
    print("Notunuz FD")
elif toplam_not >=50:
    print("Notunuz FF")
else:
    print("Maalesef tekrar denemelisin...")
"""
'''
def geo():
    print("\t\t\tGeometrik şekil hesaplama aracına hoşgeldiniz...")
    geo()
print("""**********
İşlemler;
1.Üçgen
2.Dörtgen
**********
""")
while True:
    isl = input("Yapmak istediğiniz işlemi seçiniz(Çıkmak için 'q'ya basın):")
    if (isl == "q"):
        print("Program kapanıyor...")
        break
    elif isl == "2":
        birk = abs(int(input("Birinci kenarı giriniz:")))
        ikik = abs(int(input("İkinci kenarı giriniz:")))
        uck = abs(int(input("Üçüncü kenarı giriniz:")))
        dortk = abs(int(input("Dördüncü kenarı giriniz:")))
        if birk and ikik and uck and dortk == birk:
            print("Verdiğiniz değerlere göre geometrik şekliniz bir KARE!!!")
        elif (birk == ikik and uck == dortk) or (birk == uck and ikik == dortk) or (birk == dortk and ikik == uck):
            print("Verdiğiniz değerlere göre geometrik şekliniz bir DİKDÖRTGEN!!!")
        else:
            print("Verdiğiniz değerlere göre geometrik şekliniz bir DÖRTGEN!!!")
    elif isl == "1":
        a = abs(int(input("Birinci kenarı giriniz:")))
        b = abs(int(input("İkinci kenarı giriniz:")))
        c = abs(int(input("Üçüncü kenarı giriniz:")))
        if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
            if a and b and c == a:
                print("Verdiğiniz değerlere göre geometrik şekliniz bir EŞKENAR ÜÇGEN!!!")
            elif a == b or a == c or b == c:
                print("Verdiğiniz değerlere göre geometrik şekliniz bir İKİZKENAR ÜÇGEN!!!")
            else:
                print("Verdiğiniz değerlere göre geometrik şekliniz bir ÜÇGEN!!!")
        else:
            print("Verdiğiniz değerlere göre bir üçgen oluşturulamaz!!!")

    else:
        print("HATALI İŞLEM!!!!!!!!!!!!!!!!")
    a = input("Yeniden hesap yapmak için 'Y'e kapatmak için 'N'ye basınız:")
    if a == "N":
        print("Program kapanıyor...")
        break
'''
"""
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12],[13,14,15]]
liste1 = list()
for i in liste:
    for j in i:
        liste1.append(j)
print(liste1)

liste = [[1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14],[15]]
liste1 = [x for i in liste for x in i]
print(liste1)
"""
'''
print("""*****************
Faktöriyel hesaplama programına hoşgeldiniz.
Çıkmak için 'q'ya basınız.
*****************
""")
while True:
    sayi = input("Faktöriyelini almak istediğiniz sayıyı giriniz:")
    if (sayi == "q") :
        print("Program kapatılıyor...")
        break
    sayi = int(sayi)
    faktoriyel = 1
    for i in range(2,sayi+1):
        faktoriyel *= i
    print("Faktoriyel:", faktoriyel)

a = 1
b = 1
fibonacci = [a,b]
for i in range(40):
    a,b = b,a+b
    
    fibonacci.append(b)
print(fibonacci)
'''
"""
a = int(input("Bölenlerini bulmak istediğiniz sayıyı giriniz:"))
liste = list()
for i in range(1,a+1):
    if a % i == 0:
        liste.append(i)
print(f"{a}'nın tam bölenleri = {liste}")
"""
'''import random
import time
tarla = list("""
""")
print("""❤❤❤💣💣💣...Mayın Tarlası...💣💣💣❤❤❤
/-/Zorluk seviyeleri/-/
    Kolay: 1
    Orta: 2
    Zor: 3
Çıkmak için 'q' ya basınız...
---------------------------------------------""")
z_dict ={1:50,2:80,3:143}
while True:
    zorluk = input("Zorluk seçiniz:")
    if zorluk == "q" or zorluk == "Q":
        print("Program kapatılıyor...")
        time.sleep(1)
        break
    elif not zorluk:
        print("Boş bırakılamaz.")
        continue
    elif len(zorluk) > 1:
        print("Birden fazla rakam girilemez.")
        continue
    elif zorluk == "1" or zorluk == "2" or zorluk == "3":
        print("Oyun hazırlanıyor")
        time.sleep(1.5)
        print("""1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
1-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
2-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
3-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
4-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
5-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
6-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
7-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
8-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
9-🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
""")
        zorluk = int(zorluk)
        toplam = -1
        bomb = random.choices(population=tarla,k=(z_dict[zorluk]))
        print(f"Zorluk seviyesi {zorluk}. seviye olarak seçildi.\nDikkat edin {z_dict[zorluk]} tane mayınla karşı karşıyasınız...")
        print(bomb)
        while True:
            a = int(input("Mayınların olmadığı bölgeyi seçin(Önce yukardan aşağı):"))
            b = int(input("Mayınların olmadığı bölgeyi seçin(Şimdi soldan sağa):"))
            if a == 1:
                toplam += b
            elif a > 9 or b > 18:
                print("Yukardan aşağı için 9, soldan sağa için en fazla 18'i tuşlayabilirsiniz...")
                continue
            else:
                toplam += (18 * (a - 1) + b) + (a - 1)
            for j in bomb:
                if toplam == j:
                    tarla[j - 1] = "💣"
                    print("MAYINA YAKALANDINIZ!!!!")
                    print("".join(tarla))
                    break
                else:
                    print("Bir sorun yok")
                    tarla[toplam] = "❤"
                    toplam = -1
                    print("".join(tarla))
    else:
        print("Hatalı işlem")
        '''

