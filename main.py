from pygame_wrapper import PygameWrapper as pw
import sprite_manager as sm
import logging
from entity import Entity
import camera

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

spr = None



def update(delta_time):

    
    global ui_fps_counter, ui_frame_timer, ui_refresh


    ui_camera_pos.set_text(f"Camera: {camera.get_pos()}")
    if ui_refresh == 0:
        ui_frame_timer.set_text("Frame time: " + str(round(delta_time * 1000, 2)) + "ms")
        ui_fps_counter.set_text("FPS: " + str(round(1 / delta_time, 2)))
        ui_refresh = pw.get_fps()
    ui_refresh -= 1

def render():
    spr.draw()
    spr.draw_collision_rect()




pw.init_window(800, 600, "vs", 120)

ui_fps_counter = UILabel(pygame.Rect(10,16,200,24),"FPS: 0", pw.get_ui_manager(),object_id='#fps_counter')
ui_frame_timer = UILabel(pygame.Rect(10,32,200,24),"Frame time: 0", pw.get_ui_manager(),object_id='#frame_timer')
ui_camera_pos = UILabel(pygame.Rect(10,48,200,24),f"Camera: {camera.get_pos()}", pw.get_ui_manager(),object_id='#camera')
ui_refresh = pw.get_fps()

spr = Entity(sm.get_sprite("bird.png"), 2700, 2700)
#spr.set_pos(2600, 2600)
spr.resize(64, 64)

pw.loop(update, render)


