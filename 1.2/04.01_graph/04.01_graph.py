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
        matrix.append(list(map(int, graph[i][1:])))
    return matrix
    
def minimum(T, set):
    global m
    amin = -1 
    for i, t in enumerate(T):      #счетчик элементов последовательности для циклка
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

graph = read('abc.txt')
print("graph", "\n", graph, "\n")
a = adjacency_matrix(graph)
print("aaaaa", "\n", a)

N = len(graph)
start, end = list(map(int,input('У вас всего ' + str(len(graph)) + ' вершины. Введите вершины начала и конца пути: ').split()))
starts = start
T = [m]*N 
set = {start}
T[start] = 0
M = [0]*N 
search()
print(T)
print("От вершины", starts, "до вершины", end, "растояние", T[end:end+1])


