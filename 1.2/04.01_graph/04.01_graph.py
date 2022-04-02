import math
m = math.inf
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
                w = T[start] + dw
                if w < T[j]:
                    T[j] = w
                    M[j] = start
        start = minimum(T, set)
        if start >= 0:
            set.add(start)
    
def read(title):
    string = []
    with open(title, "r", encoding='utf-8') as file:
        for line in file:
            string.append([int(x) for x in line.split()])
    return string

graph = read('abc.txt')
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
