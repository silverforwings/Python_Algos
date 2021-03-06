"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

try:
    X1_VAL = float(input("Введите значение координаты X для первой точки: "))
    Y1_VAL = float(input("Введите значение координаты Y первой точки: "))
    X2_VAL = float(input("Введите значение координаты X для второй точки: "))
    Y2_VAL = float(input("Введите значение координаты Y второй точки: "))

    if X1_VAL - X2_VAL == 0:
        raise ZeroDivisionError(
            "x1 - x2 = 0! x1 и x2 должны иметь разные значения! Деление на ноль запрещено!")
except ValueError as exception:
    print(f"Ошибка ввода данных! \n{exception}")
except ZeroDivisionError as exception:
    print(exception)
else:
    print(
        f"y = kx + b – функция общего вида \n"
        f"Первая точка: {X1_VAL}k + b = {Y1_VAL}; b = {Y1_VAL} - {X1_VAL}k \n"
        f"Вторая точка: {X2_VAL}k + b = {Y2_VAL} ; -{X2_VAL}k + {Y1_VAL} - {X1_VAL}k = {Y2_VAL} \n")

    K_VAL = (Y1_VAL - Y2_VAL) / (X1_VAL - X2_VAL)
    B_VAL = Y2_VAL - K_VAL * X2_VAL

    print(f"y = {K_VAL:.2f}x + {B_VAL:.2f}")
