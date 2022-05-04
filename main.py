#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard modules
from enum import Enum
import random
import os
import math

# Project modules
from bird import Bird
from block import Block
from menu import Menu
from background import Background
from enemy import Enemy

# Third-party modules
import neat
from pygame import (
    Surface, event, mouse, mixer,
    QUIT, KEYDOWN, K_SPACE, K_ESCAPE
)
from pygame.sprite import Group, spritecollideany
from pygame.font import Font
from pygame.display import update, set_mode, set_caption
from pygame.time import Clock

WIN_HEIGHT = 450
WIN_WIDHT = 640
NUM_OF_BIRDS = 15
best_score = 0
generation = 0


class Directions(Enum):
    up = 0
    down = 1
    right = 2
    left = 3


def remove(index):
    birds.pop(index)
    ge.pop(index)
    nets.pop(index)


def distance(pos_a, pos_b):
    dx = pos_a[0] - pos_b[0]
    dy = pos_a[1] - pos_b[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def eval_genomes(genomes, config):
    global best_score, birds, obstacles_group, ge, nets, window, screen, generation

    generation += 1
    print(f"The {generation} generation of birds!")

    score_font = Font("fonts/freesansbold.ttf", 50)
    scores_screen = Surface((640, 50))
    current_score = 0
    # TODO: compute current score
    done = False
    timer = Clock()

    seed = []
    for i in range(4):
        seed.append(random.randint(0, 50))

    obstacles_group = Group()
    obstacles_group.add(Block(640, Directions.up, seed[0]))
    obstacles_group.add(Block(640, Directions.down, seed[0]))
    obstacles_group.add(Block(840, Directions.up, seed[1]))
    obstacles_group.add(Block(840, Directions.down, seed[1]))
    obstacles_group.add(Block(1040, Directions.up, seed[2]))
    obstacles_group.add(Block(1040, Directions.down, seed[2]))
    obstacles_group.add(Block(1240, Directions.up, seed[3]))
    obstacles_group.add(Block(1240, Directions.down, seed[3]))
    # obstacles_group.add(Enemy(1240))

    birds = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        birds.append(Bird(80, 120))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    mixer.init()
    mixer.pre_init(44100, -16, 1, 600)
    mixer.music.load("bird/music/music.ogg")
    mixer.music.play(-1)

    while not done:
        for e in event.get():
            if e.type == QUIT:
                done = True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                for bird in birds:
                    bird.end = True
                done = True

        background = Background("bird/background_2.png", (0, 0))
        background.draw(screen)
        scores_screen.fill((50, 50, 50))

        obstacles_group.update()
        obstacles_group.draw(screen)
        for bird in birds:
            bird.update()
            bird.draw(screen)

        if len(birds) == 0:
            done = True

        # TODO: Correct remove. After removing, the next bird after removed bird skipped and hasn't been checked!
        for i, bird in enumerate(birds):
            col = spritecollideany(bird, obstacles_group)
            if col is not None or bird.end is True:
                bird.end = True
                ge[i].fitness -= 10
                remove(i)
            else:
                ge[i].fitness += 5

        obstacles = obstacles_group.sprites()
        for bird in birds:
            for obstacle in obstacles:
                obstacle.per(bird)

        for i, bird in enumerate(birds):
            output = nets[i].activate((bird.rect.y,
                                       distance((bird.rect.x, bird.rect.y),
                                                (obstacles[0].rect.x, obstacles[0].rect.y)),
                                       obstacles[0].rect.y,
                                       obstacles[1].rect.y))
            if output[0] > 0.5:
                bird.up = True
                ge[i].fitness -= 1

        first_member = obstacles[0]
        if first_member.rect.x + 50 < 0:
            if isinstance(first_member, Block):
                seed[0] = random.randint(0, 50)
                obstacles_group.add(Block(first_member.rect.x + 800, Directions.up, seed[0]))
                obstacles_group.add(Block(first_member.rect.x + 800, Directions.down, seed[0]))
                obstacles[0].kill()
                obstacles[1].kill()

            elif isinstance(first_member, Enemy):
                obstacles_group.add(Enemy(first_member.rect.x + 800))
                first_member.kill()

        scores_screen.blit(score_font.render(str(current_score) + "  Best score: " + str(best_score), 1,
                                             (255, 255, 255)), (0, 0))
        window.blit(screen, (0, 50))
        window.blit(scores_screen, (0, 0))
        update()

        timer.tick(35)

    mixer.music.stop()

    if best_score < current_score:
        best_score = current_score
        win = mixer.Sound("bird/music/win.ogg")
        win.play()

    return done


def main():
    global window, screen
    window = set_mode((WIN_WIDHT, WIN_HEIGHT))

    set_caption("Flappy bird")
    screen = Surface((WIN_WIDHT, WIN_HEIGHT))

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    fin = open("score.txt", "r")
    global best_score
    for i in fin:
        best_score = int(i)

    game_menu = Menu()
    while game_menu.main(window, screen, "bird/menu.png", "bird/patterns/skeleton/skeleton-animation_00.png") \
            and run(config_path) is None:
        game_menu = Menu()

    fin.close()
    fout = open("score.txt", "w")
    fout.write(str(best_score))
    fout.close()


# Set up the NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    main()
