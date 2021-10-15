def Perevod():
    print('Введите число и СС')
    a,b=map(int,input().split())
    s=0
    st=''
    x=['A', 'B', 'C', 'D', 'E', 'F']
    while a>0:
        s=a%b
        if s>=10:
           s=x[s-10]
        else:
            s=str(s)
        st+=s
        a=a//b
    #print(st[::-1])
    return st
hr=Perevod()
print(hr)


try:
    a = int(a)
    c = int(c)
    b = str(b)
except:
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


#except SyntaxError:
#    print('Второй знак должен быть одним из операторов: +, -, *, /.')
