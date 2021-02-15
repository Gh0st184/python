def addition(number):
    """Складывает числа

    :param number: Строка чисел разделенных пробелом
    :return: Возвращает сумму
    """
    number = number.split()
    j = 0
    for i in number:
        if i.isdigit():
            j += int(i)
        elif i == "q":
            return j, False
    return j, True


sum_number = 0
data = input("Введите строку чисел разделенную пробелом: ")
sum_number += addition(data)[0]
print(f"Сумма чисел = {sum_number}")
while True:
    data = input("Продолжите ввод чисел или введите q для выхода: ")
    a = addition(data)
    if a[1] is False:
        sum_number += a[0]
        break
    else:
        sum_number += a[0]
        print(f"Сумма чисел = {sum_number}")

print(f"Сумма чисел = {sum_number}, программа закончена.")
