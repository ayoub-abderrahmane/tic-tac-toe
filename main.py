import pygame

surf = pygame.display.set_mode((900,600))
run = True

def draw_board():
   pygame.draw.line(surf,(255,255,255),(300,0),(300,600),2)
   pygame.draw.line(surf,(255,255,255),(600,0),(600,600),2)
   pygame.draw.line(surf,(255,255,255),(0,200),(900,200),2)
   pygame.draw.line(surf,(255,255,255),(0,400),(900,400),2)
   pygame.display.flip()

def draw_cross(a,z,e,r):
      pygame.draw.line(surf,(255,255,255),(a),(z),8)
      pygame.draw.line(surf,(255,255,255),(e),(r),8)
      pygame.display.flip()

def draw_circle(x , y):
      pygame.draw.circle (surf ,(255,255,255),(x , y),80 , 5)
      pygame.display.flip()

while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

         # Cercle de la première colonne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y <= (200):
                  draw_circle(145 ,100)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (200) and y <= (400):
                  draw_circle(145 ,300)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (400):
                  draw_circle(145 ,500)

         
         
         # Cercle de la deuxième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y <= (200):
                  draw_circle(450 ,100)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (200) and y <= (400):
                  draw_circle(450 ,300)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (400):
                  draw_circle(450 ,500)
         
         
         # Cercle de la troisième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y <= (200):
                  draw_circle(750 ,100)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (200) and y <= (400):
                  draw_circle(750 ,300)
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (400):
                  draw_circle(750 ,500)
         
         #//////////////////////////////////:: TEST POUR PASSER AU SECOND JOUEUR /////////////////////////////////////////////////////////////////////

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
         draw_board()

pygame.quit()