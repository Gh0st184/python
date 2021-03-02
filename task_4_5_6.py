from abc import abstractmethod, ABC


class OfficeEquipment(ABC):
    """Офисная техника"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def report(self):
        pass


class Printer(OfficeEquipment):
    """Принтер"""
    type = 'Принтер'
    __prints = 0

    def print_document(self):
        print('Печатает документ')
        self.__prints += 1

    def report(self):
        self.print_document()
        return f'Марка принтера: {self.brand}\nМодель принтера: {self.model}\nВсего распечатано листов: {self.__prints}'


class Scanner(OfficeEquipment):
    """Сканер"""
    type = 'Сканер'
    __scans = 0

    def scan_document(self):
        print('Сканирует документ')
        self.__scans += 1

    def report(self):
        return f'Марка cканера: {self.brand}\nМодель сканера: {self.model}\nВсего отсканировано листов: {self.__scans}'


class Xerox(OfficeEquipment):
    """Ксерокс"""
    type = 'Ксерокс'
    __scans = 0
    __prints = 0
    __copies = 0

    def copy_document(self):
        print('Копирует документ')
        self.__copies += 1

    def print_document(self):
        print('Печатает документ')
        self.__prints += 1

    def scan_document(self):
        print('Сканирует документ')
        self.__scans += 1

    def report(self):
        self.print_document()
        return f'Марка принтера: {self.brand}\nМодель принтера: {self.model}\nВсего распечатано листов: ' \
               f'{self.__prints}\nВсего скопировано листов: {self.__copies}\nВсего отсканировано листов: {self.__scans}'


class Warehouse:
    """Склад"""

    def __init__(self, warehouse_name):
        self.warehouse_name = warehouse_name
        self.warehouse = []

    def admission_warehouse(self, obj, quantity):
        for _ in range(int(quantity)):
            self.warehouse.append(obj)

    def moving(self, obj_warehouse):
        """Функция перемещения

        obj_warehouse: Объект склада
        """
        while True:
            answer = input('Введите тип перемещаемой техники, варианты(Принтер, Сканер, Ксерокс):')
            if answer.lower() == 'принтер' or answer.lower() == 'сканер' or answer.lower() == 'ксерокс':
                for i in self.warehouse:
                    if answer.lower() == i.type.lower():
                        obj_warehouse.warehouse.append(self.warehouse.pop(self.warehouse.index(i)))
                        break
                break
            print('Здесь необходимо ввести (Принтер, Сканер или Ксерокс) попробуйте еще раз')



    def report(self):
        __printer = [i for i in self.warehouse if i.type == 'Принтер']
        __scanner = [i for i in self.warehouse if i.type == 'Сканер']
        __copies = [i for i in self.warehouse if i.type == 'Ксерокс']
        return f'Всего техники на {self.warehouse_name} {len(self.warehouse)}\nИз них:\nПринтеров: {len(__printer)}\n' \
               f'Сканеров: {len(__scanner)}\nКопиров: {len(__copies)}'


class ItDepartment(Warehouse):
    pass


class AccountingDepartment(Warehouse):
    pass


def validation(data):
    while True:
        if data.isdigit():
            return int(data)
        else:
            data = input('Необходимо ввести число: ')


wr = Warehouse('Склад')
wr.admission_warehouse(Printer(input('Введите марку: '), input('Введите модель: ')),
                       validation(input('Введите количество: ')))
wr.admission_warehouse(Scanner(input('Введите марку: '), input('Введите модель: ')),
                       validation(input('Введите количество: ')))
wr.admission_warehouse(Xerox(input('Введите марку: '), input('Введите модель: ')),
                       validation(input('Введите количество: ')))

it = ItDepartment('IT подразделение')
ac = AccountingDepartment('Бухгалтерия')
print(wr.report())
print(30 * '-')
for i in wr.warehouse:
    if i.type == 'Принтер':
        i.print_document()
        print(i.report())
        print(30 * '-')
    elif i.type == 'Сканер':
        i.scan_document()
        print(i.report())
        print(30 * '-')
    elif i.type == 'Ксерокс':
        i.scan_document()
        i.print_document()
        i.copy_document()
        print(i.report())

print(30 * '-')
print(it.report())
wr.moving(it)
print(30*'-')
print(wr.report())
print(30 * '-')
print(it.report())
for i in it.warehouse:
    if i.type == 'Принтер':
        i.print_document()
        print(i.report())
        print(30 * '-')
    elif i.type == 'Сканер':
        i.scan_document()
        print(i.report())
        print(30 * '-')
    elif i.type == 'Ксерокс':
        i.scan_document()
        i.print_document()
        i.copy_document()
        print(i.report())
