from datetime import datetime as dt


class State:
    Angry = 1
    Sad = 2
    Normal = 3
    Kind = 4
    Happy = 5
    Cheerful = 6
    Dead = 0


class Behaviour:
    Calmness = 0
    Satisfaction = 1
    Joy = 2
    Fatigue = 3


class LittleAnimal:
    def __init__(self, name="Anon", eat_timeout=10):
        self.__flag = True
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__st = dt.now()
        self.__state = State.Normal
        self.__behaviour = Behaviour.Calmness

    def __str__(self):
        print(str(f"Name: {self.__name}, Status:  {self.__state} (0 to 6), Behaviour:  {self.__behaviour} (0 to 3)"))

    def eat(self, amount=0):
        """Покормить"""
        st.now = (dt.now() - self.__st).seconds()
        if st.now / self.__eat_timeout > amount:
            self.__state == State.Dead
            self.__flag = False
            print("Dead")

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self):
        self.__state = state

    # def eat(self, amount=0):
    #     """Покормить"""
    #     st.now = (dt.now() - self.__st).seconds()
    #     if (dt.now() - st.now) / self.__eat_timeout > amount:
    #         self.__state = State.
    #         return
    #     if st.now > 20:
    #         if amount - 2 < 0:
    #             self.__state = State.Angry
    #             st = dt.now()
    #         else:
    #             self.__state = State.Normal
    #             st = dt.now()
    #         return
    #
    #     if amount == 1:
    #         self.__state = State.Angry
    #     elif amount == 2:
    #         self.__state = State.Sad
    #     elif amount == 3:
    #         self.__state = State.Normal
    #     elif amount == 4:
    #         self.__state = State.Kind
    #     elif amount == 5:
    #         self.__state = State.Happy
    #     elif amount == 6:
    #         self.__state = State.Cheerful
    #     elif amount == 0:
    #         self.__state = State.Dead
    #
    #
    #
    #
    #
    # def state(self):
    #     if (dt.now() - st).seconds() > 30:
    #         self.__state = Xrxr.states["Dead"]
    #     return self.__state

    # @property
    # def state(self):
    #     return self.__state
    #
    # @state.setter
    # def state(self):
    #     self.__state = state


a = LittleAnimal()
# if (v := int(input("Если хотите узнать о животном 1, покормить 2\n   "))) == 1:
#     a.__str__()
# else:
#     a.eat()

print( (dt.now() - 1).seconds())
