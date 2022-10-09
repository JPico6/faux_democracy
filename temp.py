from pygame.locals import *
import json
from create_world import State


def initiate_game():

    # A. initiate world
    game_data = {}
    state1 = {}
    game_dat = {}
    game_dat['turn'] = 1

    # b. initiate state(s)
    state1 = State()
    state1_attributes = state1.generate_attributes()
    print(state1_attributes)
    game_data['game_dat'] = game_dat
    game_data['state1'] = state1_attributes
    # game_data = json.dumps(game_data)
    print(game_data)

    with open('data/turn_dat.json', 'w') as f:
        json.dump(game_data, f)

    return game_data

def main_screen():

    # load game data
    f = open('data/turn_dat.json')
    game_data = json.load(f)

    state_attributes = game_data.get('state1')

    #print(data['places'][0]['post code'])
    return state_attributes

# map_1 = open('C:/Users/jp/Documents/democracy/map_1.json', encoding="utf8")
#
# data = json.load(map_1)
#
# print(data)

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import imageio as iio
#
# # read an image
# img = iio.imread('C:/Users/jp/Documents/democracy/map_2.png')
# imgplot = plt.imshow(img)
# plt.show()