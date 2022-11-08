import datetime
import math
import time
from random import randint

from memory_profiler import profile


@profile
def task1():
    start = datetime.datetime.now()
    a, b, c = input("Введите 3 переменных: ").split()
    a, b, c = b, c, a
    end = datetime.datetime.now()
    return f"{a} {b} {c} \nВремя, затраченное на выполнение =  {end - start}"


def task2_1():
    flag = True
    while flag:
        a, b = input("Введите 2 числа: ").split()
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('Введено не число')
        else:
            return a + b


def task2_2():
    sum1 = 0
    n = int(input("Введите N - количество чисел: "))
    k = list(map(float, input(f"Введите {n} чисел: ").split()))
    if n == len(k):
        for i in k:
            sum1 += i
    else:
        print("Количество введенных не соответствыет числу N")
        return task2_2()
    return sum1


def task3_1():
    x = randint(0, 100)
    x1 = x ** 5
    return x1


@profile
def task3_2():
    start = datetime.datetime.now()
    x = task3_1()
    x2 = 1
    for i in range(5):
        x2 = x * x2
    end = datetime.datetime.now()
    return f"{x2} \nВремя, затраченное на выполнение =  {end - start}"


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
        return "Это число входит в список фибоначи"
    else:
        return "Это число не входит в список фибоначи"


def task5():
    res = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
    num = int(input("Введите номер месяца: "))
    print([key for key in res.keys() if num in res[key]])

    num = int(input("Введите номер месяца: "))
    if (num <= 2) or (num == 12):
        return "Зима"
    if (num >= 3) and (num <= 5):
        return "Весна"
    if (num >= 6) and (num <= 8):
        return "Лето"
    if (num >= 9) and (num <= 11):
        return "Осень"


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


@profile
def task7():
    start = datetime.datetime.now()
    N = int(input("Введите N: "))
    for i in range(1, N + 1):
        print(i, divider(i))
    end = datetime.datetime.now()
    return f"Время, затраченное на выполнение =  {end - start}"


def task8():
    N, M = map(int, input("Введите N и M: ").split())
    for b in range(N, M):
        for a in range(N, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                return a, b, int(c)


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
    return roster


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
    f = []
    while N < 5:
        i += 1
        if i == divider1(i):
            f.append(i)
            N += 1
    return f


def task11():
    mac = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start1 = time.time()
    res = mac[-1]
    print(res)
    end1 = time.time()
    start2 = time.time()
    print(next(reversed(mac)))
    end2 = time.time()
    start3 = time.time()
    print(mac.pop())
    end3 = time.time()
    print(f"1: {start1 - end3}, 2: {start2 - end2}, 3: {start3 - end3}")


def task12():
    mac = [1, 2, 3, 4, 5]
    return list(range(len(mac), -1, -1))


def task13():
    def sum_mac(m, l_m):
        if l_m != 0:
            return sum_mac(m, l_m - 1) + m[l_m - 1]
        else:
            return 0

    mac = [1, 2, 3, 4, 5]
    res = sum_mac(mac, len(mac))
    return res


print("Доступные задачи: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13")
num = int(input("Номер задачи: "))
if num == 3 or num == 2:
    print("Доступные подномера задачи: 1, 2")
    if num == 2:
        lst = [task2_1, task2_2]
    else:
        lst = [task3_1, task3_2]
    num = int(input("Выберете подномер: "))
    print(lst[num - 1]())
else:
    lst = [task1, None, None, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13]
    print(lst[num - 1]())
