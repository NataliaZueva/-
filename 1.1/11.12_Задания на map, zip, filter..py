#Удвоить каждый элемент коллекции.
print('№1')
m=list(map(int, input('Введите коллекцию: ').split()))
for i in range(len(m)):
    m[i]=m[i]*2
print(m)

#Найти произведение по-элементно элементов из трех коллекций.
def f(a=[1,2,3]):
    return a[0]*a[1]*a[2]
print('№2')
a=list(map(int, input('Введите коллекцию 1: ').split()))
b=list(map(int, input('Введите коллекцию 2: ').split()))
c=list(map(int, input('Введите коллекцию 3: ').split()))
v=list(zip(a,b,c))
d=list(map(f, v))
print(d)


# Найти длину каждого элемента из коллекции.
print('№3')
m=input('Введите коллекцию: ').split()
print(list(map(len, m)))


#Оставить только четные элементы коллекции.
print('№4')
print(list(filter(lambda x: int(x) % 2 == 0, a)))

# Оставить только непустые элементы коллекции.
print('№5')
lis = ['socks', '' , 'T-shirt', '', '', 'shorts', 'pullover', 'sweater', '', '']
print(list(filter(lambda x: x != '', lis)))


#Есть три коллекции, нужно упаковать элементы тройками.
print('№6')
print(list(zip(a,b,c)))


#Есть две коллекции, нужно упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.
print('№7')
for i in range(len(c)):
    c[i]=c[i]*2
print(list(zip(a,c)))




