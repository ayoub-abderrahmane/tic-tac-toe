
import pygame

# Croix de la première cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y <= (200):
                  draw_cross((100,50),(200,150),(100, 150),(200,50))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (200) and y <= (400):
                  draw_cross((100,250),(200,350),(100, 350),(200,250))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (400):
                  draw_cross((100,450),(200,550),(100, 550),(200,450))
         
         # Croix de la deuxième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y <= (200):
                  draw_cross((400,50),(500,150),(400, 150),(500,50))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (200) and y <= (400):
                  draw_cross((400,250),(500,350),(400, 350),(500,250))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (400):
                  draw_cross((400,450),(500,550),(400, 550),(500,450))
         
         # Croix de la troisième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y <= (200):
                  draw_cross((700,50),(800,150),(700, 150),(800,50))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (200) and y <= (400):
                  draw_cross((700,250),(800,350),(700, 350),(800,250))
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) : 
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (400):
                  draw_cross((700,450),(800,550),(700, 550),(800,450))