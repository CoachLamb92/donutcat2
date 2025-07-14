import pygame
import time
import sys
from game_objects import Player, Window, Border, Player, Enemy, Token
from game_over import game_over

def game_state():

    clock = pygame.time.Clock()
    pygame.font.init()
    pygame.init()
    start_time = time.time()
    multi_time = start_time

    # Window stuff
    my_window = Window(1000, 500, (0, 0, 0))
    border = Border(my_window, 2, (255, 255, 255))
    window = pygame.display.set_mode((my_window.get_width(), my_window.get_height()))
    pygame.display.set_caption("DonutCat 2!")

    # Game objects
    player = Player(my_window)
    token = Token(border)
    enemy = Enemy(my_window, border)

    # Game stuff
    run = True
    duration = 0
    time_limit = 120
    multiplier = 1
    global score
    score = 0
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.mouse.set_visible(False)

    while run and duration < time_limit:
        duration = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        if any([player.token_collection(position) for position in token.get_border_coords()]):
            # Time at level computed
            time_span = (time.time() - multi_time)
            # Reset starting time for next level
            multi_time = time.time()
            # Score updated
            score += int(time_span * multiplier * 1000)
            multiplier += 1
            if multiplier % 5 == 1:
                enemy.reset_velocity()
                enemy.increase_radius()
            else:
                enemy.increase_velocity()            
            token.generate_token()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.get_x() > my_window.get_width()/10 + (player.get_radius() + border.get_thickness()):
            player.update_x("left")

        if keys[pygame.K_RIGHT] and player.get_x() < 9*my_window.get_width()/10 - (player.get_radius() + border.get_thickness()):
            player.update_x("right")

        if keys[pygame.K_UP] and player.get_y() > my_window.get_height()/10 + (player.get_radius() + border.get_thickness()):
            player.update_y("up")

        if keys[pygame.K_DOWN] and player.get_y() < 9*my_window.get_height()/10 - (player.get_radius() + border.get_thickness()):
            player.update_y("down")

        enemy.movement()

        # Put this as a game function later
        x_diff_sq = (enemy.get_x()-player.get_x())**2
        y_diff_sq = (enemy.get_y()-player.get_y())**2
        if (x_diff_sq + y_diff_sq)**0.5 < (enemy.get_radius() + player.get_radius()):
            run = False

        # Put the below as a game function later
        window.fill(my_window.get_colour())
        pygame.draw.circle(window, player.get_colour(), player.get_position(), player.get_radius())
        pygame.draw.circle(window, enemy.get_colour(), enemy.get_position(), enemy.get_radius())
        pygame.draw.rect(window, border.get_colour(), border.get_rect(), border.get_thickness())
        pygame.draw.rect(window, token.get_colour(), token.get_token())
        score_text = my_font.render(f"Score: {score}", False, (255, 255, 255))
        time_text = my_font.render(f"Time remaining: {120-duration:.2f}", False, (255, 255, 255))
        window.blit(score_text, (0,0))
        window.blit(time_text, (770,0))
        pygame.display.flip()

        clock.tick_busy_loop(600)
    time_span = (time.time() - multi_time)
    score += int(time_span * multiplier * 1000)
    game_over(score)

if __name__ == "__main__":
    game_state()