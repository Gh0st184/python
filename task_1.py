file = open("task_1.txt", "w", encoding="utf-8")
while True:
    data = input("Введите данные для записи или пустую строку: ")
    if data:
        file.write(f"{data}\n")
    else:
        break
file.close()
