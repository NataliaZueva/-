# import pygame as pg
#
#
# class Planet:
#     def __init__(self, r, V, color):
#         self.__r = r * 40
#         self.__V = V * 10
#         self.__color = color
#
#     def draw(self):
#         for a in range(0, 1):
#             # pg.display.update()
#             Fi = a * pi / 180
#             # X = (self.__r * m.cos(Fi)) + WIDTH / 2 - self.__r
#             # Y = (self.__r * m.sin(Fi)) + HEIGHT / 2 - self.__r
#             X = (self.__r * m.cos(Fi)) + WIDTH / 2 - self.__r
#             Y = (self.__r * m.sin(Fi)) + HEIGHT / 2 - self.__r
#             pg.draw.circle(screen, self.__color, (X, Y), self.__V)
#             # pg.display.update()
#         # pg.draw.circle(screen, BLUE, (sun_1 + self.__r, sun_2 + self.__r), 10)




# class Planes:
#     Mercury = Planet(0.387, 0.055, Color.GRAY)
#     Venus = Planet(0.72, 0.857, Color.YELLOW)
#     Earth = Planet(1.00, 1, Color.GREEN)
#     Mars = Planet(1.52, 0.5, Color.RED)
#     Jupiter = Planet(5.20, 1321, Color.PALE_ORANGE)
#     Saturn = Planet(9.55, 764, Color.LIGHT_YELLOW)
#     Uranus = Planet(19.19, 63, Color.TWEETER)
#     Neptune = Planet(30.10, 57.7, Color.LIGHT_BLUE)


# class Planet:
#     def __init__(self, r, V):
#         self.__r = r
#         self.__V = V
#
#     def draw_circle(self):
#         pg.draw.circle(screen, YELLOW, (sun_1, sun_2), 10)


# 1. Меркурий 0.387  0.055
# 2. Венера   0.72   0.857
# 3. Земля    1.00   1
# 4. Марс     1.52   0.5
# 5. Юпитер   5.20   1321
# 6. Сатурн   9.55   764
# 7. Уран     19.19  63
# 8. Нептун   30.10  57.7

# Mercury = Planet(0.387, 0.055)
# Venus = Planet(0.72, 0.857)
# Earth = Planet(1.00, 1)
# Mars = Planet(1.52, 0.5)
# Jupiter = Planet(5.20, 1321)
# Saturn = Planet(9.55, 764)
# Uranus = Planet(19.19, 63)
# Neptune = Planet(30.10, 57.7)

import pygame
from pygame.locals import (K_UP,
                           K_DOWN,
                           K_LEFT,
                           K_RIGHT,
                           K_ESCAPE,
                           KEYDOWN,
                           QUIT, )


def coloring(col, iteration):
    import random
    seting = random.randint(1, 2)
    colLi = list(col)
    if iteration:
        colLi[1] = colLi[1] - colLi[1] * random.randint(5, 9) / 50
    elif not iteration:

        colLi = [240, 58, 64]
        colLi[0] = colLi[0] - colLi[0] * random.randint(5, 9) / 50
        if seting == 2:
            colLi = [222, 252, 48]
            colLi[1] = colLi[1] - colLi[1] * random.randint(1, 7) / 50

    print(colLi)
    return list(map(int, colLi))


def paint_tree(iteration):
    color = [0, 250, 0]
    pygame.draw.circle(screen, coloring(color, iteration), (371, 235), 45)
    pygame.draw.circle(screen, coloring(color, iteration), (347, 164), 25)
    pygame.draw.circle(screen, coloring(color, iteration), (304, 251), 39)
    pygame.draw.circle(screen, coloring(color, iteration), (309, 303), 39)
    pygame.draw.circle(screen, coloring(color, iteration), (368, 311), 14)
    pygame.draw.circle(screen, coloring(color, iteration), (312, 99), 24)
    pygame.draw.circle(screen, coloring(color, iteration), (255, 142), 35)
    pygame.draw.circle(screen, coloring(color, iteration), (192, 160), 70)
    pygame.draw.circle(screen, coloring(color, iteration), (221, 231), 39)
    pygame.draw.circle(screen, coloring(color, iteration), (178, 267), 34)
    pygame.draw.line(screen, (107, 45, 15), (263, 459), (263, 270), 4)
    pygame.draw.line(screen, (107, 45, 15), (263, 270), (282, 253), 5)
    pygame.draw.line(screen, (107, 45, 15), (263, 270), (266, 181), 4)
    pygame.draw.line(screen, (107, 45, 15), (267, 237), (244, 218), 5)
    pygame.display.flip()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

screen.fill((0, 150, 189))

iteration = True
paint_tree(iteration)

TreeRect = pygame.Rect(119, 64, 300, 406)

running = True
while running:
    print(pygame.mouse.get_pos())
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if TreeRect.collidepoint(x, y):
                paint_tree(iteration)
    # if not iteration:
    # screen.fill((179, 25, 97))
    # if iteration:
    # screen.fill((0, 150, 189))
    iteration = not iteration

pygame.quit()