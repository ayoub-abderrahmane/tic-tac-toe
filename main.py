import pygame

surf = pygame.display.set_mode((800,600))
run = True

def draw_board():
   pygame.draw.line(surf,(255,255,255),(250,0),(250,600),2)
   pygame.draw.line(surf,(255,255,255),(540,0),(540,600),2)
   pygame.draw.line(surf,(255,255,255),(0,195),(800,195),2)
   pygame.draw.line(surf,(255,255,255),(0,405),(800,405),2)
   pygame.display.flip()

def draw_cross(pos2):
      pygame.draw.line(surf,(255,255,255),(pos2),(pos2),5)
      pygame.draw.line(surf,(255,255,255),(pos2),(pos2),5)
      pygame.display.flip()

def draw_circle(pos):
   pygame.draw.circle (surf ,(255,255,255),(pos),80 , 5)
   pygame.display.flip()

while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               draw_circle(pygame.mouse.get_pos())
         elif event.type == pygame.MOUSEBUTTONDOWN:
             if pygame.mouse.get_pressed() == (0,0,1) :
                 draw_cross(pygame.mouse.get_pos())
     draw_board()

pygame.quit()