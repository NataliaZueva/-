import time
from random import randint

# # задача 1
# a, b, c = input().split()
# startTime = time.time()
# a, b, c = b, c, a
# endTime = time.time()
# print(a, b, c)
# totalTime = endTime
# print("Время, затраченное на выполнение = ", totalTime)

# # задача 2.1
# flag = True
# while flag:
#     a, b = input("Введите 2 числа: ").split()
#     try:
#         a = int(a)
#         b = int(b)
#     except ValueError:
#         print('Введено не число')
#     else:
#         print(a + b)
#         flag = False


# задача 2.2

# # задача 3.1
# x = randint(0, 100)
# x1 = x ** 5
# print(x1)


# # задача 3.2
# x2 = 1
# for i in range(5):
#     x2 = x * x2
# print(x2)

# задача 4
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


