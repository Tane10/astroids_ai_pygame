import pygame
import constant

from input_handler import input_handler, move_entity
from enemies import Enemies
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
        pygame.init()
        pygame.display.set_caption("Astroids")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

    def run(self) -> None:
        player = Player(self.screen)
        enemies = Enemies(self.screen)

        while True:
            self.screen.fill('cadetblue')
            self.screen.blit(player.texture, player.pos)


            input_handler(player.inputs)
            move_entity(player)

            player.logic_handler()
            enemies.logic_handler()

            pygame.display.update()
            self.clock.tick(60)
