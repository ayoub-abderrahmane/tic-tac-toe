import pygame
pygame.init()

font_path = "./Kids Draw.ttf"
current_player = True
surf = pygame.display.set_mode((900,600))
run = True
a = 0
z = 0
e = 0
r = 0
t = 0
w = 0
q = 0
s = 0
d = 0
f = 0
g = 0
h = 0
k = 0
m = 0
c = 0
v = 0

font = pygame.font.Font(font_path, 64)
text = font.render("VOUS ÊTES LE VAINQUEUR !",1,(0, 219, 253))

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

def draw_text():
   surf.blit(text, (150,300))
   pygame.display.flip()

def check_for_victory():
   if a == 3 or r == 3:
      pygame.draw.line(surf, (255,0,0),(150,50),(150,550) ,5)
      draw_text()
   if z == 3 or t == 3:
      pygame.draw.line(surf, (255,0,0),(450,50),(450,550) ,5)
   if e == 3 or w == 3:
      pygame.draw.line(surf, (255,0,0),(750,50),(750,550) ,5)
   if q == 3 or f == 3:
      pygame.draw.line(surf, (255,0,0),(50,100),(850,100) ,5)
   if s == 3 or g == 3:
      pygame.draw.line(surf, (255,0,0),(50,300),(850,300) ,5)
   if d == 3 or h == 3:
      pygame.draw.line(surf, (255,0,0),(50,500),(850,500) ,5)
   if k == 3:
      pygame.draw.line(surf, (255,0,0),(50,50),(850,550) ,5)
   if m == 3:
      pygame.draw.line(surf, (255,0,0),(50,550),(850,50) ,5)
   if c == 3:
      pygame.draw.line(surf, (255,0,0),(50,50),(850,550) ,5)
   if v == 3:
      pygame.draw.line(surf, (255,0,0),(50,550),(850,50) ,5)



while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

         # Cercle de la première colonne

         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               current_player = not current_player
               current_player != current_player

               print(current_player,'currentPlayer')
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
         
         
         
         if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
               surf.fill((0,0,0))        
         
         
         
      
         check_for_victory()
         draw_board()

pygame.quit()