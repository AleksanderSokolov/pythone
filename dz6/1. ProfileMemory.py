#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти

import memory_profiler
@memory_profiler.profile
def f():
    age = int(input("age ="))

    if ((age % 4) == 0 and (age % 100) != 0) or ((age % 400) == 0):
        print("Високосный")
    else:
        print("Не високосный")

f()


#(venv) C:\Users\avsokolov-adm\PycharmProjects\pythone>python --version
#Python 3.7.2

# Line #    Mem usage    Increment   Line Contents
# ================================================
#      5     15.2 MiB     15.2 MiB   @memory_profiler.profile
#      6
#      7                             def f():
#      8     15.2 MiB      0.0 MiB       age = int(input("age ="))
#      9
#     10     15.2 MiB      0.0 MiB       if ((age % 4) == 0 and (age % 100) != 0) or ((age % 400) == 0):
#     11     15.2 MiB      0.0 MiB           print("Високосный")
#     12                                 else:
#     13                                     print("Не високосный")
#
#
#
# Process finished with exit code 0