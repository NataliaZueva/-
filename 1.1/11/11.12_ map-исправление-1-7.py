#Удвоить каждый элемент коллекции.
print('№1')
m=list(map(int, input('Введите коллекцию: ').split()))
b = list(map(lambda x: 2*x, m))
print(b)


#Есть две коллекции, нужно упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.
print('№7')
a=list(map(int, input('Введите коллекцию 1: ').split()))
b=list(map(int, input('Введите коллекцию 2: ').split()))
c = list(map(lambda x: 2*x, b))
d = zip(a, c)
print(list(d))

