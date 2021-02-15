import json

with open("task_7.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    organization = {}
    for i in data:
        i = i.split()
        organization[i[0]] = int(i[2]) - int(i[3])
    j = 0
    for i in organization.values():
        if int(i) > 0:
            j += int(i)
    dictionary = [organization, {"average_profit": j / len(organization.values())}]
    with open("task_7.json", "w", encoding="utf-8") as file_json:
        json.dump(dictionary, file_json)
