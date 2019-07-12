from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class Menu():
    @staticmethod
    def main_menu():

        print("|-------------------------------------------------------------|")
        print("|                          Main Menu                          |")
        print("|-------------------------------------------------------------|")
        print("| Options:                                                    |")
        print("|        1. Size Absorption Column Menu                       |")
        print("|        2. Optimize Absorption Column Menu                   |")
        print("|        3. About                                             |")
        print("|        4. Exit                                              |")
        print("|-------------------------------------------------------------|")

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            print("Invalid Selection!")
            main_menu()

        if selection == 1:
            size_absorption_sub_menu()
        elif selection == 2:
            optimize_absorption_sub_menu()
        elif selection == 3:
            about_sub_menu()
        elif selection == 4:
            print("Goodbye!")
            exit(0)
        else:
            print("Invalid Selection!")
            main_menu()

    @staticmethod
    def size_absorption_sub_menu():

        print("|-------------------------------------------------------------|")
        print("|                 Size Absorption Column Menu                 |")
        print("|-------------------------------------------------------------|")
        print("| Options:                                                    |")
        print("|        1. Size Absorption Column                            |")
        print("|        2. Instructions                                      |")
        print("|        3. Return                                             |")
        print("|        4. Exit                                              |")
        print("|-------------------------------------------------------------|")

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            print("Invalid Selection!")
            size_absorption_menu()

        if selection == 1:
            size_absorption_column()
        elif selection == 2:
            size_absorption_column_instructions()
        elif selection == 3:
            main_menu()
        elif selection == 4:
            print("Goodbye!")
            exit(0)
        else:
            print("Invalid Selection!")
            size_absorption_sub_menu()

    @staticmethod
    def optimize_absorption_sub_menu():

        print("|-------------------------------------------------------------|")
        print("|                 Size Absorption Column Menu                 |")
        print("|-------------------------------------------------------------|")
        print("| Options:                                                    |")
        print("|        1. Size Absorption Column                            |")
        print("|        2. Instructions                                      |")
        print("|        3. Return                                            |")
        print("|        4. Exit                                              |")
        print("|-------------------------------------------------------------|")

        try:
            selection = int(input("Select Option: "))
        except(BaseException):
            print("Invalid Selection!")
            size_absorption_menu()

        if selection == 1:
            size_absorption_column()
        elif selection == 2:
            size_absorption_column_instructions()
        elif selection == 3:
            main_menu()
        elif selection == 4:
            print("Goodbye!")
            exit(0)
        else:
            print("Invalid Selection!")
            size_absorption_sub_menu()
