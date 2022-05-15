#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard modules
import os

# Third-party modules
from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load
from pygame.font import Font, SysFont
from pyganim import PygAnimation

SPEED = 0
JUMP = 10
GRAVITY = 1
COLOR = (0, 0, 0)
ANIMATION_DELAY = 30

ANIMATION = [
    os.path.join("bird", "skeleton-animation_00.png"),
    os.path.join("bird", "skeleton-animation_01.png"),
    os.path.join("bird", "skeleton-animation_02.png"),
    os.path.join("bird", "skeleton-animation_03.png"),
    os.path.join("bird", "skeleton-animation_04.png"),
    os.path.join("bird", "skeleton-animation_05.png"),
    os.path.join("bird", "skeleton-animation_06.png"),
    os.path.join("bird", "skeleton-animation_07.png"),
    os.path.join("bird", "skeleton-animation_08.png"),
    os.path.join("bird", "skeleton-animation_09.png"),
    os.path.join("bird", "skeleton-animation_10.png")
    ]


class Bird(Sprite):
    def __init__(self, xpos, ypos, name, color):
        Sprite.__init__(self)

        self.name = name
        self.font = SysFont('Tahoma', 15, False, False)
        self.color = color
        self.yvel = 0
        self.score = 0
        self.up = False
        self.wasup = False
        self.end = False

        x = load(ANIMATION[0])
        h, w = x.get_size()
        self.image = Surface((h, w))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

        self.image.set_colorkey(COLOR)
        animations = []
        for anim in ANIMATION:
            animations.append((anim, ANIMATION_DELAY))
        self.anim = PygAnimation(animations)
        self.anim.play()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.font.render(f"{self.name}", 1, self.color), (self.rect.x + 7, self.rect.y - 25))

    def update(self):
        self.image.fill(COLOR)
        self.anim.blit(self.image, (0, 0))

        if self.up:
            self.yvel = -JUMP
            self.up = False
            self.wasup = True
        elif not self.wasup:
            self.yvel += GRAVITY
        else:
            self.wasup = False

        self.rect.y += self.yvel
        self.rect.x += SPEED
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y >= 400:
            self.end = True
