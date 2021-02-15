revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if revenue > costs:
    print("Фирма работает с прибылью")
    print(f"Рентабельность компании составляет {(revenue - costs) / revenue:.2f}")
    staff = int(input("Введите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сотрудника составляет {(revenue - costs) / staff:.2f}")
elif revenue < costs:
    print("Фирма работает в убыток")
elif revenue == costs:
    print("Прибыль и издержки равны")
