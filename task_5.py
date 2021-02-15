from functools import reduce


def composition(prev_el, el):
    return prev_el * el


print(reduce(composition, [i for i in range(100, 1001) if i % 2 == 0]))
