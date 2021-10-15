print('Введите число и СС')
a,b=input().split()
def Perevod(a,b):
    s=0
    st=''
    x=['A', 'B', 'C', 'D', 'E', 'F']
    try:
        a=int(a)
        b=int(b)
    except:
            print('Введено не число')
    else:        
        while a>0:
            s=a%b
            if s>=10:
               s=x[s-10]
            else:
                s=str(s)
            st+=s
            a=a//b
    st[::-1]
    return st
print(Perevod(a,b))

