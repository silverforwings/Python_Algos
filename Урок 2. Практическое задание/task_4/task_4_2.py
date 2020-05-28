"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def sum_els(quantity, sum_el=0.0, start=1.0):
    """Сумма n элементов ряда чисел

    quantity - количество элементов
    sum_el - сумма элементов
    start - стартовая позиция
    """
    if quantity:
        return sum_els(quantity - 1, sum_el + start, start / -2)
    return sum_el


try:
    NUM = int(input("Введите количество элементов: "))
    if NUM < 0:
        raise ValueError("Число должно быть положительным!")
    print(f"Количество элементов - {NUM}, их сумма - {sum_els(NUM)}")
except ValueError as exception:
    print(f"Вы ввели не натуральное число! Ошибка ввода данных: {exception}")
