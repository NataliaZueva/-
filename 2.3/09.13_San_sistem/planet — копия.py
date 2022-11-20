def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([x for x in line.split()])
    return a


# Планеты - размер, отдаленность.....
pla = file_read('Planes.txt')
kk = []
for i in pla:
    print(i[0])
