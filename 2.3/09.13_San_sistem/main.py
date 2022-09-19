import math as m
from dataclasses import dataclass

import pygame as pg


@dataclass
class Planet:
    a = b = 500
    i = 0
    r: any
    V: any
    speed: any
    color: any

    def draw(self):
        angle = self.i * pi / self.speed
        l = 0.73 - m.acos((self.a - 700) / m.sqrt(500 ** 2 - 400 ** 2))
        int(l)
        a = (self.r * 60 * m.cos(angle + l)) + sun_1
        b = (self.r * 60 * m.sin(angle + l)) + sun_2
        self.i += 3
        pg.draw.circle(screen, self.color, (int(a), int(b)), self.V * 10)
        # for event in pg.event.get():
        #     if event.type == pg.MOUSEBUTTONDOWN:
        #         if event.button == 1:
        #             print(11)


class Color():
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GRAY = (125, 125, 125)
    LIGHT_BLUE = (100, 149, 237)
    SUN = (225, 225, 0)
    YELLOW = (255, 207, 72)
    LIGHT_YELLOW = (255, 207, 244)
    PALE_ORANGE = (46, 57, 99)
    TWEETER = (31, 174, 233)


class Planes:
    Mercury = Planet(0.5, 0.4, 120, Color.GRAY)
    Venus = Planet(0.8, 0.9, 140, Color.YELLOW)
    Earth = Planet(1.2, 1, 190, Color.GREEN)
    Mars = Planet(1.7, 0.7, 250, Color.RED)
    Jupiter = Planet(3, 2.5, 500, Color.PALE_ORANGE)
    Saturn = Planet(4, 1.8, 700, Color.LIGHT_YELLOW)
    Uranus = Planet(5, 1.4, 800, Color.TWEETER)
    Neptune = Planet(6, 1.3, 1000, Color.LIGHT_BLUE)


WIDTH = 1024
HEIGHT = 768
FPS = 30
sun_1 = WIDTH / 2
sun_2 = HEIGHT / 2
pi = m.pi

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("San sistem")
clock = pg.time.Clock()

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(Color.BLACK)
    pg.draw.circle(screen, Color.SUN, (sun_1, sun_2), 10)
    Planes.Mercury.draw()
    Planes.Venus.draw()
    Planes.Earth.draw()
    Planes.Mars.draw()
    Planes.Jupiter.draw()
    Planes.Saturn.draw()
    Planes.Uranus.draw()
    Planes.Neptune.draw()
    pg.display.update()

    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        pg.draw.circle(screen, Color.RED, pos, 5)
        pg.display.update()

pg.quit()
