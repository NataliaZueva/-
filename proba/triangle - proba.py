import os
# from math import *
#
#
# def file_read(title):
#     a = []
#     b = open(title, 'r')
#     b.read(4)
#     for line in b:
#         a.append(line)
#     return a
#
#
# a = file_read('text.txt')
# a = a[0]
# i = 0
# lst = []
# while i < len(a):
#     if a[i] == "[":
#         i += 1
#         start = i
#         while a[i] != "]":
#             i += 1
#         end = i
#         lst.append(a[start:end].split(","))
#
#     i += 1
# for i in range(len(lst)):
#     lst[i] = list(map(int, lst[i]))
#
#
# class Triangle:
#     def __init__(self, a1, a2, a3):
#         self.__a1 = a1
#         self.__a2 = a2
#         self.__a3 = a3
#         self.square()
#
#     def calculations(self):
#         self.a = sqrt((self.__a1[1] - self.__a1[0]) ** 2)
#         self.b = sqrt((self.__a2[1] - self.__a2[0]) ** 2)
#         self.c = sqrt((self.__a3[1] - self.__a3[0]) ** 2)
#         self.p = (self.a + self.b + self.c) / 2
#
#     def square(self):
#         self.calculations()
#         if (self.a < (self.b + self.c)) and (self.b < (self.a + self.c)) and (self.c < (self.b + self.a)):
#             self.__square = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
#         else:
#             self.__square = -1
#
#     @property
#     def get_square(self):
#         return self.__square
#
#
# mas = []
# for i in range(1, len(lst) - 1):
#     a = Triangle(lst[i - 1], lst[i], lst[i + 1])
#     mas.append(a.get_square)
#
# print(f"max = {max(mas)}")
#
# minn = max(mas) + 1
# for i in mas:
#     if i != -1:
#         minn = min(i, minn)
#
# print(f"min = {minn}")





#
# class Points:
#     def __init__(self, title):
#         self.title = title
#         self.file_read()
#         self.creating_array()
#
#     def file_read(self):
#         self.a = []
#         b = open(self.title, 'r')
#         b.read(4)
#         for line in b:
#             self.a.append(line)
#         self.a = self.a[0]
#
#     def creating_array(self):
#         i = 0
#         self.__lst = []
#         while i < len(self.a):
#             if self.a[i] == "[":
#                 i += 1
#                 start = i
#                 while self.a[i] != "]":
#                     i += 1
#                 end = i
#                 self.__lst.append(self.a[start:end].split(","))
#             i += 1
#         for i in range(len(self.__lst)):
#             self.__lst[i] = list(map(int, self.__lst[i]))
#
#     @property
#     def array(self):
#         return self.__lst
#
#
# set_points = Points('text.txt')
# print('dsfag', set_points.array)
# print(set_points[2])




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


set_points = Points('text.txt')

mas = []
for i in range(1, set_points.__len__() - 1):
    a = Triangle(set_points[i - 1], set_points[i], set_points[i + 1])
    mas.append(a.get_square)

minn = max(mas) + 1
for i in mas:
    if i != -1:
        minn = min(i, minn)

print("max =", max(mas))
print(f"min = {minn}")
