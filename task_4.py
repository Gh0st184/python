words = input('Введите несколько слов разделенных пробелами: ')
for i, j in enumerate(words.split()):
    if len(j) > 10:
        j = j[0:10]
    print(f'{i}. {j}')
