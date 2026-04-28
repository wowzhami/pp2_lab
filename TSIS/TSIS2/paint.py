from tools import flood_fill
import pygame, datetime, math

pygame.init()
screen = pygame.display.set_mode((800, 600))
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))
clock = pygame.time.Clock()

colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
color, mode, brush_size = (0, 0, 0), 'pencil', 2

start_pos = None
last_pos = None 
text_active = False
text_content = ""
text_pos = (0, 0)
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.blit(canvas, (0, 0))
    
    if start_pos and pygame.mouse.get_pressed()[0]:
        curr = pygame.mouse.get_pos()
        if mode == 'line':
            pygame.draw.line(screen, color, start_pos, curr, brush_size)
        elif mode == 'rect':
            pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], curr[0]-start_pos[0], curr[1]-start_pos[1]), brush_size)

    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i*35, 10, 30, 30))
        if color == c: 
            pygame.draw.rect(screen, (150, 150, 150), (10 + i*35, 10, 30, 30), 2)

    if text_active:
        txt_surf = font.render(text_content + "|", True, color)
        screen.blit(txt_surf, text_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if text_active:
                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text_content, True, color), text_pos)
                    text_active = False
                    text_content = ""
                elif event.key == pygame.K_ESCAPE: 
                    text_active = False
                    text_content = ""
                elif event.key == pygame.K_BACKSPACE: 
                    text_content = text_content[:-1]
                else: 
                    text_content += event.unicode
            else:
                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    pygame.image.save(canvas, f"paint_{now}.png")
                if event.key == pygame.K_p: mode = 'pencil'
                if event.key == pygame.K_l: mode = 'line'
                if event.key == pygame.K_f: mode = 'fill'
                if event.key == pygame.K_t: mode = 'text'
                if event.key == pygame.K_r: mode = 'rect'
                if event.key == pygame.K_1: brush_size = 2
                if event.key == pygame.K_2: brush_size = 5
                if event.key == pygame.K_3: brush_size = 10

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] < 50: 
                idx = (event.pos[0] - 10) // 35
                if 0 <= idx < len(colors): color = colors[idx]
            elif mode == 'fill':
                flood_fill(canvas, *event.pos, color)
            elif mode == 'text':
                text_active = True
                text_pos = event.pos
            else:
                start_pos = event.pos
                last_pos = event.pos

        if event.type == pygame.MOUSEMOTION:
            if start_pos and pygame.mouse.get_pressed()[0]:
                if mode == 'pencil':
                    pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                    last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos
                if mode == 'line':
                    pygame.draw.line(canvas, color, start_pos, end_pos, brush_size)
                elif mode == 'rect':
                    pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), brush_size)
                start_pos = None

    pygame.display.flip()
    clock.tick(60)

pygame.quit()