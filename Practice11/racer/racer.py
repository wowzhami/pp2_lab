import pygame, random, sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5
COIN_SCORE = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spawn()
    def spawn(self):
        self.weight = random.choice([1, 1, 1, 5])
        self.image = pygame.Surface((30, 30))
        self.color = (255, 215, 0) if self.weight == 1 else (138, 43, 226)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600: self.spawn()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 400: self.rect.move_ip(5, 0)

P1, E1, C1 = Player(), Enemy(), Coin()
enemies, coins, all_sprites = pygame.sprite.Group(E1), pygame.sprite.Group(C1), pygame.sprite.Group(P1, E1, C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(font.render(f"Score: {COIN_SCORE}", True, (0,0,0)), (280, 10))
    screen.blit(font.render(f"Speed: {SPEED}", True, (0,0,0)), (10, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += C1.weight
        if COIN_SCORE >= 10 and COIN_SCORE % 10 < 5: # Ускоряем каждые 10 очков
            SPEED += 1
        C1.spawn()

    if pygame.sprite.spritecollideany(P1, enemies): pygame.quit(); sys.exit()

    pygame.display.update()
    clock.tick(60)