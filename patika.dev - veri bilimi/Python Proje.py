l = [[1, 2], [3, 4], [5, 6, 7]]

"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir.
"""

def flatten(liste):
    liste_ = [j for i in liste for j in i]
    return liste_

print(flatten(l))

"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
"""

def reversed_list(liste):
    liste_ = []
    for i in liste:
        i.reverse()
        liste_.append(i)
    return liste_

l.reverse()
print(reversed_list(l))
