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

def get_image(path) -> pygame.Surface:
    if images.get(path) == None:
        load_image(path)
    return images[path]

def get_sprite(path) -> Sprite:
    return Sprite(get_image(path))


def get_images() -> dict:
    return images

def get_image_paths() -> list:
    return list(images.keys())

def get_image_count() -> int:   
    return len(images)


