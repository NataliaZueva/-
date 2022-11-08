import time
# задача 1
a, b, c = input().split()
startTime = time.time()
a, b, c = b, c, a
endTime = time.time()
print(a, b, c)
totalTime = endTime
print("Время, затраченное на выполнение = ", totalTime)