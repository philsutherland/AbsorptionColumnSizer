from resources.text_menu import TextMenu
from formatting.formatted_text_menu import FormattedTextMenu
import os

print("\n" + FormattedTextMenu.main_title("Welcome to AbsorbSim Pro V2.0"))

string1 = "This is string1"
string2 = "This is string2"

size_absorption_column_instructions = TextMenu(
    title="Size Absorption Column Instructions", message=string1, options={'Return': '', 'Exit': ''})

optimize_absorption_column_instructions = TextMenu(
    title="Optimize Absorption Column Instructions", message=string2, options={'Return': '', 'Exit': ''})

size_absorption_column_menu = TextMenu(title="Size Absorption Column Menu", options={'Size Absorption Column': 'size_absorption_column',
                                                                                     'Instructions': size_absorption_column_instructions, 'Return': '', 'Exit': ''})

optimize_absorption_column_menu = TextMenu(title="Optimize Absorption Column Menu", options={'Optimize Absorption Column': 'optimize_absorption_column',
                                                                                             'Instructions': optimize_absorption_column_instructions, 'Return': '', 'Exit': ''})


main_menu = TextMenu(title="Main Menu", options={'Size Absorption Column Menu': size_absorption_column_menu.navigate,
                                                 'Optimize Absorption Column Menu': optimize_absorption_column_menu.navigate, 'About': 'about', 'Exit': ''})


main_menu.navigate(None)
