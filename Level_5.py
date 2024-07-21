import pygame, sys, random

from pygame import mixer

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, Cyan)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, Cyan)
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, Cyan)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if 2100 < current_time - score_time < 2800:
        number_one = game_font.render("Let's play", False, Cyan)
        screen.blit(number_one, (screen_width / 2 - 75, screen_height / 2 + 20))

    if current_time - score_time < 2800:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((-1, 1))
        ball_speed_x = 7 * random.choice((-1, 1))
        score_time = None


# General setup
pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Soccer Championship")

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 20, 20)
ball2 = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("green")
White = (255, 255, 255)
Orange = (255, 165, 0)
dodgerblue2 = (28, 134, 238)
Cyan = (0, 0, 255)
Green = (0, 255, 0)

# Game Variables
ball_speed_x = 7 * random.choice((-1, 1))
ball_speed_y = 7 * random.choice((-1, 1))
player_speed = 0
opponent_speed = 0

# Text Variables
player_score = 0
opponent_score = 0
player_name = 'SRH'
opponent_name = 'MI'
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Sound
pong_sound = pygame.mixer.Sound("Pong.ogg")

# Score Timer
score_time = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                opponent_speed += 7
            if event.key == pygame.K_s:
                opponent_speed -= 7

    # Game Logic
    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, Orange, player)
    pygame.draw.rect(screen, dodgerblue2, opponent)
    pygame.draw.ellipse(screen, White, ball)
    pygame.draw.ellipse(screen, White, ball2)
    pygame.draw.aaline(screen, White, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Score Variables
    if score_time:
        ball_start()
    player_text = game_font.render(f"{player_score}", False, Orange)
    screen.blit(player_text, (410, 315))
    opponent_text = game_font.render(f"{opponent_score}", False, dodgerblue2)
    screen.blit(opponent_text, (370, 315))
    player_text = game_font.render(f"{player_name}", False, Orange)
    screen.blit(player_text, (410, 50))
    opponent_text = game_font.render(f"{opponent_name}", False, dodgerblue2)
    screen.blit(opponent_text, (340, 50))
    pygame.display.flip()
    clock.tick(60)

    if player_score == 5:
        import Button

        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 500

        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption('Soccer Championship')

        Next_img = pygame.image.load('Next_btn.png').convert_alpha()
        Won_img = pygame.image.load('YW_btn.png').convert_alpha()

        Next_button = Button.button(350, 300, Next_img, 0.5)
        Won_button = Button.button(150, 100, Won_img, 1.0)

        run = True
        while run:
            screen.fill((202, 228, 241))

            if Next_button.draw(screen):
                import Button

                SCREEN_HEIGHT = 800
                SCREEN_WIDTH = 500

                screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
                pygame.display.set_caption('Soccer Championship')

                Level_1_img = pygame.image.load('1_png.png').convert_alpha()
                Level_2_img = pygame.image.load('2_png.png').convert_alpha()
                Level_3_img = pygame.image.load('3_png.png').convert_alpha()
                Level_4_img = pygame.image.load('4_png.png').convert_alpha()
                Level_5_img = pygame.image.load('5_png.png').convert_alpha()
                Level_6_img = pygame.image.load('6_png.png').convert_alpha()

                Level_1_button = Button.button(20, 30, Level_1_img, 0.7)
                Level_2_button = Button.button(150, 30, Level_2_img, 0.7)
                Level_3_button = Button.button(280, 30, Level_3_img, 0.7)
                Level_4_button = Button.button(410, 30, Level_4_img, 0.7)
                Level_5_button = Button.button(540, 30, Level_5_img, 0.7)
                Level_6_button = Button.button(670, 30, Level_6_img, 0.7)

                run = True
                while run:
                    screen.fill((255, 255, 255))

                    if Level_6_button.draw(screen):
                        import Button

                        SCREEN_HEIGHT = 800
                        SCREEN_WIDTH = 500

                        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
                        pygame.display.set_caption('Soccer Championship')

                        Team_img = pygame.image.load('DC_VS_SRH.png').convert_alpha()
                        start_img = pygame.image.load('start_btn.png').convert_alpha()

                        Team_button = Button.button(20, 30, Team_img, 1.0)
                        Start_button = Button.button(320, 350, start_img, 0.5)

                        run = True
                        while run:
                            screen.fill((0, 0, 0))

                            if Start_button.draw(screen):
                                import Level_6.py
                            if Team_button.draw(screen):
                                print('Team Title')
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                            pygame.display.update()


                    if Level_1_button.draw(screen):
                        print('Level 1 Completed')
                    if Level_2_button.draw(screen):
                        print('Level 2 Completed')
                    if Level_3_button.draw(screen):
                        print('Level 3 Completed')
                    if Level_4_button.draw(screen):
                        print('Level 4 Completed')
                    if Level_5_button.draw(screen):
                        print('Level 5 Completed')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    pygame.display.update()

            if Won_button.draw(screen):
                print("YOU WON")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

    if opponent_score == 5:
        import Button

        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 500

        screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption('Soccer Championship')

        Retry_img = pygame.image.load('Retry_btn.png').convert_alpha()
        lost_img = pygame.image.load('YL_btn.png').convert_alpha()

        Retry_button = Button.button(350, 300, Retry_img, 0.5)
        lost_button = Button.button(150, 100, lost_img, 1.0)

        run = True
        while run:
            screen.fill((202, 228, 241))

            if Retry_button.draw(screen):
                import Level_5.py
            if lost_button.draw(screen):
                print('YOU LOST')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()