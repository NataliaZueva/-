import pygame as pg
import tkinter as tk
from pygame.locals import * 
import random

speed = 5
FPS = 60
color = (10,20,30)
black = (0,0,0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
speed2 = 5
quantity = 0
size=50
W=20
H=SCREEN_HEIGHT - size*3.5

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

def counter(x):
    f1 = pg.font.Font(None, 36)
    text1 = f1.render(x, True, (0, 100, 0))
    screen2 = text1.get_rect(center=(75, 20))
    screen.blit(text1, screen2)
           
def tkk():
    window = tk.Tk()
    greeting = tk.Label(text="Игра законченна", width=20,height=10)
    greeting = tk.Label(text=("Со счётом: " + str(quantity)), width=20,height=10)
    greeting.pack()
    window.mainloop()

class Live(pg.sprite.Sprite):
    def __init__(self, x, y, screen2):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(screen2).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        
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

manikin=Player(100, 100, "manikin.png")
enemy=Enemy(random.randint(0,SCREEN_HEIGHT),"enemy.png")

lives = pg.sprite.Group()
for i in range(3):
    H+=size
    lives.add(Live(H, W, 'live.png'),
             Live(H, W, 'live.png'))

enemys = pg.sprite.Group()
for i in range (3):
    H+=size
    lives.add(Enemy(random.randint(0,SCREEN_HEIGHT),"enemy.png"),
    Enemy(random.randint(0,SCREEN_HEIGHT),"enemy.png"))

    

running = True 
while running:
    
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT: 
            running = False

    cc="Ваш счет " + str(quantity)
    counter(cc)
    screen.blit(manikin.image, manikin.rect)
    screen.blit(enemy.image, enemy.rect)
    enemys.draw(screen)  
    lives.draw(screen)
    pg.display.flip()

    keys=pg.key.get_pressed()
    manikin.update(keys)
    screen.fill(color)
    enemy.update()
    enemys.update()




    keys=pg.key.get_pressed()
    manikin.update(keys)
    screen.fill(color)
    enemy.update()

    if pg.sprite.collide_rect(manikin,enemy):
        running=False
        tkk()
   
          
pg.quit() 
 
