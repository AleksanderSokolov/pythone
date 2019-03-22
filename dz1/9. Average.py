# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше
# другого).

x = int(input("x="))
y = int(input("y="))
z = int(input("z="))

isFind = False

if x < y < z or x > y > z:
    isFind = True
    print("y= " + str(y))

if y < x < z or y > x > z:
    isFind = True
    print("x= " + str(x))

if y < z < x or y > z > x:
    isFind = True
    print("z= " + str(z))

if not isFind:
    print("Два или три числа равны")


