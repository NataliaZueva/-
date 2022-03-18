a = list(map(int, input('Введите числа: ').split()))
k=0
for i in range (len(a)):
    if (a[i] % 2)  == 0:
        k+=1
print(k)
