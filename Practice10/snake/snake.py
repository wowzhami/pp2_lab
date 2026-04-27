import pygame
import time
import random

pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Размеры окна
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game Practice 10')

clock = pygame.time.Clock()
snake_block = 20
font_style = pygame.font.SysFont("bahnschrift", 25)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    
    # Начальные параметры
    score = 0
    level = 1
    snake_speed = 10

    # Генерация еды (чтобы не на змейке)
    def generate_food():
        while True:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            if [foodx, foody] not in snake_List:
                return foodx, foody

    foodx, foody = generate_food()

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Ты проиграл! Q-Выход или C-Играть снова", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # ПРОВЕРКА ГРАНИЦ (Задание 10.2)
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка столкновения с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        
        # Счётчики на экране
        score_txt = font_style.render(f"Score: {score}", True, black)
        level_txt = font_style.render(f"Level: {level}", True, black)
        dis.blit(score_txt, [0, 0])
        dis.blit(level_txt, [dis_width - 100, 0])

        pygame.display.update()

        # Если съел еду
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1
            score += 1
            
            # ПОВЫШЕНИЕ УРОВНЯ (Задание 10.2)
            # Каждые 3 еды повышаем уровень и скорость
            if score % 3 == 0:
                level += 1
                snake_speed += 3

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()