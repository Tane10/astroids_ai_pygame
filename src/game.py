import pygame
import logging

from input_handler import input_handler, move_entity
from player import Player
from assets_loader import load_assets
# '''
# - [X] import textures
# - get basic movement
# - fire bullet
#
# - collisions
# - enemies
# '''
#


class Game:
    assets_dict = load_assets()

    def __init__(self) -> None:
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        pygame.init()
        pygame.display.set_caption("Astroids")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def run(self) -> None:
        player = Player()

        while True:
            self.screen.fill('black')

            self.screen.blit(player.texture, player.pos)
            input_handler(player.inputs)
            move_entity(player.inputs, player.pos, player.speed)

            # # player.handle_logic()
            # logging.debug('Debug message: Game is running')
            # logging.info('Info message: Game is processing events')
            # logging.warning('Warning message: Something might be wrong')

            pygame.display.update()
            self.clock.tick(60)
