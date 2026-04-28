import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([60, 160, 260, 340]), -100)

class Player(pygame.sprite.Sprite):
    def __init__(self, color_name="blue"):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        colors = {"blue": (0,0,255), "green": (0,255,0), "red": (255,0,0)}
        self.image.fill(colors.get(color_name, (0,0,255)))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
        self.shield = False
        self.oil_timer = 0

    def move(self):
        pressed = pygame.key.get_pressed()
        step = 5 * (-1 if self.oil_timer > 0 else 1)
        if pressed[pygame.K_LEFT] and self.rect.left > 0: self.rect.move_ip(step, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH: self.rect.move_ip(-step, 0)
        if self.oil_timer > 0: self.oil_timer -= 1

class Hazard(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        if type == 'oil': pygame.draw.ellipse(self.image, (50, 50, 50), [0,0,50,30])
        else: self.image.fill((150, 75, 0)) # Pothole
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([60, 160, 260, 340]), -50)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, p_type):
        super().__init__()
        self.type = p_type
        self.image = pygame.Surface((30, 30))
        colors = {'nitro': (255,255,0), 'shield': (0,255,255), 'repair': (255,255,255)}
        self.image.fill(colors[p_type])
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice([60, 160, 260, 340]), -50)
        self.spawn_time = pygame.time.get_ticks()