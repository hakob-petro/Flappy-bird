#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bird import Bird
#from bird import *
from block import *
from menu import *
from background import *
from enemy import *

from pygame.sprite import Group, Sprite
from pygame.font import Font
from pygame import Surface, event, mouse, mixer
from pygame import QUIT, KEYDOWN, K_SPACE, K_ESCAPE
from pygame.image import load
from pygame.display import update, set_mode, set_caption
from pygame.time import Clock

WIN_HEIGHT = 450
WIN_WIDHT = 640

def level(window, screen):
    global best_score
    score_font = Font("fonts/freesansbold.ttf", 50)
    scores_screen = Surface((640, 50))
    done = True
    hero = Bird(80, 120, "bird/red_bird_patern.png") #FlappyBird_1.png")
    timer = Clock()
    b = list()
    b_len = 4
    b_first = 0
    b.append(Block(640))
    b.append(Block(840))
    b.append(Block(1040))
    b.append(Enemy(1290))
    hero.up = True

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
                
        #screen.fill((120, 150, 255))
        #ground = load("bird/ground.png")
        #screen.blit(ground, (0, 430))
        picture = Background("bird/background_2.png", (0,0))
        picture.draw(screen)
        scores_screen.fill((50, 50, 50))
        hero.update()
        for barrier in b:
            barrier.per(hero)
            barrier.update(hero)
            barrier.draw(screen)
        if b[b_first].x + 50 < 0:
            if b_first != 3:
                b[b_first] = Block(b[b_first - 1].x + 200) 
            elif b_first == 3:
                b[b_first] = Enemy(b[b_first - 1].x + 200)
            b_first = (b_first + 1) % b_len   

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
        #mainmenu = Menu()
    fin.close()
    fout = open("score.txt", "w")
    fout.write(str(best_score))
    fout.close()


best_score = 0
if __name__ == "__main__":
    main()
