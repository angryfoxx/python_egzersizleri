__author__ = "FOX"
from datetime import datetime

'''
def kayit():
    a = input("Öğrencinin adını ve soyadını giriniz:")
    b = input("Öğrencinin numarasını giriniz:")
    algo1 = int(input("'Algoritma' dersinin notunu giriniz:"))
    eem_giris1 = int(input("'Elektrik Elektronik Mühendisliğine Giriş' dersinin notunu giriniz:"))
    mat1 = int(input("'Matematik' dersinin notunu giriniz:"))
    if not a or not b or not algo1 or not eem_giris1 or not mat1:
        print("LÜTFEN HİÇBİR YERİ BOŞ BIRAKMAYINIZ")
    with open("Öğrenci ders notları.txt","a",encoding="utf-8") as file:
        file.write(f"{b},")
        if algo1<50:
            file.write(f"{a},FF")
        elif algo1>=50 and algo1<70:
            file.write(f"{a},CC")
        else:
            file.write(f"{a},AA")
        if eem_giris1<50:
            file.write(",FF")
        elif eem_giris1>=50 and eem_giris1<70:
            file.write(",CC")
        else:
            file.write(",AA")
        if mat1<50:
            file.write(",FF\n")
        elif mat1>=50 and mat1<70:
            file.write(",CC\n")
        else:
            file.write(",AA\n")

def not_hesap(veri):
    # Benim yaptığım öğrenci listesinden bir örnek:  374,Mustafa Kürşat,FF,AA,DD
    # Kalmayı ve geçmeyi problemi yapmak için kendime göre kurguladım bir gerçeklik barındırmıyor.
    # 3 FF veya 2 FF aldığı her durumda dersten kalır. Geri kalan durumlarda dersten geçer.
    veri = veri [:-1] # sondaki '\n'i siliyoruz
    kalanlar = []
    gecenler = []
    liste = veri.split(",") # öğrenci verilerilerini virgüller ile ayırıyoruz
    numara = liste[0] # öğrencinin numarasına ulaşıyoruz
    isim = liste[1]   # öğrencinin ismine ulaşıyoruz
    na = liste[2]     # öğrencinin ilk ders notuna ulaşıyoruz
    ne = liste[3]     # öğrencinin ikinci ders notuna ulaşıyoruz
    nm = liste[4]     # öğrencinin üçüncü ders notuna ulaşıyoruz
    if na == "FF" and ne == "FF" and nm == "FF":
        kalanlar.append(f"{isim,numara} --------------------> Kaldınız\n")
    elif na == "FF" and ne == "FF" or na == "FF" and nm == "FF" or nm == "FF" and ne == "FF":
        kalanlar.append(f"{isim,numara} --------------------> Kaldınız\n")
    else:
        gecenler.append(f"{isim,numara} --------------------> Geçtiniz\n")
    with open("Kalanlar.txt", "a", encoding="utf-8") as file:
        for i in kalanlar:
            file.write(i)
    with open("Geçenler.txt", "a", encoding="utf-8") as file:
        for i in gecenler:
            file.write(i)
def bilgi():
    while True:
        a= input("""Öğrencilerin notlarını öğrenmek için '1'
Kalan öğrencileri öğrenmek için '2'
Geçen öğrencileri öğrenmek için '3'
Çıkmak için 'q'ya basınız
""")
        if a == "1":
            with open("Öğrenci ders notları.txt","r",encoding="utf-8") as file:
                print(file.read())
        elif a == "2":
            with open("Kalanlar.txt","r",encoding="utf-8") as file:
                print(file.read())
        elif a == "3":
            with open("Geçenler.txt", "r", encoding="utf-8") as file:
                print(file.read())
        elif a == "q" or a == "Q":
            break
        else:
            print("Hatalı tuşlama tekrar deneyiniz...")
print("""
Öğrenci kayıt etmek ve not girmek için: 1
Öğrenci ve notlar hakkında bilgi sahibi olmak için: 2


Çıkmak için 'q' ya basınız


""")
while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz:")
    if islem == "q" or islem == "Q":
        print("Program kapatılıyor...")
        break
    elif islem == "1":
        kayit()
    elif islem == "2":
        with open("Öğrenci ders notları.txt", "r", encoding="utf-8") as file:
            for i in file:
                not_hesap(i)
        bilgi()
    else:
        print("Hatalı işlem...Tekrar deneyiniz...")
''' #öğrenci kayı,not hesap vs.
"""
def kayt(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    oyuncular = liste[0]
    takimlar = liste[1]
    if takimlar == "Galatasaray":
        with open("gs.txt","a",encoding="utf-8") as file:
            file.write(f"{oyuncular}\n")
    if takimlar == "Beşiktaş":
        with open("bjk.txt","a",encoding="utf-8") as file:
            file.write(f"{oyuncular}\n")
    if takimlar == "Fenerbahçe":
        with open("fb.txt","a",encoding="utf-8") as file:
            file.write(f"{oyuncular}\n")
with open("C:\\Users\\Fox\\Desktop\\takımlar.txt","r+",encoding="utf-8") as file:
    for i in file:
        kayt(i)
"""
"""
class Dosya():
    def __init__(self):
        with open("text/metin.txt","r",encoding="utf-8") as self.file:
            dosya_icerigi = self.file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip()
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("Bütün kelimeler....")
        for i in kelimeler_kumesi:
            print(i)
            print("******************************************")
    def kelime_frekansi(self):
        self.kelime_sayisi = dict()
        for i in self.sade_kelimeler:
            if i in self.kelime_sayisi:
                self.kelime_sayisi[i] += 1
            else:
                self.kelime_sayisi[i] = 1
        for kelime,sayi in self.kelime_sayisi.items():
            print(f"{kelime} kelimesi paragraf içinde '{sayi}' kere geçmiş ")
            print("************************************************************************")
    def kelime_bulma(self):
        while True:
            a = input("Bulmak istediğiniz kelimeyi giriniz:")
            try:
                for i,j in enumerate(self.sade_kelimeler):
                    if j == a:
                        print(f"{a} Kelimesi tam burada {i}")
                if sys.stdout.read() == None:
                    print("Lütfen metin içinde olan kelimeleri giriniz.")
            except ValueError:
                print("Lütfen metin içinde olan kelimeleri giriniz.")
dosya = Dosya()
print(dosya.kelime_bulma())
 """# metin üzerinde dosya işlemleri
"""
string = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
harf_sayisi = dict()
for i in string.lower():
    if i in harf_sayisi:
        harf_sayisi[i] += 1
    else:
        harf_sayisi[i] = 1

for harf,sayisi in harf_sayisi.items():

    print(f"'{harf}' harfi '{sayisi}' tane bulunmakta")
    print("*********************************************")
""" # harf sayısı bulma |Problem 1
"""
bas_harf = ""
with open("şiir.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")
        bas_harf += i[0]
print(bas_harf)
""" # baş harf yazdırma |Problem 2
"""
with open("mail.txt","r+",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")
        i = i.split(":")
        i.pop()
        for j in i:
            with open("mailler.txt","a",encoding="utf-8") as file2:
                file2.write(f"{j}\n")
"""
"""
with open("text/mail0.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")
        i0 = i.endswith(".com")
        i1 = i.find("@")
        if i0 == True and i1 != -1:
            print(i)
""" # mail olup olmadığını doğrıulama |Problem 3
"""
isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
liste = list(zip(isim,soyisim))
liste.sort()
for i,j in liste:
    print(i,j)
""" # isimleri alfabetik sıraya sokma |Problem 4
suan = datetime.now().strftime("%H.%M  |  %d.%m.%Y")
print(suan)