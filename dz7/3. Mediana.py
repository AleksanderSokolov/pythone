#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках

import random
k = 5
li = []
for j in range(0,k):
    li.append(random.randint(0, 100))

def quickselect_median(li, pivot_fn=random.choice):
    if len(li) % 2 == 1:
        return quickselect(li, len(li) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(li, len(li) / 2 - 1, pivot_fn) +
                      quickselect(li, len(li) / 2, pivot_fn))

def quickselect(li, k, pivot_fn):
    if len(li) == 1:
        assert k == 0
        return li[0]

    pivot = pivot_fn(li)

    lows = [el for el in li if el < pivot]
    highs = [el for el in li if el > pivot]
    pivots = [el for el in li if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

print(li)
print(quickselect_median(li))
