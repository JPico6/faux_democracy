import PySimpleGUI as sg
import matplotlib.pyplot as plt
from plot_state_attributes import plot_state_attribute


def population_screen():

    layout = [[sg.Button('Population'), sg.Button('Birth/Death Rate'), sg.Cancel()]]

    window = sg.Window('Historical Population Characteristics', layout, size=(400, 400))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Population':
            plot_state_attribute(attribute1="Population", custom_title="Population (Thousands)")
            plt.show(block=False)
        elif event == 'Birth/Death Rate':
            plot_state_attribute(attribute1="Birth Rate", attribute2="Death Rate", custom_title="Birth/Death Rate (per k)")
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
            plot_state_attribute(attribute1="Approval", custom_title="Approval Rate (%)")
            plt.show(block=False)
        elif event == 'Conservative/Liberal Approval':
            plot_state_attribute(attribute1="Conservative Approval", attribute2="Liberal Approval",
                                 custom_title="Conservative/Liberal Approval Rates (%)")
            plt.show(block=False)

    window.close()
