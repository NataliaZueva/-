import time

# задача 1
# a, b, c = input().split()
# startTime = time.time()
# a, b, c = b, c, a
# endTime = time.time()
# print(a, b, c)
# totalTime = endTime
# print("Время, затраченное на выполнение = ", totalTime)

# задача 2
flag = True
while flag:
    a, b = input("Введите 2 числа: ").split()
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('Введено не число')
    else:
        print(a + b)
        flag = False
