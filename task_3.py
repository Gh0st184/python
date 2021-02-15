file = open("task_3.txt", "r", encoding="utf-8")
data = file.readlines()
salary = 0
j = 0
for i in data:
    i = i.split()
    salary += int(i[2])
    j += 1
    if int(i[2]) < 20000:
        print(f"Сотрудник {i[0]} имеет оклад менее 20к, его оклад составляет {i[2]}")
print(f"Средняя зарплата сотрудников составляет {salary / j:.2f}")
file.close()
