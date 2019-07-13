from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class TextMenu:
    def __init__(self, title, message="", options={'Return': 'return', 'Exit': 'exit'}):
        self.title = title
        self.message = message
        self.options = options

    def navigate(self, previous_menu, returning=False):
        if not returning:
            if previous_menu is None:
                self.previous_menu = self
            else:
                self.previous_menu = previous_menu

        menu_options = list(self.options)
        print(FormattedTextMenu.sub_title(self.title))

        if self.message:
            print(FormattedTextMenu.body_content(self.message))

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
            self.navigate(self, True)

        if str(selection) in nav_map:
            if self.options[nav_map[str(selection)]] == "return":
                TextMenu.clear()
                self.previous_menu.navigate(self, True)
                pass
            elif self.options[nav_map[str(selection)]] == "exit":
                TextMenu.clear()
                print(FormattedTextMenu.main_title("Goodbye!"))
                exit(0)
            else:
                TextMenu.clear()
                self.options[nav_map[str(selection)]](self)
        else:
            TextMenu.clear()
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            self.navigate(self, True)

    @staticmethod
    def clear():
        os.system("cls")
        print("")
