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

        # if selection == 1:
        #     Menu.size_absorption_sub_menu()
        # elif selection == 2:
        #     Menu.optimize_absorption_sub_menu()
        # elif selection == 3:
        #     Menu.about_sub_menu()
        # elif selection == 4:
        #     Menu.clear()
        #     print(FormattedTextMenu.main_title("Goodbye!"))
        #     exit(0)
        # else:
        #     print(FormattedTextMenu.error_title("Invalid Selection!"))
        #     Menu.main_menu()

    @staticmethod
    def clear():
        os.system("cls")
        print("")

    # @classmethod
    # def navigate(cls):
    #     print("This is how the menu navigates")
