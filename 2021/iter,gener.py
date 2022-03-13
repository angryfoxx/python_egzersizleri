"""
def asal(x):
    liste = list()
    for i in range(2, x+1):
        if x % i == 0:
            liste.append(i)
    if len(liste) >= 2:
        return f"{x} asal değil"
    else:
        return f"{x} asal"
for i in range(1, 1000):
    print(asal(i))
"""
"""
liste = range(1,1000,2)
iterator = iter(liste)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("listenin sonuna geldik")
        break
"""
"""
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield b
iteration = iter(fib())
while True:
    print(next(iteration))
"""
"""
liste = list()
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        liste.append(b)

print(fib())
print(liste)
"""
"""
class Kareler():
    def __init__(self, max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.kuvvet <= self.max:
            sonuc = 2 ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration
kareler = Kareler(8)
while True:
    print(next(kareler))
"""