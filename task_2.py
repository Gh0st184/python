class ZeroDev(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
try:
    b = input('Введите делитель: ')
    if int(b) == 0:
        raise ZeroDev('Вы ввели делитель = 0')
except ZeroDev as err:
    print(err)
else:
    print(f'Результат деления {int(a)/int(b)}')
