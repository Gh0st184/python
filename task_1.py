def division(n_1, n_2):
    """Функция делит два числа

    :param n_1: Число 1
    :param n_2: Число 2, должно быть != 0
    :return: Возвращает результат деления
    """
    div = n_1 / n_2
    return div


while True:
    number_1 = input("Введите первое число: ")
    number_2 = input("Введите второе число: ")
    if number_1.isdigit() and number_2.isdigit() and int(number_2) != 0:
        number_1, number_2 = int(number_1), int(number_2)
        break
    print("Необходимо ввести два числа, а также второе число не может быть 0, попробуйте еще раз.")
print(division(number_1, number_2))
