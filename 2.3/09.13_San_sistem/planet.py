from dataclasses import dataclass
from math import *

import pygame as pg


@dataclass
class Planet:
    x = y = 500
    boost = 200
    i = 0
    __n: any
    __r: any
    __V: any
    __speed: any

    def draw(self):
        angle = self.i * pi / (self.__speed * self.boost)
        # initial_angle = int(0.73 - acos((self.x - 700) / sqrt(500 ** 2 - 400 ** 2)))
        self.x = int((self.__r * 100 * cos(angle)) + sun_1)
        self.y = int((self.__r * 70 * sin(angle)) + sun_2)
        self.i += 3
        image = pg.image.load(PLAN[self.__n - 1])
        size = (self.__V * 30, self.__V * 30)
        image = pg.transform.scale(image, size)
        screen.blit(image, (self.x, self.y))

    def angle_return(self):
        return round((self.i * 3.14 / (self.__speed * 200) / 3.14 * 180) % 360, 2)


def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([x for x in line.split()])
    return a


WIDTH = 1500
HEIGHT = 810
FPS = 30
sun_1 = WIDTH / 2
sun_2 = HEIGHT / 2

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("San sistem")
clock = pg.time.Clock()

bg = pg.image.load('fon.png').convert()

# Планеты - размер, отдаленность.....

pla = file_read('Planes.txt')
kk = []
for i in pla:
    kk.append(Planet(int(i[1]), float(i[2]), float(i[3]), float(i[4])))

# Отрисовка надписей
f1 = pg.font.SysFont('serif', 36)
tx = file_read("Planes1.txt")
txt = []
pos = []
for i in tx:
    txt.append(f1.render(i[0], True, (255, 255, 255)))
    pos.append((int(i[5]), int(i[6])))
global text22
text22 = f1.render("Нажмите на любую планету", True, (255, 255, 255))

# Точка нажатия на экран
touchR = file_read("title.txt")
touchRect = []
for i in touchR:
    touchRect.append(pg.Rect(int(i[0]), int(i[1]), int(i[2]), int(i[3])))


class Printed:
    def __init__(self):
        self.d = kk[2].angle_return()

    def qwe(self, a):
        text22 = f1.render(f'{pla[a][0]}: {self.d}', True, (255, 255, 255))
        return text22


global PLAN
PLAN = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            x, y = pg.mouse.get_pos()
            for i in range(0, 8):
                if touchRect[i].collidepoint(x, y):
                    te = Printed()
                    text22 = te.qwe(i)

    screen.blit(bg, (0, 0))

    for a in range(0, 1):
        pg.draw.circle(screen, (225, 225, 0), (sun_1, sun_2), 10)
        for i in range(len(pla)):
            kk[i].draw()

    for i in range(len(txt)):
        screen.blit(txt[i], pos[i])

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

    pg.display.update()

pg.quit()
