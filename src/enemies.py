import random

import pygame

import assets_loader
import constant


class Enemies:
    def __init__(self, screen: pygame.Surface | pygame.SurfaceType):
        self.texture = assets_loader.get_enemies()["pixel_ship3_blue.png"]
        self.speed = constant.SPEED
        self.rect = self.texture.get_rect()
        self.pos = pygame.math.Vector2(300,300)
        # self.projectiles = [Projectiles(start_pos=self.pos) for _ in range(0,10)]
        self.screen = screen


    #
    # def __set_texture__(self):
    #     asset_len = len(self.opt_textures)
    #     self.texture = list(self.opt_textures.values())[random.randint(0, asset_len -1)]
    #     self.rect = self.texture.get_rect()


    def draw_entity(self):
        self.screen.blit(self.texture, self.pos)

    def logic_handler(self):
        self.draw_entity()

