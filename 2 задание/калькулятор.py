print ('Добрый день, перед вами калькулятор')
print ('Введите число-оператор-число через пробелы')
while True:
    a,b,c=input().split()
    z=['+', '-', '*', '/']
    def xrxr(a,b,c):
        try:
            a = int(a)
            c = int(c)
        except ValueError:
            print('Введено не число')
        else: 
            if b=='+':
                print(a+c)
            elif b=='-':
                print(a-c)
            elif b=='/':
                print(a/c)
            elif b=='*':
                print(a*c)
            if b not in z:
                print('Введен не правильный оператор')
    xrxr(a,b,c)
