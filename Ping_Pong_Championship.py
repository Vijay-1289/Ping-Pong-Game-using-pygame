import pygame
import Button

# Create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Soccer Championship')

# Load Button Images
start_img = pygame.image.load('start_btn.png').convert_alpha()
title_img = pygame.image.load('Soccer_Title.png').convert_alpha()


# Create Button Instances
Start_button = Button.button(320, 300, start_img, 0.5)
Title_button = Button.button(140, 100, title_img, 1.5)

# Game Loop
run = True
while run:
    screen.fill((202, 228, 241))

    if Start_button.draw(screen):
        import Button

        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 500

        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption('Soccer Championship')

        Level_1_img = pygame.image.load('1_png.png').convert_alpha()

        Level_1_button = Button.button(20, 30, Level_1_img, 0.7)

        run = True
        while run:
            screen.fill((255, 255, 255))

            if Level_1_button.draw(screen):
                import Button

                SCREEN_HEIGHT = 800
                SCREEN_WIDTH = 500

                screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
                pygame.display.set_caption('Soccer Championship')

                Logo_img = pygame.image.load('RCB_VS_SRH.png').convert_alpha()
                start_img = pygame.image.load('start_btn.png').convert_alpha()

                Logo_button = Button.button(20, 30, Logo_img, 1.0)
                Start_button = Button.button(320, 350, start_img, 0.5)

                run = True
                while run:
                    screen.fill((0, 0, 0))

                    if Start_button.draw(screen):
                       import Level_1.py
                    if Logo_button.draw(screen):
                        print('LOGO')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    if Title_button.draw(screen):
        print('Title')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()