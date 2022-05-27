"""
def mutlak_deger(a):
    if a < 0:
        return a*-1
    else:
        return a

a = mutlak_deger(int(input("Mutlak değerini almak istediğiniz sayıyı giriniz:")))

""" #mutlakd_bitmis
'''
def tam_bolen(sayi):
    liste = list()
    for i in range(1,sayi+1):
        if sayi % i == 0:
            liste.append(i)
        else:
            return liste
while True:
    sayi = input("Tam bölenini bulmak istediğiniz sayıyı giriniz:")
    if  sayi == "q":
        print("Program kapatılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam bölenler:",tam_bolen(sayi))
''' #tam bolen_bitmis
"""
liste = list()
def fib(n):
    a , b = 0 , 1
    while a < n:
        liste.append(a)
        a , b = b , a+b
n = fib(int(input("Fibonacci için sınır belirleyiniz:")))
print(liste)
""" #fib_bitmis
"""
def kayit():
    print("-"*30)
    sys_id = a
    sys_id0 = a0
    sys_count = a1
    sys_os = a2
    print(f"İsim:{sys_id}",f"Soyisim:{sys_id0}",f"Şehir:{sys_count}",f"İşletim sistemi:{sys_os}", sep = "\n")
    print("-" * 30)
    print(f"Başarıyla kaydedildi.Hoşgeldin {sys_id}...")
while True:
    aa = input("Kayıt oluşturmak için 'r', çıkmak için 'q'ya basınız:")
    if aa == "q":
        print("Görüşmek üzere...")
        break
    elif aa == "r":
        a = input("Ad giriniz:")
        a0 = input("Soyad giriniz:")
        a1 = input("Şehir giriniz:")
        a2 = input("İşletim sistemi giriniz:")
        kayit()
    elif not aa:
        print("İşlem boş bırakılamaz...")
        continue
    else:
        print("Hatalı tuşlama tekrar deneyiniz...")
        continue
""" #öylesine_bitmis
"""
def mukemmel(a):
    liste1 = list()
    for i in range(0,a+1):
        toplam = 0
        liste = list()
        liste.append(i)
        for x in liste:
            for j in range(1, x):
                if i % j == 0:
                    toplam += j
        if toplam == i:
            liste1.append(i)
    print(f"{liste1} mükemmel sayılar!!!!!")
a = mukemmel(int(input("Mükemmel sayı için sınır belirleyiniz:")))
""" #mükemmel_bitmis
"""
def pisagor_bulma(c):
    a = range(1,c+1)
    for i in a:
        for j in a:
            for x in a:
                if i ** 2 + j**2 == x**2:
                    if i < j:
                        print(f"{i},{j},{x} ile bir pisagor üçgeni oluşturabilirsin !!!!")
c = pisagor_bulma((int(input("Pisagorlar için üst sınır belirleyiniz:"))))
""" #pisagor bulma_bitmis
"""
def sayi_okuma(a):
    dict_birler = {0:"",1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
    dict_onlar = {0:"",1:"On",2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan"}
    dict_yuzler = {0:"",1:"Yüz", 2:"İki yüz", 3:"Üç yüz", 4:"Dört yüz", 5:"Beş yüz", 6:"Altı yüz", 7:"Yedi yüz", 8:"Sekiz yüz",9:"Dokuz yüz"}
    for i in range(1,a):
        i = str(i)
        if len(i) == 1:
            print(f"{i}:{dict_birler[int(i)]}")
        elif len(i) == 2:
            print(f"{i}:{dict_onlar[int(i[0])]} {dict_birler[int(i[1])]}")
        else:
            print(f"{i}:{dict_yuzler[int(i[0])]} {dict_onlar[int(i[1])]} {dict_birler[int(i[2])]}")
while True:
    a = input("a:")
    if a == "q":
        print("Program kapatılıyor...")
        break
    else:
        a = int(a)
        sayi_okuma(a)
""" #sayı okuma_bitmis
import re

"""import re
n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())
print(re.sub(r'(\w)(\W)+(\w)',r'\1 \3',''.join([u for t in zip(*a) for u in t])))"""
"""import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())
print(a)
for z in zip(*a):
    print(z)
    b += "".join(z)
print(b)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
This$#is% Matrix#  %!
"""

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
punc_list = list("!@#$%&")

def list_gen(input):
    for i in range(len(input)):
        matrix.append([])
        matrix[i].append(input[i])

for _ in range(n):
    matrix_item = input()
    list_gen(matrix_item)

mat = []
mate = [j for _ in range(1,m-1) for j in matrix[_]]

for _ in range(0,m,m-1):
    mat.append(matrix[_])
mat.insert(1,mate)

mat_ = [j for i in mat for j in i]

print("".join(mat_).replace("  "," "))
"""
5 9
#%$r%r$n 
O%Mi$iTi$
yiaxsprt 
est%ctiy#
  t c i %
""" # - #Oye is Mattrix sccript Triinity  $ #%
"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
""" # - This is Matrix#  %! (This$#is% Matrix#  %!)
"""
4 6
T%Mic&
h%axr%
iit#p!
ssrst&
""" # - This isMatrix scrpt&%!&
"""
2 4
# i#
 @#U
"""# - #  @i U
