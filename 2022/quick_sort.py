random_numbers = [26,74,0,87,68,86,65,64,8,75]


def quick_sort(liste:list):
    copy_list = liste.copy()
    i = -1
    loop = 0
    pivot = liste.copy()[-1]
    while loop < len(liste):
        if liste[loop] < pivot:
            i += 1
            copy_list[i] = liste[loop]
            copy_list[loop] = liste[i]
            liste = copy_list.copy()
        loop += 1

    copy_list[i] = liste[loop-1]
    copy_list[loop-1] = liste[i]

    return copy_list

print(quick_sort(random_numbers))

