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
