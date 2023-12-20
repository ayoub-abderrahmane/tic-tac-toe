import pygame
pygame.init()

font_path = "./Kids Draw.ttf"
current_player = True
surf = pygame.display.set_mode((900,600))
run = True

# Variable pour le menu d'acceuil

font_path2 = "./SuperMario256.ttf "
police = pygame.font.SysFont(font_path2, 120)
text_col = (0, 255, 147 )
rect_color = (93, 0, 255 )
home = pygame.display.set_mode((900,600))
back_img = pygame.image.load("vraifond.jpg")

def draw_text2(text,police,text_col,x,y):
    img = police.render(text,True,text_col)
    home.blit(img,(x,y))

run2 = True



# Variable pour vérifier sur une case a été utilisée

vérif1 = 0
vérif2 = 0
vérif3 = 0
vérif4 = 0
vérif5 = 0
vérif6 = 0
vérif7 = 0
vérif8 = 0
vérif9 = 0

# Variable pour vérifier les combinaison vainqueurs et afficher les messages de fin

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
i = 0

font = pygame.font.Font(font_path, 74)
font2 = pygame.font.Font(None, 32)
text = font.render("VOUS ÊTES LE VAINQUEUR !",1,(0, 219, 253))
text_equality = font.render("MATCH NUL",1,(0, 219, 253))
to_continue = font2.render("Appuyer sur la barre pour recommencer",1,(0, 219, 253))

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
   surf.blit(text, (50,300))
   pygame.display.flip()

def draw_to_continue():
   surf.blit(to_continue,(220,500))
   pygame.display.flip()

def draw_text_equality():
   surf.blit(text_equality, (275,300))
   draw_to_continue()
   pygame.display.flip()

def check_for_victory():
   if a == 3 or r == 3:
      pygame.draw.line(surf, (255,0,0),(150,50),(150,550) ,5)
      draw_text()
      draw_to_continue()
   if z == 3 or t == 3:
      pygame.draw.line(surf, (255,0,0),(450,50),(450,550) ,5)
      draw_text()
      draw_to_continue()
   if e == 3 or w == 3:
      pygame.draw.line(surf, (255,0,0),(750,50),(750,550) ,5)
      draw_text()
      draw_to_continue()
   if q == 3 or f == 3:
      pygame.draw.line(surf, (255,0,0),(50,100),(850,100) ,5)
      draw_text()
      draw_to_continue()
   if s == 3 or g == 3:
      pygame.draw.line(surf, (255,0,0),(50,300),(850,300) ,5)
      draw_text()
      draw_to_continue()
   if d == 3 or h == 3:
      pygame.draw.line(surf, (255,0,0),(50,500),(850,500) ,5)
      draw_text()
      draw_to_continue()
   if k == 3:
      pygame.draw.line(surf, (255,0,0),(50,50),(850,550) ,5)
      draw_text()
      draw_to_continue()
   if m == 3:
      pygame.draw.line(surf, (255,0,0),(50,550),(850,50) ,5)
      draw_text()
      draw_to_continue()
   if c == 3:
      pygame.draw.line(surf, (255,0,0),(50,50),(850,550) ,5)
      draw_text()
      draw_to_continue()
   if v == 3:
      pygame.draw.line(surf, (255,0,0),(50,550),(850,50) ,5)
      draw_text()
      draw_to_continue()

def check_for_equality():
   if i == 9:
      draw_text_equality()


def draw_cross_in_board():
   global r,f,c,g,h,v,t,w,i
   global vérif1,vérif2,vérif3,vérif4,vérif5,vérif6,vérif7,vérif8,vérif9

     # Croix de la première colonne         
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x <= (300) and y <= (200) and vérif1 == 0 :
            draw_cross((100,50),(200,150),(100, 150),(200,50))
            r += 1
            f += 1
            c += 1
            i += 1
            vérif1 = 1
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x <= (300) and y >= (200) and y <= (400) and vérif2 == 0:
            draw_cross((100,250),(200,350),(100, 350),(200,250))
            r += 1
            g += 1
            i += 1
            vérif2 = 1
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x <= (300) and y >= (400) and vérif3 == 0:
            draw_cross((100,450),(200,550),(100, 550),(200,450))
            r += 1
            h += 1
            v += 1
            i += 1
            vérif3 = 1
   
   # Croix de la deuxième colonne

   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (600) and y <= (200) and vérif4 == 0:
            draw_cross((400,50),(500,150),(400, 150),(500,50))
            t += 1
            f += 1
            i += 1
            vérif4 = 1
            
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (600) and y >= (200) and y <= (400) and vérif5 == 0:
            draw_cross((400,250),(500,350),(400, 350),(500,250))
            t += 1
            g += 1
            c += 1
            v += 1
            i += 1
            vérif5 = 1
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (600) and y >= (400) and vérif6 == 0 :
            draw_cross((400,450),(500,550),(400, 550),(500,450))
            t += 1
            h += 1
            i += 1
            vérif6 = 1
   
   # Croix de la troisième colonne

   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (600) and y <= (200) and vérif7 == 0 :
            draw_cross((700,50),(800,150),(700, 150),(800,50))
            w += 1
            f += 1
            v += 1
            i += 1
            vérif7 = 1
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (600) and y >= (200) and y <= (400) and vérif8 == 0 :
            draw_cross((700,250),(800,350),(700, 350),(800,250))
            w += 1
            g += 1
            i += 1
            vérif8 = 1
   if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) : 
         x , y = pygame.mouse.get_pos()
         if x >= (600) and y >= (400) and vérif9 == 0 :
            draw_cross((700,450),(800,550),(700, 550),(800,450))
            w += 1
            h += 1
            c += 1
            i += 1
            vérif9 = 1

