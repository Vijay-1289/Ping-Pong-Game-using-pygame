import Button
import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Soccer Championship')

Next_img = pygame.image.load('Next_btn.png').convert_alpha()
Inst_1_img = pygame.image.load('Instruction_1.png').convert_alpha()
Inst_2_img = pygame.image.load('Instruction_2.png').convert_alpha()
Inst_3_img = pygame.image.load('Instruction_3.png').convert_alpha()
Inst_4_img = pygame.image.load('Instruction_4.png').convert_alpha()
Inst_5_img = pygame.image.load('Instruction_5.png').convert_alpha()
Inst_6_img = pygame.image.load('Instruction_6.png').convert_alpha()
Inst_7_img = pygame.image.load('Instruction_7.png').convert_alpha()
Soccer_trophy_img = pygame.image.load('Soccer_Trophy.png').convert_alpha()

Inst_1_button = Button.button(10, 30, Inst_1_img, 0.7)
Inst_2_button = Button.button(10, 70, Inst_2_img, 0.7)
Inst_3_button = Button.button(10, 110, Inst_3_img, 0.7)
Inst_4_button = Button.button(5, 170, Inst_4_img, 0.7)
Inst_5_button = Button.button(10, 225, Inst_5_img, 0.7)
Inst_6_button = Button.button(10, 250, Inst_6_img, 0.7)
Inst_7_button = Button.button(10, 305, Inst_7_img, 0.7)
Next_button = Button.button(330, 400, Next_img, 0.5)
Soccer_trophy_button = Button.button(550, 50, Soccer_trophy_img, 0.5)

run = True
while run:
    screen.fill((255, 255, 255))

    if Soccer_trophy_button.draw(screen):
        print('Soccer Trophy')
    if Inst_1_button.draw(screen):
        print('Instruction 1')
    if Inst_2_button.draw(screen):
        print('Instruction 2')
    if Inst_3_button.draw(screen):
        print('Instruction 3')
    if Inst_4_button.draw(screen):
        print('Instruction 4')
    if Inst_5_button.draw(screen):
        print('Instruction 5')
    if Inst_6_button.draw(screen):
        print('Instruction 6')
    if Inst_7_button.draw(screen):
        print('Instruction 7')
    if Next_button.draw(screen):
        import Level_11.py
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

