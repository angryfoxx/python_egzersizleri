"""
print("*Programdan çıkmak için 'q'ya basınız...")
while True:
    cinsiyet = input("Cinsiyetinizi belirtiniz(K veya E):")
    if cinsiyet == "K" or cinsiyet == "k":
        print("Askere gitmeniz uygun değil")
        break
    elif cinsiyet == "E" or cinsiyet == "e":
        yas = int(input("Yaşınızı giriniz:"))
        if yas >= 21:
            print("Askere gitmeniz uygun...")
            break
        else:
            print("Askere gitmeniz uygun değil...")
            break
    elif cinsiyet == "q" or cinsiyet == "Q":
        print("Program kapatılıyor...")
        break
    else:
        print("Hatalı tuşlama!!!")
        continue
"""
'''
print("*Programdan çıkmak için 'q'ya basınız...")
system_id = "Angryfox"
system_passw = "123456aa"
while True:
    id = input("Kullanıcı adınızı giriniz:")
    passw = input("Parolanızı giriniz:")
    if id == "q" or passw == "q":
        print("Programdan çıkış yapılıyor...")
        break
    elif not id or not passw:
        print("Kullanıcı adı veya Parola boş bırakılamaz")
        continue
    elif system_id == id and system_passw != passw or system_id != id and system_passw == passw \
            or system_id != id and system_passw != passw:
        print("Kullanıcı adı veya parola HATALI!!!!!")
        continue
    else:
        print("Sisteme başarıyla giriş yapıldı...Hoşgeldiniz {}.".format(id))
        break
'''
