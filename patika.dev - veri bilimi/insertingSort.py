# Insertion Sort

## [22,27,16,2,18,6] -> Insertion Sort
### Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
### Big-O gösterimini yazınız.
### Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
### Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.
"""
*
-[(22,27),16,2,18,6]
    0 ve 1. index arasında karşılaştırma yapılır. Küçük olan sola yazılır eğer soldaki küçükse öylece kalır. İndexler ise birer artırılır
-[22,(27,16),2,18,6]
    1. ve 2. index arasında karşılaştırma yapılır. "16" 22 ve 27'den küçük olduğu için listenin başına geçer. İndexler ise birer artırılır
-[16,22,(27,2),18,6]
    2. ve 3. index arasında karşılaştırma yapılır. "2" 16, 22 ve 27'den küçük olduğu için listenin başına geçer. İndexler ise birer artırılır
-[2,16,22,(27,18),6]
    3. ve 4. index arasında karşılaştırma yapılır. "18" 22 ve 27'den küçük, 2 ve 16'dan büyük olduğu için 2. sıraya geçer. İndexler ise birer artırılır
-[2,16,18,22,(27,6)]
    4. ve 5. index arasında karşılaştırma yapılır. "6" 16, 18, 22 ve 27'den küçük, 2'den büyük olduğu için 1. sıraya geçer. İndexler ise birer artırılır

[2,6,16,18,22,27]

** Big-O gösterimi = O(n^2) sebebi ise ilk aşamada n tane yapılan işlem bir azalıyor (n-1) ve bu işlemler azalarak gidiyor (n,n-1,n-2....+1) = n*(n+1)/2
    Big-O gösteriminde ise domine eden alındığı için n^2 yazıyoruz.

*** Best Case = 2 , Worst Case = 27 , Average Case = 16 veya 18

**** 18 Average Case kapsamına girer

"""
def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [22,27,16,2,18,6]
ins_sort(arr)
print(arr)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

## [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.

"""
-[(7,3),5,8,2,9,4,15,6]
    0 ve 1. index arasında karşılaştırma yapılır. Küçük olan sola yazılır. İndexler ise birer artırılır
-[3,(7,5),8,2,9,4,15,6]
    1 ve 2. index arasında karşılaştırma yapılır. "5" 7'den küçük 3'ten büyük olduğu için 1.sıraya geçer. İndexler ise birer artırılır
-[3,5,(7,8),2,9,4,15,6]
    2 ve 3. index arasında karşılaştırma yapılır. Küçük olan sola yazılır eğer soldaki küçükse öylece kalır. İndexler ise birer artırılır
-[3,5,7,(8,2),9,4,15,6]
    3 ve 4. index arasında karşılaştırma yapılır. "2" 3, 5, 7 ve 8'den küçük olduğu için 0.sıraya geçer.
    
[2,3,5,7,8,9,4,15,6]

"""

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while 4 > j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [7,3,5,8,2,9,4,15,6]
ins_sort(arr)
print(arr)