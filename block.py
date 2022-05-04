#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard modules
import random

# Third-party modules
from pygame.sprite import Sprite
from pygame.image import load

SPEED = 7
WIDTH = 50
PIPE_IMAGES = [
    "bird/pipe_1.png",
    "bird/pipe_2.png"
]


class Block(Sprite):
    def __init__(self, x, direction, seed):
        Sprite.__init__(self)

        self.was = False
        random.seed(seed)
        self.N1 = random.randint(0, 80)
        self.direction = direction
        if direction.name == "up":
            self.image = load(PIPE_IMAGES[0])
            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = - self.N1
        elif direction.name == "down":
            self.image = load(PIPE_IMAGES[1])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 340 - self.N1

    def draw(self, screen):
        if self.direction == 0:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        elif self.direction == 1:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        # if not bird.end:
        self.rect.x -= SPEED

    def per(self, bird):
        if (bird.rect.x > self.rect.x + WIDTH) and not self.was and (self.direction.name == "up"):
            bird.score += 1
            self.was = True
