class Road:

    def __init__(self, lenght, width):
        self._length = int(lenght)
        self._width = int(width)
        self.__thickness = 5
        self.__weight = 25

    def calculation_of_the_mass(self):
        mass = self._length * self._width * self.__weight * self.__thickness
        print(f"Масса асфальта составляет {mass / 1000:.0f} тонн")


while True:
    try:
        r = Road(input("Введите длинну: "), input("Введите ширину: "))
        r.calculation_of_the_mass()
        break
    except ValueError:
        print("Необходимо ввести цифры")
