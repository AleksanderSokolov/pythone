# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.

x = int(input("x="))
y = int(input("y="))
z = int(input("z="))

if x < (y+z) and y < (x+z) and z < (y+x):
    print("Существует")
    if x == y == z:
        print("Равносторонний")
    else:
        if x == y or y == z or z == x:
            print("Равнобедренный")
        else:
            print("Разносторонний")
else:
    print("Не существует")
