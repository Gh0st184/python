from itertools import count

number = input("Введите челое число не более 10: ")
if number.isdigit():
    for i in count(int(number)):
        print(i)
        if i == 10:
            break
