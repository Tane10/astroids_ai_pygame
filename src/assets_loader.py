import os
import pygame

assets_dict = {}

def load_assets() -> dict[str, pygame.Surface | pygame.SurfaceType]:
    folder_path = os.path.join(os.path.dirname(__file__), '..', 'assets')
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            texture_path = os.path.join(folder_path,filename)
            texture = pygame.image.load(texture_path)
            assets_dict[filename] = texture

    return assets_dict

def get_player_textures() -> pygame.Surface | pygame.SurfaceType:
    if "pixel_ship.png" not in assets_dict:
        print("Failed to get pixel_ship.png from Assets")

    return assets_dict["pixel_ship.png"]

def get_projectiles_textures() -> pygame.Surface | pygame.SurfaceType:
    if "pixel_laser_red.png" not in assets_dict:
        print("Failed to get pixel_laser_red.png from Assets")

    return assets_dict["pixel_laser_red.png"]
