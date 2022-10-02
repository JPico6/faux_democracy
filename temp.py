import pygame
from pygame.locals import *
import json

# map_1 = open('C:/Users/jp/Documents/democracy/map_1.json', encoding="utf8")
#
# data = json.load(map_1)
#
# print(data)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio as iio

# read an image
img = iio.imread('C:/Users/jp/Documents/democracy/map_2.png')
imgplot = plt.imshow(img)
plt.show()