"""def shuffle_letters(str1,str2):
    str1_char_dict = dict()
    str2_char_dict = dict()
    for i in str1:

        if i in str1_char_dict:
            str1_char_dict[i] += 1
        else: str1_char_dict[i] = 1

    for j in str2:

         if j in str2_char_dict:
             str2_char_dict[j] += 1
         else: str2_char_dict[j] = 1

    return str1_char_dict == str2_char_dict

print(shuffle_letters("ankara","arxkan"))""" # shuffle letters
"""def shuffle_letters(str1):
    str1_char_dict = dict()
    letter = ""
    for i in str1:
        if i in str1_char_dict:
            str1_char_dict[i] += 1
        else:
            str1_char_dict[i] = 1

    for i,j in zip(str1_char_dict.keys(),str1_char_dict.values()):
        letter += str(j) + j * i
    return letter
print(shuffle_letters("ankara"))""" # letter frequently
"""
def kayipBasamak(str_:str):
    str_splitted = str_.split(" ")
    num_list = []
    forget_data_index = 0
    operator_ = "+"
    if str_splitted[1] == "+": operator_ = "-"
    elif str_splitted[1] == "-": operator_ = "-"
    elif str_splitted[1] == "*":operator_ = "/"
    elif str_splitted[1] == "/":operator_ = "*"

    for i in str_splitted:
        if "x" in i: forget_data_index = str_splitted.index(i)
        try: num_list.append(int(i))
        except: pass

    num_list.sort(reverse=True)
    data = str(int(eval(f"{num_list[0]} {operator_} {num_list[1]}")))

    dicti = dict()
    for i,j in zip(str_splitted[forget_data_index],data):
        if i != j: dicti[i] = j
    return dicti

print(kayipBasamak("20 - 1x = 4"))
print(kayipBasamak("1x0 / 3 = 50"))
print(kayipBasamak("1x * 11 = 121"))
print(kayipBasamak("36 + 1x = 50"))
print(kayipBasamak("36 + 1xyz = 1371"))
""" # kayıp basamak
"""def array_rotation(liste:list):
    string = ""
    for i in (liste[liste[0]:] + liste[:liste[0]]):
        string += str(i)
    return string

print(array_rotation([2,3,4,5]))
print(array_rotation([4,5,6,7,8,9,10,11,12,13]))""" # array rotasyonu
"""def array_pair(liste:list):
    sliced_list = []
    old_value = 0
    for i in range(0,len(liste) + 1,2):
        sliced_list.append(liste[old_value:i])
        old_value = i
    sliced_list.remove([])

    for i in sliced_list:
        if sliced_list.index(i) == sliced_list.index(i[::-1]):
            return i
    return "ok"

print(array_pair([5,6,6,5,3,3]))
print(array_pair([5,6,6,5,8,9,9,8,6,5,5,6]))""" # array pair
"""def wordSplit(liste:list):
    x = list(liste[0])
    for i in range(0,len(x)):
        c = x[::]
        c.insert(i," ")
        if "".join(c).split(" ")[0] in liste[1] and "".join(c).split(" ")[1] in liste[1]:
            return "".join(c).split(" ")

print(wordSplit(["deeplearning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,lear2ning"]))""" # word split
"""def string_tersi_recursion(string:str):
    if len(string) == 1:
        return string
    else:
        return string_tersi_recursion(string[1:]) + string[0]


print(string_tersi_recursion("elma"))
print(string_tersi_recursion("Machine Learning"))
print(string_tersi_recursion("Ömer Faruk Korkmaz"))
print(string_tersi_recursion("lukadruY naaK ahaT"))""" # reverse string with recursion
"""def multiplyRecursive(x, y):
    if y == 1:
        return x
    else:
        return x + multiplyRecursive(x, y - 1)

for i,j in enumerate([5,5,5,5,5,5,5,5,5,5,5]):
    print(multiplyRecursive(i,j))""" # multiply with recursion
"""
def powerRecursive(x,y):
    if y == 1:
        return x
    else:
        return x * powerRecursive(x, y - 1)

for i, j in enumerate(start=1,iterable=list(range(1,10))):
    print(i, j, powerRecursive(i, j))""" # power with recursion
