import pygame
import time
import sys
import asyncio
import random
import math

async def main():

    clock = pygame.time.Clock()
    pygame.font.init()
    pygame.init()
    start_time = time.time()
    multi_time = start_time

    # Window stuff
    window_height = 500
    window_width = 1000
    background_colour = (0, 0, 0)
    border_thickness = 2
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("My game")

    # Player starting position
    x = window_width/2
    y = window_height/2

    # Player stuff
    player_radius = 7
    player_colour = (255, 255, 255)
    velocity = 0.3

    # Treasure stuff
    token_thickness = 10
    token_x = random.randint(window_width//10 + border_thickness, 9*window_width//10 - (border_thickness + token_thickness))
    token_y = random.randint(window_height//10 + border_thickness, 9*window_height//10 - (border_thickness + token_thickness))
    token_colour = (0, 0, 255)

    # Enemy stuff
    enemy_radius = 7
    enemy_x_a = random.randint(window_width//10 + border_thickness, int(9*x//10) - (border_thickness + token_thickness))
    enemy_x_b = random.randint(window_width//10 + int(x), 9*window_width//10 - (border_thickness + token_thickness))
    enemy_y_a = random.randint(window_height//10 + border_thickness, int(9*y//10) - (border_thickness + token_thickness))
    enemy_y_b = random.randint(window_height//10 + int(y), 9*window_height//10 - (border_thickness + token_thickness))
    enemy_x = random.randint(enemy_x_a, enemy_x_b)
    enemy_y = random.randint(enemy_y_a, enemy_y_b)
    enemy_colour = (255, 0 ,0)


    initial_enemy_movement_angle = math.radians(random.randint(0, 3599)/10)
    enemy_velocity = 0.3
    enemy_x_vel = enemy_velocity * math.cos(initial_enemy_movement_angle)
    enemy_y_vel = enemy_velocity * math.sin(initial_enemy_movement_angle)

    # Game stuff
    run = True
    duration = 0
    time_limit = 120
    multiplier = 1
    score = 0
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    while run and duration < time_limit:
        duration = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        # Determines whether the token and player collide
        player_x_area = set(range(int(x-player_radius), int(x+player_radius)))
        token_x_area = set(range(int(token_x), int(token_x+token_thickness)))
        x_overlap = bool(player_x_area & token_x_area)
        player_y_area = set(range(int(y-player_radius), int(y+player_radius)))
        token_y_area = set(range(int(token_y), int(token_y+token_thickness)))
        y_overlap = bool(player_y_area & token_y_area)
        token_collection = x_overlap and y_overlap

        # If token is "collected"
        if token_collection:
            # Time at level computed
            time_span = (time.time() - multi_time)
            # Reset starting time for next level
            multi_time = time.time()
            # Score updated
            score += time_span * multiplier
            multiplier += 1
            if multiplier % 5 == 1:
                enemy_velocity = 0.3
                enemy_radius += 7
            else:
                enemy_velocity += 0.1
            
            # Token location randomised
            token_x = random.randint(window_width//10 + border_thickness, 9*window_width//10 - (border_thickness + token_thickness))
            token_y = random.randint(window_height//10 + border_thickness, 9*window_height//10 - (border_thickness + token_thickness))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > window_width/10 + (player_radius + border_thickness):
            x -= velocity

        if keys[pygame.K_RIGHT] and x < 9*window_width/10 - (player_radius + border_thickness):
            x += velocity

        if keys[pygame.K_UP] and y > window_height/10 + (player_radius + border_thickness):
            y -= velocity

        if keys[pygame.K_DOWN] and y < 9*window_height/10 - (player_radius + border_thickness):
            y += velocity

        # Enemy Movement
        if enemy_x < (9*window_width//10 - (border_thickness + enemy_radius)) and enemy_x > window_width//10 + border_thickness + enemy_radius:
            enemy_x += enemy_x_vel
        elif enemy_x >= (9*window_width//10 - (border_thickness + enemy_radius)):
            enemy_movement_angle = math.radians(random.randint(901, 2699)/10)
            enemy_x_vel = enemy_velocity * math.cos(enemy_movement_angle)
            enemy_y_vel = enemy_velocity * math.sin(enemy_movement_angle)
            enemy_x += enemy_x_vel
        elif enemy_x <= window_width//10 + border_thickness + enemy_radius:
            enemy_movement_angle = math.radians(random.randint(2701, 4499)/10)
            enemy_x_vel = enemy_velocity * math.cos(enemy_movement_angle)
            enemy_y_vel = enemy_velocity * math.sin(enemy_movement_angle)
            enemy_x += enemy_x_vel
        else:
            print("THIS SHOULD NOT BE REACHED")

        if enemy_y < (9*window_height//10 - (border_thickness + enemy_radius)) and enemy_y > window_height//10 + border_thickness + enemy_radius:
            enemy_y += enemy_y_vel
        elif enemy_y >= (9*window_height//10 - (border_thickness + enemy_radius)):
            enemy_movement_angle = math.radians(random.randint(1801, 3599)/10)
            enemy_x_vel = enemy_velocity * math.cos(enemy_movement_angle)
            enemy_y_vel = enemy_velocity * math.sin(enemy_movement_angle)
            enemy_y += enemy_y_vel
        elif enemy_y <= window_height//10 + border_thickness + enemy_radius:
            enemy_movement_angle = math.radians(random.randint(1, 1799)/10)
            enemy_x_vel = enemy_velocity * math.cos(enemy_movement_angle)
            enemy_y_vel = enemy_velocity * math.sin(enemy_movement_angle)
            enemy_y += enemy_y_vel
        else:
            print("THIS SHOULD NOT BE REACHED")
        
        # Determines whether the enemy and player collide
        enemy_x_area = set(range(int(enemy_x-enemy_radius), int(enemy_x+enemy_radius)))
        enemy_x_overlap = bool(player_x_area & enemy_x_area)
        enemy_y_area = set(range(int(enemy_y-enemy_radius), int(enemy_y+enemy_radius)))
        enemy_y_overlap = bool(player_y_area & enemy_y_area)
        enemy_collision = enemy_x_overlap and enemy_y_overlap

        if enemy_collision:
            run = False

        window.fill(background_colour)
        pygame.draw.circle(window, player_colour, (x, y), player_radius)
        pygame.draw.circle(window, enemy_colour, (enemy_x, enemy_y), enemy_radius)
        pygame.draw.rect(window, player_colour, (window_width/10, window_height/10, 4*window_width/5, 4*window_height/5), border_thickness)
        pygame.draw.rect(window, token_colour, (token_x, token_y, token_thickness, token_thickness))
        text_surface = my_font.render(str(score), False, (255, 255, 255))
        window.blit(text_surface, (0,0))
        pygame.display.flip()

        clock.tick_busy_loop()
        await asyncio.sleep(0)


asyncio.run(main())
