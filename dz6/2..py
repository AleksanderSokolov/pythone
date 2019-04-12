#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти

# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.

import platform
import timeit
print(platform.python_version())
print(platform.architecture())
import memory_profiler
@memory_profiler.profile

def f():
    x = int(input("x="))
    y = int(input("y="))
    z = int(input("z="))

    start_time = timeit.default_timer()

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

    print(timeit.default_timer() - start_time)

f()

# при увеличении сторон треугольника память увеличивается незначительно (в пределах погрешности), время существенно
# (при повтроном запуске не убывает)

# 3.7.2
# ('32bit', 'WindowsPE')
# x=1
# y=2C:\Users\avsokolov-adm\PycharmProjects\pythone\venv\Scripts\python.exe C:/Users/avsokolov-adm/PycharmProjects/pythone/dz6/2..py
# 3.7.2
# ('32bit', 'WindowsPE')
# x=100000000000000000000000
# y=200000000000000000000000
# z=200000000000000000000000
# Существует
# Равнобедренный
# 0.000623104999998958
# Filename: C:/Users/avsokolov-adm/PycharmProjects/pythone/dz6/2..py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     14     15.3 MiB     15.3 MiB   @memory_profiler.profile
#     15
#     16                             def f():
#     17     15.3 MiB      0.0 MiB       x = int(input("x="))
#     18     15.3 MiB      0.0 MiB       y = int(input("y="))
#     19     15.3 MiB      0.0 MiB       z = int(input("z="))
#     20
#     21     15.3 MiB      0.0 MiB       start_time = timeit.default_timer()
#     22
#     23     15.3 MiB      0.0 MiB       if x < (y+z) and y < (x+z) and z < (y+x):
#     24     15.3 MiB      0.0 MiB           print("Существует")
#     25     15.3 MiB      0.0 MiB           if x == y == z:
#     26                                         print("Равносторонний")
#     27                                     else:
#     28     15.3 MiB      0.0 MiB               if x == y or y == z or z == x:
#     29     15.3 MiB      0.0 MiB                   print("Равнобедренный")
#     30                                         else:
#     31                                             print("Разносторонний")
#     32                                 else:
#     33                                     print("Не существует")
#     34
#     35     15.3 MiB      0.0 MiB       print(timeit.default_timer() - start_time)
# z=2
# Существует
# Равнобедренный
# 0.0005006830000002793
# Filename: C:/Users/avsokolov-adm/PycharmProjects/pythone/dz6/2..py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     14     15.4 MiB     15.4 MiB   @memory_profiler.profile
#     15
#     16                             def f():
#     17     15.4 MiB      0.0 MiB       x = int(input("x="))
#     18     15.4 MiB      0.0 MiB       y = int(input("y="))
#     19     15.4 MiB      0.0 MiB       z = int(input("z="))
#     20
#     21     15.4 MiB      0.0 MiB       start_time = timeit.default_timer()
#     22
#     23     15.4 MiB      0.0 MiB       if x < (y+z) and y < (x+z) and z < (y+x):
#     24     15.4 MiB      0.0 MiB           print("Существует")
#     25     15.4 MiB      0.0 MiB           if x == y == z:
#     26                                         print("Равносторонний")
#     27                                     else:
#     28     15.4 MiB      0.0 MiB               if x == y or y == z or z == x:
#     29     15.4 MiB      0.0 MiB                   print("Равнобедренный")
#     30                                         else:
#     31                                             print("Разносторонний")
#     32                                 else:
#     33                                     print("Не существует")
#     34
#     35     15.4 MiB      0.0 MiB       print(timeit.default_timer() - start_time)

