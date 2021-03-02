class NotComplex(Exception):
    def __init__(self, txt):
        self.txt = txt


class ComplexNumber:
    def __init__(self, data):
        try:
            self.data = data
            if not ComplexNumber.validation(self.data):
                raise NotComplex('Необходимо подать на вход комплексное число')
        except NotComplex as err:
            print(err)

    @staticmethod
    def validation(data):
        return isinstance(data, complex) and data.imag != 0

    def __add__(self, other):
        return ComplexNumber(self.data + other.data)

    def __mul__(self, other):
        return ComplexNumber(self.data * other.data)


mc3 = ComplexNumber('4+3i')
mc = ComplexNumber(complex(1, 2))
print(mc.data)
mc1 = ComplexNumber(complex(2, 3))
print(mc1.data)
print((mc + mc1).data)
print((mc + mc1 + mc).data)
print((mc * mc1).data)
print((mc * mc1 * mc).data)
