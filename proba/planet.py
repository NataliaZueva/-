from dataclasses import dataclass
from math import *

import pygame as pg


@dataclass
class Planet:
    x = y = 500
    i = 0
    __n: any
    __r: any
    __V: any
    __speed: any

    def draw(self):
        angle = self.i * pi / self.__speed
        initial_angle = int(0.73 - acos((self.x - 700) / sqrt(500 ** 2 - 400 ** 2)))
        x = int((self.__r * 100 * cos(angle + initial_angle)) + sun_1)
        y = int((self.__r * 70 * sin(angle + initial_angle)) + sun_2)
        self.i += 3
        image = pg.image.load(PLAN[self.__n-1])
        size = (self.__V*30, self.__V*30)
        image = pg.transform.scale(image, size)
        screen.blit(image, (x, y))


    def angle_return(self):
        return (self.i * 3.14 / self.__speed / 3.14 * 180) % 360


class Color:
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
    Mercury = Planet(1, 0.5, 0.4, 120)
    Venus = Planet(2, 0.8, 0.9, 140)
    Earth = Planet(3, 1.2, 1, 190)
    Mars = Planet(4, 1.7, 0.7, 250)
    Jupiter = Planet(5, 3, 2.1, 500)
    Saturn = Planet(6, 4, 2.4, 700)
    Uranus = Planet(7, 5, 1.6, 800)
    Neptune = Planet(8, 6, 1.3, 1000)


# WIDTH = 1024
# HEIGHT = 768
WIDTH = 1500
HEIGHT = 810
FPS = 30
sun_1 = WIDTH / 2
sun_2 = HEIGHT / 2

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
# screen = pg.display.set_mode((10, 10), pg.FULLSCREEN)
pg.display.set_caption("San sistem")
clock = pg.time.Clock()

touchRect = pg.Rect(450, 450, 100, 100)

touchRect1 = pg.Rect(50, 50, 100, 100)
touchRect2 = pg.Rect(50, 250, 100, 100)
touchRect3 = pg.Rect(50, 450, 100, 100)
touchRect4 = pg.Rect(50, 650, 100, 100)

touchRect5 = pg.Rect(1350, 50, 100, 100)
touchRect6 = pg.Rect(1350, 250, 100, 100)
touchRect7 = pg.Rect(1350, 450, 100, 100)
touchRect8 = pg.Rect(1350, 650, 100, 100)

f1 = pg.font.SysFont('serif', 36)
text1 = f1.render('Mercury', True, Color.WHITE)
text2 = f1.render('Venus', True, Color.WHITE)
text3 = f1.render('Earth', True, Color.WHITE)
text4 = f1.render('Mars', True, Color.WHITE)
text5 = f1.render('Jupiter', True, Color.WHITE)
text6 = f1.render('Saturn', True, Color.WHITE)
text7 = f1.render('Uranus', True, Color.WHITE)
text8 = f1.render('Neptune', True, Color.WHITE)
text22 = f1.render("Нажмите на любую планету", True, Color.WHITE)

# pg.draw.rect(screen, Color.YELLOW, (50, 50, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (50, 250, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (50, 450, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (50, 650, 100, 100))
#
# pg.draw.rect(screen, Color.YELLOW, (1350, 50, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (1350, 250, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (1350, 450, 100, 100))
# pg.draw.rect(screen, Color.YELLOW, (1350, 650, 100, 100))



bg = pg.image.load('fon.png').convert()


class Printed:
    def __init__(self):
        self.d = Planes.Mercury.angle_return()
        # self.d = 123

    def qwe(self, a):
        b = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        text22 = f1.render(f'{b[a-1]}: {self.d}', True, Color.WHITE)
        return text22


ball = pg.sprite.Group()
# ball.add(WIDTH//2, "1.png")

global PLAN
PLAN = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']

running = True
while running:
    clock.tick(FPS)
    s = (Planes.Jupiter.angle_return())
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            x, y = pg.mouse.get_pos()
            if touchRect1.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(1)
            elif touchRect2.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(2)
            elif touchRect3.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(3)
            elif touchRect4.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(4)

            elif touchRect5.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(5)
            elif touchRect6.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(6)
            elif touchRect7.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(7)
            elif touchRect8.collidepoint(x, y):
                te = Printed()
                text22 = te.qwe(8)

    # screen.fill(Color.BLACK)
    screen.blit(bg, (0, 0))

    for a in range(0, 1):
        pg.draw.circle(screen, Color.SUN, (sun_1, sun_2), 10)
        Planes.Mercury.draw()
        Planes.Venus.draw()
        Planes.Earth.draw()
        Planes.Mars.draw()

        Planes.Jupiter.draw()
        Planes.Saturn.draw()
        Planes.Uranus.draw()
        Planes.Neptune.draw()

        # pg.draw.rect(screen, Color.YELLOW, (50, 50, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (50, 250, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (50, 450, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (50, 650, 100, 100))
        #
        # pg.draw.rect(screen, Color.YELLOW, (1350, 50, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (1350, 250, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (1350, 450, 100, 100))
        # pg.draw.rect(screen, Color.YELLOW, (1350, 650, 100, 100))

        screen.blit(text1, (40, 150))
        screen.blit(text2, (50, 350))
        screen.blit(text3, (60, 550))
        screen.blit(text4, (60, 750))

        screen.blit(text5, (1350, 150))
        screen.blit(text6, (1350, 350))
        screen.blit(text7, (1350, 550))
        screen.blit(text8, (1340, 750))

        screen.blit(text22, (550, 650))

        q = 0
        for i in range(len(PLAN)):
            dog = pg.image.load(PLAN[i])
            if i < 4:
                screen.blit(dog, (40, q + 50))
                q += 200
            elif i == 4:
                q = 50
                screen.blit(dog, (1350, q))
            elif i > 4:
                q += 200
                screen.blit(dog, (1350, q))

        ball.draw(screen)
        # screen.blit(ppp, (50, 20))
        pg.display.update()

pg.quit()
