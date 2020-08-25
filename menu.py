#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from buttons import Button
from pygame.sprite import Group, Sprite
from pygame.font import Font
from pygame import Surface, event, mouse 
from pygame import QUIT, KEYDOWN, K_SPACE, K_ESCAPE
from pygame.image import load
from pygame.display import update

X_1 = 60
X_2 = 70
Y_1 = 200
Y_2 = 250
WIDTH_1 = 500
WIDTH_2 = 480
HEIGHT = 40

class Menu():
    def __init__(self):
        self.font = Font(None, 50)
        self.output = ["MAIN menu", "PRESS Space or CLICK with Mouse to PLAY", "PRESS ESC or CLICK with Mouse to QUIT"] 

        
    def main(self, window, screen, image_1, image_2):
        done = True
        progamm_done = True
        btnGroup = Group()
        btn_1 = Button(X_1, Y_1, WIDTH_1, HEIGHT, text_size = 34, text = self.output[1])
        btn_2 = Button(X_2, Y_2, WIDTH_2, HEIGHT, text_size = 34, text = self.output[2])
        btnGroup.add(btn_1)
        btnGroup.add(btn_2)
        self.image_1 = load(image_1)
        self.image_2 = load(image_2)
        while done and progamm_done:
            for e in event.get():
                if e.type == QUIT:
                    progamm_done = False
                if e.type == KEYDOWN and e.key == K_SPACE:
                    done = False
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    progamm_done = False
            #screen.fill((255, 20, 50))
            screen.blit(self.image_1, (0,0))
            screen.blit(self.image_2, (190, 300))
            
            if mouse.get_pressed() == (1, 0, 0):
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
            update()
        return progamm_done
