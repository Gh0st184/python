class Cell:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        """Сложение клеток"""
        return f"Результат операции сложения = {Cell(self.a + other.a)}"

    def __sub__(self, other):
        """Вычитание клеток"""
        if self.a > other.a:
            return f"Результат операции вычитания = {Cell(self.a - other.a)}"
        else:
            return "Разность клеток меньше нуля"

    def __mul__(self, other):
        """Умножение клеток"""
        return f"Результат операции умножения = {Cell(self.a * other.a)}"

    def __truediv__(self, other):
        """Деление клеток"""
        return f"Результат операции деления = {Cell(round(self.a / other.a))}"

    def __str__(self):
        return f"{self.a}"

    def make_order(self, count):
        b = [count * '*' for _ in range(self.a // count)]
        b.append((self.a % count) * '*')
        return '\n'.join(b)


cell1 = Cell(6)
cell2 = Cell(5)
cell3 = Cell(2)
print(cell1.a)
print(cell2.a)
print(cell3.a)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell3 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(Cell.make_order(cell2, 2))
