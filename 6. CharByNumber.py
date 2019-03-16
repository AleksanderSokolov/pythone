# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc = "abcdefghijklmnopqrstuvwxyz"  # словарь

charPosition = int(input("charPosition = "))

n = 0   # Счетчик букв в строке
char = "Не найден"

for i in abc:
    n = n+1
    if n == charPosition:
        char = i
        break

print(char)
