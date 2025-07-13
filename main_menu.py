import pygame
import sys
from game_objects import Window
from game_state import game_state
from highscores import highscores


def main_menu():
    pygame.font.init()
    pygame.init()

    my_window = Window(1000, 500, (0, 0, 0))
    window = pygame.display.set_mode((my_window.get_width(), my_window.get_height()))
    pygame.display.set_caption("DonutCat 2!")

    width = window.get_width()
    height = window.get_height()
    padding = 10
    box_width = (width-(4*padding))//3
    box_height = height-(2*padding)
    play_game_box = (padding, padding, box_width, box_height)
    highscore_box = ((padding * 2) + box_width, padding, box_width, box_height)
    options_box = ((padding * 3) + (box_width * 2), padding, box_width, box_height)

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    run = True
    pygame.mouse.set_visible(True)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if all([padding <= mouse_x <= padding + box_width, padding <= mouse_y <= padding + box_height]):
                    game_state()
                    run = False
                    sys.exit()
                if all([padding*2 + box_width <= mouse_x <= (padding + box_width) * 2, padding <= mouse_y <= padding + box_height]):
                    highscores()
                    run = False
                    sys.exit()
                if all([padding*3 + box_width*2 <= mouse_x <= (padding + box_width) * 3, padding <= mouse_y <= padding + box_height]):
                    pass

        window.fill(my_window.get_colour())
        pygame.draw.rect(window, (255, 255, 255), play_game_box, 1)
        pygame.draw.rect(window, (255, 255, 255), highscore_box, 1)
        pygame.draw.rect(window, (255, 255, 255), options_box, 1)
        play_game_text = my_font.render("play game", False, (255, 255, 255))
        highscore_text = my_font.render("highscore", False, (255, 255, 255))
        options_text = my_font.render("options", False, (255, 255, 255))
        window.blit(play_game_text, (padding * 2, 20))
        window.blit(highscore_text, ((padding * 3) + box_width, 20))
        window.blit(options_text, ((padding * 4) + (box_width * 2), 20))
        pygame.display.flip()
    
    pygame.quit()
    

if __name__ == "__main__":
    main_menu()