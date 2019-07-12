from resources.text_menu import TextMenu
from formatting.formatted_text_menu import FormattedTextMenu
import os

print("\n" + FormattedTextMenu.main_title("Welcome to AbsorbSim Pro V2.0"))


size_absorption_column_menu = TextMenu("Size Absorption Column Menu", {'Size Absorption Column': 'size_absorption_column',
                                                                       'Instructions': 'instructions', 'Return': 'return', 'Exit': 'exit'})

optimize_absorption_column_menu = TextMenu("Optimize Absorption Column Menu", {'Optimize Absorption Column': 'optimize_absorption_column',
                                                                               'Instructions': 'instructions', 'Return': 'return', 'Exit': 'exit'})


main_menu = TextMenu("Main Menu", {'Size Absorption Column Menu': size_absorption_column_menu.navigate,
                                   'Optimize Absorption Column Menu': optimize_absorption_column_menu.navigate, 'About': 'about', 'Exit': 'exit'})


main_menu.navigate(None)
