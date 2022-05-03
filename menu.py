#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Third-party modules
from pygame import event, mouse, QUIT, KEYDOWN, K_SPACE, K_ESCAPE
from pygame.sprite import Group
from pygame.font import Font
from pygame.image import load
from pygame.display import update

# Project modules
from buttons import Button

X_1 = 60
X_2 = 70
Y_1 = 200
Y_2 = 250
WIDTH_1 = 500
WIDTH_2 = 480
HEIGHT = 40
FONT_SIZE = 50


class Menu:
    def __init__(self):
        self.image_1 = None
        self.image_2 = None
        self.font = Font(None, FONT_SIZE)
        self.output = [
            "MAIN menu",
            "PRESS Space or CLICK with Mouse to PLAY",
            "PRESS ESC or CLICK with Mouse to QUIT"
        ]

    def main(self, window, screen, image_1, image_2):
        done = True
        progamm_done = True
        self.image_1 = load(image_1)
        self.image_2 = load(image_2)

        btn_group = Group()
        btn_1 = Button(X_1, Y_1, WIDTH_1, HEIGHT, text_size=34, text=self.output[1])
        btn_2 = Button(X_2, Y_2, WIDTH_2, HEIGHT, text_size=34, text=self.output[2])
        btn_group.add(btn_1)
        btn_group.add(btn_2)

        while done and progamm_done:
            for e in event.get():
                if e.type == QUIT:
                    progamm_done = False
                if e.type == KEYDOWN and e.key == K_SPACE:
                    done = False
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    progamm_done = False

            screen.blit(self.image_1, (0, 0))
            screen.blit(self.image_2, (190, 300))

            if mouse.get_pressed() == (1, 0, 0):
                mouse_click = True
            else:
                mouse_click = False

            # Show buttons
            btn_group.update()
            btn_group.draw(screen)

            if btn_1.on_click(mouse_click):
                done = False
            elif btn_2.on_click(mouse_click):
                programm_done = False

            screen.blit(self.font.render(self.output[0], 1, (255, 255, 255)), (220, 100))
            window.blit(screen, (0, 0))
            update()
        return progamm_done
