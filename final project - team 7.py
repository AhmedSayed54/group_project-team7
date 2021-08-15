import pygame  
pygame.init()  
black = (0, 0, 0)  
white = (255, 255, 255)
height = 800  
width = 800
blue=(0,110,255)

display_surface = pygame.display.set_mode((height, width))  
  
pygame.display.set_caption('Image')  

x=107
y=107
i=0



pygame.display.flip()
display_surface.fill(black)
pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
for i in range(7):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        y += 82
x=600
y=107
for i in range(7):
        pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
        y += 82
x=190
y=107
for i in range(5):
    pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
    x+= 82
x=190
y=600
for i in range(5):
    pygame.draw.rect(display_surface, blue, [x, y, 80, 80])
    x += 82
x=190
y=190
for i in range (5):

    for i in range (5):
        pygame.draw.rect(display_surface, white, [x,y,80,80])
        x+=82
    x=190
    y+=82


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()