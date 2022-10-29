import pygame
import pygame_menu
from create_world import initiate_game
from pygame.locals import *
import sys
import json
from adjust_state_attributes import new_turn
from state_plot_screens import population_screen, approval_screen#, currency_screen


color_white = (255, 255, 255)
color_black = (0, 0, 0)
surface = pygame.display.set_mode((1000, 600))
game_initiated = False

pygame.mouse.set_visible(False)
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


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
        main_game_screen(player_name, state_name, True)

    player_name = name_box.get_value()
    state_name = state_name_box.get_value()
    menu = pygame_menu.Menu('Modern Democracy: The Game!', 600, 400,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button(f'Welcome {player_name}!', close_menu)
    menu.mainloop(surface)


def main_game_screen(player_name, state_name, initiate=False):

    def in_game_menu(inpt):

        if inpt == 0:
            new_turn()
            main_game_screen(player_name, state_name)
        if inpt == 1:
            population_screen()
        if inpt == 2:
            approval_screen()
        # if inpt == 3:
        #     currency_menu()

    # create player-state attributes
    if initiate:
        game_data = initiate_game()
        game_data['game_dat']['player_name'] = player_name
        game_data['game_dat']['state_name'] = state_name
        # save:
        game_object = json.dumps(game_data)
        with open("data/turn_dat.json", "w") as outfile:
            outfile.write(game_object)
        print(game_data)
    if not initiate:
        with open('data/turn_dat.json') as f:
            game_data = json.load(f)

    pygame.font.init()
    pygame.display.set_caption('Modern Democracy: The Game!')
    pygame.init()
    surface = pygame.display.set_mode((1000, 600))

    bg = pygame.transform.scale(pygame.image.load("images/redblue.jpg"), (1000,600))

    # INSIDE OF THE GAME LOOP
    while True:

        surface.blit(bg, (0, 0))
        pygame.display.flip()

        MAPWIDTH = 25
        MAPHEIGHT = 15
        TILESIZE = 40

        Turn, Population, Approval, Currency = 0, 1, 2, 3

        current_turn = game_data['game_dat']['turn']
        display_attributes = {
            Turn: game_data['game_dat']['turn'],
            Population: format(game_data[f'turn{current_turn}']['pop'], ","),
            Approval: "%s%%"%game_data[f'turn{current_turn}']['approval_level'],
            Currency: 100
        }

        textures = {
            Turn: pygame.transform.scale(pygame.image.load('images/turn.png'), (40, 40)),
            Population: pygame.transform.scale(pygame.image.load('images/pop.jpg'), (40, 40)),
            Approval: pygame.transform.scale(pygame.image.load('images/approval.jpg'), (40, 40)),
            Currency: pygame.transform.scale(pygame.image.load('images/currency.png'), (40, 40))
        }

    # add 50 pixels to the height for the inventory
        DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
        # setup a font for displaying inventory numbers
        INVFONT = pygame.font.Font('freesansbold.ttf', 12)

        # so you can click out of - quit the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # display select game attributes
            place_position = 10
            for item in display_attributes:
                DISPLAYSURF.blit(textures[item], (place_position, MAPHEIGHT * TILESIZE + 10))
                place_position += 30
                textObj = INVFONT.render(str(display_attributes[item]), True, color_white, color_black)
                DISPLAYSURF.blit(textObj, (place_position, MAPHEIGHT * TILESIZE + 10))
                place_position += 50

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if DISPLAYSURF.blit(textures[item], (place_position-80, MAPHEIGHT * TILESIZE + 10)).collidepoint(mouse_pos):
                        #pygame.mouse.set_visible(False)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()

                    if DISPLAYSURF.blit(textures[item], (place_position-80, MAPHEIGHT * TILESIZE + 10)).collidepoint(click_pos):
                        in_game_menu(item)





