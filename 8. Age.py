# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным

age = int(input("age ="))

if ((age % 4) == 0 and (age % 100) != 0) or ((age % 400) == 0):
    print("Високосный")
else:
    print("Не високосный")
