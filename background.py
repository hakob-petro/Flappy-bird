#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
from pygame import *


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location
        
    def draw(self, screen):
            screen.blit(self.image, self.location)
            

