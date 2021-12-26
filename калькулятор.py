print ('Добрый день, перед вами калькулятор')
print ('Введите число-оператор-число через пробелы')
while True:
    try:
        a,b,c=input().split()
    except ValueError:
        print('Вы ничего не ввели')
    else: 
        z=['+', '-', '*', '/']
        def xrxr(a,b,c):
            try:
                a = float(a)
                b = str(b)
                c = float(c)
            except ValueError:
                print('Введено не число')
            else: 
                if b=='+':
                    print(a+c)
                elif b=='-':
                    print(a-c)
                elif b=='/':
                    try:
                        print(a/c)
                    except ZeroDivisionError:
                        print("Не стоит делить на ноль")
                        return "Error"
                elif b=='*':
                    print(a*c)
                if b not in z:
                    print('Введен не правильный оператор')  
        xrxr(a,b,c)
