# 5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.
import math

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # словарь

firstChar = input("firstChar")

secondChar = input("secondChar")

n = 0   # Счетчик букв в строке
firstCharPosition = 0  # Необходимо инициализоровать, символа может вообще не оказаться в словаре
secondCharPosition = 0

for i in abc:
    n = n+1
    if i == firstChar:
        firstCharPosition = n

    if i == secondChar:
        secondCharPosition = n

print(firstCharPosition)
print(secondCharPosition)

print(math.fabs(firstCharPosition-secondCharPosition))  # первый введенный символ может оказаться дальше второго

