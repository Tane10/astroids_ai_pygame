import pygame
import constant

from assets_loader import get_player_textures
from projectiles import Projectiles

'''
Bug list:
TODO: fix when you fire it fires X amount of bullets not just one

'''


class Player:
    def __init__(self, screen: pygame.Surface | pygame.SurfaceType) -> None:
        self.texture = get_player_textures()
        self.speed = constant.SPEED
        self.rect = self.texture.get_rect()
        self.pos = pygame.math.Vector2(10,10)
        self.inputs = {'left': False, 'right': False, 'up': False, 'down': False, "fire": False}
        self.projectiles = [Projectiles(start_pos=self.pos) for _ in range(0,10)]
        self.screen = screen


    def fire_projectiles(self)-> None:
        if self.inputs["fire"]:
            for projectile in self.projectiles:
                if not projectile.active:
                    new_pos = pygame.math.Vector2(self.pos.x + 10, self.pos.y)
                    projectile.fire(new_pos)
                    break

    def draw_projectiles(self)-> None:
        for projectile in self.projectiles:
            if projectile.active:
                self.screen.blit(projectile.texture, projectile.pos)

    def update_projectiles(self)-> None:
        for projectiles in self.projectiles:
            projectiles.update()

    def logic_handler(self):
        self.fire_projectiles()
        self.draw_projectiles()
        self.update_projectiles()

