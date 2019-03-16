# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

from decimal import Decimal  # float не удобно использовать для подобных расчетов

x1 = Decimal(input("x1 = "))
y1 = Decimal(input("y1 = "))

x2 = Decimal(input("x2 = "))
y2 = Decimal(input("y2 = "))

k = (y1-y2)/(x1-x2)
b = y2-k*x2

if b < 0:
    minusOrPlus = ""  # минус содержится в значении переменной
else:
    minusOrPlus = "+"

print("y = " + str(k) + "x" + minusOrPlus + str(b))


