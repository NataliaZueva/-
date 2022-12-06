from math import *


class Points:
    def __init__(self, title):
        self.title = title
        self.file_read()
        self.creating_array()

    def file_read(self):
        self.a = []
        b = open(self.title, 'r')
        b.read(4)
        for line in b:
            self.a.append(line)
        self.a = self.a[0]

    def creating_array(self):
        i = 0
        self.__lst = []
        while i < len(self.a):
            if self.a[i] == "[":
                i += 1
                start = i
                while self.a[i] != "]":
                    i += 1
                end = i
                self.__lst.append(self.a[start:end].split(","))
            i += 1
        for i in range(len(self.__lst)):
            self.__lst[i] = list(map(int, self.__lst[i]))

    @property
    def array(self):
        return self.__lst

    def __len__(self):
        return len(self.__lst)

    def __getitem__(self, key):
        return self.__lst[key]


class Triangle:
    def __init__(self, a1, a2, a3):
        self.a, self.b, self.c, self.p = None, None, None, None
        self.__square = -1
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
        # if (self.a < (self.b + self.c)) and (self.b < (self.a + self.c)) and (self.c < (self.b + self.a)):
        #     self.__square = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
        # self.__square = 0.5 * (self.__a1[0] * (self.__a2[1] - self.__a3[1]) +
        #                        self.__a2[0] * (self.__a3[1] - self.__a1[1]) +
        #                        self.__a3[0] * (self.__a1[1] - self.__a2[1]))
        # self.__square = 0.5 * ((self.__a1[0] - self.__a3[0]) * (self.__a2[1] - self.__a3[1]) -
        #                        (self.__a2[0] - self.__a3[0]) * (self.__a1[1] - self.__a3[1]))
        # else:
        #     pass
        self.__square = 0.5 * (self.__a1[0] * (self.__a2[1] - self.__a3[1]) +
                               self.__a2[0] * (self.__a3[1] - self.__a1[1]) +
                               self.__a3[0] * (self.__a1[1] - self.__a2[1]))

    @property
    def get_square(self):
        return self.__square

    def __ne__(self, other):
        return self.__square != other

    def __lt__(self, other):
        return self.__square < other

    def __gt__(self, other):
        return self.__square > other


class Fourangle:
    def __init__(self, a1, a2, a3, a4):
        self.a, self.b, self.c, self.p = None, None, None, None
        self.__square = -1
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.square()

    def calculations(self):
        self.a = sqrt((self.__a1[1] - self.__a1[0]) ** 2)
        self.b = sqrt((self.__a2[1] - self.__a2[0]) ** 2)
        self.c = sqrt((self.__a3[1] - self.__a3[0]) ** 2)
        self.d = sqrt((self.__a4[1] - self.__a4[0]) ** 2)
        self.p = (self.a + self.b + self.c) / 2

    def square(self):
        self.calculations()
        self.__square = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))


set_points = Points('plist.txt')

maximum, minimum = 0, 0
for i in range(1, set_points.__len__() - 1):
    a = Triangle(set_points[i - 1], set_points[i], set_points[i + 1])
    if a != -1 and maximum == 0 and minimum == 0:
        maximum, minimum = a.get_square, a.get_square
    if a != -1:
        if a.get_square > maximum:
            maximum = a.get_square
        if a.get_square < minimum:
            minimum = a.get_square

print(f"max = {maximum}, min = {minimum}")
