
import pygame

surf = pygame.display.set_mode((800,600))
run = True
while run :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN :
      if pygame.mouse.get_pressed() == (1,0,0) :
        pos = pygame.mouse.get_pos()
        print(pos)
      if pygame.mouse.get_pressed() == (0,0,1) :
        pos2 = pygame.mouse.get_pos()
        print (pos2 , "clic droit")
      if pygame.mouse.get_pressed() == (0,1,0):
        pos3 = pygame.mouse.get_pos()
        print (pos3)
  
  surf.fill((0,0,0))
  pygame.display.flip()
pygame.quit()
		