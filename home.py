import pygame
pygame.init()




font_path = "./SuperMario256.ttf "
police = pygame.font.SysFont(font_path, 120)
text_col = (255,0,0)
rect_color = (167, 167, 167 )
home = pygame.display.set_mode((900,600))
back_img = pygame.image.load("vraifond.jpg")

def draw_text2(text,police,text_col,x,y):
    img = police.render(text,True,text_col)
    home.blit(img,(x,y))

run2 = True
while run2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False
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
         if x >= (300) and x <= (520) and y >= (270) and y <= (330):
            run2 = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed() == (1,0,0) :
         x , y = pygame.mouse.get_pos()
         if x >= (300) and x <= (520) and y >= (370) and y <= (430):
             pygame.quit()
    
    pygame.display.flip()
pygame.quit()