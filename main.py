from pygame_wrapper import PygameWrapper as pw
import sprite_manager as sm
import logging
from entity import Entity
import camera
import random 
import numpy as np
from player import Player

import pygame
from pygame_gui import *
from pygame_gui.elements import *

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


log = logging.getLogger(__name__)



entity_list = []
player = None
spr = None
bg_tile_map = [None]*256*256
bg_tiles = None

def generate_tilemap():
    global bg_tile_map
    for y in range(0, 256):
        for x in range(0, 256):
            bg_tile_map[y*256 + x] = (1,1)
            rnd = random.randrange(0, 100)
            if rnd < 12:
                bg_tile_map[y*256 + x] = (rnd - 6, 5)
                if rnd < 6:
                    bg_tile_map[y*256 + x] = (rnd, 6)


def update(delta_time):
    for entity in entity_list:
        entity.update(delta_time)



    
    global ui_fps_counter, ui_frame_timer, ui_refresh


    ui_camera_pos.set_text(f"Camera: {camera.get_pos()}")
    if ui_refresh == 0:
        ui_frame_timer.set_text("Frame time: " + str(round(delta_time * 1000, 2)) + "ms")
        ui_fps_counter.set_text("FPS: " + str(round(1 / delta_time, 2)))
        ui_refresh = pw.get_fps()
    ui_refresh -= 1

def render():
    global bg_tile_map, bg_tiles, spr
    tile_draw_range = (int(camera.get_pos()[0] // 32), int(camera.get_pos()[1] // 32))
    for y in range(tile_draw_range[1], tile_draw_range[1] + 16):
        for x in range(tile_draw_range[0], tile_draw_range[0] + 16):
            bg_tiles = sm.get_sprite("Grass.png", bg_tile_map[y*256 + x])
            bg_tiles.set_pos(x * 32, y * 32)
            bg_tiles.draw()

        
    
    for entity in entity_list:
        entity.draw()
        entity.draw_collision_rect()





pw.init_window(800, 600, "vs", 120)

ui_fps_counter = UILabel(pygame.Rect(10,16,200,24),"FPS: 0", pw.get_ui_manager(),object_id='#fps_counter')
ui_frame_timer = UILabel(pygame.Rect(10,32,200,24),"Frame time: 0", pw.get_ui_manager(),object_id='#frame_timer')
ui_camera_pos = UILabel(pygame.Rect(10,48,200,24),f"Camera: {camera.get_pos()}", pw.get_ui_manager(),object_id='#camera')
ui_refresh = pw.get_fps()

generate_tilemap()

spr = Entity(sm.get_sprite("bird.png"), 2700, 2700)
#spr.set_pos(2600, 2600)
spr.resize(64, 64)

player = Player(sm.get_sprite("bird.png"), 2750, 2750, 64, 64)

entity_list.append(spr)
entity_list.append(player)

sm.load_image_tiles("Grass.png", 16, 11, 7, 32)


pw.loop(update, render)