"""def binarySearch(liste, L, H, number):
    M = (H - L) // 2 + L
    if H >= L:
        if liste[M] != number:
            if liste[M] < number:
                return binarySearch(liste, M + 1, H, number)
            else:
                return binarySearch(liste, L, M - 1, number)
        return f"Listenin {M}. indexi: {liste[M]}"
    else: return -1

liste = [2,3,4,5,6,7,8,9,10,11,12,13,15,16,18,19,20]

print(binarySearch(liste, 0, len(liste) - 1, 7))
print(binarySearch(liste, 0, len(liste) - 1, 13))
print(binarySearch(liste, 0, len(liste) - 1, 22))
""" # binary search recursive
"""def jumpSearch(liste, L, H, step, number):
    if H >= L:
        if liste[L + step] != number:
            if liste[L + step] < number:
                return jumpSearch(liste, L + step, H, step, number)
            else:
                return jumpSearch(liste, L, L + step, step - 1, number)
        return f"Listenin {L + step}. indexi: {number}"
    return -1

liste = [0,1,4,5,6,7,8,9,10,12,13,14,16,17,19,20]

print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 14))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 6))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 20))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 19))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 16))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 0))
print(jumpSearch(liste,0 , len(liste) - 1, int(len(liste) ** 0.5), 22))"""
"""
def bubbleSort(arr, H):
    if H > 0:
        check = 0
        for i in range(H):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                check = i
        if check:
            return bubbleSort(arr, H - 1)
    return arr
    
A = [6,1,17,22,24,50,41,15,34,28,23,39]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(bubbleSort(A, len(A) - 1))
print(bubbleSort(B, len(B) - 1))""" # bubble sort recursive
"""def mergeSort(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if len(arr) > 1:
        partition(left)
        partition(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(mergeSort(A))
print(mergeSort(B))""" # merge short
"""def insertionSort(liste,h):
    if len(liste) > 1 and h != len(liste):
        for i in range(h):
            if liste[h] < liste[i]:
                liste[i], liste[h] = liste[h], liste[i]
        return insertionSort(liste, h + 1)
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(insertionSort(A, 1))
print(insertionSort(B, 1))""" # insertion sort recursive
"""
def selectionSort(liste):
    for j in range(len(liste)):
        #lowest_number = liste[j]
        lowest_number = j
        for i in range(j, len(liste)):
            if liste[i] < liste[lowest_number]:
                 lowest_number = i
            #if liste[i] < lowest_number:
                #lowest_number = liste[i]
        #il = liste[j::].index(lowest_number) + j
        #liste[j], liste[il] = liste[il], liste[j]
        liste[j], liste[lowest_number] = liste[lowest_number], liste[j]
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(selectionSort(A))
print(selectionSort(B))""" # selection sort
"""def countSort(liste):
    dict_ = dict()
    for i in range(len(liste)):
        if liste[i] in dict_:
            dict_[liste[i]] += 1
        else:
            dict_[liste[i]]  = 1
    for i in range(1, 10):
        print(str(i) * dict_[i], end = "")
A = [1, 3, 9, 6, 5, 8, 5, 4, 7, 6, 2, 2, 1]
countSort(A)""" # count sort
"""def parti(liste, L, H):
    pivot = liste[H]
    j = L - 1
    for i in range(L,H):
        if liste[i] <= pivot:
            j += 1
            liste[i], liste[j] = liste[j], liste[i]
    liste[H], liste[j + 1] = liste[j + 1], liste[H]
    return j + 1

def quickSort(liste, L, H):
    if L < H:
        pi = parti(liste, L, H)
        quickSort(liste, pi + 1, H)
        quickSort(liste, L, pi - 1)
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
print(quickSort(A, 0, len(A) - 1))

""" # quick sort
"""def secondGreatLow(arr):
    sorted_list = sorted(set(arr))
    if len(arr) < 2:
        return sorted_list[1],sorted_list[0]
    return sorted_list[1],sorted_list[-2]

print(secondGreatLow([90,4]))
print(secondGreatLow([90,2,1,3,5,5,2,80,60]))""" # second Great Low
"""from itertools import combinations
def threeSum(arr):
    check = 0
    c = 3
    for i in combinations(arr[1:],c):
        if sum(i) == arr[0]:
            check += 1
    if check >= c:
        return True
    return False

A = [10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]
print(threeSum(A))

B = [12, 3, 1, -5, -4, 7]
print(threeSum(B))""" # three sum