import os
from math import *


def file_read(title):
    a = []
    b = open(title, 'r')
    b.read(4)
    for line in b:
        a.append(line)
    return a


a = file_read('text.txt')
a = a[0]
i = 0
lst = []
while i < len(a):
    if a[i] == "[":
        i += 1
        start = i
        while a[i] != "]":
            i += 1
        end = i
        lst.append(a[start:end].split(","))

    i += 1
for i in range(len(lst)):
    lst[i] = list(map(int, lst[i]))


class Triangle:
    def __init__(self, a1, a2, a3):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.square()

    def calculations(self):
        self.a = sqrt((self.__a1[1] - self.__a1[0]) ** 2)
        self.b = sqrt((self.__a2[1] - self.__a2[0]) ** 2)
        self.c = sqrt((self.__a3[1] - self.__a3[0]) ** 2)
        self.p = (self.a + self.b + self.c) / 2

    def square(self):
        self.calculations()
        if (self.a < (self.b + self.c)) and (self.b < (self.a + self.c)) and (self.c < (self.b + self.a)):
            self.__square = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
        else:
            self.__square = -1

    @property
    def get_square(self):
        return self.__square


mas = []
for i in range(1, len(lst) - 1):
    a = Triangle(lst[i - 1], lst[i], lst[i + 1])
    mas.append(a.get_square)

print(f"max = {max(mas)}")

minn = max(mas) + 1
for i in mas:
    if i != -1:
        minn = min(i, minn)

print(f"min = {minn}")
