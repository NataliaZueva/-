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

    def __init__(self, name="Anon", eat_timeout=5, play_timeout=5):
        self.__flag = True
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__play_timeout = play_timeout
        self.__st = dt.now()
        self.__st_b = dt.now()
        self.__state = State.Normal
        self.__behaviour = Behaviour.Calmness

    def __str__(self):
        return str(f"Name: {self.__name}, Status:  {self.__state} (0 to 6), Behaviour:  {self.__behaviour} (0 to 3)")

    def eat(self, amount=0):
        """Покормить"""
        if self.__state != State.Dead:
            self.__state += amount
            self.__st = dt.now()
        if self.__state <= 0:
            self.__state = State.Dead
        if self.__state >= 6:
            self.__state = State.Cheerful

    def play(self):
        """Поиграть"""
        if self.__state != State.Dead:
            self.__behaviour += 1
            self.__st_b = dt.now()
        if self.__behaviour <= 0:
            self.__behaviour = Behaviour.Calmness
        if self.__behaviour >= 3:
            self.__behaviour = Behaviour.Fatigue

    def death_check(self):
        """Проверка на смерть"""
        if self.__state == State.Dead:
            self.__del__()
            return 123
        else:
            st_now = (dt.now() - self.__st).seconds
            if st_now // self.__eat_timeout > 0:
                print(st_now // self.__eat_timeout)
                self.__state -= 1
                print('Ваше состояние ухудшелость на 1 (еда)')
            st_now_b = (dt.now() - self.__st_b).seconds
            if st_now_b // self.__play_timeout > 0:
                print(st_now_b // self.__play_timeout)
                self.__behaviour -= 1
                print('Ваше состояние ухудшелость на 1 (игра)')

    def __del__(self):
        """Смерть"""
        print(f'Ваш зверек - {self.__name} умер, очень жаль...')

    @property
    def feeding(self):
        return self.__state

    @feeding.setter
    def feeding(self, state):
        self.__state = state


def menu():
    print('Что бы покормить зверька введите "eat" + "кол-во еды" - (иначе кормежка = 0)')
    print('Для игры с зверьком введите "play"')
    print('Чтобы узнать состояния зверька введите "1"')
    print('')


running = True
end = 'Приятно было поиграть'
num = input('Начать: 1, закрыть: 0 \n  ')
if num == '0':
    print(end)
elif num == '1':
    animal = LittleAnimal(input('Введите имя зверька: '))
    menu()
    track = '10 10'
    while running:
        animal.death_check()
        if animal.death_check() == 123:
            running = False
        if track == '0':
            print(end)
            running = False
        if track == '1':
            print(animal.__str__())
        if track.split()[0] == 'eat':
            animal.eat(int(a.split()[1]))
        if track == 'play':
            animal.play()
        if running:
            track = input('#: ')
print(end)
