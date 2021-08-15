# Initializing variables
import pygame
from random import randint
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255 , 0, 0)
green = (0 , 255, 0)
height = 800
width = 800
blue = (0, 110, 255)
X_cat = (randint(1,5)*82)+108
Y_cat = (randint(1,5)*82)+108
X_m = (randint(1,5)*82)+108
Y_m = (randint(1, 5) * 82) + 108
grey = (190, 190, 190)
display_surface = pygame.display.set_mode((height, width))
pygame.display.set_caption('mouse and cat')
def Draw_m():
    pygame.draw.rect(display_surface, grey, [X_m, Y_m, 80, 80])
def delay():
    pygame.time.delay(100)
def background():
    display_surface.fill(black)
    pygame.draw.rect(display_surface, white, [100, 100, 605, 605])
    x = 107
    y = 107
    i = 0

    display_surface.fill(black)
    pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
    for i in range(7):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        y += 82
    x = 600
    y = 107
    for i in range(7):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        y += 82
    x = 190
    y = 107
    for i in range(5):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        x += 82
    x = 190
    y = 600
    for i in range(5):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        x += 82
    x = 190
    y = 190
    for i in range(5):

        for j in range(5):
            pygame.draw.rect(display_surface, white , [x, y, 80, 80])
            x += 82
        x = 190
        y += 82
def end():
    pygame.draw.rect(display_surface,(0,255,0),[600,353,80,80])
background()
pygame.draw.rect(display_surface, red, [X_cat, Y_cat, 80, 80])
end()
for k in range(20):
    RM = randint(1, 4)
    if (X_m < 200 or X_m > 520) or (Y_m < 200 or Y_m > 520):
        delay()
        break
    if X_m == X_cat and Y_m == Y_cat:
        delay()
        break
    if (X_m < 680 or X_m > 520) and (Y_m < 400 or Y_m > 520):
        delay()
        break

    if RM == 1:
        X_m += 82
        Draw_m()

    elif RM == 2:
        X_m -= 82
        Draw_m()

    elif RM == 3:
        Y_m += 82
        Draw_m()

    elif RM == 4:
        Y_m -= 82
        Draw_m()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()