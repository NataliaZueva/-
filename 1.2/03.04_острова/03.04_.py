def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([int(x) for x in line.split()])
    return a


def fas(w, v):
    i1 = len(v)  # строки
    j1 = len(v[1])  # cтолбцы
    for i in range(len(v)):
        for j in range(len(v[1])):
            if v[i][j] != w:
                v[i][j] = 0
    for i in v:
        for i2 in i:
            print(i2, end=' ')
        print()

    return v


def counter(i, j, i1, j1):
    global v
    save = v[i][j]
    v[i][j] = 0
    v1 = set()
    # print(v1)
    if save == 0:
        return v1
    elif save != 0:
        # влево
        if j - 1 > 0 and save == v[i][j - 1]:
            v[i][j - 1] = 0
            v1 |= counter(i, j - 1, i1, j1)
            v1.add((v[i][j - 1], i, j - 1))
        # вверх
        if i - 1 > 0 and save == v[i - 1][j]:
            v[i - 1][j] = 0
            v1 |= counter(i - 1, j, i1, j1)
            v1.add((v[i - 1][j], i - 1, j))
        # вправо
        if j + 1 < j1 and save == v[i][j + 1]:
            v[i][j + 1] = 0
            v1 |= counter(i, j + 1, i1, j1)
            v1.add((v[i][j + 1], i, j + 1))
        # вниз
        if i + 1 < i1 and save == v[i + 1][j]:
            v[i + 1][j] = 0
            v1 |= counter(i + 1, j, i1, j1)
            v1.add((v[i + 1][j], i + 1, j))
    # print(v)
    return v1


# for w in range(1, 10):
#     print("Нахождение всех", w, ":")
#     fas(w, file_read("island.txt"))
k = 0
v1 = set()
v = file_read("island.txt")
i1 = len(v)  # строки
j1 = len(v[1])  # cтолбцы
for i in range(i1):
    for j in range(j1):
        counters = counter(i, j, i1, j1)
        print("Privet",counters)
        if counter != set():
            k += 1

print("Всего острoвков", counter(0,0,i1,j1))
