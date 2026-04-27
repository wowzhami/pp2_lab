import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint Practice 10")
    
    clock = pygame.time.Clock()
    
    draw_color = (0, 0, 0) 
    mode = 'pencil' 
    start_pos = None
    
    canvas = pygame.Surface((800, 600))
    canvas.fill((255, 255, 255)) 

    running = True
    while running:
        screen.blit(canvas, (0, 0)) 
        
        font = pygame.font.SysFont("Arial", 18)
        mode_text = font.render(f"Mode: {mode} | Press: R-Rect, C-Circle, E-Eraser, P-Pencil", True, (100, 100, 100))
        screen.blit(mode_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'rect'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_e: mode = 'eraser'
                if event.key == pygame.K_p: mode = 'pencil'
                if event.key == pygame.K_1: draw_color = (255, 0, 0) # Красный
                if event.key == pygame.K_2: draw_color = (0, 0, 255) # Синий

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                if mode == 'pencil':
                    pygame.draw.circle(canvas, draw_color, event.pos, 3)

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]: 
                    curr_pos = event.pos
                    if mode == 'pencil':
                        pygame.draw.circle(canvas, draw_color, curr_pos, 3)
                    elif mode == 'eraser':
                        pygame.draw.circle(canvas, (255, 255, 255), curr_pos, 15)

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if mode == 'rect':
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(canvas, draw_color, (start_pos[0], start_pos[1], width, height), 2)
                elif mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, draw_color, start_pos, radius, 2)
                start_pos = None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()