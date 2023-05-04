import random
import os

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT,  K_RIGHT

pygame.init()

FPS = pygame.time.Clock() 

HEIGHT = 800
WIDHT = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELOW = (255, 255, 0)

main_display = pygame.display.set_mode((WIDHT, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDHT, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 2

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

PLAYER_SIZE = (20, 20)
player = pygame.image.load('player.png').convert_alpha() #pygame.Surface(PLAYER_SIZE)
# player.fill(COLOR_BLACK)
player_rect = pygame.Rect(40, 350, *PLAYER_SIZE) #player.get_rect()


player_move_down = [0, 4]
player_move_up = [0, -4]
player_move_right = [4, 0]
player_move_left = [-6, 0]

# Додаємо ворогів
def create_enemy():
    ENEMY_SIZE = (30, 30)
    enemy = pygame.image.load('enemy.png').convert_alpha() #pygame.Surface(ENEMY_SIZE)
    # enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDHT, random.randint(150, 650), *ENEMY_SIZE)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREATE_GIFT = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_GIFT, 4000)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)


enemies = []
gifts = []

score = 0

image_index = 0

# Додаємо призи
def create_gift():
    GIFT_SIZE = (30, 30)
    gift = pygame.image.load('bonus.png').convert_alpha() #pygame.Surface(GIFT_SIZE)
    # gift.fill(COLOR_YELOW)
    gift_rect = pygame.Rect(random.randint(250, 1000), -100, *GIFT_SIZE)
    gift_move = [0, random.randint(4, 8)]
    return [gift, gift_rect, gift_move]

playing = True

while playing:
    FPS.tick(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == CREATE_GIFT:
           gifts.append(create_gift())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH,PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
            
    # main_display.fill(COLOR_BLACK)
    bg_X1 -= bg_move
    bg_X2 -= bg_move
    
    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()
    
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))


    # Пересування гравця клавішамив
    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)
    if keys[K_RIGHT] and player_rect.right < WIDHT:
        player_rect = player_rect.move(player_move_right)
   
    # Відображення суперників та гравців
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False
         
    for gift in gifts:
        gift[1] = gift[1].move(gift[2])
        main_display.blit(gift[0], gift[1])

        if player_rect.colliderect(gift[1]):
            gifts.pop(gifts.index(gift))
            score +=1

    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDHT-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()
    
    # Видалення супротивників та бонусів з 
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
            
    for gift in gifts:
        if gift[1].top > HEIGHT:
            gifts.pop(gifts.index(gift))
    