file = open("task_6.txt", "r", encoding="utf-8")
data = file.readlines()
dictionary = {}
for i in data:
    num = []
    for j in i.split():
        number = ""
        for a in j:
            if a.isdigit():
                number += a
        if number:
            num.append(int(number))
    dictionary[i.split()[0]] = sum(num)
print(dictionary)
file.close()
