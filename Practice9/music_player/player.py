import pygame
import os

def run_player():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Madi's Music Player")
    
    # Цвета
    BLACK = (30, 30, 30)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    music_dir = os.path.join(os.path.dirname(__file__), 'music')
    songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    
    if not songs:
        print("Ошибка: В папке music нет песен!")
        return

    current_idx = 0
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_idx]))
    
    font = pygame.font.SysFont("Arial", 24)
    playing = False
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # PLAY
                    pygame.mixer.music.play()
                    playing = True
                elif event.key == pygame.K_s: # STOP
                    pygame.mixer.music.stop()
                    playing = False
                elif event.key == pygame.K_n: # NEXT
                    current_idx = (current_idx + 1) % len(songs)
                    pygame.mixer.music.load(os.path.join(music_dir, songs[current_idx]))
                    pygame.mixer.music.play()
                    playing = True
                elif event.key == pygame.K_b: # BACK (Previous)
                    current_idx = (current_idx - 1) % len(songs)
                    pygame.mixer.music.load(os.path.join(music_dir, songs[current_idx]))
                    pygame.mixer.music.play()
                    playing = True

        screen.fill(BLACK)
        
        text_name = font.render(f"Сейчас играет: {songs[current_idx]}", True, WHITE)
        text_hint = font.render("P: Play | S: Stop | N: Next | B: Back", True, GREEN)
        
        screen.blit(text_name, (50, 100))
        screen.blit(text_hint, (50, 200))
        
        pygame.display.flip()

    pygame.quit()