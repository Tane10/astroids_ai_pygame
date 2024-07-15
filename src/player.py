import sys


class Player:
    def __init__(self, asset_dic) -> None:
        if "pixel_ship.png" not in asset_dic:
            print("Failed to get pixel_ship.png from Assets")
            sys.exit(1)

        self.texture = asset_dic["pixel_ship.png"]
        self.speed = 4
        self.rect = self.texture.get_rect()
        self.pos = [100, 100]
        self.move = {'left': False, 'right': False, 'up': False, 'down': False}


