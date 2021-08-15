import pygame
from random import randint
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255 , 0, 0)
height = 800
width = 800
blue = (0, 110, 255)
x_cm = 0
y_cm = 0
def position(x_cm, y_cm):
    x_cm = (randint(1,5)*82)+108
    y_cm = (randint(1,5)*82)+108
    pygame.draw.rect(display_surface, red, [x_cm, y_cm, 80, 80])
  
pygame.display.set_caption('Image')  
  



display_surface = pygame.display.set_mode((height, width))

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


position(x_cm, y_cm)




end = pygame.draw.rect(display_surface,(0,255,0),[600,353,80,80])

mouse = pygame.image.load('mouse.jpg')
mouse_t = pygame.transform.scale(mouse, (5,5))
rect = mouse.get_rect()
display_surface.blit(mouse, (rect.x,rect.y))

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

