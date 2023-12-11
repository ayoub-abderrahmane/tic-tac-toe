import pygame

surf = pygame.display.set_mode((800,600))
run =  True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                pos = pygame.mouse.get_pos()
            pygame.draw.circle (surf ,(255,255,255),(pos),80 , 5)
            pygame.display.flip()

    pygame.quit
