from pygame_wrapper import PygameWrapper as pw
from sprite import Sprite
import pygame
import logging
log = logging.getLogger(__name__)

images = {}

def load_image(path) -> None:
    img = pw.get_pygame().image.load(path)
    if img == None:
        log.error("Failed to load image: " + path)
    else:
        log.info("Loaded image: " + path)
        img.set_colorkey((255,0,255))
        img = img.convert_alpha()
        images[path] = img

def load_image_tiles(path, orginal_tile_size, num_tiles_x, num_tiles_y, tile_size) -> None:
    img = pw.get_pygame().image.load(path)
    if img == None:
        log.error("Failed to load image: " + path)
    else:
        log.info("Loaded image: " + path)
        img.set_colorkey((255,0,255))
        img = img.convert_alpha()
        for x in range(num_tiles_x):
            for y in range(num_tiles_y):
                images[path + "_" + str(x) + "_" + str(y)] = pw.get_pygame().transform.scale(img.subsurface(x * orginal_tile_size, y * orginal_tile_size, orginal_tile_size, orginal_tile_size), (tile_size, tile_size))

    

def get_image(path, tile = (-1, -1)) -> pygame.Surface:

    if tile[0] != -1 and tile[1] != -1:
        try:
            tmp = images[path + "_" + str(tile[0]) + "_" + str(tile[1])]
        except:
            log.error("Failed to get image: " + path + "_" + str(tile[0]) + "_" + str(tile[1]) + " tile not found")
            return None
        return tmp
    
    if images.get(path) == None:
        load_image(path)
    return images[path]

def get_sprite(path, tile = (-1, -1)) -> Sprite:
    return Sprite(get_image(path, tile))


def get_images() -> dict:
    return images

def get_image_paths() -> list:
    return list(images.keys())

def get_image_count() -> int:   
    return len(images)


