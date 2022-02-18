print ('Добрый день, перед вами калькулятор')
print ('Введите число-оператор-число через пробелы')
while True:
    a,b,c=input().split()
    z=['+', '-', '*', '/']
    def xrxr(a,b,c):
        xr=0
        try:
            a = int(a)
            b = str(b)
            c = int(c)
            
        except ValueError:
            print('Введено не число')
        else: 
            if b=='+':
                xr=a+c
                print(xr)
                return xr
            elif b=='-':
                xr=a-c
                print(xr)
                return xr
            elif b=='*':
                xr=a*c
                print(xr)
                return xr
            elif b=='/':
                try:
                    xr=a/c
                    print(xr)
                except ZeroDivisionError:
                    print("Не стоит делить на ноль")
                    return "Error"
                return xr
            if b not in z:
                print('Введен не правильный оператор')
        print(xrxr(a,b,c))
        


