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