def my_func(x, y):
    """Вычисляет отрицательную степень числа

    :param x: Действительное положительное число
    :param y: Целое отрицательное число
    :return:
    """
    exp = 1 / (x ** abs(y))
    return exp


def my_func_1(x, y):
    """Вычисляет отрицательную степень числа

    :param x: Действительное положительное число
    :param y: Целое отрицательное число
    :return:
    """
    a = 1
    for i in range(0, abs(y)):
        a *= x
    exp = 1 / a
    return exp


while True:
    x = input("Введите x - действительное положительное число: ")
    y = input("Введите y - отрицательное целое число: ")
    if x.isdigit() and float(x) > 0:
        try:
            x, y = float(x), int(y)
            if y < 0:
                break
        except ValueError:
            print("Необходимо ввести y - отрицательное целое число")
            continue
    print("Необходимо ввести x - действительное положительное число")

print(f"Функция с ** {my_func(x, y)}")
print(f"Функция без ** {my_func_1(x, y)}")
