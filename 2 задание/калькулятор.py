print ('Добрый день, перед вами калькулятор')
print ('Введите число-оператор-число через пробелы')
def xrxr(a,b,c):
    z=['+', '-', '*', '/']
    xr=0
    try:
        a = float(a)
        b = str(b)
        c = float(c)
    except ValueError:
        print('Введено не число')
    else: 
        if b=='+':
            xr=a+c
            return xr
        elif b=='-':
            xr=a-c
            return xr
        elif b=='*':
            xr=a*c
            return xr
        elif b=='/':
            try:
                xr=a/c
            except ZeroDivisionError:
                print("Не стоит делить на ноль")
                return "Error"
            return xr
        if b not in z:
            print('Введен не правильный оператор')
while True:
    a,b,c=input().split()
    print(xrxr(a,b,c))

