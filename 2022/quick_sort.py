"""
random_numbers = [25, 10, 5, 30, 40, 2, 1, 18, 7]
def partition(liste:list):
    i, j, pivot = -1, 0, liste[-1]

    while j < len(liste):
        if liste[j] < pivot:
            i += 1
            liste[i], liste[j] = liste[j], liste[i]
        j += 1

    liste[i + 1], liste[j - 1] = liste[j - 1], liste[i + 1]

    return quick_sort(liste, liste.index(pivot))


def quick_sort(liste:list,pivot:int):
    sorted_list = []
    if len(liste[:pivot]) == 1:
    return liste[:pivot], liste[pivot:]



print(partition(random_numbers))
print(partition([5, 2, 1]))
print(partition([1, 2, 5]))
print(partition([1, 2]))
print(partition([7, 40, 10, 25, 18, 30]))
print(partition([7, 10, 25, 18]))
print(partition([30, 40]))



# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
"""

