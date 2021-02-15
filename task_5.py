file = open("task_5.txt", "w+", encoding="utf-8")
for i in range(101):
    file.write(f"{i} ")
file.seek(0)
data = sum(map(int, file.read().split()))
print(data)
file.close()
