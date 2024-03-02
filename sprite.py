from pygame_wrapper import PygameWrapper as pw


class Sprite:
    image = None
    x = None
    y = None
    w = None
    h = None

    def __init__(self, image, x = 0, y = 0, w = 0, h = 0):
        self.image = image
        self.x = x
        self.y = y

        self.adjust_size(w, h)

    def adjust_size(self, w, h):
        self.w = w
        self.h = h

        if w == 0 or h == 0:
            self.w = self.image.get_width()
            self.h = self.image.get_height()

        if not self.w == self.image.get_width() or not self.h == self.image.get_height():
            self.image = pw.get_pygame().transform.scale(self.image, (self.w, self.h))

    def draw(self):
        pw.get_surface().blit(self.image, (self.x, self.y))

    def resize(self, w, h):
        self.adjust_size(w, h)

