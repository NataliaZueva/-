import pygame as pg
import tkinter as tk
from pygame.locals import * 
import random

speed = 5
FPS = 60
black = (10,20,30) 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
speed2 = 5
quantity = 0
live1 = 3

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, SCREEN2):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(SCREEN2).convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))
    def update(self,keys):
        global speed
        #отслеживаем нажатие на кнопки
        if keys[K_LEFT] or keys[K_a]:
             self.rect.move_ip(-speed, 0)
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.move_ip(speed, 0)
        if keys[K_UP] or keys[K_w]:
            self.rect.move_ip(0,-speed)
        if keys[K_DOWN] or keys[K_s]:
            self.rect.move_ip(0, speed)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pg.sprite.Sprite):
    def __init__(self, y, SCREEN2):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(SCREEN2).convert_alpha()
        self.rect=self.image.get_rect(center=(650,y//2))
    def update(self):
        global speed2, quantity
        
        self.rect.move_ip(-speed2,0)
        if self.rect.right<0:
            quantity+=1
            if quantity>1 and quantity<5:
                speed2+=1
            self.rect=self.image.get_rect(center=(random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),random.randint(0,SCREEN_HEIGHT)))
def tkk():
    window = tk.Tk()
    greeting = tk.Label(text="Game over", width=20,height=10)
    greeting.pack()
    window.mainloop()
    
#class loss_of_life(pg.sprite.Sprite):
#    def __init__(self, x, y, SCREEN2):
#        pg.sprite.Sprite.__init__(self)
#        self.image=pg.image.load(SCREEN2).convert_alpha()
#        self.rect=self.image.get_rect(center=(x,y))
#    def update(self):
#        global live1
#        loss = 0
#        x = 20
#        while show != live1:
#            screen.blit(live, (x, y))
#            x += 60
#            loss +=1



    





pg.init()
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pg.display.set_caption("My Game") 
clock = pg.time.Clock()
screen.fill(black)

manikin=Player(100, 100, "manikin.png")
enemy=Enemy(random.randint(0,SCREEN_HEIGHT),"enemy.png")
#live1=loss_live(10, 10, "live.png")

running = True 
while running:
    
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT: 
            running = False



    screen.blit(manikin.image, manikin.rect)
    screen.blit(enemy.image,enemy.rect)

    pg.display.flip()

    keys=pg.key.get_pressed()
    manikin.update(keys)
    screen.fill(black)
    enemy.update()

    if pg.sprite.collide_rect(manikin,enemy):
        running=False
        tkk()
        
    
pg.quit() 
 
