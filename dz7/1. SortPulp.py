#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
k = 10
li = []
for j in range(0,k):
    li.append(random.randint(-100, 100))

def sortPulp(li):
    n = 1
    while n < len(li):
        for i in range(len(li)-n):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
        n += 1

print(li)
sortPulp(li)
print(li)

