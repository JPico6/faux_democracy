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
        pass

    def load_game():
        # open list of prior games
        pass

    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('New Game', start_the_game)
    menu.add.button('Load Game', load_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)


def start_game():

    def return_main_menu():
        main_menu()
        pass

    def go_to_game():
        menu.disable()
        main_game_screen()

    def get_name(value):
        player_name = value
        # add name to game file - or to state object?

        return player_name

    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)

    player_name = menu.add.text_input('Name : ', default='', onchange=get_name)
    #menu.add.text_input('Ruler Name :', default='')
    menu.add.button('Return to Main Menu', return_main_menu)
    menu.add.button('Start', go_to_game)
    menu.mainloop(surface)

    return player_name


def game_screen():

    while True:

        MAPWIDTH = 25
        MAPHEIGHT = 15
        TILESIZE = 40

        Population, Approval, Currency = 0, 1, 2

        display_attributes = {
            Population: 0,
            Approval: 0,
            Currency: 0
    #        'Political Clout': 0
        }

        textures = {
            Population: pygame.image.load('images/pop.jpg'),
            Approval: pygame.image.load('images/approval.jpg'),
            Currency: pygame.image.load('images/currency.png')
        }

        # add 50 pixels to the height for the inventory
        DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
        # setup a font for displaying inventory numbers
        INVFONT = pygame.font.Font('freesansbold.ttf', 18)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # render current game status
        place_position = 10
        for item in display_attributes:
            DISPLAYSURF.blit(textures[item], (place_position, MAPHEIGHT * TILESIZE + 20))
            place_position += 30
            textObj = INVFONT.render(str(display_attributes[item]), True, color_white, color_black)
            DISPLAYSURF.blit(textObj, (place_position, MAPHEIGHT * TILESIZE + 20))
            place_position += 50

    #    DISPLAYSURF.blit(player, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
        pygame.display.update()





pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()
surface = pygame.display.set_mode((1000, 600))
main_menu()

