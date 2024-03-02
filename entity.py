from sprite import Sprite
from pygame_wrapper import PygameWrapper as pw

class Entity(Sprite):
    colliosion_rect = None

    def __init__(self, image, x = 0, y = 0, w = 0, h = 0):
        super().__init__(image, x, y, w, h)
        self.colliosion_rect = pw.get_pygame().Rect(self.x, self.y, self.w, self.h)

    def __init__(self, sprite, x = 0, y = 0, w = 0, h = 0):
        super().__init__(sprite.image, x, y, w, h)
        self.colliosion_rect = pw.get_pygame().Rect(self.x, self.y, self.w, self.h)

    def draw_collision_rect(self):
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.topleft), (self.colliosion_rect.topright), 1)
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.topright), (self.colliosion_rect.bottomright), 1)
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.bottomright), (self.colliosion_rect.bottomleft), 1)
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.bottomleft), (self.colliosion_rect.topleft), 1)
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.topleft), (self.colliosion_rect.bottomright), 1)
        pw.get_pygame().draw.line(pw.get_surface(), (255, 0, 0), (self.colliosion_rect.topright), (self.colliosion_rect.bottomleft), 1)

    def resize(self, w, h):
        super().resize(w, h)
        self.colliosion_rect = pw.get_pygame().Rect(self.x, self.y, self.w, self.h)

    def update(self, delta_time):
        pass

    def recaludate_collision_rect(self):
        self.colliosion_rect = pw.get_pygame().Rect(self.x, self.y, self.w, self.h)


