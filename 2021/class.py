'''
import random
import time
class Kumanda():
    def __init__(self,tv_durumu = "Kapalı", tv_ses = 0, tv_kanal = "TRT",kanal_listesi = ["TRT"]):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.tv_kanal = tv_kanal
        self.kanal_listesi = kanal_listesi
    def tv_ac(self):
        if (self.tv_durumu=="Açık"):
            print("Tv zaten açık")
        else:
            print("Televizyon açılıyor")
            time.sleep(1)
            self.tv_durumu = "Açık"
    def tv_kapat(self):
        if (self.tv_durumu=="Kapalı"):
            print("Tv zaten Kapalı")
        else:
            print("Televizyon Kapanıyor")
            time.sleep(1)
            self.tv_durumu = "Kapalı"
    def ses_seviye(self):
        while True:
            a = input("Artırmak için '>' azaltmak için '<' tuşuna basınız:")
            if self.tv_durumu == "Kapalı":
                print("TV kapalı.Öncelikle açmayı dene...")
                break
            elif (a == ">"):
                if self.tv_ses != 50:
                    self.tv_ses += 1
                    print(f"Ses artırılıyor.\nYeni Ses seviyesi {self.tv_ses}")
                elif self.tv_ses == 50:
                    print("Ses seviyesi minimum")
                else:
                    print("Hatalı tuşlama")
            elif a == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print(f"Ses azaltılıyor.\nYeni Ses seviyesi {self.tv_ses}")
                elif self.tv_ses == 0:
                    print("Ses seviyesi minimum")
                else:
                    print("Hatalı tuşlama")
            elif a == "q" or a == "Q":
                break
            else:
                print("Ses maksimum seviyede")
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print(f"Şuan ki kanal:{self.kanal}")
    def __len__(self):
        print(f"{len(self.kanal_listesi)} tane kanal var")
    def __str__(self):
        print(f"Tv durumu:{self.tv_durumu}\nSes seviyesi:{self.tv_ses}\nŞuan ki kanal:{self.tv_kanal}\nKanal listesi:{self.kanal_listesi}")
kumanda = Kumanda()

print("""...Bilgilendirme...
1-) Televizyonu açma
2-) Televizyonu kapatma
3-) Ses ayarları
4-) Kanal ekleme
5-) Rastgele kanal
6-) Kanal listesi
7-) Tv bilgisi
""")
while True:
    a1 = input("Yapmak istediğiniz işlemi seçiniz:")
    if a1 == "1":
        kumanda.tv_ac()
    elif a1 == "2":
        kumanda.tv_kapat()
    elif a1 == "3":
        kumanda.ses_seviye()
    elif a1 == "4":
        if kumanda.tv_durumu == "Kapalı":
            print("TV kapalı.Öncelikle açmayı dene...")
        else:
            a0 = input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz:")
            for eklenecekler in a0.split(','):
                kumanda.kanal_ekle(eklenecekler)
                print(f"Kanallara {eklenecekler} kanalı eklendi!!!")
    elif a1 == "5":
        if kumanda.tv_durumu == "Kapalı":
            print("TV kapalı.Öncelikle açmayı dene...")
        else:
            kumanda.rastgele_kanal()
    elif a1 == "6":
        kumanda.__len__()
    elif a1 == "7":
        kumanda.__str__()
    elif a1 == "q" or a1 == "Q":
        print("Program kapatılıyor...")
        time.sleep(1)
    else:
        print("Hatalı tuşlama...")
        time.sleep(1)
        print("Tekrar deneyiniz")
'''
import datetime
import time

