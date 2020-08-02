#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load

SPEED = 7

class Enemy():
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = random.randrange(0, 450)
        self.image = pygame.image.load("bird/enemy_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.was = False
        self.width_enemy, self.height_enemy = self.image.get_size()
        self.direct_y = random.randrange(-5, 5)


    def draw(self, screen):     
        screen.blit(self.image, (self.x, self.y))
                    

    def update(self, bird):
        if not bird.end:
            self.x -= SPEED
            self.rect.x = self.x
            self.y += self.direct_y
            self.rect.y = self.y
            if self.y + self.height_enemy >= 450 or self.y <0:
                self.direct_y = -self.direct_y
                

    def per(self, bird):
        #the coordinate metod with sprites
        """
        if (bird.x >= self.x and bird.x <= self.x + self.width_enemy) or (bird.x + 40 >= self.x and bird.x + 40 <= self.x + self.width_enemy):
            if not (bird.y > self.y + self.height_enemy or bird.y + 40 < self.y):
                bird.end = True
        if bird.x > self.x + self.width_enemy and not self.was:
            bird.score += 1
            self.was = True
        """
        col = self.rect.colliderect(bird)
        if col:
            bird.end = True
        if bird.x > self.x + self.width_enemy and not self.was:
            bird.score += 1
            self.was = True       
