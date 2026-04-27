import pygame, random

pygame.init()
dis_width, dis_height = 600, 400
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

def gameLoop():
    x1, y1 = 300, 200
    x1_c, y1_c = 0, 0
    snake_List = []
    Length = 1
    score, speed = 0, 10
    food_weight = 1
    
    FOOD_TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(FOOD_TIMER, 5000) 

    def gen_food():
        return round(random.randrange(0, 580)/20)*20, round(random.randrange(0, 380)/20)*20

    fx, fy = gen_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            if event.type == FOOD_TIMER: 
                fx, fy = gen_food()
                food_weight = random.choice([1, 1, 3]) 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_c, y1_c = -20, 0
                elif event.key == pygame.K_RIGHT: x1_c, y1_c = 20, 0
                elif event.key == pygame.K_UP: x1_c, y1_c = 0, -20
                elif event.key == pygame.K_DOWN: x1_c, y1_c = 0, 20

        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0: gameLoop()
        
        x1 += x1_c; y1 += y1_c
        dis.fill((255, 255, 255))
        
        f_col = (0, 255, 0) if food_weight == 1 else (255, 165, 0)
        pygame.draw.rect(dis, f_col, [fx, fy, 20, 20])
        
        head = [x1, y1]
        snake_List.append(head)
        if len(snake_List) > Length: del snake_List[0]
        
        for x in snake_List: pygame.draw.rect(dis, (0,0,0), [x[0], x[1], 20, 20])
        dis.blit(font.render(f"Score: {score}", True, (0,0,0)), [0, 0])
        
        if x1 == fx and y1 == fy:
            score += food_weight; Length += 1; fx, fy = gen_food()
            food_weight = random.choice([1, 1, 3])
            pygame.time.set_timer(FOOD_TIMER, 5000) 

        pygame.display.update()
        clock.tick(speed)

gameLoop()