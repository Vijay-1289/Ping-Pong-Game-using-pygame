import Button
import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Soccer Championship')

CSK_img = pygame.image.load('CSK_LOGO.png').convert_alpha()
KKR_img = pygame.image.load('KKR_LOGO.png').convert_alpha()
RR_img = pygame.image.load('RR_LOGO.png').convert_alpha()
MI_img = pygame.image.load('MI_LOGO.png').convert_alpha()
GT_img = pygame.image.load('GT_LOGO.png').convert_alpha()
LSG_img = pygame.image.load('LSG_LOGO.png').convert_alpha()
PBKS_img = pygame.image.load('PBKS_LOGO.png').convert_alpha()
RCB_img = pygame.image.load('RCB_LOGO.png').convert_alpha()
DC_img = pygame.image.load('DC_LOGO.png').convert_alpha()

CSK_button = Button.button(10, 80, CSK_img, 0.32)
RR_button = Button.button(160, 80, RR_img, 0.35)
MI_button = Button.button(290, 80, MI_img, 0.5)
KKR_button = Button.button(500, 80, KKR_img, 0.35)
LSG_button = Button.button(590, 80, LSG_img, 0.5)
GT_button = Button.button(80, 250, GT_img, 0.32)
RCB_button = Button.button(290, 230, RCB_img, 0.7)
PBKS_button = Button.button(450, 220, PBKS_img, 0.5)
DC_button = Button.button(600, 220, DC_img, 0.25)

run = True
while run:

    screen.fill((255, 255, 255))

    if CSK_button.draw(screen):
        import Button

        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 500

        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption('Soccer Championship')

        Level_1_img = pygame.image.load('1_png.png').convert_alpha()
        Level_2_img = pygame.image.load('2_png.png').convert_alpha()
        Level_3_img = pygame.image.load('3_png.png').convert_alpha()

        Level_1_button = Button.button(20, 30, Level_1_img, 0.7)
        Level_2_button = Button.button(150, 30, Level_2_img, 0.7)
        Level_3_button = Button.button(280, 30, Level_3_img, 0.7)

        run = True
        while run:
            screen.fill((255, 255, 255))
            import Level_2.py
    if KKR_button.draw(screen):
        import Level_4.py
    if RR_button.draw(screen):
        import Level_7.py
    if DC_button.draw(screen):
        import Level_6.py
    if MI_button.draw(screen):
        import Level_5.py
    if PBKS_button.draw(screen):
        import Level_9.py
    if GT_button.draw(screen):
        import Level_3.py
    if LSG_button.draw(screen):
        import Level_8.py
    if RCB_button.draw(screen):
        import Level_1.py
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()