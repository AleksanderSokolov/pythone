#1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
for k in range(2, 10):
    n = 0
    for i in range(2, 1000001):
        if i % k == 0:
            n = n + 1
    print(k, n)