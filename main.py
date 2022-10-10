import pygame
import pygame_menu
from pygame.locals import *
import sys
from main_2 import main_game_screen

color_white = (255, 255, 255)
color_black = (0, 0, 0)


def main_menu():

    pygame.display.set_caption('Modern Democracy: The Game!')

    def start_the_game():
        start_game()

    def load_game():
        # open list of prior games
        pass

    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('New Game', start_the_game)
    menu.add.button('Load Game', load_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


def start_game():

    def return_main_menu():
        main_menu()

    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)
    name_box = menu.add.text_input('Name : ', default='')
    state_name_box = menu.add.text_input('State Name : ', default='')
    menu.add.button('Play', game_start, name_box, state_name_box)
    menu.add.button('Return to Main Menu', return_main_menu)
    menu.mainloop(surface)


def game_start(name_box, state_name_box):

    def close_menu():
        menu.disable()
        main_game_screen(player_name, state_name)

    player_name = name_box.get_value()
    state_name = state_name_box.get_value()
    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button(f'Welcome {player_name}!', close_menu)
    menu.mainloop(surface)


def game_screen():

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()
surface = pygame.display.set_mode((1000, 600))
main_menu()

