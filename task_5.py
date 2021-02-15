rating = [7, 5, 3, 3, 2]
while True:
    number = input('Введите число: ')
    if number.isdigit():
        number = int(number)
        break
print(f'Рейтинг начальный {rating}')
if number in rating:
    rating.reverse()
    rating.insert(rating.index(number), number)
    rating.reverse()
else:
    for i in rating:
        if number > i:
            rating.insert(rating.index(i), number)
            break
        elif number < rating[-1]:
            rating.insert(len(rating), number)
            break
print(f'Рейтинг конечный {rating}')
