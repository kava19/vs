from entity import Entity
import camera
from pygame_wrapper import PygameWrapper as pw

class Player(Entity):
    speed = 400

    def __init__(self, image, x = 0, y = 0, w = 0, h = 0):
        super().__init__(image, x, y, w, h)

    def __init__(self, sprite, x = 0, y = 0, w = 0, h = 0):
        super().__init__(sprite, x, y, w, h)

    def update(self, delta_time):
        super().update(delta_time)

        if pw.is_key_down(pw.get_pygame().K_LEFT):
            self.x -= self.speed * delta_time
        if pw.is_key_down(pw.get_pygame().K_RIGHT):
            self.x += self.speed * delta_time
        if pw.is_key_down(pw.get_pygame().K_UP):
            self.y -= self.speed * delta_time
        if pw.is_key_down(pw.get_pygame().K_DOWN):
            self.y += self.speed * delta_time

        camera.move_to(self.x - pw.get_width() / 2 + self.w / 2, self.y - pw.get_height() / 2 + self.h / 2)

        self.recaludate_collision_rect()
