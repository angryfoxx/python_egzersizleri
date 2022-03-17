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