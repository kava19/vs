import pygame
import camera
import logging
from pygame_gui import *
from pygame_gui.elements import *

log = logging.getLogger(__name__)


class PygameWrapper(object):
    global log

    _pygame = None
    _width = None
    _height = None
    _title = None
    _clock = None
    _surface = None
    _window = None
    _ui_manager = None
    _fps = 60.0
    _delta_time = 0.0
    surface_width, surface_height = 32*256, 32*256

    @classmethod
    def get_ui_manager(cls):
        return cls._ui_manager
    @classmethod
    def get_surface(cls):
        return cls._surface


    @classmethod
    def is_key_down(cls, key):
        return cls._pygame.key.get_pressed()[key]
    @classmethod
    def loop(cls, update_callback, render_callback):
        running = True
        while running:
            
            for event in cls._pygame.event.get():
                if event.type == cls._pygame.QUIT:
                    running = False
                elif event.type == cls._pygame.VIDEORESIZE:
                    cls._pygame.display.update()
                    cls.resize_window(event.dict['size'][0], event.dict['size'][1])


            cls._ui_manager.process_events(event)
                    
                    
            cls._ui_manager.update(cls._delta_time)
            update_callback(cls._delta_time)
            render_callback()
            cls._pygame.display.get_surface().blit(cls._surface, (-camera.get_pos()[0], -camera.get_pos()[1]))
            cls._ui_manager.draw_ui(cls._pygame.display.get_surface())
            cls._pygame.display.update()
            frame_time = cls._clock.tick(cls._fps)
            cls._delta_time = frame_time / 1000.0
            

    @classmethod
    def init(cls):
        if cls._pygame is None:
            pygame.init()
            cls._pygame = pygame
            

    @classmethod
    def resize_window(cls, width, height):
        cls._width = width
        cls._height = height
        cls._window = cls._pygame.display.set_mode((width, height), cls._pygame.RESIZABLE)
        log.info("Resized window to %dx%d" % (width, height))

    @classmethod
    def init_window(cls, width, height, title, fps=120):
        if cls._pygame is None:
            cls.init()
        cls._width = width
        cls._height = height
        cls._title = title
        cls._fps = fps
        cls._clock = cls._pygame.time.Clock()
        cls._window = cls._pygame.display.set_mode((width, height), cls._pygame.RESIZABLE)
        cls._pygame.display.set_caption(title)
        cls._surface = pygame.Surface((cls.surface_width, cls.surface_height))
        cls._clock.tick(cls._fps)
        cls._ui_manager= UIManager((width, height), 'quick_theme.json')
        log.info("Created window: %s (%dx%d)" % (title, width, height))

    @classmethod
    def get_pygame(cls):
        return cls._pygame


    @classmethod
    def get_width(cls):
        return cls._width


    @classmethod
    def get_height(cls):
        return cls._height


    @classmethod
    def get_title(cls):
        return cls._title


    @classmethod
    def get_fps(cls):
        return cls._fps


    @classmethod
    def get_dt(cls):
        return cls._delta_time
        
