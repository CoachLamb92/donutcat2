import pygame
import sys

from game_objects import Window, Border, Highscore_Table

def game_over(score):
    pygame.font.init()
    pygame.init()

    my_window = Window(1000, 500, (0, 0, 0))
    border = Border(my_window, 2, (255, 255, 255))
    window_width = my_window.get_width()
    window_height = my_window.get_height()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("DonutCat 2!")

    my_font = pygame.font.SysFont('Comic Sans MS', 100)
    user_name = ""
    run = True
    pygame.mouse.set_visible(True)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            elif event.type == pygame.KEYDOWN and len(user_name) < 10 and event.key != pygame.K_RETURN:
                user_name += event.unicode
            elif len(user_name) > 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                hs = Highscore_Table()
                hs.update_table({"Player": user_name, "Score":score})
                hs.save_highscores()
                run = False
                from main_menu import main_menu
                main_menu()
                sys.exit()
            elif len(user_name) > 0 and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if all([3*window_width//20 <= mouse_x <= 15*window_width//20, 145*window_height//200 <= mouse_y <= 175*window_height//200]):
                    hs = Highscore_Table()
                    hs.update_table({"Player": user_name, "Score":score})
                    hs.save_highscores()
                    run = False
                    from main_menu import main_menu
                    main_menu()
                    sys.exit()

        window.fill(my_window.get_colour())
        pygame.draw.rect(window, border.get_colour(), border.get_rect(), border.get_thickness())
        text_surface_1 = my_font.render("GAME OVER", False, (255, 255, 255), (0, 0, 0))
        text_surface_2 = my_font.render(f"Score: {score}", False, (255, 255, 255), (0, 0, 0))
        text_surface_3 = my_font.render(user_name, True, (255, 255, 255))
        text_surface_4 = my_font.render("Submit highscore", True, (255, 255, 255))
        pygame.draw.rect(window, (50, 50, 50), (3*window_width//20, 105*window_height//200, 6*window_width//10, 4*window_height//30))
        window.blit(text_surface_1, (3*window_width//20, 3*window_height//20))
        window.blit(text_surface_2, (3*window_width//20, 65*window_height//200))
        window.blit(text_surface_3, (3*window_width//20, 105*window_height//200))
        if len(user_name) > 0:
            pygame.draw.rect(window, (255, 0, 0), (3*window_width//20, 145*window_height//200, 6*window_width//10, 45*window_height//300), 2)
            window.blit(text_surface_4, (3*window_width//20, 145*window_height//200))
            

        pygame.display.flip()


if __name__ == "__main__":
    game_over(1)