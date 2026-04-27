import pygame
import datetime
import os

def run_clock():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Mickey's Clock")
    WHITE = (255, 255, 255)

    
    base = os.path.join(os.path.dirname(__file__), 'images')
    
    image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
    hand_l = pygame.image.load(os.path.join(base, 'hand_left_centered.png')).convert_alpha()
    hand_r = pygame.image.load(os.path.join(base, 'hand_right_centered.png')).convert_alpha()

    resized_image = pygame.transform.scale(image_surface, (800, 600))
    hand_l_base = pygame.transform.scale(hand_l, (400, 400)) # Подбери размер под экран
    hand_r_base = pygame.transform.scale(hand_r, (400, 400)) 

    CLOCK_CENTER = (600, 340)
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        now = datetime.datetime.now()
        m = now.minute
        s = now.second

        minutes_angle = - (m * 6) + 90 
        seconds_angle = - (s * 6) + 90

        rotated_minutes = pygame.transform.rotate(hand_r_base, minutes_angle)
        rotated_seconds = pygame.transform.rotate(hand_l_base, seconds_angle)

        minutes_rect = rotated_minutes.get_rect(center=CLOCK_CENTER)
        seconds_rect = rotated_seconds.get_rect(center=CLOCK_CENTER)

        screen.fill(WHITE)
        
        image_rect = resized_image.get_rect(center=CLOCK_CENTER)
        screen.blit(resized_image, image_rect)
        screen.blit(rotated_minutes, minutes_rect) 
        screen.blit(rotated_seconds, seconds_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()