# /////////////////////////////////////////////////////////////////////////////////////////////////////

def draw_circle_in_board():
      global a ,k, q ,d , m, s, z, e ,i
      global vérif1,vérif2,vérif3,vérif4,vérif5,vérif6,vérif7,vérif8,vérif9
# Cercle de la première colonne

      if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            if x <= (300) and y <= (200) and vérif1 == 0 :
               draw_circle(145 ,100)
               a += 1
               q += 1
               k += 1
               i += 1
               vérif1 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x <= (300) and y >= (200) and y <= (400) and vérif2 == 0 :
               draw_circle(145 ,300)
               a += 1
               s += 1
               i += 1
               vérif2 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x <= (300) and y >= (400) and vérif3 == 0 :
               draw_circle(145 ,500)
               a += 1
               d += 1
               m += 1
               i += 1
               vérif3 = 1

      
      
      # Cercle de la deuxième colonne

      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (300) and x <= (600) and y <= (200) and vérif4 == 0 :
               draw_circle(450 ,100)
               z += 1
               q += 1
               i += 1
               vérif4 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (300) and x <= (600) and y >= (200) and y <= (400) and vérif5 == 0 :
               draw_circle(450 ,300)
               z += 1
               s += 1
               k += 1
               m += 1
               i += 1
               vérif5 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (300) and x <= (600) and y >= (400) and vérif6 == 0 :
               draw_circle(450 ,500)
               z += 1
               d += 1
               i += 1
               vérif6 = 1
      
      
      # Cercle de la troisième colonne

      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (600) and y <= (200) and vérif7 == 0 :
               draw_circle(750 ,100)
               e += 1
               q += 1
               m +=1
               i += 1
               vérif7 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (600) and y >= (200) and y <= (400) and vérif8 == 0 :
               draw_circle(750 ,300)
               e += 1
               s += 1
               i += 1
               vérif8 = 1
      if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pressed() == (1,0,0) :
            x , y = pygame.mouse.get_pos()
            if x >= (600) and y >= (400) and vérif9 == 0 :
               draw_circle(750 ,500)
               e += 1
               d += 1
               k += 1
               i += 1
               vérif9 = 1

while run2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    home.blit(back_img,(0,0))
    pygame.draw.rect(home ,rect_color ,(180,80,520,80))
    pygame.draw.rect(home ,rect_color ,(280,220,290,80))
    pygame.draw.rect(home ,rect_color ,(300,360,240,80))
    draw_text2("MAIN MENU",police,text_col,200,80)
    draw_text2("START",police,text_col,290,220)
    draw_text2("QUIT",police,text_col,310,360)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (520) and y >= (230) and y <= (300):
            home.fill((0,0,0))
            run2 = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (520) and y >= (370) and y <= (430):
             pygame.quit()
    
    pygame.display.flip()


while run:
   for event in pygame.event.get():
         if event.type == pygame.QUIT:
               run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
            
               if current_player == False:
                  draw_circle_in_board()
               else:
                  draw_cross_in_board()
               current_player = not current_player
      
      
         if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
               surf.fill((0,0,0))
               draw_board()    
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
               i = 0
               vérif1 = 0
               vérif2 = 0
               vérif3 = 0
               vérif4 = 0
               vérif5 = 0
               vérif6 = 0
               vérif7 = 0
               vérif8 = 0
               vérif9 = 0      
         check_for_victory()
         check_for_equality()
         draw_board()
         

pygame.quit()