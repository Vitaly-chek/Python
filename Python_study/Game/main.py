import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT,  K_RIGHT

pygame.init()

FPS = pygame.time.Clock() 

HEIGHT = 800
WIDHT = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELOW = (255, 255, 0)

main_display = pygame.display.set_mode((WIDHT, HEIGHT))

PLAYER_SIZE = (20, 20)
player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_right = [1, 0]
player_move_left = [-1, 0]

# Додаємо ворогів
def create_enemy():
    ENEMY_SIZE = (30, 30)
    enemy = pygame.Surface(ENEMY_SIZE)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDHT, random.randint(0, HEIGHT), *ENEMY_SIZE)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []

# Додаємо призи
def create_gift():
    GIFT_SIZE = (30, 30)
    gift = pygame.Surface(GIFT_SIZE)
    gift.fill(COLOR_YELOW)
    gift_rect = pygame.Rect(random.randint(0, WIDHT), 0, *GIFT_SIZE)
    gift_move = [0, random.randint(1, 3)]
    return [gift, gift_rect, gift_move]

CREATE_GIFT = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_GIFT, 4000)

gifts = []

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == CREATE_GIFT:
           gifts.append(create_gift())
    main_display.fill(COLOR_BLACK)

    # # Перший варіант пересування
    # if player_rect.bottom >= HEIGHT and player_speed == [1, 1]: 
    #     player_speed = [1, -1]
    # elif player_rect.bottom >= HEIGHT and player_speed == [-1, 1]:
    #     player_speed = [-1, -1]
    # elif  player_rect.right >= WIDHT and player_speed == [1, 1]:
    #     player_speed = [-1, 1]  
    # elif  player_rect.right >= WIDHT and player_speed == [1, -1]:
    #     player_speed = [-1, -1] 
    # elif player_rect.left <= 0 and player_speed == [-1, 1]:
    #     player_speed = [1, 1]
    # elif player_rect.left <= 0 and player_speed == [-1, -1]:
    #     player_speed = [1, -1]
    # elif player_rect.top <= 0 and player_speed == [-1, -1]:
    #     player_speed = [-1, 1]
    # elif player_rect.top <= 0 and player_speed == [1, -1]:
    #     player_speed = [1, 1]

    # # Другий варіант пересування
    # if player_rect.bottom >= HEIGHT: 
    #     player_speed[1] = player_speed[1] * -1
    # elif player_rect.right >= WIDHT:
    #     player_speed[0] = player_speed[0] * -1
    # elif player_rect.left <= 0 and player_speed[0] == -1:
    #     player_speed[0] = player_speed[0] * -1 
    # elif player_rect.top <= 0 and player_speed[1] == -1:
    #     player_speed[1] = player_speed[1] * -1

    # # Третій варіант пересування (Рандомне пересування кубика)
    # if player_rect.bottom >= HEIGHT:
    #     player_speed = random.choice(([1, -1], [-1, -1]))
    # if player_rect.top <= 0:
    #     player_speed = random.choice(([-1, 1], [1, 1]))
    # if player_rect.right >= WIDHT:
    #     player_speed = random.choice(([-1, -1], [-1, 1]))
    # if player_rect.left <= 0:
    #     player_speed = random.choice(([1, 1], [1, -1]))

    # Пересування клавішамив
    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
    elif keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
    elif keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)
    elif keys[K_RIGHT] and player_rect.right < WIDHT:
        player_rect = player_rect.move(player_move_right)
   
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
         print("Boom")
    
    for gift in gifts:
        gift[1] = gift[1].move(gift[2])
        main_display.blit(gift[0], gift[1])

        if player_rect.colliderect(gift[1]):
            print("Yepp")

    # enemy_rect = enemy_rect.move(enemy_move)
    # gift_rect = gift_rect.move(gift_move)
    
    
    main_display.blit(player, player_rect)
    # main_display.blit(enemy, enemy_rect)
    # main_display.blit(gift, gift_rect)
    
    # player_rect = player_rect.move(player_speed)

    print(len(enemies))
    print(len(f"gifts {gifts}"))

    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
            
    for gift in gifts:
        if gift[1].bottom > 800:
            gifts.pop(gifts.index(gift))
    