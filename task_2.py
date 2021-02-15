data = input("Введите список элементов через пробел: ").split()
print(data)
for j, i in enumerate(data):
    if j % 2 == 0 and data.index(i) + 1 != len(data):
        data[j], data[j + 1] = data[j + 1], data[j]
print(data)
