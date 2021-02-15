begin_km = int(input("Введите количество км которое спортсмен пробежал в 1 день: "))
end_km = int(input("Введите количество км которое нужно пробежать спортсмену: "))
day = 1
while begin_km < end_km:
    print(f"{day}-й день: {begin_km:.2f}")
    begin_km += (begin_km / 100) * 10
    day += 1
print(f"{day}-й день: {begin_km:.2f}")
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {end_km} км.")
