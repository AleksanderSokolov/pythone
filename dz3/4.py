# 4. Определить, какое число в массиве встречается чаще всего.

import random
m = []
max = 0
x = 0
min = 100
n = 0
for i in range(0, 20):
    m.append(random.randint(0, 10))
print(m)

n = m[0]
max_f = 1
for i in range(len(m)):
    f = 1
    for k in range(i + 1, len(m)):
        if m[i] == m[k]:
            f += 1
    if f > max_f:
        max_f = f
        n = m[i]

print(max_f, n)
