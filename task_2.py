seconds = int(input("Введите время в секундах: "))
print(f"{seconds // 60 // 60:02}:{seconds // 60 % 60:02}:{seconds % 60:02}")
