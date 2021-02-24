class Matrix:

    def __init__(self, data):
        self.data = data
        pass

    def __str__(self):
        max_len = max([len(str(e)) for r in self.data for e in r])
        return ''.join([f"""{''.join([f'{j:<{max_len + 1}}' for j in i])}\n""" for i in self.data])

    def __add__(self, other):
        return Matrix([[k + l for k, l in zip(i, j)] for i, j in zip(self.data, other.data)])


ma = Matrix([[112, 2, 3], [4, 5, 6], [7, 8, 9]])
ma1 = Matrix([[9, 8123, 7], [6, 544, 4], [3, 2, 1]])

print(ma)
print(ma1)
print(ma + ma1 + ma + ma1)
