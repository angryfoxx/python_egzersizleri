"""
liste = [(3,4),(10,3),(5,6),(1,9)]
def map_icin(x):
    return x[0]*x[1]
print(list(map(map_icin,liste)))
""" # Map ile dikd. alan hesaplama   |Problem 1
""""
liste = [(3,4,5),(6,8,10),(3,10,7)]
def uclu(demet):
    if abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]:
        return True
    else:
        return False
print(list(filter(uclu,liste)))
""" # Filter ile üçgen hesaplama     |Problem 2
"""
from functools import reduce
liste = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y :x+y, list(filter(lambda x : x%2==0,liste))))
""" # Çift sayı getirme ve toplama   |Problem 3
"""
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(isimler,soyisimler):
    print(i,j)
""" # Zip ile isim soyisim yazdıjrma |Problem 4
