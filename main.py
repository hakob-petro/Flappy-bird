#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bird import Bird
#from bird import *
from block import *
from menu import *
from background import *
from enemy import *

from pygame.sprite import Sprite, Group, spritecollideany
from pygame.font import Font
from pygame import Surface, event, mouse, mixer
from pygame import QUIT, KEYDOWN, K_SPACE, K_ESCAPE
from pygame.image import load
from pygame.display import update, set_mode, set_caption
from pygame.time import Clock
from enum import Enum
import random

WIN_HEIGHT = 450
WIN_WIDHT = 640

class directions(Enum):
    up = 0
    down = 1
    right = 2
    left = 3

def level(window, screen):
    global best_score
    score_font = Font("fonts/freesansbold.ttf", 50)
    scores_screen = Surface((640, 50))
    done = True
    hero = Bird(80, 120, "bird/red_bird_patern.png")
    timer = Clock()

    #initial list of seeds
    seed = list()
    seed_len = 3
    seed_first = 0
    for i in range(3):
        seed.append(random.randint(0, 50))
        


    #initialing Group of obstacles
    obgroup = Group()
    obgroup.add(Block(640, directions.up, seed[0]))
    obgroup.add(Block(640, directions.down, seed[0]))
    obgroup.add(Block(840, directions.up, seed[1]))
    obgroup.add(Block(840, directions.down, seed[1]))
    obgroup.add(Block(1040, directions.up, seed[2]))
    obgroup.add(Block(1040, directions.down, seed[2]))
    obgroup.add(Enemy(1240))

    
    #music
    mixer.init()
    mixer.pre_init(44100, -16, 1, 600)
    mixer.music.load("bird/music/music.ogg")
    mixer.music.play(-1)
    
    while done and not hero.end:
        for e in event.get():
            if e.type == QUIT:
                done = False
            if (e.type == KEYDOWN and e.key == K_SPACE) or mouse.get_pressed() == (1, 0, 0):
                hero.up = True
                jump_sound = mixer.Sound("bird/music/jump.ogg")
                jump_sound.play()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                hero.end = True
                done = False
                
        picture = Background("bird/background_2.png", (0,0))
        picture.draw(screen)
        scores_screen.fill((50, 50, 50))
        hero.update()

        col = spritecollideany(hero, obgroup)
        if col is not None:
            hero.end = True
        
        drinks = obgroup.sprites()
        for pepsi in drinks:
            pepsi.per(hero)
        obgroup.update(hero)
        obgroup.draw(screen)
        coca_cola = drinks[0]

        if coca_cola.rect.x + 50 < 0:
            if isinstance(coca_cola, Block):
                seed[seed_first] = random.randint(0,50)
                obgroup.add(Block(coca_cola.rect.x + 800, directions.up, seed[seed_first]))
                obgroup.add(Block(coca_cola.rect.x + 800, directions.down, seed[seed_first]))
                drinks[0].kill()
                drinks[1].kill()
                
            elif isinstance(coca_cola, Enemy):
                obgroup.add(Enemy(coca_cola.rect.x + 800))
                coca_cola.kill()
        
        hero.draw(screen)
        scores_screen.blit(score_font.render(str(hero.score) + "  Best score: " + str(best_score), 1, (255, 255, 255)), (0, 0))
        window.blit(screen, (0, 50))
        window.blit(scores_screen, (0, 0))
        update()

        timer.tick(35)

    if hero.end:
        mixer.music.stop()
    if not hero.end:
        mixer.music.play(-1)
    
    if best_score < hero.score:
        best_score = hero.score
        win = mixer.Sound("bird/music/win.ogg")
        win.play()
    
    return done

 
def main():
    window = set_mode((WIN_WIDHT, WIN_HEIGHT))
    #setting caption for window
    set_caption("Flappy bird")
    screen = Surface((WIN_WIDHT, WIN_HEIGHT))
    fin = open("score.txt", "r")
    global best_score
    for i in fin:
        best_score = int(i)
    print(best_score)
    mainmenu = Menu()
    while mainmenu.main(window, screen, "bird/menu.png", "bird/patterns/skeleton/skeleton-animation_00.png") and level(window, screen):
        pass
    fin.close()
    fout = open("score.txt", "w")
    fout.write(str(best_score))
    fout.close()


best_score = 0
if __name__ == "__main__":
    main()
