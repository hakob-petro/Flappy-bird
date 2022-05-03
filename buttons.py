# -*- coding:utf-8 -*-

# Third-party modules
from pygame import Surface, font
from pygame.sprite import Sprite
from pygame.mouse import get_pos

COLOR = [150, 150, 150]
font.init()


class Button(Sprite):
    def __init__(self, x=0, y=0, width=10, height=10, text='',
                 text_size=0, color=(10, 20, 130)):
        Sprite.__init__(self)

        self.color = color
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text

        if text_size == 0:
            self.font = font.Font(None, width)
        elif text_size > 0:
            self.font = font.Font(None, text_size)

    def update(self):
        if self.mouse_on_button():
            self.image.fill((255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))
            self.image.blit(self.font.render(self.text, True, self.color), (5, 3))
        else:
            self.image.fill(self.color)
            self.image.blit(
                self.font.render(self.text, True, (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])),
                (5, 3))

    def on_click(self, mouse_click=False):
        if self.mouse_on_button() and mouse_click:
            return 1
        return 0

    def mouse_on_button(self):
        mx, my = get_pos()
        if (self.rect.x < mx < self.rect.x + self.rect.width) and (self.rect.y < my < self.rect.y + self.rect.height):
            return 1
        return 0
