"""
liste = ["345", "sadas", "324a", "14", "kemal"]
for i in liste:
    try:
            print(int(i))
    except:
        print(i,"Harf içerdiği için olamaz")
"""
"""
def cift_mi(a):
    a = int(a)
    if a % 2 == 0:
        print(f"{a} bir çift sayı")
    else:
        raise ValueError("Seçtiğiniz sayı tek sayı")
while True:
    c = input("sayi:")
    if c == "q" or c == "Q":
        break
    else:
        c = int(c)
        cift_mi(c)

"""

liste_2 = [[[[["a"],5]],4,3],[0.2,5,"asd",True],[[7],[6]],8,9] # ['a', 5, 4, 3, 0.2, 5, 'asd', True, 7, 6, 8, 9]
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

new_list = []

def iflist(x):
    for i in range(len(x)):
        if type(x[i]) != list:
            new_list.append(x[i])
        else:
            iflist(x[i])

for i in liste:
    if type(i) != list:
        new_list.append(i)
    else:
        iflist(i)
print(new_list)

