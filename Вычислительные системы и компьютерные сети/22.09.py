def mask(a):
    s = [0, 128, 192, 224, 240, 248, 252, 254]
    try:
        a = int(a)
    except ValueError:
        print('Введено не число')
    else:
        if a > 32:
            print("Число не входит в область значений")
        elif a // 8 == 0:
            print(f"{s[a % 8]}.0.0.0")
        elif a // 8 == 1:
            print(f"255.{s[a % 8]}.0.0")
        elif a // 8 == 2:
            print(f"255.255.{s[a % 8]}.0")
        elif a // 8 == 3:
            print(f"255.255.255.{s[a % 8]}")
        elif a == 32:
            print(f"255.255.255.255")


print('Добрый день, перед вами "Вычисление маски подсети" \nВведите число от 0 до 32 \nОстановка программы "stop"')


while True:
    a = input("Ваше число: ")
    if a == "stop":
        print("Программа завершена")
        break
    mask(a)
