import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mplcyberpunk
import json


def plot_state_attribute(attribute1, attribute2=False, custom_title=False):

    def plot(dat, attribute1, attribute2=False, custom_title=False):

        plt.style.use("cyberpunk")

        fig, ax = plt.subplots()
        ax.plot(
            dat['Turn'],
            dat[attribute1],
            color="red",
            label=attribute1
        )
        if attribute2:
            ax.plot(
                dat['Turn'],
                dat[attribute2],
                color="blue",
                label=attribute2
            )
        if custom_title:
            ax.set_ylabel(custom_title, fontsize=14)
        else:
            ax.set_ylabel(attribute1, fontsize=14)
        ax.set_xlabel("Turn", fontsize=14)
        #ax.set_xticks(dat["Turn"])
        ax.get_xticklabels()

        ax.get_yaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

        if attribute2:
            ax.legend()

        if custom_title:
            matplotlib.pyplot.title("{}".format(custom_title), fontsize=16)
        else:
            matplotlib.pyplot.title("Historical {}".format(attribute1), fontsize=16)
        mplcyberpunk.add_glow_effects()

        return fig

    # create table for plotting
    with open("data/turn_dat.json", "r") as jsonFile:
        game_data = json.load(jsonFile)
    n_turns = game_data['game_dat']['turn']
    turn = np.arange(1, n_turns + 1)

    att1 = []
    att2 = []
    for i in range(1, n_turns + 1):
        att1.append(game_data[f'turn{i}'][attribute1])
    if attribute2:
        for i in range(1, n_turns + 1):
            att2.append(game_data[f'turn{i}'][attribute2])
    if not att2:
        dat = pd.DataFrame(list(zip(turn, att1)), columns=['Turn', attribute1])
    else:
        dat = pd.DataFrame(list(zip(turn, att1, att2)), columns=['Turn', attribute1, attribute2])
    surf = plot(dat, attribute1, attribute2, custom_title)

    return surf

