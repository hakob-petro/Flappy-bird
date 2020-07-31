#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame import *
from buttons import Button
from pygame import mouse

X_1 = 60
X_2 = 70
Y_1 = 200
Y_2 = 250
WIDTH_1 = 500
WIDTH_2 = 480
HEIGHT = 40

class Menu():
    def __init__(self):
        self.font = pygame.font.Font(None, 50)
        self.output = ["MAIN menu", "PRESS Space or CLICK with Mouse to PLAY", "PRESS ESC or CLICK with Mouse to QUIT"] 

        
    def main(self, window, screen, image_1, image_2):
        done = True
        progamm_done = True
        btnGroup = pygame.sprite.Group()
        btn_1 = Button(X_1, Y_1, WIDTH_1, HEIGHT, text_size = 34, text = self.output[1])
        btn_2 = Button(X_2, Y_2, WIDTH_2, HEIGHT, text_size = 34, text = self.output[2])
        btnGroup.add(btn_1)
        btnGroup.add(btn_2)
        self.image_1 = pygame.image.load(image_1)
        self.image_2 = pygame.image.load(image_2)
        while done and progamm_done:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    progamm_done = False
                if e.type == KEYDOWN and e.key == K_SPACE:
                    done = False
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    progamm_done = False
            #screen.fill((255, 20, 50))
            screen.blit(self.image_1, (0,0))
            screen.blit(self.image_2, (190, 300))
            
            if pygame.mouse.get_pressed() == (1, 0, 0):
                mouse_click = True
            else:
                mouse_click = False

            #отображение кнопок
            btnGroup.update()
            btnGroup.draw(screen)
            
            if btn_1.onClick(mouse_click):
                done = False
            elif btn_2.onClick(mouse_click):
                programm_done = False

            screen.blit(self.font.render(self.output[0], 1, (255, 255, 255)), (220, 100))
            window.blit(screen, (0, 0))
            pygame.display.update()
        return progamm_done
