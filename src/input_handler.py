import pygame
import sys


def input_handler(input_dict) -> None:
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
                    input_dict['right'] = True
                    break
                case pygame.K_w:
                    input_dict['up'] = True
                    break
                case pygame.K_a:
                    input_dict['left'] = True
                    break
                case pygame.K_s:
                    input_dict['down'] = True
                    break
                case pygame.K_SPACE:
                    input_dict['fire'] = True
                    break
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_d:
                    input_dict['right'] = False
                    break
                case pygame.K_w:
                    input_dict['up'] = False
                    break
                case pygame.K_a:
                    input_dict['left'] = False
                    break
                case pygame.K_s:
                    input_dict['down'] = False
                    break
                case pygame.K_SPACE:
                    input_dict['fire'] = False
                    break


def move_entity(input_dict, position,speed) -> None:
    if input_dict['left']:
        position[0] -= speed
    if input_dict['right']:
        position[0] += speed
    if input_dict['up']:
        position[1] -= speed
    if input_dict['down']:
        position[1] += speed
