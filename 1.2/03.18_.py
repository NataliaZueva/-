a, k = list(map(int, input('Введите числа: ').split())), 0
for i in range (len(a)):
    if (a[i] % 2)  == 0:
        k+=1
print(k)

print(len(list(filter(lambda x: (x % 2 == 0), list(map(int,input().split()))))))


