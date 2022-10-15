import pandas as pd
import pygame
import matplotlib
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import mplcyberpunk
import sys
from pygame.locals import *


def plot_attribute():

    def plot_state_attribute(attribute):

        def plot(dat, attribute):

            matplotlib.use("Agg")
            plt.style.use("cyberpunk")

            fig, ax = plt.subplots()
            ax.plot(
                dat['Turn'],
                dat[attribute],
                color="red",
                marker="o",
                label= attribute
            )
            ax.set_ylabel(attribute, fontsize=14)
            ax.set_xlabel("Turn", fontsize=14)
            ax.set_xticks(dat["Turn"])

            ax.legend()

            matplotlib.pyplot.title("Historical {} Characteristics".format(attribute), fontsize=16)
            mplcyberpunk.add_glow_effects()

            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()

            size = canvas.get_width_height()

            surf = pygame.image.fromstring(raw_data, size, "RGB")

            return surf

        turn = [1, 2, 3, 4]
        pop = [100, 101, 105, 110]
        birth_rate = [7.0, 6.6, 7.7, 9.0]
        death_rate = [3.0, 3.5, 4.0, 4.1]

        dat = pd.DataFrame(list(zip(turn, pop, birth_rate, death_rate)),
                       columns =['Turn', 'Population', 'Birth Rate', 'Death Rate'])
        surf = plot(dat, attribute)
        return surf

    pygame.font.init()
    pygame.display.set_caption('Modern Democracy: The Game!')
    pygame.init()
    surface = pygame.display.set_mode((1000, 600))

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            surf = plot_state_attribute("Population")
            surface.blit(surf, (0, 0))
            pygame.display.flip()


# # TODO: make it change scale when turns get to a certain threshold
