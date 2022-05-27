import math


class Hexagon:
    def __init__(self, r):
        self.__r = r
        self.__area = (3 * math.sqrt(3) * self.__r ** 2) / 2

    def set_r(self, new_r):
        self.__r = new_r
        self.calc_area()

    def r(self):
        return self.__r

    def area(self):
        return self.__area

    def calc_area(self):
        self.__area = (3 * math.sqrt(3) * self.__r ** 2) / 2
        return self.__area

    def __str__(self):
        return str(self.__r)


q = Hexagon(int(input("Введите радиус: ")))
print("area", q.area())
q.set_r(2)
print("calc_area", q.calc_area())
