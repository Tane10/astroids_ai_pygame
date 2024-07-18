import pygame
import sys
import constant

from player import Player


def input_handler(input_dict: dict[str,bool]) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit(0)

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q | pygame.K_ESCAPE:
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

def move_entity(entity: Player) -> None:
    # Moving entity
    if entity.inputs['left']:
        entity.pos[0] -= entity.speed
    if entity.inputs['right']:
        entity.pos[0] += entity.speed
    if entity.inputs['up']:
        entity.pos[1] -= entity.speed
    if entity.inputs['down']:
        entity.pos[1] += entity.speed


    # Boundary check and position correction
    if entity.pos.x < 0:
        entity.pos.x = 0
    if entity.pos.x + entity.rect.width > constant.SCREEN_WIDTH:
        entity.pos.x = constant.SCREEN_WIDTH - entity.rect.width
    if entity.pos.y < 0:
        entity.pos.y = 0
    if entity.pos.y + entity.rect.height > constant.SCREEN_HEIGHT:
        entity.pos.y = constant.SCREEN_HEIGHT - entity.rect.height
