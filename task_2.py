from abc import ABC, abstractmethod


class Clothing(ABC):
    count = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def total_count(self):
        return f"Общий расход ткани составляет {Clothing.count:.2f}"


class Coat(Clothing):
    def __init__(self, name, v):
        self.v = v
        super().__init__(name)

    @property
    def fabric_consumption(self):
        b = float(f"{self.v / 6.5 + 0.5:.2f}")
        Clothing.count += b
        return f"Расход ткани на пальто размера {self.v} составит {b}"


class Costume(Clothing):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def fabric_consumption(self):
        b = 2 * self.h + 0.3
        Clothing.count += b
        return f"Расход ткани на костюм с ростом {self.h} составит {b}"


coat1 = Coat("Пиджак", 7)
print(coat1.fabric_consumption)
print(coat1.total_count)
costume1 = Costume("Костюм", 97)
print(costume1.fabric_consumption)
print(costume1.total_count)
print(coat1.total_count)
