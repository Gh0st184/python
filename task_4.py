file = open("task_4.txt", "r", encoding="utf-8")
data = file.readlines()
dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file1 = open("task_4_w.txt", "w", encoding="utf-8")
for i in data:
    i = i.split()
    if i[0] in dictionary:
        file1.write(f"{dictionary[i[0]]} {i[1]} {i[2]}\n")
file, file1.close()
