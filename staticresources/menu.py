from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class Menu():
    @staticmethod
    def clear():
        os.system("cls")
        print("")

    @staticmethod
    def main_menu():
        menu_options = ["Size Absorption Column Menu",
                        "Optimize Absorption Column Menu", "About", "Exit"]

        print(FormattedTextMenu.sub_title("Main Menu"))
        print(FormattedTextMenu.options_menu(menu_options))

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            Menu.clear()
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            Menu.main_menu()

        if selection == 1:
            Menu.size_absorption_sub_menu()
        elif selection == 2:
            Menu.optimize_absorption_sub_menu()
        elif selection == 3:
            Menu.about_sub_menu()
        elif selection == 4:
            Menu.clear()
            print(FormattedTextMenu.main_title("Goodbye!"))
            exit(0)
        else:
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            Menu.main_menu()

    @staticmethod
    def size_absorption_sub_menu():
        menu_options = ["Size Absorption Column",
                        "Instructions", "Return", "Exit"]

        print(FormattedTextMenu.sub_title("Main Menu"))
        print(FormattedTextMenu.options_menu(menu_options))

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            Menu.clear()
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            Menu.main_menu()

        if selection == 1:
            Menu.size_absorption_column()
        elif selection == 2:
            Menu.size_absorption_column_instructions()
        elif selection == 3:
            Menu.main_menu()
        elif selection == 4:
            Menu.clear()
            print(FormattedTextMenu.main_title("Goodbye!"))
            exit(0)
        else:
            print(FormattedTextMenu.error_title("Invalid Selection!"))
            Menu.main_menu()
