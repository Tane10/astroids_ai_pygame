import numpy as np
import pygame.math

import constant
from assets_loader import get_projectiles_textures


class Projectiles:
    def __init__(self, start_pos: pygame.math.Vector2) -> None:
        self.texture = get_projectiles_textures()
        self.rect = self.texture.get_rect()
        self.active = False

        self.pos = np.array(start_pos,dtype=np.float64)
        self.velocity = np.array([10,0], dtype=np.float64)

    def fire(self, start_pos: pygame.math.Vector2) -> None:
        self.pos[:] = start_pos
        self.active = True

    def update(self) -> None:
        if self.active:
            self.pos += self.velocity
        if self.out_bounds():
            self.active = False

    def out_bounds(self):
        return (self.pos[0] < 0 or self.pos[0] > constant.SCREEN_WIDTH or
                self.pos[1] < 0 or self.pos[1] > constant.SCREEN_HEIGHT)
