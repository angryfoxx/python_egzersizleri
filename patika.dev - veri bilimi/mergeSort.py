# Merge Sort

"""*
-[16,21,11,8,12,22]
    Liste ortadan ikiye ayrılır [16, 21, 11] [8, 12, 22] ve soldaki listeden devam edilir.

-[16, 21, 11]
    Liste ortadan ikiye ayrılır [16, 21] [11] ve soldaki listeden devam edilir.
-[16, 21]
    Liste ortadan ikiye ayrılır [16] [21] arasında sıralama yapılır bu sıralama yapıldıktan sonra [11] ile sıralama yapılır.
-[11,16,21]
    Sıralama solda biter ve sağdakine geçer [8, 12, 22].

-[8, 12, 22]
    Liste sıralı olduğu için aynı kalır ve üstteki listeyle beraber işleme sokulur.
    Burada iki liste arasında sıralama yapılırken soldaki listenin 0. indexi ile sağdaki listenin 0. indexi,
    karşılaştırarak liste sıralanır.

-[8, 11, 12, 16, 21, 22]

**Big-O gösterimi = O(nLogn) sebebi ise son aşamada iki liste arasında karşılaştırılmalı yapılan işlem O(n) olur,
    üst taraftaki işlemler de sürekli yarıya bölünerek yapılıyor onu da şöyle yazarız: (2^n = x) = O(logn = x).
    İkisini birleştirdiğimizde O(nLogn) olur.

"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [16,21,11,8,12,22]
mergeSort(arr)
print(arr)
