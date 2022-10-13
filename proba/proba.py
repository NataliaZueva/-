def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([x for x in line.split()])
    return a


tx = file_read("name.txt")
txt = []
pos = []
for i in tx:
    txt.append([str(i[0]), bool(i[1]), (int(i[2]), int(i[3]), int(i[4]))])
    pos.append((int(i[5]), int(i[6])))

print(txt)
