def int_func(var):
    """Функция проверяет состоит ли строка из маленьких латинских букв

    :param var: строка
    :return: возвращает исходное слово с большой буквы или False
    """
    for i in var:
        if ord(i) not in range(97, 123):
            return False
    return var.title()


while True:
    data = input("Введите строку состоящую из маленьких латинских букв разделенных пробелами: ")
    data = data.split()
    a = []
    j = 0
    for i in data:
        if int_func(i) is False:
            print(f"Необходимо вводить слова из маленьких латинских букв, попробуйте еще раз.")
            break
        else:
            j += 1
            a.append(int_func(i))
    if j == len(data):
        print(' '.join(a))
        break
