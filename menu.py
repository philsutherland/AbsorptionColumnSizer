from sys import exit


class Menu():
    @staticmethod
    def main_menu():
        selection = 0

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
