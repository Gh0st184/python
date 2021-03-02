class Number(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    try:
        data = input("Введите данные: ")
        if data.lower() == 'stop':
            break
        if not data.isdigit():
            raise Number('Вы должны ввести число. Чтобы выйти введите "stop"')
    except Number as err:
        print(err)
    else:
        my_list.append(int(data))

print(my_list)
