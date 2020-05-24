#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
from pygame import *

SPEED = 7
WIDTH = 50


class Block():
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y_first = 0
        N1 = random.randrange(170) // 20
        self.N1 =N1
        self.first_height = N1*20 + 20
        self.image_peak = pygame.image.load("bird/peak.png")
        self.image_body = pygame.image.load("bird/body.png")
        self.y_second = self.first_height + 150
        self.second_height = 450 - self.y_second
        N2 = self.second_height // 20
        self.N2 = N2
        self.was = False
        """
        self.x = x
        self.y_first = 0
        self.first_height = random.randrange(170) % 170 + 30
        self.image_first = Surface((WIDTH, self.first_height))
        self.image_first.fill((0, 0, 0))
        self.y_second = self.first_height + 150
        self.second_height = 450 - self.y_second
        self.image_second = Surface((WIDTH, self.second_height))
        self.image_second.fill((0, 0, 0))
        self.was = False
        """

    def draw(self, screen):
            for i in range(self.N1+1):
                screen.blit(self.image_body, (self.x, i*20))
            screen.blit(self.image_peak, (self.x -3, self.N1*20+20))
            screen.blit(self.image_peak, (self.x -3, self.y_second))
            for i in range(self.N2):
                screen.blit(self.image_body, (self.x, self.y_second+i*20+20))
            """
            screen.blit(self.image_first, (self.x, self.y_first))
            screen.blit(self.image_second, (self.x, self.y_second))
            """

    def update(self, bird):
        if not bird.end:
            self.x -= SPEED

    def per(self, bird):
        if (bird.x >= self.x and bird.x <= self.x + WIDTH) or (bird.x + 40 >= self.x and bird.x + 40 <= self.x + WIDTH):
            if not (bird.y > self.first_height and bird.y + 40 < self.y_second):
                bird.end = True
        if bird.x > self.x + WIDTH and not self.was:
            bird.score += 1
            self.was = True
