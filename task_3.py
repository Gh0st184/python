class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника {self.surname} {self.name}")

    def get_total_income(self):
        print(f"Доход с учетом премии {self._income['wage'] + self._income['bonus']}")


while True:
    try:
        staff = Position(input("Введите имя сотрудника: "), input("Введите фамилию сотрудника: "),
                         input("Введите должность: "), input("Введите аванс: "), input("Введите премию: "))
        staff1 = Position(input("Введите имя сотрудника: "), input("Введите фамилию сотрудника: "),
                          input("Введите должность: "), input("Введите аванс: "), input("Введите премию: "))
        break
    except ValueError:
        print("Аванс и премию необходимо вводить цифрами, попробуйте еще раз")

print("Первый сотрудник")
print(f"Имя сотрудника {staff.name}, фамилия {staff.surname}, должность {staff.position}")
staff.get_total_income()
staff.get_full_name()

print(f"Имя сотрудника {staff1.name}, фамилия {staff1.surname}, должность {staff1.position}")
staff1.get_total_income()
staff1.get_full_name()
