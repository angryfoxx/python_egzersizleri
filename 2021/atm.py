'''

__author__ = "FOX"

sys_nick = "Fox"
sys_pass = "12491811"
giris_hakki = 3
print("""*********************************************
     3 yanlış girişte hesabınız bloke olur.
**********************************************""")
while True:
    nick = input("Kullanıcı adınızı giriniz:")
    passw = input("Parolayı giriniz:")
    if nick != sys_nick and passw == sys_pass:
        print("!Kullanıcı adı veya parola hatalı!")
        giris_hakki -= 1
        print("KALAN GİRİŞ DENEMESİ", giris_hakki)
    elif nick != sys_nick and passw != sys_pass:
        print("!Kullanıcı adı veya parola hatalı!")
        giris_hakki -= 1
        print("KALAN GİRİŞ DENEMESİ", giris_hakki)
    elif nick == sys_nick and passw != sys_pass:
        print("!Kullanıcı adı veya parola hatalı!")
        giris_hakki -= 1
        print("KALAN GİRİŞ DENEMESİ", giris_hakki)
    elif nick == sys_nick and passw == sys_pass:
        print("Başarıyla giriş yapıldı.Lütfen bekleyiniz...")
        print("""*********************************************
        Bakiye sorgulama için 1'e basınız.

        Para çekme için 2'ye basınız.

        Para yatırma için 3'e basınız.

        Çıkmak için 4'e basınız.

        Ana menü için 152634'ü tuşlayınız.
**********************************************""")

        bakiye = 3000

        while True:
            islem = int(input("Yapmak istediğiniz işlemi giriniz:"))
            if islem == 1:
                print("Bakiyeniz {} Türk Lirası.".format(bakiye))
                islem1 = int(input("Başka bir işlem yapmak ister misiniz ?:"))
                if islem1 == 4:
                    print("Yine bekleriz görüşmek üzere.")
                    break
                elif islem1 == 152634:
                    continue
                else:
                    print("Hatalı tuşlama!!!")
                    continue
            elif islem == 2:
                miktar = int(input("Çekmek istediğiniz miktarı giriniz:"))
                if miktar == 152634:
                    continue
                elif bakiye - miktar < 0:
                    print("Bakiyenizde yeterli miktarda para bulunmamaktadır...")
                    continue
                bakiye -= miktar
                print("Yeni bakiyeniz {}.".format(bakiye))
                islem2 = int(input("Başka bir işlem yapmak ister misiniz ?:"))
                if islem2 == 4:
                    print("Yine bekleriz görüşmek üzere.")
                    break
                elif islem2 == 152634:
                    continue
                else:
                    print("Hatalı tuşlama!!!")
                    continue
            elif islem == 3:
                miktar1 = int(input("Yatırmak istediğiniz miktarı giriniz:"))
                if miktar1 == 152634:
                    continue
                bakiye += miktar1
                print("Yeni bakiyeniz {}.".format(bakiye))
                islem3 = int(input("Başka bir işlem yapmak ister misiniz ?:"))
                if islem3 == 4:
                    print("Yine bekleriz görüşmek üzere.")
                    break
                elif islem3 == 152634:
                    continue
                else:
                    print("Hatalı tuşlama!!!")
                    continue
            elif islem == 4:
                print("Yine bekleriz görüşmek üzere.")
                break
            else:
                print("HATALI İŞLEM!!!!")

    if giris_hakki == 0:
        print("Geçersiz giriş denemesi yaptınız sistemden atılıyorsunuz...")
        break
'''

