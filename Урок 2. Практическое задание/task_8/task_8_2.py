"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def how_many_times(count, target_num, num=1, count_target_num=0):
    """Рекурсивный подсчёт

    count - количество чисел
    target_num - целевое число, которое будем искать
    num - порядковый номер вводимого числа
    count_target_num - количество найденных целевых чисел
    """
    if count <= 0:
        return f"Было введено {count_target_num} цифр '{target_num}'"
    user_num = int(input(f"Число {num}: "))
    while user_num > 0:
        if user_num % 10 == target_num:
            count_target_num += 1
        user_num //= 10
    return how_many_times(count - 1, target_num, num + 1, count_target_num)


try:
    COUNT = int(input("Сколько будет чисел?\n"))
    TARGET_NUMBER = int(input("Какую цифру считать?\n"))

    print(how_many_times(COUNT, TARGET_NUMBER))
except ValueError:
    print("Необходимо вводить только числа, последовательно, "
          "без запятых и других знаков, а не текст!")
