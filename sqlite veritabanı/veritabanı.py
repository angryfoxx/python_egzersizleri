__author__ = "FOX"
import sqlite3
"""
con  = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa sayısı INT)")
    con.commit()
def veri_ekleme_oto():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul hatırası','Ahmet Ümit','Everest',571)")
    con.commit()
def veri_ekleme_man(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
isim = input("Kitap ismini giriniz:")
yazar = input("Yazar ismini giriniz:")
yayinevi = input("Yayınevi ismini giriniz:")
sayfa_sayisi = int(input("Sayfa sayısını giriniz:"))
veri_ekleme_man(isim,yazar,yayinevi,sayfa_sayisi)

con.close()
"""
""""
con = sqlite3.connect("deneme.db")
curs = con.cursor()
def baglanti():
    curs.execute("CREATE TABLE IF NOT EXISTS deneme(birinci TEXT,ikinci TEXT,üçüncü TEXT,dördüncü TEXT,beşinci INT)")
    con.commit()
def baglantik():
    con.close()
def veri(bir,iki,uc,dort,bes):
    curs.execute("INSERT INTO deneme VALUES(?,?,?,?,?)",(bir,iki,uc,dort,bes))
    con.commit()
while True:
    a = input("deger gir:")
    if a == "q":
        break
    elif a == "1":
        baglanti()
    elif a == "2":
        bir = input("birinci TEXT:")
        iki = input("ikinci TEXT:")
        uc = input("üçüncü TEXT:")
        dort = input("dördüncü TEXT:")
        bes = int(input("beşinci INT:"))
        veri(bir,iki,uc,dort,bes)
    elif a == "3":
        baglantik()
        break
"""
"""def silme(x):
    sorgu = "Delete From deneme where isim = ?"
    curs.execute(sorgu, (x,))
    con.commit()
con = sqlite3.connect("deneme.db")
curs = con.cursor()

a = input("deeger:")
silme(a)
if a == "q":
    con.close()
"""
"""con  = sqlite3.connect("deneme.db")
curs = con.cursor()

x = input("veri:")
a = input("isim:")
b = input("ikinci:")
c = input("üçüncü:")
d = input("dördüncü:")
e = int(input("beşinci:"))

sorgu0 = "UPDATE deneme SET isim = ?,ikinci = ?,üçüncü = ?,dördüncü = ?,beşinci = ? WHERE isim = ?"
curs.execute(sorgu0, (a, b, c, d, e, x,))
con.commit()

sorgu = "SELECT * FROM deneme"
curs.execute(sorgu)
xxf = curs.fetchall()
for i in xxf:
    print(i)
con.close()
"""