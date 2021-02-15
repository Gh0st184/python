file = open("task_2.txt", "r", encoding="utf-8")
data = file.readlines()
for j, i in enumerate(data, 1):
    a = 0
    for _ in i.split():
        a += 1
    print(f"В {j} строке {a} слов")
print(f"Всего строк {j}")
file.close()
