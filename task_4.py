class Car:

    speed = 1079252848.8
    color = "stealth"
    name = "Космолет"
    is_police = False

    def go(self):
        print(f"Автомобиль {self.name}, цвет {self.color} движется вперед")

    def stop(self):
        print(f"Автомобиль {self.name}, цвет {self.color} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.name}, цвет {self.color} повернул на {direction}")

    def show_speed(self):
        print(f"Автомобиль движется со скоростью {self.speed}")


class TownCar(Car):
    is_police = False
    name = "Kia"
    color = "Красный"
    speed = 60

    def show_speed(self):
        if int(self.speed) > 60:
            print(f"Превышение скорости, у автомобиля {self.name} на {int(self.speed) - 60}")


class PoliceCar(Car):
    is_police = True
    name = "BMW"
    color = "Синий"
    speed = 140


class SportCar(Car):
    is_police = False
    name = "Mercedes"
    color = "Белый"
    speed = 190


class WorkCar(Car):
    is_police = False
    name = "Scania"
    color = "Оранжевый"
    speed = 40

    def show_speed(self):
        if int(self.speed) > 40:
            print(f"Превышение скорости у автомобиля {self.name} на {int(self.speed) - 40}")


town_car = TownCar()
police_car = PoliceCar()
sport_car = SportCar()
work_car = WorkCar()

cars = [town_car, work_car, sport_car, police_car]

for car in cars:
    print(f"\n{car.name}, цвет {car.color} движется со скоростью {car.speed}")
    car.name = "Hyundai"
    car.color = "Черный"
    print(f"{car.name}, цвет {car.color} движется со скоростью {car.speed}")
    car.go()
    car.turn("Направо")
    car.show_speed()
    car.speed = 100
    car.show_speed()
    car.stop()
    print("-" * 20)
