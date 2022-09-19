import math as m

import pygame as pg
# from planet import Planet


class Planet:
    def __init__(self, r, V, color):
        self.__r = r * 40
        self.__V = V * 10
        self.__color = color

    def draw(self, a):
        # pg.display.update()
        Fi = a * pi / 180 + a
        X = (self.__r * m.cos(Fi)) + sun_1
        Y = (self.__r * m.sin(Fi)) + sun_2
        # X = (self.__r * m.cos(Fi)) + WIDTH / 2 - self.__r
        # Y = (self.__r * m.sin(Fi)) + HEIGHT / 2 - self.__r
        pg.draw.circle(screen, self.__color, (X, Y), self.__V)
        # pg.display.update()
    # pg.draw.circle(screen, BLUE, (sun_1 + self.__r, sun_2 + self.__r), 10)


class Color():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (66, 170, 255)
    GRAY = (125, 125, 125)
    LIGHT_BLUE = (100, 149, 237)
    SUN = (225, 225, 0)
    YELLOW = (255, 207, 72)
    LIGHT_YELLOW = (255, 207, 244)
    PALE_ORANGE = (46, 57, 99)
    PINK = (230, 50, 230)
    TWEETER = (31, 174, 233)


class Planes:
    Mercury = Planet(0.3, 1, Color.GRAY)
    Venus = Planet(0.7, 1, Color.YELLOW)
    Earth = Planet(1, 1, Color.GREEN)
    Mars = Planet(1.5, 1, Color.RED)
    Jupiter = Planet(3, 1, Color.PALE_ORANGE)
    Saturn = Planet(5, 1, Color.LIGHT_YELLOW)
    Uranus = Planet(7, 1, Color.TWEETER)
    Neptune = Planet(10, 1, Color.LIGHT_BLUE)


WIDTH = 1024
HEIGHT = 768
FPS = 30
sun_1 = WIDTH / 2
sun_2 = HEIGHT / 2

# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("San sistem")
clock = pg.time.Clock()

pi = m.pi

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(Color.WHITE)
    pg.draw.circle(screen, Color.SUN, (sun_1, sun_2), 10)

    for a in range(0, 360):
        screen.fill(Color.WHITE)
        pg.draw.circle(screen, Color.SUN, (sun_1, sun_2), 10)
        Planes.Mercury.draw(a)
        Planes.Venus.draw(a)
        Planes.Earth.draw(a)
        Planes.Mars.draw(a)
        Planes.Jupiter.draw(a)
        Planes.Saturn.draw(a)
        Planes.Uranus.draw(a)
        Planes.Neptune.draw(a)
        pg.display.update()

    # for a in range(0, 360):
    #     screen.fill(WHITE)
    #     pg.draw.circle(screen, YELLOW, (sun_1, sun_2), 10)
    #     pg.display.update()
    #     Fi = a * pi / 180
    #     X = (50 * m.cos(Fi)) + sun_1
    #     Y = (50 * m.sin(Fi)) + sun_2
    #     pg.draw.circle(screen, GREEN, (X, Y), 10)
    #     pg.display.update()

pg.quit()
