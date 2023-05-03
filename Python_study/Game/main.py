import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT,  K_RIGHT

pygame.init()

FPS = pygame.time.Clock() 

HEIGHT = 800
WIDHT = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDHT, HEIGHT))

PLAYER_SIZE = (20, 20)
player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

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

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    
    main_display.blit(player, player_rect)
    
    # player_rect = player_rect.move(player_speed)

    pygame.display.flip()