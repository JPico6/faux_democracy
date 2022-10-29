import pygame
from game_screens import main_menu


def run_game():

    pygame.font.init()
    # my_font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.init()
    main_menu()


if __name__ == "__main__":
    run_game()


