'''
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))


delta_hesaplama = b ** 2 - 4 * a * c

x1 = ((-b - delta_hesaplama) ** 0.5) / (2 * a)
x2 =  ((-b + delta_hesaplama) ** 0.5) / (2 * a)

print("Birinci kök: {}\nİkinci kök: {}".format(x1,x2))
'''