<<<<<<< HEAD
from random import randint


class Player:
    hp = 100
    damage = 10


# Записываем в переменную, чтобы было удобно.
p = Player()


class Enemy:
    # Рандомно получает хп врага от 70 до 130, рандомно получает дамаг врага от 6 до 13.
    hp = randint(70, 130)
    damage = randint(6, 13)


# Записываем в переменную, чтобы было удобно.
e = Enemy()


def menu(p):
    while True:
        print("1) Сражаться")
        print("2) Посмотреть статистику")
        # try и except просто фиксят ошибки. Не обращайте внимания.
        try:
            n = input("Введите число: ")
            if n == '1':
                menu_fight(p)
            if n == '2':
                menu_stats(p)
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")


def menu_stats(p):
    print("Статистика игрока")
    print("*****************")
    # Попробую обьяснить, что значит %s. Она по последовательности списка вписывает в %s переменную.
    print("hp %s." % (p.hp))
    print(f"Вы hp: {p.hp} damage: {p.damage}")
    print("damage %s." % (p.damage))
    input("Нажмите Enter для продолжения.")


def menu_fight(p):
    while e.hp > 0:
        # Также, как я и сказал по последовательности списка расставляет переменные.
        print("Вы hp: %s damage: %s" % (p.hp, p.damage))
        print("Враг hp: %s damage: %s" % (e.hp, e.damage))
        print("**********************")
        print("1)Ударить")
        print("2)Хил 0-5")
        n = input("Введите число: ")
        if n == '1':
            # Здоровье врага отнимает от вашего дамага.
            e.hp -= p.damage
            print("Вы ударили противника, у него осталось %s hp" % (e.hp))
            # Здоровье игрока отнимает от дамага врага.
            p.hp -= e.damage
            print("Противник ударил вас, у вас осталось %s hp" % (p.hp))

            print("*********************")

        if n == '2':
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0, 5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            print("Ваши хп %s" % (p.hp))

        else:
            print("Чего ждем?")
        if p.hp < 0:
            print("Вы проиграли")
        if e.hp < 0:
            print("Вы победили")

        print("******************")


# Вызов меню.
menu(p)
=======
# class State:
#     Angry = 1
#     Sad = 2
#     Normal = 3
#     Kind = 4
#     Happy = 5
#     Cheerful = 6
#     Dead = 0
#
#
# class LittleAnimal:
#
#     def __init__(self):
#         self.__st = None
#         self.__state = State.Normal
#
#     def eat(self, amount=0):
#         """Покормить"""
#         if self.__state != State.Dead:
#             self.__state += amount
#             self.__st = dt.now()
#         if self.__state <= 0:
#             self.__state = State.Dead
#         if self.__state >= 6:
#             self.__state = State.Cheerful
#
#     def death_check(self):
#         """Проверка на смерть"""
#         if self.__state == State.Dead:
#             self.death()
#         elif:
#             st.now = (dt.now() - self.__st).seconds()
#             if (dt.now() - st.now) / self.__eat_timeout > amount:
#
#
# def death(self):
#     """Смерть"""
#
#
# @property
# def feeding(self):
#     return self.__state
#
#
# @feeding.setter
# def feeding(self, state):
#     self.__state = state
#
#
# a = LittleAnimal()
# a.eat(-5)
# print(a.feeding)
#
#

# from datetime import datetime as dt
#
#
# current_date_time = dt.now()
#
# flag = True
# while flag:
#     print((dt.now() - current_date_time).seconds)
#     if int((dt.now() - current_date_time).seconds) >= 5:
#         flag = False


a = 'eat 1'

print(a.split()[1])
>>>>>>> parent of 2c78281 (Исправление зверушки)
