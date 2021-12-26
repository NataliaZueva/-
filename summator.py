print("Работу выполнила Зуева Наталья, 14122\nПрограмма суммиирует числа пока сумма не будет равна 0\nBведите первое число")
summ=0
while True:
    while True:
        try:
            list1=list(map(float,input().split()))
            break
        except ValueError:
            print('Введены *не* числа')
    summ+=sum(list1)
    if summ!=0:
        print(summ)
    else:
        print('Сумма равна 0\nПрограмма завершена')
        break

