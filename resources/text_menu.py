from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class TextMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def navigate(self, previous_menu):
        if previous_menu is None:
            previous_menu = self

        menu_options = list(self.options)
        print(FormattedTextMenu.sub_title(self.title))
        print(FormattedTextMenu.options_menu(menu_options))

        nav_map = {}
        x = 0
        for option in menu_options:
            x += 1
            nav_map[str(x)] = option

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            TextMenu.clear()
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            self.navigate(self)

        if str(selection) in nav_map:
            if nav_map[str(selection)] == "Return":
                TextMenu.clear()
                previous_menu.navigate(self)
            elif nav_map[str(selection)] == "About":
                pass
            elif nav_map[str(selection)] == "Instructions":
                pass
            elif nav_map[str(selection)] == "Exit":
                TextMenu.clear()
                print(FormattedTextMenu.main_title("Goodbye!"))
                exit(0)
            else:
                TextMenu.clear()
                self.options[nav_map[str(selection)]](self)
        else:
            TextMenu.clear()
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            self.navigate(self)

    @staticmethod
    def clear():
        os.system("cls")
        print("")