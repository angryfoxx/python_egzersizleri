__author__ = "Fox"
"""
#problem 1
def selamla():
    print("\t\t\t\t\t\tÇarpma İşlemi Makinesi")
selamla()

a = int(input("İlk sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))
c = int(input("Üçüncü sayıyı giriniz:"))
d = a*b*c
print("1. : {}\n2. : {}\n3. : {}\nTOPLAM: {}".format(a,b,c,d))
"""
"""
#problem 2
def selamla():
    print("\t\t\t\t\t...Vücut kitle indeksi hesaplamasına hoş geldiniz...")
selamla()

kilo = int(input("Kilonuzu giriniz(kg):"))
boy = int(input("Boyunuzu giriniz(cm):"))
vki = kilo/((boy/100)**2)

if vki <= 18.49:
    print("Boy kilo indeksi: {}".format(vki))
    print("İdeal Kilonun Altında!!\nİdeal kilonun altında kalmışsın ama yükselmen için yanındayım!\nTek ihtiyacın biraz motivasyon biraz da düzenli ve dengeli beslenme. Ben de tam bunun için varım")

elif vki >= 18.50 and vki <= 24.49:
    print("Boy kilo indeksi: {}".format(vki))
    print("Kilonuz İdeal\nHarikasın! Tam da ideal kilondasın! Şimdi sana düşen bunu korumak.\nHareketi ihmal etmeden, düzenli ve dengeli beslen.")

elif vki >= 25.00 and vki <= 29.99:
    print("Boy kilo indeksi: {}".format(vki))
    print("İdeal Kilonun Üzerinde\nHedefe yakınsın! Önünde kısa bir yol var. Dengeli beslenme ve düzenli fiziksel aktivite ile tam 12'den en ideali vurabilirsin!")

else:
    print("Boy kilo indeksi: {}".format(vki))
    print("İdeal Kilonun Çok Çok Üzerinde!!!!!!!\nİdeal kilonu biraz uzakta bırakmışsın ama güzel bir haberimiz var; ona kavuşmak sandığın kadar zor değil.\n Her şey kararlı ve motive olmakla başlıyor, asla pes etme ve motivasyonunu yüksek tut,\nhareket ve dengeli beslenme hayatının bir parçası olduğunda değişimin hızına sen bile inanamayacaksın.\n Motivasyonu yüksek tutup, dengeli ve düzenli beslenmeye dikkat edip, hareketi artırarak umduğunuzdan bile kolay olacak. \nİhtiyacınız olan her şey, okunmak üzere burada sizi bekliyor! Haydi ilk iş olarak biraz ilham al ve harekete geç!")
"""
"""
#problem 3
def selamla():
    print("\t\t\t\t\tAracımın Km Başı Yakıt Tüketimi Ne Kadar?")
selamla()

km = int(input("Gidilecek Mesafe(Km):"))
litre = float(input("100 Km'de kaç Lt yakıyor ?:"))
hesap = (km*litre)/100
fiyat = hesap*3.19


print("Aracınız {} Kilometrede {} ₺ yakar ".format(km,fiyat))
"""
"""

#problem 5

def selamla():
    print("\t\tLütfen bilgilerinizi giriniz...")
selamla()

k_ad = input("Lütfen adınızı giriniz:")
k_soyad = input("Lütfen soyadınızı giriniz:")
k_num = input("Lütfen numaranızı giriniz:")

print("Ad:{}\nSoyad:{}\nNumara:{}".format(k_ad,k_soyad,k_num))
"""
"""
# Problem 5
ilk_s = input("Birinci sayıyı giriniz: ")
ikinc_s = input("İkinci sayıyı giriniz: ")
print("Birinci sayı: {}\nİkinci sayı: {}".format(ikinc_s,ilk_s))
"""
"""
# Problem 6
def uzunkenar():
    print("\t\t\t\t\tDik üçgenin uzun kenarını hesaplama!!!")
uzunkenar()
a = int(input("Üçgenin ilk kenarını giriniz:"))
b = int(input("Üçgenin ikinci kenarını giriniz:"))
hipotenus = a**2 + b**2
c = hipotenus**0.5
print("Hipotenus: {}".format(c))
"""

