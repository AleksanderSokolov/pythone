
6.
import random
x = random.randint(0,100)
for i in range(10):
        y = int(input("ВВЕДИТЕ ЧИСЛО:"))
        if x<y:
                print("меньше")
        elif x>y:
                print("больше")
        else:
                print("верно")
                break

7
n = int(input("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО"),0)
a = 0
for i in range(n+1):
        a = a + i
b = n*(n+1)/2

if a == b:
        print("верно")

8
a= input("ВВЕДИТЕ ЧИСЛО")
b=input("КАКУЮ ЦИФРУ ПОСЧИТАТЬ?")
n=0
for i in a:
        if i==b:
                n=n+1
print(n)

9.

max=0
maxSum=0
while True:
        a = input("ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО")
        if a == "0":
                print(max)
                print(maxSum)
                break
        sum=0
        for i in a:
                sum = sum + int(i, 0)
        if sum > maxSum:
                max = a
                maxSum = sum
