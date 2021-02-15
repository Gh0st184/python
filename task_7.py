from functools import reduce


def fact(n):
    for i in range(1, n + 1):
        my_list = [j for j in range(1, i + 1)]
        yield reduce(lambda el, el1: el * el1, my_list)


for el in fact(5):
    print(el)
