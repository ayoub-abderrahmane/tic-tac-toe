import pygame

surf = pygame.display.set_mode((900,600))
current_player = False
run =  True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
               pygame.draw.circle (surf ,(255,255,255),(200,200),80 , 5)
               pygame.display.flip()
               current_player = not current_player
            if current_player == False:
                pygame.draw.circle (surf ,(255,255,255),(200,200),80 , 5)
                pygame.display.flip()
            else:
                pygame.draw.line(surf,(255,255,255),(50,100),(200, 300),5)

               
            
            
            
            # if pygame.mouse.get_pressed() == (1,0,0) :
            #     pos = pygame.mouse.get_pos()
            # pygame.draw.circle (surf ,(255,255,255),(pos),80 , 5)
            # pygame.display.flip()

pygame.quit()
