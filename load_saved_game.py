import PySimpleGUI as sg
import settings
import os
import pygame
import json
from game_screens import main_game_screen


def select_saved_game():
    # get path, which could differ by user install location
    f_path = os.path.dirname(os.path.abspath(__file__))
    settings.game_vars_dict.update({"file_location": f_path})
    f_path = settings.game_vars_dict['file_location'] + '/data'

    sg.theme("DarkTeal2")
    layout = [
        [sg.T("")],
        [sg.Text("Choose a file: "),
         sg.Input(key="-IN2-",
                  change_submits=True),
         sg.FileBrowse(initial_folder=f_path,
                       key="-IN-")],
        [sg.Button("Submit")],
        [sg.Button("Cancel")]
    ]

    window = sg.Window('Load a Game', layout, size=(800, 250))

    while True:
        event, values = window.read()
        # print(values["-IN2-"])
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            file_path = values["-IN-"]
            with open(file_path) as f:
                window.close()
                game_data = json.load(f)
                # load the data to settings
                player_name = game_data['game_dat']['player_name']
                state_name = game_data['game_dat']['state_name']
                settings.game_vars_dict.update({"player": player_name})
                settings.game_vars_dict.update({"state": state_name})
                settings.game_vars_dict.update({"file_location": f_path})
                # go to main menu and bring game_data
                main_game_screen(player_name, state_name)

        elif event == "Cancel":
            from game_screens import main_menu
            window.close()
            pygame.font.init()
            pygame.init()
            main_menu()

