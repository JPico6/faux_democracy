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
            marker="o",
            label= attribute1
        )
        if attribute2:
            ax.plot(
                dat['Turn'],
                dat[attribute2],
                color="blue",
                marker="o",
                label=attribute2
            )
        if custom_title:
            ax.set_ylabel(custom_title, fontsize=14)
        else:
            ax.set_ylabel(attribute1, fontsize=14)
        ax.set_xlabel("Turn", fontsize=14)
        ax.set_xticks(dat["Turn"])

        ax.legend()

        if custom_title:
            matplotlib.pyplot.title("{}".format(custom_title), fontsize=16)
        else:
            matplotlib.pyplot.title("Historical {}".format(attribute1), fontsize=16)
        mplcyberpunk.add_glow_effects()

        return fig

    turn = [1, 2, 3, 4]
    pop = [100, 101, 105, 110]
    birth_rate = [7.0, 6.6, 7.7, 9.0]
    death_rate = [3.0, 3.5, 4.0, 4.1]
    approval = [46.0, 46.7, 46.9, 46.3]
    conservative_approval = [68.0, 67.7, 67.5, 67.0]
    liberal_approval = [35.7, 36.0, 36.0, 35.4]

    dat = pd.DataFrame(list(zip(turn, pop, birth_rate, death_rate, approval, conservative_approval, liberal_approval)),
                       columns=['Turn', 'Population', 'Birth Rate', 'Death Rate', 'Approval', 'Conservative Approval',
                                'Liberal Approval'])

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
    print(dat)
    surf = plot(dat, attribute1, attribute2, custom_title)

    return surf


# TODO: make it change scale when turns get to a certain threshold
