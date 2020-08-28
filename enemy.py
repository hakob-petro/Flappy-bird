#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load

SPEED = 7

class Enemy(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        self.image = load("bird/enemy_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randrange(0, 450)
        self.was = False
        self.width_enemy, self.height_enemy = self.image.get_size()
        self.direct_y = random.randrange(-5, 5)


    def draw(self, screen):     
        screen.blit(self.image, (self.rect.x, self.rect.y))
                    

    def update(self, bird):
        if not bird.end:
            self.rect.x -= SPEED
            self.rect.y += self.direct_y 
            if self.rect.y + self.height_enemy >= 450 or self.rect.y <0:
                self.direct_y = -self.direct_y
                

    def per(self, bird):
        if bird.rect.x > self.rect.x + self.width_enemy and not self.was:
            bird.score += 1
            self.was = True       
