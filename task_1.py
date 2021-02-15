time = 16
hello = "Привет, это первая программа на курсе 'Основы языка Python'"
print(hello)
name = input("Как тебя зовут? ")
age = int(input('Сколько тебе лет? '))
age_month = age * 12
age_month_last = age_month + time
age_last = age_month_last // 12
print(f"Привет {name}, тебе уже {age_month} месяцев или {age} лет и все это время ты жил без Python!\n")
print("""Но ничего, через каких-то {} месяцев тебе стукнет {} лет или опять же {} месяцев и ты уже будешь 
знать Python на достаточно неплохом уровне!  
      """.format(time, age_last, age_month_last))
print("Однако необходимо учиться %d месяцев и не отлынивать! Сдвавать все домашние задания вовремя!" % time)
