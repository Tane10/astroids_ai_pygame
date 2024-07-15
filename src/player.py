import sys
import numpy as np


class Player:
    def __init__(self, asset_dic,screen) -> None:
        if "pixel_ship.png" not in asset_dic:
            print("Failed to get pixel_ship.png from Assets")
            sys.exit(1)

        if "pixel_laser_red.png" not in asset_dic:
            print("Failed to get pixel_laser_red.png from Assets")
            sys.exit(1)

        self.texture = asset_dic["pixel_ship.png"]
        self.speed = 4
        self.rect = self.texture.get_rect()
        self.pos = [100, 100]
        self.inputs = {'left': False, 'right': False, 'up': False, 'down': False, "fire": False}
        self.bullet_texture = asset_dic["pixel_laser_red.png"]
        self.projectiles = np.empty((0,2), int) # creates a [[pos_x,pos_y]]
        self.screen = screen

    def fire_project(self):
        if self.inputs["fire"]:
            new_projectile = np.array([[self.pos[0] + 25, self.pos[1]]])
            self.projectiles = np.append(self.projectiles,new_projectile,axis=0)
            print(f"projectilesL {new_projectile}")
            print(f"All Projectails {self.projectiles }")

    def update_projectiles(self):
        if len(self.projectiles) > 0:
            self.projectiles[:, 0] += 5

    def draw_projectiles(self):
        if len(self.projectiles) != 0:
            self.screen.blit(self.bullet_texture, self.projectiles[0])

    def handle_logic(self):
        self.fire_project()
        self.draw_projectiles()
        self.update_projectiles()