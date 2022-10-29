import pygame
from game_screens import main_menu


def run_game():

    pygame.font.init()
    pygame.init()
    main_menu()


if __name__ == "__main__":
    run_game()


