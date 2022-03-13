"""class VendingMachine:
    def __init__(self, num_items = 0, item_price = 0):
        self.num_items = num_items
        self.item_price = item_price
        super().__init__()
    def buy(self, req_items, money):
        limit = 100
        if self.num_items < req_items:
            print()
            return "Not enough req items"
        else:
            self.num_items -= req_items
            if limit < money:
                return "Not enough coins"
            else:
                method = money - req_items * self.item_price
                limit -= method
                if limit > method:
                    return "Not enough coins"
                else:
                    return method
"""
"""from functools import reduce
def HouseSale(num_items,money,items):
    for i in range(num_items):
        for j in range(num_items):
            if i != j:
                liste = list()
                T = items[i] + items[j]
                if T <= money:
                    liste.append(items[i])
                    liste.append(items[j])
                    return len(liste)
                else:
                    return 0

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num_items, money = map(int, input().split())
        items = list(map(int, input().split()))
        a = HouseSale(num_items, money, items)
        print(f"Case #{_ + 1}: {a}")

"""
