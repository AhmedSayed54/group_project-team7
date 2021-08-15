import pygame  
pygame.init()  
black = (0, 0, 0)  
white = (255, 255, 255)
height = 800  
width = 800 
lives = 0

display_surface = pygame.display.set_mode((height, width), ,8)  
  
pygame.display.set_caption('Image')  
  

 
while True:  
    display_surface.fill(black)  
    pygame.draw.rect(display_surface, white, [100, 100, 605, 605])

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()    
            quit()  
        pygame.display.update()   


