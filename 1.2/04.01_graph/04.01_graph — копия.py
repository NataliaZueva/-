import math

m = math.inf


def read(title):
    string = []
    with open(title, "r", encoding='utf-8') as file:
        for line in file:
            string.append(list(line.split(" ")))
    return string


def adjacency_matrix(graph):
    matrix = []
    for i in range(1, len(graph)):
        matrix.append(list(map(int, graph[i][1:-1])))
    return matrix


def vertexes(graph):
    string = []
    v = []
    for i in range(1):
        string.append(list(graph[i][1:-1]))
    for el in string:
        for le in el:
            v += [le]
    v += ['H']
    return v


def qwe_qwe(start, end):
    global gra
    a = []
    b = []
    for i in range(len(gra)):
        if i == start:
            a = gra[i]
        if i == end:
            b = gra[i]
    return a, b


def qwe():
    global graph, gra
    a, b = list(input('Ведите вершины начала и конца маршрута ').split())
    end = -1
    start = -1
    n = len(gra)
    # print(n)
    for i in range(n):
        if gra[i] == a:
            start = i
        if gra[i] == b:
            end = i
    return start, end


def minimum(T, set):
    global m
    amin = -1
    for i, t in enumerate(T):  # счетчик элементов последовательности для циклка
        if t < m and i not in set:
            m = t
            amin = i
    return amin


def search():
    global start, set, T
    while start != -1:
        for j, dw in enumerate(graph[start]):
            if j not in set:
                w = T[start] + int(dw)
                if w < T[j]:
                    T[j] = w
                    M[j] = start
        start = minimum(T, set)
        if start >= 0:
            set.add(start)


graph1 = read('abc.txt')
graph = adjacency_matrix(graph1)
gra = vertexes(graph1)
start, end = qwe()
a, b = qwe_qwe(start, end)

N = len(graph)
starts = start
T = [m] * N
set = {start}
T[start] = 0
M = [0] * N
search()
print(T)
print("От вершины", a, "до вершины", b, "растояние", T[end:end + 1])
