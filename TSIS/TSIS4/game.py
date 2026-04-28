import pygame
import random

CELL = 20
WIDTH, HEIGHT = 800, 600

class Snake:
    def __init__(self, color):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.dir = [CELL, 0]
        self.color = color
        self.shield = False

    def move(self):
        head = [self.body[0][0] + self.dir[0], self.body[0][1] + self.dir[1]]
        self.body.insert(0, head)
        self.body.pop()

class Food:
    def __init__(self, f_type='normal'):
        self.type = f_type
        self.pos = [0, 0]
        self.timer = pygame.time.get_ticks()
        self.colors = {'normal': (0, 255, 0), 'poison': (139, 0, 0), 'powerup': (255, 255, 0)}

    def spawn(self, forbidden):
        while True:
            self.pos = [random.randrange(1, WIDTH//CELL)*CELL, random.randrange(1, HEIGHT//CELL)*CELL]
            if self.pos not in forbidden: break
        self.timer = pygame.time.get_ticks()

class Obstacle:
    def __init__(self, level):
        self.blocks = []
        if level >= 3:
            for _ in range(level * 3):
                self.blocks.append([random.randrange(1, WIDTH//CELL)*CELL, random.randrange(1, HEIGHT//CELL)*CELL])