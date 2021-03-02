class Date:
    @classmethod
    def extract_str(cls, row_data):
        data = row_data.split('-')
        if len(data) == 3:
            try:
                day = int(data[0])
                month = int(data[1])
                year = int(data[2])
            except ValueError:
                raise ValueError(f'Функция принимает строку вида 10-10-2010, вы ввели {row_data}')
        else:
            raise ValueError(f'Функция принимает строку вида 10-10-2010, вы ввели {row_data}')
        if not Date.validation(day, month, year):
            raise ValueError(f'Функция принимает строку вида 10-10-2010, день от 0 до 31, месяц от 0 до 12,'
                             f' год от 0 до 2100 {row_data}')
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if 32 > day > 0 and 13 > month > 0 and 2101 > year > 0:
            return True
        else:
            return False


mc = Date()
print(mc.extract_str('12-09-2000'))
print(mc.extract_str('31-2-2009'))
print(mc.extract_str('31-12-2009'))
print(mc.extract_str('31-13-2009'))
