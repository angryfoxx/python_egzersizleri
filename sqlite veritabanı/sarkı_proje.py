import sqlite3
import time


class Sarki():
    def __init__(self,isim,sanatçı,albüm,şirket,sarkıuzunluk):
        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.şirket = şirket
        self.sarkıuzunluk = sarkıuzunluk
    def __str__(self):
        return f"Şarkı İsmi:{self.isim}\nSanatçı:{self.sanatçı}\nAlbüm:{self.albüm}\nProdüksiyon Şirketi:{self.şirket}\nŞarkı Süresi:{self.sarkıuzunluk}"

class iPod():
    def __init__(self):
        self.connection()
    def connection(self):
        self.con = sqlite3.connect("ipod.db")
        self.curs = self.con.cursor()
        tablo = "CREATE TABLE IF NOT EXISTS playlist(Şarkı_İsmi TEXT,Sanatçı TEXT,Albüm TEXT,Plak_Şirketi TEXT,Şarkı_Süresi INT)"
        self.curs.execute(tablo)
        self.con.commit()
    def c_connection(self):
        self.con.close()
    def add_songs(self, sarki):
        sorgu = "INSERT INTO playlist VALUES(?,?,?,?,?)"
        self.curs.execute(sorgu, (sarki.isim,sarki.sanatçı,sarki.albüm,sarki.şirket,sarki.sarkıuzunluk))
        self.con.commit()
    def del_songs(self, isim):
        sorgu = "DELETE FROM playlist WHERE Şarkı_İsmi = ?"
        self.curs.execute(sorgu, (isim,))
        self.con.commit()
    def data(self):
        sorgu = "SELECT * FROM playlist"
        self.curs.execute(sorgu)
        song_list = self.curs.fetchall()
        if len(song_list) == 0:
            print("Playlistinizde hiç şarkı yok...")
        else:
            for i in song_list:
                song = Sarki(i[0],i[1],i[2],i[3],i[4],)
                print("********************************")
                print(song)

    def select_data(self, a):
        sorgu = "SELECT * FROM playlist WHERE Şarkı_İsmi = ? "
        self.curs.execute(sorgu, (a,))
        song_list = self.curs.fetchall()
        if len(song_list) == 0:
            print("Playlistinizde böyle bir şarkı yok...")
        else:
            for i in song_list:
                song = Sarki(i[0], i[1], i[2], i[3], i[4], )
                print("********************************")
                print(song)
    def plus_len(self):
        sorgu = "SELECT * FROM playlist"
        self.curs.execute(sorgu)
        song_list = self.curs.fetchall()
        if len(song_list) == 0:
            print("Playlistinizde hiç şarkı yok...")
        else:
            sorgu0 = "SELECT Şarkı_Süresi FROM playlist"
            self.curs.execute(sorgu0)
            song_len = self.curs.fetchall()
            uzunluk = 0
            for i in song_len:
                for j in i:
                    uzunluk += j
            islem = ( uzunluk / 60 ) / 60
            islem0 = str(islem).split(".")
            dakika = float("0." + islem0[1]) * 60
            islem1 = str(dakika).split(".")
            saniye = float("0." + islem1[1]) * 60
            islem2 = str(saniye).split(".")
            print(f"\nPlaylisti toplam: '{islem0[0]}' Saat, '{islem1[0]}' Dakika, '{islem2[0]}' Saniye\n")
