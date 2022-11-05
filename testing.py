import PySimpleGUI as sg
import settings
import os
import json
from game_screens import main_menu
import pygame


def select_saved_game():

    #get path, which could differ by user install location
    f_path = os.path.dirname(os.path.abspath(__file__))
    settings.game_vars_dict.update({"file_location": f_path})
    f_path = settings.game_vars_dict['file_location'] + '/data'


    sg.theme("DarkTeal2")
    layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(key="-IN2-", change_submits=True),
                           sg.FileBrowse(initial_folder=f_path, key="-IN-")], [sg.Button("Submit")],
              [sg.Button("Cancel")]
             ]

    sg.theme("DarkTeal2")
    layout = [[sg.T("")],
              [sg.Text("Choose a folder: "), sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN-")],
              [sg.Button("Submit")]]

    window = sg.Window('Load Game', layout, size=(600, 250))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            return values["-IN-"]
        elif event == 'Cancel':
            window.close()
            pygame.font.init()
            pygame.init()
            main_menu()



select_saved_game()
loaded_game = select_saved_game()
with open(loaded_game) as f:
    game_data = json.load(f)

#then go to main screen
#or go back to the initial screen if they cancel
print(game_data)

#
# message = "pick a file, foo"
#
# popup_get_file(message,
#     title = "Load Game File",
#     default_path = f_path,
#     default_extension = ".json",
#     save_as = False,
#     multiple_files = False,
#     file_types = (('ALL Files', '*.* *'),),
#     no_window = False,
#     size = (None, None),
#     button_color = None,
#     background_color = None,
#     text_color = None,
#     icon = None,
#     font = None,
#     no_titlebar = False,
#     grab_anywhere = False,
#     keep_on_top = None,
#     location = (None, None),
#     relative_location = (None, None),
#     initial_folder = None,
#     image = None,
#     files_delimiter = ";",
#     modal = True,
#     history = False,
#     show_hidden = True,
#     history_setting_filename = None)
#
