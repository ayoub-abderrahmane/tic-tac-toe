import pygame

surf = pygame.display.set_mode((800,600))
run = True
posX = 50
vx = 1
img = pygame.image.load("TPN.png")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    surf.fill((0,0,0))
    surf.blit(img ,(-550,-200))
    pygame.draw.line(surf,(255,255,255),(10,20),(150,200),2)
    pygame.draw.line(surf,(255,255,255),(150,10),(20,200),2)
    pygame.draw.circle(surf,(255,0,0),(400,100), 80,2)
    
    pygame.display.flip()

pygame.quit()