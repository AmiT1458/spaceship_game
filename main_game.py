import pygame
from sys import exit
import os
 #import time
#import random
pygame.font.init()



pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("First game!")
clock = pygame.time.Clock()
FPS = 60


MAX_BULLETS = 4
BULLET_VEL = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
ABILITY_COLLIDE = pygame.USEREVENT + 3

space = pygame.image.load(os.path.join('Emojy','space.png'))
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)
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

#def ability_collision(ability_slots ,red , yellow):
    #for speed_ability in ability_slots:
        #if red.colliderect(speed_ability):
            #ability_slots.remove(speed_ability)
    #for speed_ability in ability_slots:
        #if yellow.colliderect(speed_ability):
            #ability_slots.remove(speed_ability)

def ability_collision_red(ability_slots,red):
    for speed_ability in ability_slots:
        if red.colliderect(speed_ability):
            ability_slots.remove(speed_ability)
            pygame.event.post(pygame.event.Event(ABILITY_COLLIDE))
            return True

    return False

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

    #pygame.display.update()


BULLETS_YELLOW = []
BULLETS_RED = []
ability_slots = []


def main():
    VEL = 5
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    red = pygame.Rect(800, 100,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(300, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    is_speed_ability_on_screen = True
    current_time = 0
    ability_time_start = 0
    while True:

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

        yellow_spaceship_movement(key_pressed, yellow,VEL)
        red_spaceship_movement(key_pressed, red,VEL)
        current_time = pygame.time.get_ticks()
        #print(current_time)
        #print(VEL)
        handle_bullets(BULLETS_YELLOW,BULLETS_RED,red,yellow)
        draw_window(red, yellow, BULLETS_YELLOW, BULLETS_RED, YELLOW_HEALTH, RED_HEALTH )

        if current_time > 4000:

            if is_speed_ability_on_screen:
                speed_ability = pygame.Rect(700, 300, ability_WIDTH, ability_HEIGHT)
                screen.blit(speed_ability_image,(speed_ability.x,speed_ability.y))
                ability_slots.append(speed_ability)

                if ability_collision_red(ability_slots,red):
                    is_speed_ability_on_screen = False
                    VEL += 10
                    ability_time_start = pygame.time.get_ticks()


                if ability_collision_yellow(ability_slots, yellow):
                    is_speed_ability_on_screen = False
                    VEL += 10
                    ability_time_start = pygame.time.get_ticks()

        if current_time - ability_time_start > 3000:
            VEL = 5

        pygame.display.update()

    main()


if __name__ =="__main__":
    main()