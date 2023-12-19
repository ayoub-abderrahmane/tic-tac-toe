import pygame
pygame.init()


font_path = "./SuperMario256.ttf "
police = pygame.font.SysFont(font_path, 120)
text_col = (255,0,0)
rect_color = (167, 167, 167 )
home = pygame.display.set_mode((900,600))
back_img = pygame.image.load("homepage.webp")
play_img = pygame.image.load("ideeplay_quit.jpg")

def draw_text(text,police,text_col,x,y):
    img = police.render(text,True,text_col)
    home.blit(img,(x,y))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    home.blit(back_img,(0,0))
    pygame.draw.rect(home ,rect_color ,(180,80,520,80))
    pygame.draw.rect(home ,rect_color ,(280,220,290,80))
    pygame.draw.rect(home ,rect_color ,(300,360,240,80))
    draw_text("MAIN MENU",police,text_col,200,80)
    draw_text("START",police,text_col,290,220)
    draw_text("QUIT",police,text_col,310,360)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (520) and y >= (270) and y <= (330):
            print ("tkt")
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (520) and y >= (370) and y <= (430):
             pygame.quit()
    
    pygame.display.flip()
pygame.quit()