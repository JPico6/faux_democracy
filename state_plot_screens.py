import PySimpleGUI as sg
import matplotlib.pyplot as plt
from plot_state_attributes import plot_state_attribute
import json

sg.set_options(font=("Helvetica", 14))


def population_screen():

    layout = [[sg.Button('Population'), sg.Button('Birth/Death Rate'), sg.Cancel()]]

    window = sg.Window('Historical Population Characteristics', layout, size=(400, 400))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Population':
            plot_state_attribute(attribute1="pop", custom_title="Population")
            plt.show(block=False)
        elif event == 'Birth/Death Rate':
            plot_state_attribute(attribute1="birth_rate", attribute2="death_rate", custom_title="Birth/Death Rate (per k)")
            plt.show(block=False)

    window.close()


def approval_screen():

    layout = [[sg.Button('Total Approval'), sg.Button('Conservative/Liberal Approval'), sg.Cancel()]]

    window = sg.Window('State Approval Ratings', layout, size=(400, 400))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Total Approval':
            plot_state_attribute(attribute1="approval_level", custom_title="Approval Rate (%)")
            plt.show(block=False)
        elif event == 'Conservative/Liberal Approval':
            plot_state_attribute(attribute1="approval_conservative", attribute2="approval_liberal",
                                 custom_title="Conservative/Liberal Approval Rates (%)")
            plt.show(block=False)

    window.close()


def election_screen():

    with open('data/turn_dat.json') as f:
        game_data = json.load(f)
        turns_to_election = game_data['game_dat']['turns_next_election']

    layout = [
        [sg.Text(f'Turns until the next election: {turns_to_election}')],
        [sg.Button('Cancel Election'),
         sg.Cancel()]]

    window = sg.Window('State Elections', layout, size=(400, 400))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Cancel Election':
            sg.set_options(font=("Helvetica", 14))
            sg.popup('To hell with the pretense of democracy, then', title='Cancel Elections')

    window.close()
