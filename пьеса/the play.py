def read():
    global number, dictionary, replica, roles
    with open("roles.txt", "r",encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            if line != "roles:":
                if line != "textLines:":
                    roles.append(line)
                else:
                    break
        roles.append("Слова автора")
        for i in range(len(roles)):
            replica.append([])
        for line in file:
            number += 1
            #print(number)
            line = line.rstrip()
            if ":" in line:
                if "(" in line:
                    value = line.partition("(")[2]
                    for i in range(len(roles)):
                        if "Слова автора" == roles[i]:
                            replica[i].append(value.replace(')', ''))
                    line = line.partition("(")[0]
                if line.partition(":")[0] in roles:  #разделение:   роль - ":" - слова
                    key = line.partition(":")[0]
                    value = line.partition(":")[2]    #Bозвращает коллекцию значений в словаре..
                    dictionary[key] = value
                    for i in range(len(roles)):
                        if key == roles[i]:
                            result = str(number) + str(")") + str(dictionary[key])
                            replica[i].append(result)    
                    last_key = key
            else:
                if "(" in line:
                    value = line.partition("(")[0]
                    for i in range(len(roles)):
                        if "Слова автора" == roles[i]:
                            replica[i].append(value.replace(')', ''))
                else:
                    value = line
                    dictionary[last_key] = value
                    for i in range(len(roles)):
                        if last_key == roles[i]:
                            replica[i].append(dictionary[last_key])         
number = 0
dictionary = { }
replica = []
roles = []
print("Перед вами чтение пьесы по ролям\nЗуева Наталья 14122")
try:
    open("roles.txt", "r",encoding='utf-8')
except FileNotFoundError:
    print("Кажется файл исчез... Добавте в папку файл roles.txt")
else:
    read()
for i in range(len(roles)):
    print()
    #w='Ничего не говорит'
    print(str(roles[i]) + str(": "))
    for q in range(len(replica[i])):
        print(replica[i][q])
