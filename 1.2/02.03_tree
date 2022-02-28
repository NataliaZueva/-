import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Game") 
def eee(x,y,z):
    font = pygame.font.Font(None, 40)
    text = font.render("Нажми на меня", True, [z,y,x], 3)
    textpos = (150, 60)
    screen.blit(text, textpos)
    pygame.draw.polygon(screen, (x,y,z),[(140, 420),
                                           (170,360), (160, 360),
                                           (200,280), (190,280),
                                           (220,220), (210,220),
                                           (235,180), (225,180),
                                           (250, 150),
                                           (275,180), (265,180),
                                           (290,220), (280,220),
                                           (310,280), (300,280), 
                                           (340,360), (330,360), 
                                           (360, 420)])
import random
FPS=100
running = True

pygame.draw.rect(screen,(139, 69, 19), [240, 420, 20, 50])
eee(0, 128, 0)
pygame.display.update()
while running:
    rn1 = random.randint(0,255)
    rn2 = random.randint(0,255)
    rn3 = random.randint(0,255)
    #print(rn1, rn2, rn3)
    pygame.time.delay(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    keys = pygame.key.get_pressed() #Список всех кнопок
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            eee(rn1, rn2, rn3)
            pygame.display.update()
pygame.quit() 
 
