str=(input("Введите пример, состоящий из цифр"))
if (str[1]=="+"):
    result=int(str[0])+int(str[2])
if (str[1] == "-"):
    result = int(str[0]) - int(str[2])
if (str[1] == "*"):
    result = int(str[0]) * int(str[2])
if (str[1] == "/"):
    result = int(str[0]) / int(str[2])
print("Ответ:", result)
