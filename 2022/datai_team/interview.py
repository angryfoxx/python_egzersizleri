'''
You will be given a list of stock prices for a given day and your goal is to
return the maximum profit that could have been made by buying a stock at the given
price and then selling the stock later on. For example if the input is: [45, 24, 35, 31, 40, 38, 11]
then your program should return 16 because if you bought the stock at dolar 24 and sold it at dolar 40, a
profit of dolar 16 was made and this is the largest profit that could be made. If no profit could have been made,
return -1.

Örneğin: buy_price = 11, sell_price = 45, max_profit = 34

def smp(arr):
    max_profit = -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                process = arr[j] - arr[i]
                if max_profit < process:
                    max_profit = process

    return max_profit

print(smp([45, 24, 35, 31, 355, 40, 38, 11]))
''' # Google - Stock Maximum Profit
"""
Suppose you want climb a staircase of N steps, and on each step you can take either 1 or 2 steps. 
How many distinct ways are there to climb the staircase? For example, if you wanted to climb 4 steps, 
you can take the following distinct number of steps

* 1) 1, 1, 1, 1
* 2) 1, 1, 2
* 3) 1, 2, 1
* 4) 2, 1, 1
* 5) 2, 2


def countStep(N):
    if N <= 2:
        return N
    return countStep(N - 1) + countStep(N - 2)

print(countStep(5))

""" # Google - Step Counting Using Recursion
"""
For this popular algorithm interview question, the input will be a string consisting only of the characters 0, 1 and ?, 
where the ? acts as a wildcard that can be either a 0 or 1, and your goal is to print all possible combinations of the string. 
For example, if the string is "011?0" then your program should output a set of all strings, which are: ["01100", "01110"].

from itertools import combinations
def scc(word):
    qu_mark = word.count("?")
    arr = []
    for _ in range(qu_mark):
        arr.append(0)
        arr.append(1)

    arr_ = []
    for i in combinations(arr, qu_mark):
        if i not in arr_:
            arr_.append(i)

    new_arr = []
    for j in arr_:
        word_ = word
        for x in range(len(j)):
            word_ = word_.replace("?",str(j[x]),1)

        new_arr.append(word_)

    return new_arr

print(scc("0???0"))
""" # Google - String Combinations Consisting only of 0, 1 and ?
"""
This is a common interview question where you need to write a program to find all duplicates 
in an array where the numbers in the array are in the range of 0 to n-1 where n is the size of the array. 
For example: [1, 2, 3, 3] is okay but [1, 2, 6, 3] is not. 
In this version of the challenge there can be multiple duplicate numbers as well.
def fad(arr):
    dup_arr = []
    flag = True

    for i in arr:
        if len(arr) - 1 < i:
            flag = False
    if flag:
        for i in arr:
            if arr.count(i) > 1 and dup_arr.__contains__(i) is False:
                dup_arr.append(i)

    dup_arr.sort()
    
    return dup_arr

print(fad([1, 2, 3, 3])) # [3]
print(fad([1, 2, 6, 3])) # []
print(fad([1, 2, 6, 3, 2, 6, 3]))# [2, 3, 6]
print(fad([1, 2, 6, 3, 2, 6, 3, 9, 9])) # []
print(fad([2, 0, 1, 3, 5, 6, 4])) # []
print(fad([2, 0, 1, 1, 3, 5, 6, 4, 5])) # [1, 5]

""" # Facebook - Find All Duplicates in Array in Linear Time
"""
For this problem, your goal is to sort an array of 0, 1 and 2's but you must do this in place, 
in linear time and without any extra space (such as creating an extra array). 
This is called the Dutch national flag sorting problem. For example, if the input array is [2,0,0,1,2,1] 
then your program should output [0,0,1,1,2,2] and the algorithm should run in O(n) time.


def dnfs(arr):
    H = len(arr) - 1
    while H > 0:
        check = 0
        for i in range(H):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                check += 1
        if check == 0:break
        H -= 1
    return arr

print(dnfs([2,0,0,1,2,1]))

""" # Facebook - Dutch National Flag Sorting Problem"
"""
The sieve of Eratosthenes algorithm generates all the primes up to a given limit. 
This is a common and fast algorithm used to generate a list of primes up to a given limit. 
It works by making a list from 1 to N, and then iterating through the list and progressively removing non-prime, 
composite numbers until only primes are left in a list.
1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
2  3  5  7  11  13  17  19   23  29

def eratosthenes(A):
    cop, B = A.copy(), []
    while len(A) != 0:
        if A[0] ** 2 < cop[-1]:
            B.append(A[0])
            A.pop(0)
            for i in A:
                if i % B[-1] == 0:
                    A.remove(i)
        else:
            B = B + A
            A.clear()
    return B

def numGen(n):
    return eratosthenes(list(range(2, n + 1)))


print(numGen(1000))
""" # Amazon - Generate Primes Up To N Using Sieve of Eratosthenes Algorithm",
