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
            sizeAbsorptionSubMenu()
        elif selection == 2:
            optimizeAbsorptionSubMenu()
        elif selection == 3:
            aboutSubMenu()
        elif selection == 4:
            print("Goodbye!")
            exit(0)
        else:
            print("Invalid Selection!")
            main_menu()
