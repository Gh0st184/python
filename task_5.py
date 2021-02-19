class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"Пишем с помощью {self.title}")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"Рисуем с помощью {self.title}")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"Подчеркиваем с помощью {self.title}")


handle = Handle()
pencil = Pencil()
pen = Pen()
stationery = Stationery()

stationery.draw()
handle.draw()
pencil.draw()
pen.draw()

