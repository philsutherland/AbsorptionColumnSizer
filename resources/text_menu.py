from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class TextMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def navigate(self):
        # TextMenu.clear()
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
            self.navigate()

        if str(selection) in nav_map:
            print("Go to: " + self.options[nav_map[str(selection)]])
        else:
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            self.navigate()

    @staticmethod
    def clear():
        os.system("cls")
        print("")
