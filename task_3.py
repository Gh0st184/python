def my_func(var_1, var_2, var_3):
    """Функция удаляет минимальное число

    :param var_1: Число
    :param var_2: Число
    :param var_3: Число
    :return: возвращает сумму двух чисел
    """
    number = [var_1, var_2, var_3]
    number.remove(min(number))
    return number[0] + number[1]


while True:
    number_1 = input("Введите первое число: ")
    number_2 = input("Введите второе число: ")
    number_3 = input("Введите третье число: ")
    try:
        number_1, number_2, number_3 = int(number_1), int(number_2), int(number_3)
        break
    except ValueError:
        print("Необходимо ввести три числа, попробуйте еще раз.")

print(my_func(number_1, number_2, number_3))
