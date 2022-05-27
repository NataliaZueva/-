import math

m = math.inf

vertexes = {i[0]: i.split()[1:] for i in open('abc.txt').readlines()[1:]}

star = True

while not star:
    start, end = list(input('Ведите вершины начала и конца маршрута ').split())
    star =