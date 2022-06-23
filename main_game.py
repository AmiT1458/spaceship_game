import pygame
from sys import exit
import os
import random
pygame.font.init()
from Button import Button



pygame.init()
game_name = 'The god of the space...'
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(game_name)
clock = pygame.time.Clock()
FPS = 60


MAX_BULLETS = 4
BULLET_VEL = 10

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
ABILITY_COLLIDE = pygame.USEREVENT + 3
EXIST_ability, t , trail = pygame.USEREVENT + 4 , 7000 , []
pygame.time.set_timer(EXIST_ability, t) #sets a timer for every 7 seconds have passed


space = pygame.image.load(os.path.join('Emojy','space.png'))
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)
MENU_FONT = pygame.font.SysFont('Gameplay,',60)
BORDER = pygame.Rect(SCREEN_WIDTH//2 - 5, 0 , 11 , SCREEN_HEIGHT)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (100,0,255)
YEllOW_crl = (255, 255, 0)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50,40
ability_WIDTH = 40
ability_HEIGHT = 45


yellow_spaceship_image = pygame.image.load(os.path.join("Emojy","PEPEGA.png"))
red_spaceship_image = pygame.image.load(os.path.join("Emojy","5HEAD.png"))
speed_ability_image = pygame.image.load(os.path.join('Emojy',"pixil-frame-0.png"))
speed_ability_image = pygame.transform.scale(speed_ability_image,(ability_WIDTH , ability_HEIGHT))
yellow_spaceship_image = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
red_spaceship_image = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
speed_ability_gained = pygame.image.load(os.path.join("Emojy","speed_ability(black).png"))
speed_ability_gained = pygame.transform.scale(speed_ability_gained, (50, 55))
menu_screen_image = pygame.image.load(os.path.join('Emojy','menu_screen.png'))
menu_screen_image = pygame.transform.scale(menu_screen_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
menu_screen_buttons = pygame.image.load(os.path.join('Emojy','rectangle2.png'))
menu_screen_buttons= pygame.transform.scale(menu_screen_buttons,(240,100))


#red's keys
def yellow_spaceship_movement(key_pressed,yellow,VELO):

    if key_pressed[pygame.K_a] and yellow.x - VELO > 0: #left
        yellow.x -= VELO
    if key_pressed[pygame.K_d] and yellow.x + VELO + yellow.width < BORDER.x: #right
        yellow.x += VELO
    if key_pressed[pygame.K_w] and yellow.y - VELO > 0: #up
        yellow.y -= VELO
    if key_pressed[pygame.K_s] and yellow.y + VELO + yellow.height < SCREEN_HEIGHT:  #down
        yellow.y += VELO

#yellow's keys
def red_spaceship_movement(key_pressed,red,VELO):
    if key_pressed[pygame.K_LEFT]and red.x - VELO > BORDER.x + BORDER.width : #left
        red.x -= VELO
    if key_pressed[pygame.K_RIGHT] and red.x + VELO + red.width < SCREEN_WIDTH : #right
        red.x += VELO
    if key_pressed[pygame.K_UP] and red.y - VELO > 0: #up
        red.y -= VELO
    if key_pressed[pygame.K_DOWN] and red.y + VELO + red.height < SCREEN_HEIGHT: #down
        red.y += VELO


#checks if there's a collision
def ability_collision_red(ability_slots,red):
    for speed_ability in ability_slots:
        if red.colliderect(speed_ability):
            ability_slots.remove(speed_ability)
            pygame.event.post(pygame.event.Event(ABILITY_COLLIDE))
            return True

    return False

#checks if there's a collision
def ability_collision_yellow(ability_slots,yellow):
    for speed_ability in ability_slots:
        if yellow.colliderect(speed_ability):
            ability_slots.remove(speed_ability)
            pygame.event.post(pygame.event.Event(ABILITY_COLLIDE))
            return True

    return False

def handle_bullets(BULLETS_YELLOW, BULLETS_RED, red, yellow):
    for bullet in BULLETS_YELLOW:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            BULLETS_YELLOW.remove(bullet)
        elif bullet.x > SCREEN_WIDTH:
            BULLETS_YELLOW.remove(bullet)
    for bullet in BULLETS_RED:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            BULLETS_RED.remove(bullet)

        elif bullet.x < 0:
            BULLETS_RED.remove(bullet)




def GAME_OVER_SCREEN(text):
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_SPACE:
                    pause = False

        screen.fill(WHITE)
        draw_text = WINNER_FONT.render(text,1,BLACK)
        PLAY_AGAIN_TEXT = HEALTH_FONT.render('press SPACE to play again or press Q to quit',1, BLUE)
        screen.blit(PLAY_AGAIN_TEXT,(SCREEN_WIDTH/2 - PLAY_AGAIN_TEXT.get_width()/2 , SCREEN_HEIGHT/2 - PLAY_AGAIN_TEXT.get_height()/2 +17))
        screen.blit(draw_text , (SCREEN_WIDTH/2 - draw_text.get_width()/2,SCREEN_HEIGHT/3 - draw_text.get_height()/2))
        pygame.display.update()
    main()


def options_screen():

    back_button = Button(menu_screen_buttons, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 'Back')
    while True:
        clock.tick(FPS)
        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput((MOUSE_POS)):
                    menu()
                    break


        screen.fill((0,0,0))
        dev_text = MENU_FONT.render('IN DEVELOPMENT',True,WHITE)
        screen.blit(dev_text , (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT /2 - 150))
        back_button.update()
        back_button.changeColor((MOUSE_POS))

        pygame.display.update()

def draw_window(red,yellow, BULLETS_YELLOW, BULLETS_RED,YELLOW_HEALTH,RED_HEALTH):
    screen.blit(space,(0, 0))
    pygame.draw.rect(screen, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render('Health: '+ str(RED_HEALTH), 1 , WHITE )
    yellow_health_text = HEALTH_FONT.render('Health: ' + str(YELLOW_HEALTH), 1 , WHITE)
    screen.blit(red_health_text,(SCREEN_WIDTH - red_health_text.get_width() -10 , 10))
    screen.blit(yellow_health_text, (10, 10))
    screen.blit(yellow_spaceship_image, (yellow.x,yellow.y))
    screen.blit(red_spaceship_image , (red.x, red.y))



    for bullet in BULLETS_RED:
        pygame.draw.rect(screen,RED,bullet)

    for bullet in BULLETS_YELLOW:
        pygame.draw.rect(screen,YEllOW_crl,bullet)



def menu():
    running = True
    menu_game_name = MENU_FONT.render(game_name, True, WHITE)
    menu_game_name_rect = menu_game_name.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 - 50))
    play_button = Button(menu_screen_buttons, SCREEN_WIDTH / 2, menu_game_name_rect.y + 170 , 'Play')
    options_button = Button(menu_screen_buttons ,SCREEN_WIDTH / 2, menu_game_name_rect.y + 310 , 'Options')
    quit_button = Button(menu_screen_buttons,SCREEN_WIDTH / 2, menu_game_name_rect.y + 450,'Quit')

    while running:
        clock.tick(FPS)
        MOUSE_POS = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(MOUSE_POS):
                    main()
                    break
                if options_button.checkForInput(MOUSE_POS):
                    options_screen()
                    break
                if quit_button.checkForInput(MOUSE_POS):
                    pygame.quit()
                    exit()



        screen.blit(menu_screen_image,(0,0)) #menu image
        screen.blit(menu_game_name, menu_game_name_rect)
        play_button.update()
        play_button.changeColor((MOUSE_POS))
        options_button.update()
        options_button.changeColor((MOUSE_POS))
        quit_button.update()
        quit_button.changeColor((MOUSE_POS))


        pygame.display.update()




BULLETS_YELLOW = []
BULLETS_RED = []
ability_slots = []

def main():
    VEL_yellow = 5
    VEL_red = 5
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    red = pygame.Rect(800, 100,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(300, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    is_speed_ability_on_screen = True
    current_time = 0
    ability_time_start = 0
    speed_ability_gained_on_screen_red = False
    speed_ability_gained_on_screen_yellow = False
    speed_pos_x = random.randint(0,1200)
    speed_pos_y = random.randint(0, 800)
    ability_time_usesage = 0
    while True: #game loop

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(BULLETS_YELLOW) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height// 2 - 2, 10, 5)
                    BULLETS_YELLOW.append(bullet)

                if event.key == pygame.K_RCTRL and len(BULLETS_RED) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height // 2 - 2, 10, 5)
                    BULLETS_RED.append(bullet)
            if event.type == EXIST_ability: # checking if 7 sec have passed every time
                print('7 sec')
                if is_speed_ability_on_screen:
                    is_speed_ability_on_screen = False
                    continue
                if is_speed_ability_on_screen == False:
                    speed_pos_x = random.randint(0, 1200) # giving a new x / y pos before creating the ability again
                    speed_pos_y = random.randint(0, 800)
                    is_speed_ability_on_screen = True
                    continue
            if event.type == RED_HIT:
                RED_HEALTH -= 1

            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1




        winner_text = ""
        if RED_HEALTH <= 0:
            winner_text = "yellow wins!"
        if YELLOW_HEALTH <= 0:
            winner_text = "red wins!"
        if winner_text != "":
            GAME_OVER_SCREEN(winner_text)
            break

        key_pressed = pygame.key.get_pressed()

        yellow_spaceship_movement(key_pressed, yellow,VEL_yellow)
        red_spaceship_movement(key_pressed, red,VEL_red)
        current_time = pygame.time.get_ticks()
        handle_bullets(BULLETS_YELLOW,BULLETS_RED,red,yellow)
        draw_window(red, yellow, BULLETS_YELLOW, BULLETS_RED, YELLOW_HEALTH, RED_HEALTH )



        if current_time > 4000: # if it past four secs it creates the ability

            if is_speed_ability_on_screen:
                speed_ability = pygame.Rect(speed_pos_x, speed_pos_y, ability_WIDTH, ability_HEIGHT) #speed_rect
                screen.blit(speed_ability_image,(speed_ability.x,speed_ability.y)) #speed image
                ability_slots.append(speed_ability)

                if ability_collision_red(ability_slots,red): # if collide with red the image disappears and increacses his speed
                    is_speed_ability_on_screen = False
                    VEL_red = 10
                    ability_time_start = pygame.time.get_ticks()
                    speed_ability_gained_on_screen_red = True
                    ability_time_usesage += 3000

                if ability_collision_yellow(ability_slots, yellow): # if collide with yellow the image disappears and increacses his speed
                    is_speed_ability_on_screen = False
                    VEL_yellow = 10
                    ability_time_start = pygame.time.get_ticks()
                    speed_ability_gained_on_screen_yellow = True
                    ability_time_usesage += 3000

        if speed_ability_gained_on_screen_red:

            screen.blit(speed_ability_gained, ( SCREEN_WIDTH - speed_ability_gained.get_width() -10 , 63))

        if speed_ability_gained_on_screen_yellow:
            screen.blit(speed_ability_gained, (10, 63))

        if current_time - ability_time_start > ability_time_usesage: # checking if it past ability_time_usesage (7) seconds
            VEL_red = 5
            VEL_yellow = 5
            speed_ability_gained_on_screen_yellow = False
            speed_ability_gained_on_screen_red = False
            ability_time_usesage = 0

        pygame.display.update()

    main()


if __name__ =="__main__":
    menu()
