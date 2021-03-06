"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

try:
    USER_VAL = int(input(
        "Введите номер буквы на латинском языке: "))
    USER_LETTER = chr(ord("a") + USER_VAL - 1)

except ValueError as exception:
    print(
        f"Необходимо ввести номер буквы в виде числа!\n"
        f"{exception}")
else:
    print(f"Введёному номеру соответствует буква: {USER_LETTER}")
