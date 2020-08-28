#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import Sprite
from pygame.image import load
from pygame import Surface

class Background(Sprite):
    def __init__(self, image_file, location):
        Sprite.__init__(self)
        self.image = load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location
        
    def draw(self, screen):
            screen.blit(self.image, self.location)
            
