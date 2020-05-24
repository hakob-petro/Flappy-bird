#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
from pygame import *

SPEED = 7

class enemy():
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = random.randrange(0, 450)
        #p = random.randrange(0, 1)
        #if p >= 0.5:
        #    self.image_enemy = pygame.image.load("bird/rick.png")
        #elif p < 0.5:
        self.image_enemy = pygame.image.load("bird/enemy.png")
        self.was = False
        self.width_enemy, self.height_enemy = self.image_enemy.get_size()
        self.direct_y = random.randrange(-5, 5)


    def draw(self, screen):     
        screen.blit(self.image_enemy, (self.x, self.y))
                    

    def update(self, bird):
        if not bird.end:
            self.x -= SPEED
            self.y += self.direct_y
            if self.y + self.height_enemy >= 450 or self.y <0:
                self.direct_y = -self.direct_y
                

    def per(self, bird):
        if (bird.x >= self.x and bird.x <= self.x + self.width_enemy) or (bird.x + 40 >= self.x and bird.x + 40 <= self.x + self.width_enemy):
            if not (bird.y > self.y + self.height_enemy or bird.y + 40 < self.y):
                bird.end = True
        if bird.x > self.x + self.width_enemy and not self.was:
            bird.score += 1
            self.was = True

