import math
import time
from random import randint


def task1():
    a, b, c = input("Введите 3 переменных: ").split()
    a, b, c = b, c, a
    endTime = time.time()
    print(a, b, c)
    totalTime = endTime
    print("Время, затраченное на выполнение = ", totalTime)


def task2_1():
    flag = True
    while flag:
        a, b = input("Введите 2 числа: ").split()
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print('Введено не число')
        else:
            return a + b


def task3_1():
    x = randint(0, 100)
    x1 = x ** 5
    return x1


def task3_2():
    task3_1()
    x2 = 1
    for i in range(5):
        x2 = x * x2
    return x2


def task4():
    i = 0
    a = 1
    f = []
    while i <= 250:
        i += a
        a = i - a
        f.append(i)
    flag = True
    while flag:
        c = int(input("Введите число от 0 до 250: "))
        if (c >= 0) and (c <= 250):
            flag = False
        else:
            print("Кажется вы не попали в промежуток чисел...")
    if c in f:
        print("Это число входит в список фибоначи")
    else:
        print("Это число не входит в список фибоначи")


# задача 5
# mydict = {"Зима": {1, 2, 12}, "Весна": {3, 4, 5}, "Лето": {6, 7, 8}, "Осень": {9, 10, 11},}
# # a = input("Введите номер месяца: ")
# print(list(mydict.keys())[list(mydict.values()).index(19)])

def task6():
    N = int(input("Введите N: "))
    sum_num, k1, k2 = 0, 0, 0
    for i in range(1, N + 1):
        sum_num += i
        if i % 2 != 0:
            k1 += 1
        else:
            k2 += 1
    return sum_num, k1, k2


def divider(a):
    if a == 1:
        return 1
    sum_num = 2
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            sum_num += 1
    return sum_num


def task7():
    n = int(input("Введите n: "))
    for i in range(1, n + 1):
        print(i, divider(i))


def task8():
    N, M = map(int, input("Введите N и M: ").split())
    for b in range(N, M):
        for a in range(N, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                print(a, b, int(c))


def refund(a):
    flag = -1
    c = a
    while c != 0:
        d = c % 10
        if d != 0:
            if a % d == 0:
                flag = 1
            elif a % d != 0:
                flag = 0
                break
        else:
            flag = 0
            break
        c = c // 10
    if flag:
        return a


def task9():
    N, M = map(int, input("Введите N и M ").split())
    roster = []
    for i in range(N, M + 1):
        a = refund(i)
        if a is not None:
            roster.append(i)
    print(roster)


def task10():
    def divider1(a):
        if a == 1:
            return 1
        sum_num = 0
        for i in range(1, a // 2 + 1):
            if a % i == 0:
                sum_num += i
        return sum_num

    N, i = 1, 1
    while N < 5:
        i += 1
        if i == divider1(i):
            print(i)
            N += 1


def task12():
    mac = [1, 2, 3, 4, 5]
    my_mac = list(range(len(mac), -1, -1))
    print(my_mac)


def task13():
    def sum_mac(m, l_m):
        if l_m != 0:
            return sum_mac(m, l_m - 1) + m[l_m - 1]
        else:
            return 0

    mac = [1, 2, 3, 4, 5]
    res = sum_mac(mac, len(mac))
    print(res)
#
#
# a = input("Номер задачи: ")
# list = [task1, task2_1, task3_1, task3_2, task4, task6, task7, task8, task9, task10]
# list[a - 1]()
