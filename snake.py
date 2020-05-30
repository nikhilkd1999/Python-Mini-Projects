import pygame
import random
import sys
import time


SNAKE_X = 100
SNAKE_Y = 100
SNAKE_SIZE = 15

VELOCITY = 4
VELOCITY_X = 0
VELOCITY_Y = 0

FPS = 60

FOOD_X = 200 
FOOD_Y = 200

SNAKE_LENGTH = 1
SNAKE_LIST = []


pygame.init()

def draw_SNAKE():
    
    for x,y in SNAKE_LIST:
        pygame.draw.rect(GAME_WINDOW,(0,0,0),[x,y,SNAKE_SIZE,SNAKE_SIZE])



GAME_WINDOW = pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Game")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
           
           if event.key == pygame.K_UP:
               VELOCITY_X = 0
               VELOCITY_Y = -VELOCITY

           if event.key == pygame.K_DOWN:
               VELOCITY_X = 0
               VELOCITY_Y = VELOCITY

           if event.key == pygame.K_LEFT:
               VELOCITY_X = -VELOCITY
               VELOCITY_Y = 0

           if event.key == pygame.K_RIGHT:
               VELOCITY_X = VELOCITY
               VELOCITY_Y = 0

    
    if abs( SNAKE_X - FOOD_X ) < SNAKE_SIZE and abs( SNAKE_Y - FOOD_Y ) < SNAKE_SIZE:

        FOOD_X = random.randint(200,800)
        FOOD_Y = random.randint(200,500)

        SNAKE_LENGTH += 10

    HEAD = []
    HEAD.append(SNAKE_X)
    HEAD.append(SNAKE_Y)

    SNAKE_LIST.append(HEAD)

    if len(SNAKE_LIST) > SNAKE_LENGTH:
        del SNAKE_LIST[0]




    SNAKE_X += VELOCITY_X
    SNAKE_Y += VELOCITY_Y

    if HEAD in SNAKE_LIST[:-1]:
        sys.exit()


    GAME_WINDOW.fill((0,204,0))
    #GAME_WINDOW.blit(pygame.image.load('D:/background.png').convert_alpha(),(0,0))
    pygame.draw.rect(GAME_WINDOW,(255,0,0),[FOOD_X,FOOD_Y,SNAKE_SIZE,SNAKE_SIZE])
    draw_SNAKE()
    pygame.display.update()
    pygame.time.Clock().tick(FPS)