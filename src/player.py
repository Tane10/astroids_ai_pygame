import logging

from projectiles import Projectiles
from assets_loader import get_player_textures
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    def __init__(self) -> None:
        self.texture = get_player_textures()
        self.speed = 4
        self.rect = self.texture.get_rect()
        self.pos = [100, 100]
        self.inputs = {'left': False, 'right': False, 'up': False, 'down': False, "fire": False}
        # self.projectiles = np.empty((0,2), int) # creates a [[pos_x,pos_y]]
        # self.screen = screen
        self.projectiles = Projectiles()

    def fire_project(self):
        if self.inputs["fire"]:
            logging.debug('Debug message: Game is running')
            print('Debug message: Game is running')

        self.projectiles.fire_projectiles()
            # new_projectile = np.array([[self.pos[0] + 25, self.pos[1]]])
            # self.projectiles = np.append(self.projectiles,new_projectile,axis=0)
            # print(f"projectilesL {new_projectile}")
            # print(f"All Projectails {self.projectiles }")

    # def update_projectiles(self):
    #     if len(self.projectiles) > 0:
    #         self.projectiles[:, 0] += 5
    #
    # def draw_projectiles(self):
    #     if len(self.projectiles) != 0:
    #         self.screen.blit(self.bullet_texture, self.projectiles[0])
    #
    # def handle_logic(self):
    #     self.fire_project()
    #     self.draw_projectiles()
    #     self.update_projectiles()