#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
k = 6
li = []
for j in range(k):
    li.append(random.uniform(0, 50))

def sortMerge(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        sortMerge(left)
        sortMerge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i = i + 1
            else:
                li[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            li[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            li[k] = right[j]
            j = j + 1
            k = k + 1

print(li)
sortMerge(li)
print(li)


