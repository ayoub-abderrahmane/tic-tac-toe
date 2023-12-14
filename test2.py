import pygame

def restart_game ():
         
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
    
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y <= (200):
                  draw_circle(145 ,100)
                  a += 1
                  q += 1
                  k += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (200) and y <= (400):
                  draw_circle(145 ,300)
                  a += 1
                  s += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (400):
                  draw_circle(145 ,500)
                  a += 1
                  d += 1
                  m += 1

         
         
         # Cercle de la deuxième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y <= (200):
                  draw_circle(450 ,100)
                  z += 1
                  q += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (200) and y <= (400):
                  draw_circle(450 ,300)
                  z += 1
                  s += 1
                  k += 1
                  m += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (400):
                  draw_circle(450 ,500)
                  z += 1
                  d += 1
         
         
         # Cercle de la troisième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y <= (200):
                  draw_circle(750 ,100)
                  e += 1
                  q += 1
                  m +=1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (200) and y <= (400):
                  draw_circle(750 ,300)
                  e += 1
                  s +=1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (400):
                  draw_circle(750 ,500)
                  e += 1
                  d += 1
                  k += 1
         
         #//////////////////////////////////:: TEST POUR PASSER AU SECOND JOUEUR /////////////////////////////////////////////////////////////////////

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y <= (200):
                  draw_cross((100,50),(200,150),(100, 150),(200,50))
                  r += 1
                  f += 1
                  c += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (200) and y <= (400):
                  draw_cross((100,250),(200,350),(100, 350),(200,250))
                  r += 1
                  g += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x <= (300) and y >= (400):
                  draw_cross((100,450),(200,550),(100, 550),(200,450))
                  r += 1
                  h += 1
                  v += 1
         
         # Croix de la deuxième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y <= (200):
                  draw_cross((400,50),(500,150),(400, 150),(500,50))
                  t += 1
                  f += 1
                  
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (200) and y <= (400):
                  draw_cross((400,250),(500,350),(400, 350),(500,250))
                  t += 1
                  g += 1
                  c += 1
                  v += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (300) and x <= (600) and y >= (400):
                  draw_cross((400,450),(500,550),(400, 550),(500,450))
                  t += 1
                  h += 1
         
         # Croix de la troisième cologne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y <= (200):
                  draw_cross((700,50),(800,150),(700, 150),(800,50))
                  w += 1
                  f += 1
                  v += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) :
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (200) and y <= (400):
                  draw_cross((700,250),(800,350),(700, 350),(800,250))
                  w += 1
                  g += 1
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (0,0,1) : 
               x , y = pygame.mouse.get_pos()
               if x >= (600) and y >= (400):
                  draw_cross((700,450),(800,550),(700, 550),(800,450))
                  w += 1
                  h += 1
                  c += 1