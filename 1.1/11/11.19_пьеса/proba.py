with open("roles.txt", "r", encoding='utf-8') as file:
    for line in file:
        line = line.rstrip()
        if line != "roles:":
            if line != "textLines:":
                roles.append(line)
            else:
                break