def sort_two(a,b):
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c
def sort(s):
    if len(s)<2:
        return s
    else:
        middle=len(s)//2
        left=sort(s[:middle])
        right=sort(s[middle:])
        return sort_two(left,right)


from random import randint
print("Зуева Наталья 14122\nПрограмма разбивает массив на несколько подмассивов меньшего размера. Затем эти массивы сортируются с помощью рекурсивного вызова. После они комбинируются, и получается сортированный файл\nПрограмма выполнена методом сортировки слияением\n")
print("Cоздание файла с рандомными числами")
try:
   n=input("Bведите имя файла: ")
except ValueError:
    print("Вы сделали что-то не так")  
else:
    my = '{}.txt' .format(n)
    try:
        z=input("Какое количетсво чисел вы хотите (до 300)? ")
    except NameError:
         print("Вы сделали что-то не так")
    else:
        try:
            z=int(z)
            x,y=input("От какого до какого значения вы хотите рандомные числа (введите числа через пробел)? ").split()
        except ValueError:
             print("Вы сделали что-то не так")
        else:
            x=int(x)
            y=int(y)
            my_file = open(my, "w+")
            for i in range(z):
                p=str(randint(x,y))
                my_file.write(p)
                my_file.write("\n")

            my_file=open(my)
            my_file=my_file.readlines()
            




            massive=[]
            for line in my_file:
                massive.append(int(line))
            result=sort(massive)

            n=input("Bведите имя конечного файла: ")
            me = '{}.txt' .format(n)
try:
    file=open(me)
except FileNotFoundError:
    file=open(me,"w")
    for num in result:
        file.write(str(num))
        file.write("\n")
    file.close()
else:
    while True:
        off=input("\nФайл с результатами уже существует. Заменить? 1) Да\n 2)Нет\no ")
        off=int(off)
        if off==1:
            file=open(me,"w+")
            for num in result:
                file.write(str(num))
                file.write("\n")
            print("Успешно!")
            break
        elif off==2:
            print("Перезапустите программу")
            break
    file.close()















def sort_two(a,b):
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c
    
def sort(s):
    
    if len(s)<2:
        return s
    else:
        middle=len(s)//2
        left=sort(s[:middle])
        right=sort(s[middle:])
        return sort_two(left,right)


from random import randint
#print("Вывод случайного целого числа ", randint(0, 9))
#print(type(randint))
#print(*sort([7,5,2, 3,9, 8,6]), sep="\n")
print("Зуева Наталья 14122\nПрограмма разбивает массив на несколько подмассивов меньшего размера. Затем эти массивы сортируются с помощью рекурсивного вызова. После они комбинируются, и получается сортированный файл\nПрограмма выполнена методом сортировки слияением\n")
print("Cоздание файла с рандомными числами")
n=input("Bведите имя файла: ")
my = '{}.txt' .format(n)
z=input("Какое количетсво чисел вы хотите (до 300)? ")
z=int(z)
x,y=input("От какого до какого значения вы хотите рандомные числа (введите числа через пробел)? ").split()
x=int(x)
y=int(y)
my_file = open(my, "w+")
for i in range(z):
    p=str(randint(x,y))
    my_file.write(p)
    my_file.write("\n")

my_file=open(my)
my_file=my_file.readlines()
massive=[]
for line in my_file:
    massive.append(int(line))
result=sort(massive)



massive=[]
for line in my_file:
    massive.append(int(line))
result=sort(massive)

n=input("Bведите имя конечного файла: ")
me = '{}.txt' .format(n)
try:
    file=open(me)
except FileNotFoundError:
    file=open(me,"w")
    for num in result:
        file.write(str(num))
        file.write("\n")
    file.close()
else:
    while True:
        off=input("\nФайл с результатами уже существует. Заменить? 1) Да\n 2)Нет\no ")
        off=int(off)
        if off==1:
            file=open(me,"w+")
            for num in result:
                file.write(str(num))
                file.write("\n")
            print("Успешно!")
            break
        elif off==2:
            print("Перезапустите программу")
            break
    file.close()


#file=open(me,"w+")
#for num in result:
#    file.write(str(num))




 
