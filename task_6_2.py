from itertools import cycle

my_list = "abcdefgh"
j = 1
for i in cycle(my_list):
    print(i)
    j += 1
    if j == 10:
        break