'''
import time
import random
class Bilgisayar():
    def __init__(self,pc_os="Windows 10",pc_hesap=["Ömer"],pc_durum="Kapalı",pc_ses=0,pc_lan="Bağlantı yok",
                 pc_fan="Kapalı",pc_moni="Kapalı",pc_ariza="Yok",
                 pc_oyun=["Adam Asmaca","Mükemmel sayı","Armstrong sayısı","Değişken toplama"],
                 pc_cevre=["Monitör","Klavye","Fare","Hoparlör"]):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.pc_lan = pc_lan
        self.pc_fan = pc_fan
        self.pc_moni = pc_moni
        self.pc_ariza = pc_ariza
        self.pc_oyun = pc_oyun
        self.pc_cevre = pc_cevre
        self.pc_hesap = pc_hesap
        self.pc_os = pc_os

    def pc_on(self):
        print("Bilgisayar açılıyor")
        time.sleep(1)
        self.pc_durum = "Açık"
        print("Hoş geldiniz")
    def pc_off(self):
        print("Bilgisayar Kapanıyor")
        time.sleep(1)
        self.pc_durum = "Kapalı"
        self.pc_fan = "Kapalı"
    def moni_on(self):
        time.sleep(1)
        print("Windows 10")
        self.pc_moni = "Açık"
    def moni_off(self):
        time.sleep(1)
        self.pc_moni = "Kapalı"
    def hesap(self,hesap_ekle):
        self.pc_hesap.append(hesap_ekle)
        print(f"{self.pc_os} işletim sistemli bilgisayarınıza {hesap_ekle} adlı hesabı başarıyla eklediniz...")
    def ses_seviyesi(self):
        while True:
            volume_up_down = input("Sesi artırmak için '>', azaltmak için '<' tuşuna basınız:")
            if volume_up_down == ">":
                if self.pc_ses != 100:
                    self.pc_ses += 2
                    print(f"Ses seviyesi:{self.pc_ses}")
                    continue
                else:
                    print("Ses maksimum seviyesinde")
                    continue
            elif volume_up_down == "<":
                if self.pc_ses != 0:
                    self.pc_ses -= 2
                    print(f"Ses seviyesi:{self.pc_ses}")
                    continue
                else:
                    print("Ses minimum seviyesinde")
                    continue
            else:
                print("Hatalı tuşlama")
                continue
    def pc_lan_on(self):
        print("İnternet açılıyor")
        time.sleep(1)
        self.pc_lan = "Açık"
        print("...Ağ bağlantınız stabil...")
    def pc_lan_off(self):
        print("İnternet Kapanıyor")
        time.sleep(1)
        self.pc_lan = "Kapalı"
        print("...Ağ bağlantınız kesildi...")
    def pc_fanse(self):
        fan_up_down = input("Fan hızı artırmak için '>', azaltmak için '<' tuşuna basınız:")
        click_press = 0
        if fan_up_down == ">":
            click_press += 1
            if click_press == 1:
                self.pc_fan = "Yavaş"
                print(f"Fan durumu:{self.pc_fan}")
            elif click_press == 2:
                self.pc_fan = "Orta"
                print(f"Fan durumu:{self.pc_fan}")
            elif click_press == 3:
                self.pc_fan = "Hızlı"
                print(f"Fan durumu:{self.pc_fan}")
            else:
                print("")
        elif fan_up_down == "<":
            click_press -= 1
            if click_press == 1:
                self.pc_fan = "Yavaş"
                print(f"Fan durumu:{self.pc_fan}")
            elif click_press == 2:
                self.pc_fan = "Orta"
                print(f"Fan durumu:{self.pc_fan}")
            elif click_press == 3:
                self.pc_fan = "Hızlı"
                print(f"Fan durumu:{self.pc_fan}")
            else:
                print("")
        else:
            print("Hatalı tuşlama")
    def oyun(self):
        oyun_secme = input(f"Oyun listesi:{self.pc_oyun}\nOynamak istediğiniz oyunları sırasına göre numerik olarak seçiniz:")
        if oyun_secme == "1":
            sehir_listesi = ["adana", "adıyaman", "afyonkarahisar", "ağrı", "aksaray", "amasya", "ankara", "antalya",
                             "ardahan", "artvin", "aydın", "balıkesir", "bartın", "batman", "bayburt", "bilecik",
                             "bingöl",
                             "bitlis", "bolu", "burdur", "bursa", "çanakkale", "çankırı", "çorum", "denizli",
                             "diyarbakır",
                             "düzce", "edirne", "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep", "giresun",
                             "gümüşhane", "hakkari", "hatay", "ığdır", "ısparta", "istanbul", "izmir", "kahramanmaraş",
                             "karabük", "karaman", "kars", "kastamonu", "kayseri", "kilis", "kırıkkale", "lırklareli",
                             "kırşehir", "kocaeli", "konya", "kütahya", "malatya", "manisa", "mardin", "mersin",
                             "muğla",
                             "muş", "nevşehir", "niğde", "ordu", "osmaniye", "rize", "sakarya", "Samsun", "şanlıurfa",
                             "siirt", "sinop", "sivas", "şırnak", "tekirdağ", "tokat", "trabzon", "tunceli", "uşak",
                             "van",
                             "yalova", "yozgat", "zonguldak"]
            sehir = random.choice(sehir_listesi)
            harfler = []
            x = len(sehir)
            z = list("_" * x)
            print("""      ...Adam asmaca oyununa hoş geldiniz...
                        Çıkmak için 'q' ya basınız.
                    Unutmayın yanlış yapmak için sadece 7 hakkınız var
            """)
            print(''.join(z), f":{len(sehir)} tane harf içeren kelime", end="\n")
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
                elif harf not in sehir:
                    print(f"{harf} harfi kelimemizin içinde yok :((")
                    hak -= 1
                    print(f"Tahmin hakkınız:{hak}")
                elif len(harf) >= 2:
                    print("Sadece bir harf girilebilir...")
                    continue
                elif hak == 0:
                    print("Hakkınız bitti. Adam asıldı...")
                    print(f"Bilemediğin kelime:{sehir}")
                    break
                else:
                    for i in range(len(sehir)):
                        if sehir[i] == harf:
                            print("Doğru tahmin:))")
                            z[i] = harf
                            harfler.append(harf)
                    print(''.join(z), f":{len(sehir)} tane harf içeren kelime", end="\n")
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
        elif oyun_secme == "2":
            print("""*****************************************************          
            'Mükemmel sayı' hesaplama programına hoşgeldiniz.
            Bir sayının kendi hariç bölenlerinin toplamı 
            kendine eşitse bu sayıya "mükemmel sayı" denir. 
            Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
            Çıkmak için 'q'ya basınız.
            *****************************************************
            """)
            while True:
                a = int(input("Bir sayı giriniz:"))
                liste = 0
                for i in range(1, a):
                    if a % i == 0:
                        liste += i
                if liste == a:
                    print("Seçtiğiniz sayı bir 'Mükemmel sayı'!!!!!")
                    res = input("""Yeni bir sayı denemek için 'e'ye,çıkmak için 'q'ya basınız:""")
                    if res == "e":
                        continue
                    elif res == "q":
                        break
                    else:
                        print("Hatalı işlem yaptınız tekrar deneyin...")
                else:
                    print("Seçtiğiniz sayı maalesef mükemmel sayı değil...")
                    res1 = input("""Yeni bir sayı denemek için 'e'ye,çıkmak için 'q'ya basınız:""")
                    if res1 == "e":
                        continue
                    elif res1 == "q":
                        break
                    else:
                        print("Hatalı işlem yaptınız tekrar deneyin...")
        elif oyun_secme == "3":
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
            a = input("Bir sayı giriniz:")
            ai = int(a)
            toplam = 0
            for i in a:
                rakam = int(i) ** len(a)
                toplam += rakam
            if toplam == ai:
                print("Seçtiğiniz sayı armstrong sayısıdır")
            else:
                print("Seçtiğiniz sayı armstrong sayısı değildir")
        elif oyun_secme == "4":
            print("""*********************************************
            Girdiğiniz sayılar sürekli toplanarak artar.
            Ta ki siz çıkana kadar.
            Çıkmak için 'q'ya basınız.
            *********************************************""")
            toplam = 0
            print("Toplam", toplam)
            while True:
                a = input("Sayı giriniz:")
                if a == "q":
                    print("Toplam Değişken:", toplam)
                    print("Program sonlandırılıyor...")
                    break
                a = int(a)
                toplam += a
        else:
            print("Hatalı tuşlama")
    def cevre_birimleri(self,cevre):
        self.pc_cevre.append(cevre)
        print(f"{cevre} birimi başarıyla eklendi, kullanıma uygun.")
    def __str__(self):
        return f"""___/-/ Bilgisayar bilgisi \-\___
        İşletim sistemi:{self.pc_os}
        Yüklü hesaplar:{self.pc_hesap}
        Bilgisayar durumu:{self.pc_durum}
        Arıza durumu:{self.pc_ariza}
        İnternet bağlantısı:{self.pc_lan}
        Fan seviyesi:{self.pc_fan}
        Monitör durumu:{self.pc_moni}
        Çevre birimleri:{self.pc_cevre}
        Oyunlar:{self.pc_oyun}
        """
    def __len__(self):
        return f"{len(self.pc_oyun)} tane oyun var"
bilgisayar = Bilgisayar()
bilgi_metni = """
1-)Bilgisayar açma 
2-)Bilgiyar kapatma
3-)Monitör açma
4-)Monitör kapatma
5-)Hesap ekleme
6-)Ses seviyesi
7-)İnternet açma
8-)İnternet kapatma
9-)Fan hız seviyesi
10-)__/-/Oyunlar\-\__
11-)Çevre birimi ekleme
12-)Bilgisayar bilgisi

Çıkmak için 'q'ya basınız
Bilgileri tekrar görmek için 'r' e basınız
"""
print(bilgi_metni)
while True:
    secilen_islem = input("Yapmak istediğiniz işlemi seçiniz:")
    if not secilen_islem:
        print("Burası boş bırakılamaz!!!")
        continue
    elif secilen_islem == "r" or secilen_islem == "R":
        print(bilgi_metni)
    elif secilen_islem == "q" or secilen_islem == "Q":
        print("Program kapatılıyor")
        time.sleep(0.5)
        break
    elif secilen_islem == "1":
        bilgisayar.pc_on()
        continue
    elif secilen_islem == "2":
        bilgisayar.pc_off()
        continue
    elif secilen_islem == "3":
        bilgisayar.moni_on()
        continue
    elif secilen_islem == "4":
        bilgisayar.moni_off()
        continue
    elif secilen_islem == "5":
        if bilgisayar.pc_durum == "Açık":
            hesap_1 = input("Eklemek istediğiniz hesap ismini giriniz:")
            bilgisayar.hesap(hesap_1)
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "6":
        if bilgisayar.pc_durum == "Açık":
            bilgisayar.ses_seviyesi()
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "7":
        if bilgisayar.pc_durum == "Açık":
            bilgisayar.pc_lan_on()
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "8":
        if bilgisayar.pc_durum == "Açık":
            bilgisayar.pc_lan_off()
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "9":
        if bilgisayar.pc_durum == "Açık":
            bilgisayar.pc_fanse()
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "10":
        if bilgisayar.pc_durum == "Açık":
            bilgisayar.oyun()
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "11":
        if bilgisayar.pc_durum == "Açık":
            cevre_1 = input("Eklemek istediğiniz çevre birimini giriniz:")
            bilgisayar.cevre_birimleri(cevre_1)
        else:
            print("Önce bilgisayarı açmalısınız")
        continue
    elif secilen_islem == "12":
        print(bilgisayar.__str__())
        continue
    elif len(secilen_islem) > 1:
        print("Birden fazla basamak tuşlayamazsınız!!!")
        continue
    else:
        print("Hatalı işlem")
        continue
'''
a = 2500

for i in range(1,2501):
    now = datetime.datetime.now()
    print(a - i, now)
    time.sleep(1)

