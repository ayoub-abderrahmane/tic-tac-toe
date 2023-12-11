import pygame
surf = pygame.display.set_mode((800,600))
def draw_board():
    run = True
    while run :
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
      pygame.draw.line(surf,(255,255,255),(250,0),(250,600),2)
      pygame.draw.line(surf,(255,255,255),(540,0),(540,600),2)
      pygame.draw.line(surf,(255,255,255),(0,195),(800,195),2)
      pygame.draw.line(surf,(255,255,255),(0,405),(800,405),2)
      pygame.display.flip()
draw_board()

def draw_cross():
   run = True
   while run:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
      pygame.draw.line(surf,(255,255,255),(10,20),(150,200),2)
      pygame.draw.line(surf,(255,255,255),(150,10),(20,200),2)
      pygame.display.flip()
   pygame.quit()

draw_cross()

   
		