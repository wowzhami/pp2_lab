import pygame, sys, json, random, os
from db import Database

# Настройки экрана
WIDTH, HEIGHT, CELL = 800, 600, 20
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
db = Database()

def load_settings():
    if not os.path.exists('settings.json'):
        with open('settings.json', 'w') as f: 
            json.dump({"color": [0, 255, 0], "grid": True}, f)
    with open('settings.json', 'r') as f: return json.load(f)

def draw_text(txt, size, pos, color=(255, 255, 255)):
    font = pygame.font.SysFont("Arial", size, bold=True)
    screen.blit(font.render(str(txt), True, color), pos)

def get_input():
    name = ""
    while True:
        screen.fill((50, 50, 50))
        draw_text("TYPE YOUR NAME:", 40, (220, 200))
        draw_text(name + "_", 50, (300, 280), (0, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: return name if name else "Player1"
                elif event.key == pygame.K_BACKSPACE: name = name[:-1]
                else: 
                    if len(name) < 10: name += event.unicode
        pygame.display.flip()

def settings_screen():
    conf = load_settings()
    while True:
        screen.fill((30, 30, 30))
        draw_text("SETTINGS", 40, (320, 50))
        draw_text(f"1. Grid: {'ON' if conf['grid'] else 'OFF'}", 30, (300, 200))
        draw_text("2. Random Snake Color", 30, (300, 260))
        draw_text("Press B to Back", 20, (350, 450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: conf['grid'] = not conf['grid']
                if event.key == pygame.K_2: conf['color'] = [random.randint(50,255) for _ in range(3)]
                if event.key == pygame.K_b:
                    with open('settings.json', 'w') as f: json.dump(conf, f)
                    return
        pygame.display.flip()

def game_loop(user):
    conf = load_settings()
    # Получаем данные из БД (если она жива)
    try:
        p_id = db.get_user_id(user)
        pb = db.get_pb(p_id)
    except:
        p_id, pb = 0, 0

    snake = [[100, 100], [80, 100], [60, 100]]
    direction = [CELL, 0]
    score, level = 0, 1
    
    food = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL]
    poison = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL]
    pw_pos = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL]
    pw_type = random.choice(['SPEED', 'SLOW', 'SHIELD'])
    pw_time = pygame.time.get_ticks()
    
    active_pu, pu_end, obstacles = None, 0, []

    while True:
        now = pygame.time.get_ticks()
        screen.fill((0, 0, 0))
        if conf['grid']:
            for x in range(0, WIDTH, CELL): pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, CELL): pygame.draw.line(screen, (30, 30, 30), (0, y), (WIDTH, y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction[1] == 0: direction = [0, -CELL]
                if event.key == pygame.K_DOWN and direction[1] == 0: direction = [0, CELL]
                if event.key == pygame.K_LEFT and direction[0] == 0: direction = [-CELL, 0]
                if event.key == pygame.K_RIGHT and direction[0] == 0: direction = [CELL, 0]

        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        
        # Столкновения
        if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or 
            new_head in snake or new_head in obstacles):
            if active_pu == 'SHIELD' and now < pu_end: 
                active_pu = None # Щит спасает
            else: 
                try: db.save_game(p_id, score, level)
                except: pass
                return

        snake.insert(0, new_head)
        
        # Еда
        if new_head == food:
            score += 1
            food = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL]
            if score % 5 == 0: 
                level += 1
                if level >= 3: 
                    obstacles.append([random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL])
        
        # Яд
        elif new_head == poison:
            if len(snake) <= 3: return
            snake.pop(); snake.pop(); snake.pop()
            poison = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL]
        
        # Бонус
        elif new_head == pw_pos:
            active_pu, pu_end, pw_pos = pw_type, now + 5000, [-100, -100]
        
        else: 
            snake.pop()

        # Респавн бонуса
        if now - pw_time > 12000:
            pw_pos, pw_type, pw_time = [random.randrange(0, WIDTH//CELL)*CELL, random.randrange(0, HEIGHT//CELL)*CELL], random.choice(['SPEED', 'SLOW', 'SHIELD']), now

        speed = 10 + level
        if active_pu == 'SPEED' and now < pu_end: speed += 10
        if active_pu == 'SLOW' and now < pu_end: speed -= 5

        # Отрисовка
        pygame.draw.rect(screen, (0, 255, 0), (*food, CELL-2, CELL-2))
        pygame.draw.rect(screen, (200, 0, 0), (*poison, CELL-2, CELL-2))
        if now - pw_time < 8000: pygame.draw.rect(screen, (255, 255, 0), (*pw_pos, CELL-2, CELL-2))
        for o in obstacles: pygame.draw.rect(screen, (100, 100, 100), (*o, CELL-2, CELL-2))
        
        for i, b in enumerate(snake):
            color = conf['color'] if i > 0 else (255, 255, 255)
            if active_pu == 'SHIELD' and now < pu_end: color = (0, 200, 255)
            pygame.draw.rect(screen, color, (*b, CELL-2, CELL-2))
        
        draw_text(f"Score: {score} | PB: {pb} | Lvl: {level}", 20, (10, 10))
        pygame.display.flip()
        clock.tick(max(5, speed))

def main_menu():
    user = "Player1"
    while True:
        screen.fill((20, 20, 20))
        draw_text("SNAKE TSIS 4", 50, (250, 100), (0, 255, 0))
        draw_text(f"USER: {user}", 25, (330, 200), (0, 200, 255))
        draw_text("1. Play Game", 30, (320, 280))
        draw_text("2. Leaderboard", 30, (320, 330))
        draw_text("3. Settings", 30, (320, 380))
        draw_text("T. Change Name", 20, (330, 450), (150, 150, 150))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: game_loop(user)
                if event.key == pygame.K_2:
                    try: top = db.get_top()
                    except: top = [("Offline", 0, 0)]
                    screen.fill((0,0,0)); draw_text("TOP 10", 40, (350, 50))
                    for i, r in enumerate(top): draw_text(f"{i+1}. {r[0]}: {r[1]}", 25, (300, 120+i*35))
                    pygame.display.flip(); pygame.time.wait(3000)
                if event.key == pygame.K_3: settings_screen()
                if event.key == pygame.K_t: user = get_input()
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()