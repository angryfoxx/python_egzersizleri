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