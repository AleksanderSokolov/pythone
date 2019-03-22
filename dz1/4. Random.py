# 4. Написать программу, которая генерирует в указанных пользователем границах
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
# надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
startInt = int(input("startInt = "))
endInt = int(input("endInt = "))

randomInt = random.randint(startInt, endInt)  # целое
print(randomInt)

startUniform = int(input("startUniform = "))
endUniform = int(input("endUniform = "))

randomUniform = random.uniform(startUniform, endUniform)  # вещественное
print(randomUniform)

codeCharStart = ord(input("Введите первый символ "))
codeCharEnd = ord(input("Введите последний символ "))

randomCodeChar = int(random.random() * (codeCharEnd-codeCharStart+1)) + codeCharStart  # символы
print(chr(randomCodeChar))
