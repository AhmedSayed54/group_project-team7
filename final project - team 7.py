import pygame
from random import randint
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255 , 0, 0)
height = 800
width = 800
blue = (0, 110, 255)
X_cat = (randint(1,5)*82)+107
Y_cat = (randint(1,5)*82)+107
display_surface = pygame.display.set_mode((height, width))

pygame.display.set_caption('mouse and cat')

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
pygame.draw.rect(display_surface, red, [X_cat, Y_cat, 80, 80])
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()