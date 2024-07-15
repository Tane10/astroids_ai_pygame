import pygame
import sys


def input_handler(move_dict):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit(0)

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    pygame.quit()
                    sys.exit(0)

                case pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                case pygame.K_d:
                    move_dict['right'] = True

                case pygame.K_w:
                    move_dict['up'] = True
                    break
                case pygame.K_a:
                    move_dict['left'] = True
                    break
                case pygame.K_s:
                    move_dict['down'] = True
                    break
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_d:
                    move_dict['right'] = False

                case pygame.K_w:
                    move_dict['up'] = False
                    break
                case pygame.K_a:
                    move_dict['left'] = False
                    break
                case pygame.K_s:
                    move_dict['down'] = False
                    break


def move_entity(move_dict, position,speed):
    if move_dict['left']:
        position[0] -= speed
    if move_dict['right']:
        position[0] += speed
    if move_dict['up']:
        position[1] -= speed
    if move_dict['down']:
        position[1] += speed
