# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# функция проверки формата и типа вводимых данных параметры начало, конец диапазона, имя вводимого значения


def input_int_in_range(start, end, name):
    while True:
        try:
            n = int(input("Введите число: " + name + "="))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if start <= n < end:
                return n
            print("Введённое число вне диапазона: [%d, %d)" % (start, end))


x = input_int_in_range(1, 999, "x")
y = input_int_in_range(1, 999, "y")
z = input_int_in_range(1, 999, "z")

# сумма
sum = x + y + z
print(sum)

# произведение
multiplication = x * y * z
print(multiplication)