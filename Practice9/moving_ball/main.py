import pygame

def run_ball():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Moving Ball")
    
    x, y = 400, 300  
    radius = 25
    step = 20        
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if y - step >= radius: y -= step
                if event.key == pygame.K_DOWN:
                    if y + step <= 600 - radius: y += step
                if event.key == pygame.K_LEFT:
                    if x - step >= radius: x -= step
                if event.key == pygame.K_RIGHT:
                    if x + step <= 800 - radius: x += step

        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (x, y), radius)
        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()

if __name__ == "__main__":
    run_ball()