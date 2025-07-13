import pygame
import sys

from game_objects import Window, Highscore_Table

def highscores():
    pygame.init()
    pygame.font.init()

    my_window = Window(1000, 500, (0, 0, 0))
    window_width = my_window.get_width()
    window_height = my_window.get_height()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("DonutCat 2!")

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    ht = Highscore_Table()

    main_menu_button_box = (7*window_width//10, 20, 5*window_width//20, (window_width/10)-40)

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
                if all([7*window_width//10 <= mouse_x <= 19*window_width//20, 20 <= mouse_y <= (window_width/10)-20]):
                    run = False
                    from main_menu import main_menu
                    main_menu()
                    sys.exit()

        window.fill(my_window.get_colour())
        highscore_title = my_font.render("Highscores", False, (255, 255, 255))
        window.blit(highscore_title, (100, 20))
        pygame.draw.rect(window, (50, 50, 50), main_menu_button_box)
        button_text = my_font.render("Main Menu", False, (255, 255, 255))
        window.blit(button_text, (77*window_width//100, 40))
        for i in range(10):
            colour = (150, 150, 150)
            if i%2 == 1: colour = (50, 50, 50)
            this_rect = (5*window_width//100, (i*8*window_height//100)+(15*window_height//100), 90*window_width//100, 8*window_height//100)
            pygame.draw.rect(window, colour, this_rect)
            highscores = ht.get_highscores()
            if len(highscores) > i:
                player_text = my_font.render(highscores[i]["Player"], False, (255, 255, 255))
                score_text = my_font.render(str(highscores[i]["Score"]), False, (255, 255, 255))
                window.blit(player_text, (15*window_width//100, (i*8*window_height//100)+(15*window_height//100)+10))
                window.blit(score_text, (65*window_width//100, (i*8*window_height//100)+(15*window_height//100)+10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    highscores()