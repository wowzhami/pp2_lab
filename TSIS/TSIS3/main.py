import pygame, sys, random
from persistence import load_json, save_json, update_leaderboard
from ui import Button, draw_text
from racer import Player, Enemy, Hazard, PowerUp

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

def get_username():
    name = ""
    while True:
        screen.fill((200, 200, 200))
        draw_text(screen, "ENTER NAME:", 30, 200, 200)
        draw_text(screen, name + "|", 40, 200, 260, (0,0,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name: return name
                elif event.key == pygame.K_BACKSPACE: name = name[:-1]
                else: name += event.unicode
        pygame.display.flip()

def game_loop(name):
    settings = load_json('settings.json', {"sound": True, "color": "blue", "diff": "Medium"})
    player = Player(settings['color'])
    enemies, hazards, powerups = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    
    score, distance, active_pu, pu_timer = 0, 0, None, 0
    base_speed = {"Easy": 3, "Medium": 5, "Hard": 8}[settings['diff']]
    
    while True:
        speed = base_speed + (distance // 1000)
        if active_pu == 'nitro': speed *= 2
        
        screen.fill((100, 100, 100)) # Road
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

        player.move()
        distance += speed / 10
        
        # Spawn logic
        if random.random() < 0.02:
            lane = random.choice([60, 160, 260, 340])
            if abs(lane - player.rect.centerx) > 40:
                r = random.random()
                if r < 0.6: enemies.add(Enemy()); enemies.sprites()[-1].rect.centerx = lane
                elif r < 0.9: hazards.add(Hazard(random.choice(['oil', 'bump']))); hazards.sprites()[-1].rect.centerx = lane
                else: powerups.add(PowerUp(random.choice(['nitro', 'shield', 'repair']))); powerups.sprites()[-1].rect.centerx = lane

        # Updates
        for e in enemies:
            e.rect.move_ip(0, speed)
            if player.rect.colliderect(e.rect):
                if player.shield: player.shield = False; e.kill()
                else: update_leaderboard(name, int(score + distance)); return int(score + distance), int(distance)
        
        for p in powerups:
            p.rect.move_ip(0, speed)
            if player.rect.colliderect(p.rect):
                active_pu = p.type; pu_timer = 300
                if p.type == 'shield': player.shield = True
                if p.type == 'repair': player.oil_timer = 0
                p.kill()

        for h in hazards:
            h.rect.move_ip(0, speed)
            if player.rect.colliderect(h.rect):
                if h.type == 'oil': player.oil_timer = 120
                h.kill()

        if pu_timer > 0: pu_timer -= 1
        else: active_pu = None

        # Drawing
        screen.blit(player.image, player.rect)
        for g in [enemies, hazards, powerups]: g.draw(screen)
        draw_text(screen, f"Score: {int(score+distance)}", 20, 60, 30, (255,255,255))
        if active_pu: draw_text(screen, f"BOOST: {active_pu.upper()}", 20, 300, 30, (255,255,0))
        
        pygame.display.flip()
        clock.tick(60)

def main_menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "RACER TSIS 3", 40, 200, 100)
        btns = [Button(100, 200, 200, 50, "PLAY"), Button(100, 270, 200, 50, "SCORES"), 
                Button(100, 340, 200, 50, "SETTINGS"), Button(100, 410, 200, 50, "QUIT")]
        for b in btns: b.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btns[0].is_clicked(event.pos): 
                    name = get_username()
                    s, d = game_loop(name)
                    # Тут можно вызвать экран Game Over
                if btns[1].is_clicked(event.pos): show_leaderboard()
                if btns[3].is_clicked(event.pos): pygame.quit(); sys.exit()
        pygame.display.flip()

def show_leaderboard():
    scores = load_json('leaderboard.json', [])
    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "TOP 10", 30, 200, 50)
        for i, s in enumerate(scores):
            draw_text(screen, f"{i+1}. {s['name']}: {s['score']}", 20, 200, 100 + i*30)
        btn = Button(100, 500, 200, 50, "BACK")
        btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and btn.is_clicked(event.pos): return
        pygame.display.flip()

if __name__ == "__main__": main_menu()