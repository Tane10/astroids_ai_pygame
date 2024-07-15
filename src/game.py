import pygame
import os

from input_handler import input_handler, move_entity
from player import Player
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
    def __init__(self) -> None:
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        pygame.init()
        pygame.display.set_caption("Astroids")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.assets_dict = {}

    def __load_assets(self):
        folder_path = os.path.join(os.path.dirname(__file__), '..', 'assets')
        for filename in os.listdir(folder_path):
            if filename.endswith('.png'):
                texture_path = os.path.join(folder_path,filename)
                texture = pygame.image.load(texture_path)
                self.assets_dict[filename] = texture

    def run(self) -> None:
        self.__load_assets()
        player = Player(self.assets_dict)

        while True:
            self.screen.fill('aqua')
            self.screen.blit(player.texture, player.pos)
            input_handler(player.inputs)
            move_entity(player.inputs, player.pos, player.speed )

            pygame.display.update()
            self.clock.tick(60)
