'''
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
    for i in range(1,a):
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
''' #Problem 1 "Mükemmel sayı" _bitmiş_
'''
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
''' # Problem 2 "Armstrong" _bitmiş_
'''
for i in range(1,11):
    for j in range(1,11):
        print(f"i:{i} , j:{j}")
''' #Problem 3 "çarpım tablosu" _bitmis_
'''
print("""*********************************************
Girdiğiniz sayılar sürekli toplanarak artar.
Ta ki siz çıkana kadar.
Çıkmak için 'q'ya basınız.
*********************************************""")
toplam = 0
print("Toplam",toplam)
while True:
    a = input("Sayı giriniz:")
    if a == "q":
        print("Toplam Değişken:", toplam)
        print("Program sonlandırılıyor...")
        break
    a = int(a)
    toplam += a
''' #Problem 4 "değişken toplama" _bitmiş_
'''
liste = list()
for i in range(1,101):
    if i % 3 == 0:
        liste.append(i)
print(liste)

liste = range(0,101)
liste1 = [i for i in liste if i % 3 == 0]
print(liste1)

for i in range(0,101):
    if i % 3 != 0:
        continue
    print(i)
''' #Problem 5 "3 e bölünen sayılar" _bitmiş_
'''
liste = range(1,101)
liste1 = [i for i in liste if i % 2 == 0]
print(liste1)
''' #Problem 6 "2 e bölünen sayılar l-comp" _bitmiş_
