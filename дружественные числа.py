print('Зуева Наталья, группа 14122')
print('Программа находящаяя все дружественными числа в интервале от 1 до 10000')
for a in range(1,10000):
    s=0
    for i in range(1,a//2+1):
        if a%i==0:
            s+=i
    s1=0
    for b in range(1,s//2+1):
        if s%b==0:
            s1+=b
    if (s1==a) and (s!=a):
        print('Числа',a, 'и', s,'являются дружественными')


