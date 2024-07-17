from assets_loader import get_projectiles_textures


class Projectiles:
    def __init__(self):
        self.texture = get_projectiles_textures()

    def fire_projectiles(self):
        print("BANG")
        # if self.inputs["fire"]:
        #     new_projectile = np.array([[self.pos[0] + 25, self.pos[1]]])
        #     self.projectiles = np.append(self.projectiles,new_projectile,axis=0)
        #     print(f"projectilesL {new_projectile}")
            # print(f"All Projectails {self.projectiles }")


