import pygame
import pygame_menu
from create_world import State
import json
from temp import initiate_game, main_screen
import os
from pygame.locals import *
import sys

clock = pygame.time.Clock()
color_white = (255, 255, 255)
color_black = (0, 0, 0)

# create player-state attributes
game_data = initiate_game()

pygame.font.init()
pygame.display.set_caption('Modern Democracy: The Game!')
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()
surface = pygame.display.set_mode((1000, 600))

bg = pygame.transform.scale(pygame.image.load("images/redblue.jpg"), (1000,600))


#INSIDE OF THE GAME LOOP

while True:

    surface.blit(bg, (0, 0))
    pygame.display.flip()

    MAPWIDTH = 25
    MAPHEIGHT = 15
    TILESIZE = 40

    Turn, Population, Approval, Currency = 0, 1, 2, 3

    display_attributes = {
        Turn: game_data['game_dat']['turn'],
        Population: format(game_data['state1']['pop'], ","),
        Approval: '50%', #game_data.get('approval')
        Currency: 100
    }

    textures = {
        Turn: pygame.transform.scale(pygame.image.load('images/turn.png'), (40,40)),
        Population: pygame.transform.scale(pygame.image.load('images/pop.jpg'), (40,40)),
        Approval: pygame.transform.scale(pygame.image.load('images/approval.jpg'), (40,40)),
        Currency: pygame.transform.scale(pygame.image.load('images/currency.png'), (40,40))
    }

# add 50 pixels to the height for the inventory
    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
    # setup a font for displaying inventory numbers
    INVFONT = pygame.font.Font('freesansbold.ttf', 12)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # render current game status
    place_position = 10
    for item in display_attributes:
        DISPLAYSURF.blit(textures[item], (place_position, MAPHEIGHT * TILESIZE + 10))
        place_position += 30
        textObj = INVFONT.render(str(display_attributes[item]), True, color_white, color_black)
        DISPLAYSURF.blit(textObj, (place_position, MAPHEIGHT * TILESIZE + 10))
        place_position += 50


    # Clamp FPS
    clock.tick_busy_loop( 120 )




