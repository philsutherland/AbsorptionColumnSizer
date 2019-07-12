from resources.text_menu import TextMenu
# from staticresources.menu import Menu
from formatting.formatted_text_menu import FormattedTextMenu
import os

print("\n" + FormattedTextMenu.main_title("Welcome to AbsorbSim Pro V2.0"))


# dicty = {'Size Absorption Column Menu': 'size_absorption_column_menu',
#          'Optimize Absorption Column Menu': 'optimize_absorption_column_menu', 'About': 'about', 'Exit': exit(0)}


main_menu = TextMenu("Main Menu", {'Size Absorption Column Menu': 'size_absorption_column_menu',
                                   'Optimize Absorption Column Menu': 'optimize_absorption_column_menu', 'About': 'about', 'Exit': 'exit(0)'})

main_menu.navigate()
# Menu.main_menu()
