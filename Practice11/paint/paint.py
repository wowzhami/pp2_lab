import pygame, math

pygame.init()
screen = pygame.display.set_mode((800, 600))
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))
clock = pygame.time.Clock()
mode, color, start_pos = 'pencil', (0, 0, 0), None

while True:
    screen.blit(canvas, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: mode = 'pencil'
            if event.key == pygame.K_e: mode = 'eraser'
            if event.key == pygame.K_s: mode = 'square' # Квадрат
            if event.key == pygame.K_t: mode = 'triangle' # Прямоугольный
            if event.key == pygame.K_f: mode = 'equilateral' # Равносторонний (Задание 11.3)
            if event.key == pygame.K_d: mode = 'rhombus' # Ромб

        if event.type == pygame.MOUSEBUTTONDOWN: start_pos = event.pos
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == 'pencil': pygame.draw.circle(canvas, color, event.pos, 3)
            if mode == 'eraser': pygame.draw.circle(canvas, (255, 255, 255), event.pos, 15)

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == 'square':
                side = abs(end_pos[0] - start_pos[0])
                pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], side, side), 2)
            elif mode == 'triangle':
                pygame.draw.polygon(canvas, color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == 'equilateral':
                side = abs(end_pos[0] - start_pos[0])
                height = side * math.sqrt(3) / 2
                pts = [start_pos, (start_pos[0] + side, start_pos[1]), (start_pos[0] + side/2, start_pos[1] - height)]
                pygame.draw.polygon(canvas, color, pts, 2)
            elif mode == 'rhombus':
                mid_x, mid_y = (start_pos[0]+end_pos[0])/2, (start_pos[1]+end_pos[1])/2
                pts = [(mid_x, start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (start_pos[0], mid_y)]
                pygame.draw.polygon(canvas, color, pts, 2)
    
    pygame.display.flip()
    clock.tick(60)