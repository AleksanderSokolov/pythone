#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
m = []
max = 0
x = 0
min = 100
n = 0
for i in range(0, 10):
    m.append(random.randint(0, 100))
print(m)

for k in range(0, len(m)):
    if max < m[k]:
        max = m[k]
        x = k
    if min > m[k]:
        min = m[k]
        n = k
m[x] = min
m[n] = max
print(m)
