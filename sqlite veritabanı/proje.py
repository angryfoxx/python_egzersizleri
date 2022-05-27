import sqlite3
import time


class Kitap():
    def __init__(self, isim, yazar, tur, yayinevi, baski):
        self.isim = isim
        self.yazar = yazar
        self.tur = tur
        self.yayinevi = yayinevi
        self.baski = baski

    def __str__(self):
        return f"İsim:{self.isim}\nYazar:{self.yazar}\nTür:{self.tur}\nYayınevi:{self.yayinevi}\nBaskı:{self.baski}"

class kutuphane():
    def __init__(self):
        self.baglantiolustur()

    def baglantiolustur(self):
        self.con = sqlite3.connect("kütüphane.db")
        self.curs = self.con.cursor()
        tablo = "CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT,yazar TEXT,tür TEXT,yayınevi TEXT,baskı INT)"
        self.curs.execute(tablo)
        self.con.commit()

    def baglantikes(self):
        self.con.close()

    def veriekleme(self, isim, yazar, tur, yayinevi, baski):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.curs.execute(sorgu, (isim, yazar, tur, yayinevi, baski,))
        self.con.commit()

    def verisilme(self, a):
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.curs.execute(sorgu, (a,))
        self.con.commit()

    def bilgilerigoster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.curs.execute(sorgu)
        kitaplar = self.curs.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor......")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print("************************")
                print(kitap)
    def verisorgulama(self, a):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.curs.execute(sorgu, (a,))
        kitaplar = self.curs.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor......")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
    def baskiyukselt(self, a):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.curs.execute(sorgu, (a,))
        kitaplar = self.curs.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor......")
        else:
            baski = kitaplar[0][4]
            baski += 1
            sorgu2 = "UPDATE kitaplar SET baskı = ? WHERE isim = ?"
            self.curs.execute(sorgu2, (baski, a,))
            self.con.commit()
