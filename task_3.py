while True:
    month_number = input("Введите месяц в формате числа от 1 до 12: ")
    if month_number.isdigit():
        month_number = int(month_number)
        break
month = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn',
         'Autumn', 'Winter', 'Winter']
print(f"Через список - {month[month_number - 1]}")

month_dict = {11: 'Winter', 12: 'Winter', 1: 'Winter',
              2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
              6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn',
              10: 'Autumn'}
print(f"Через словарь - {month_dict[month_number]}")
