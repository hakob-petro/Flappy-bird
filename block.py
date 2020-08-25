#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load


SPEED = 7
WIDTH = 50


class Block(Sprite):
    def __init__(self, x):
        Sprite.__init__(self)
        self.x = x
        self.y_first = 0
        self.N1 = random.randint(0, 80)
        self.image = load("bird/pipe_1.png")
        self.rect_1 = self.image.get_rect()
        self.rect_1.x = x
        self.rect_1.y = - self.N1
        self.image_down = load("bird/pipe_2.png")
        self.rect_2 = self.image.get_rect()
        self.rect_2.x = x
        self.rect_2.y = 340-self.N1
        self.was = False
        
        #the coordinate metod with sprites
        """
        self.N1 = random.randint(0, 20)
        self.first_height = self.N1*20 + 20
        self.image_peak = pygame.image.load("bird/peak.png")
        self.image_peak_rect = self.image_peak.get_rect()
        self.image_body = pygame.image.load("bird/body.png")
        self.image_body_rect = self.image_body.get_rect()
        self.y_second = self.first_height + 150
        self.second_height = 450 - self.y_second
        self.N2 = self.second_height // 20
        """
        #the coordinate metod with surfaces
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
            screen.blit(self.image, (self.x, -self.N1))
            screen.blit(self.image_down, (self.x, 340-self.N1))
            
            #the coordinate metod with sprites
            """
            for i in range(self.N1+1):
                screen.blit(self.image_body, (self.x, i*20))
                
            screen.blit(self.image_peak, (self.x -3, self.N1*20+20))
            screen.blit(self.image_peak, (self.x -3, self.y_second))
            for i in range(self.N2):
                screen.blit(self.image_body, (self.x, self.y_second+i*20+20))
            """
            #the coordinate metod with surfaces
            """
            screen.blit(self.image_first, (self.x, self.y_first))
            screen.blit(self.image_second, (self.x, self.y_second))
            """

    def update(self, bird):
        if not bird.end:
            self.x -= SPEED
        self.rect_1.x = self.rect_2.x = self.x 

    def per(self, bird):
        #the coordinate metod with sprites
        """
        if (bird.x >= self.x and bird.x <= self.x + WIDTH) or (bird.x + 40 >= self.x and bird.x + 40 <= self.x + WIDTH):
            if not (bird.y > self.first_height and bird.y + 40 < self.y_second):
                bird.end = True
        if bird.x > self.x + WIDTH and not self.was:
            bird.score += 1
            self.was = True
        """
        col_1 = self.rect_1.colliderect(bird)
        col_2 = self.rect_2.colliderect(bird)
        if col_1 or col_2:
            bird.end = True
        if bird.x > self.x + WIDTH and not self.was:
            bird.score += 1
            self.was = True
        
        
