def data(name, last_name, year, city, email, telephone):
    """Выводит данные пользователя на экран

    :param name: Имя пользователя
    :param last_name: Фамилия пользователя
    :param year: Год рождения пользователя
    :param city: Город пользователя
    :param email: email
    :param telephone: Телефон
    :return: Возвращает данные пользователя одной строкой
    """
    print(f"Данные о пользователе: {last_name} {name}, год рождения: {year}, город: {city}, "
          f"Email: {email}, телефон: {telephone}")


name = input("Введите имя пользователя: ")
last_name = input("Введите фамилию пользователя: ")
year = input("Введите год рождения пользователя: ")
city = input("Введите город пользователя: ")
email = input("Введите email пользователя: ")
telephone = input("Введите телефон пользователя: ")

data(name=name, last_name=last_name, year=year, city=city, email=email, telephone=telephone)
