from random import randrange

import pygame as pg

pg.init()
WIDTH = 800
HEIGHT = 700
SIZE = 30

res = (WIDTH, HEIGHT)
screen = pg.display.set_mode(res)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR = (255, 44, 56)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()

button_button = pg.mixer.Sound("sounds/button.mp3")
button_loss = pg.mixer.Sound("sounds/loss.mp3")
button_food = pg.mixer.Sound("sounds/food.mp3")

smallfont = pg.font.SysFont('Corbel', 35)
text1 = smallfont.render('Quit', True, WHITE)
text2 = smallfont.render('Start', True, WHITE)


class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


x, y = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
apple = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
FPS = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10

pg.init()
surface = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 26, bold=True)
font_end = pg.font.SysFont('Arial', 66, bold=True)
img = pg.image.load('11.png').convert()

pg.mixer.music.load("sounds/fon.mp3")
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()
vol = 1.0

flPause = False


def close_game():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()


start_bt = False
running = True
while running:
    clock.tick(FPS)
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
        if ev.type == pg.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                button_button.play()
                button_loss.play()
                pg.quit()
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 - 55 <= mouse[1] <= height / 2 - 15:
                button_button.play()
                start_bt = True
                running = False
    BackGround = Background('11.png', [0, 0])

    screen.blit(BackGround.image, BackGround.rect)

    mouse = pg.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pg.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    else:
        pg.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 - 55 <= mouse[1] <= height / 2 - 15:
        pg.draw.rect(screen, color_light, [width / 2, height / 2 - 55, 140, 40])
    else:
        pg.draw.rect(screen, color_dark, [width / 2, height / 2 - 55, 140, 40])

    screen.blit(text1, (width / 2 + 40, height / 2 + 5))
    screen.blit(text2, (width / 2 + 40, height / 2 - 55))

    pg.display.update()

pg.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
while start_bt:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPause = not flPause
            if flPause:
                pg.mixer.music.pause()
            else:
                pg.mixer.music.unpause()
    surface.blit(img, (0, 0))

    # drawing snake, apple
    [pg.draw.rect(surface, pg.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pg.draw.rect(surface, pg.Color('red'), (*apple, SIZE, SIZE))

    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pg.Color('orange'))
    surface.blit(render_score, (5, 5))

    # snake movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    # eating food
    if snake[-1] == apple:
        button_food.play()
        apple = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # game over
    if x < 0 or x > WIDTH or y < 0 or y > HEIGHT or len(snake) != len(set(snake)):
        button_loss.play()
        while True:
            render_end = font_end.render('GAME OVER', 1, pg.Color('orange'))
            surface.blit(render_end, (WIDTH // 2 - 200, HEIGHT // 3))
            pg.display.flip()
            close_game()

    pg.display.flip()

    # controls
    key = pg.key.get_pressed()
    if key[pg.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pg.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pg.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pg.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
