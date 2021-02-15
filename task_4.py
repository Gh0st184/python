number = int(input("Введите число: "))
max_number = 0
while number != 0:
    if number % 10 > max_number:
        max_number = number % 10
    number = number // 10
print(f"Наибольшим числом является {max_number}")
