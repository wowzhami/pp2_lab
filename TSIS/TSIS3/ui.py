import pygame

def draw_text(screen, text, size, x, y, color=(0,0,0)):
    font = pygame.font.SysFont("Arial", size, bold=True)
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y, width, height, text, color=(200,200,200)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (0,0,0), self.rect, 2, border_radius=10)
        draw_text(screen, self.text, 25, self.rect.centerx, self.rect.centery)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)