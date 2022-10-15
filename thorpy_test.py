import thorpy
import pandas as pd
from plot_state_attributes import build_line_plot
import matplotlib
import matplotlib.backends.backend_agg as agg
import pygame
matplotlib.use("Agg")

turn = [1, 2, 3, 4]
pop = [100, 101, 105, 110]
birth_rate = [7.0, 6.6, 7.7, 9.0]
death_rate = [3.0, 3.5, 4.0, 4.1]

dat = pd.DataFrame(list(zip(turn, pop, birth_rate, death_rate)),
               columns =['Turn', 'Population', 'Birth Rate', 'Death Rate'])

(width, height) = (900, 600)
surf = build_line_plot(dat)
screen = pygame.display.set_mode((width, height))


##Declaration of the application in which the menu is going to live.
application = thorpy.Application(size=(500, 500))

##Setting the graphical theme. By default, it is 'classic' (windows98-like).
###thorpy.theme.set_theme('human')

##Declaration of some elements...
useless1 = thorpy.Element("This button is useless.\nAnd you can't click it.")
useless1.set_pressed_state() #so user knows he can't click
useless1.scale_to_content()

text = "This button also is useless.\nBut you can click it anyway."
useless2 = thorpy.make_button(text)

draggable = thorpy.Draggable("Drag me!")
draggable.scale_to_content()

box1 = thorpy.make_ok_box([useless1, useless2, draggable])
options1 = thorpy.make_button("Some useless things...")
thorpy.set_launcher(options1, box1)


inserter = thorpy.Inserter(name="Tip text: ",
                            value="This is a default text.",
                            size=(150, 20))

file_browser = thorpy.Browser(path="C:/Users/", text="Please have a look.")

browser_launcher = thorpy.BrowserLauncher(browser=file_browser,
                                                const_text="Choose a file: ",
                                                var_text="")
browser_launcher.scale_to_title()

color_setter = thorpy.ColorSetter.make()
color_launcher = thorpy.ColorSetterLauncher(color_setter,
                                                    "Launch color setter")

options2 = thorpy.make_button("Useful things")
box2 = thorpy.make_ok_box([inserter, color_launcher, browser_launcher])
thorpy.set_launcher(options2, box2)
pop_button = thorpy.make_button("Population Characteristics")
pop_button.Image(screen.blit(surf, (0, 0)))
#    screen.blit(surf, (0, 0))
#    pygame.display.flip()
quit_button = thorpy.make_button("Quit")
quit_button.set_as_exiter()

central_box = thorpy.Box.make([options1, options2, quit_button])
central_box.set_main_color((200, 200, 200, 120))
central_box.center()

##Declaration of a background element - include your own path!
background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,
                                    elements=[central_box])

menu = thorpy.Menu(elements=background, fps=45)
menu.play()

application.quit()