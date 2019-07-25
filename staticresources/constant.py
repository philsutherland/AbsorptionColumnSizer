from formatting.formatted_text_menu import FormattedTextMenu
from sys import exit
import os


class Constant:

    @staticmethod
    def clear():
        os.system("cls")
        print("")

    # Number of steps for solving numerical integration upper limit
    @staticmethod
    def num_step_upper_limit():
        return 10000

    # Number of steps for solving numerical integration lower limit
    @staticmethod
    def num_step_lower_limit():
        return 1

    # Percent recovery upper limit
    @staticmethod
    def percent_recovery_upper_limit():
        return 99.9

    # Percent recovery lower limit
    @staticmethod
    def percent_recovery_lower_limit():
        return 0.1

    # Inlet vapour flow rate upper limit
    @staticmethod
    def V_0_upper_limit():
        return 1000000000

    # Inlet vapour flow rate lower limit
    @staticmethod
    def V_0_lower_limit():
        return 0.001

    # Inlet liquid flow rate upper limit
    @staticmethod
    def L_N_upper_limit():
        return 1000000000

    # Inlet liquid flow rate lower limit
    @staticmethod
    def L_N_lower_limit():
        return 0.001

    # Inlet vapour mole fraction of component A upper limit
    @staticmethod
    def y_A0_upper_limit():
        return 0.5

    # Inlet vapour mole fraction of component A lower limit
    @staticmethod
    def y_A0_lower_limit():
        return 0.00

    # Inlet liquid mole fraction of component A upper limit
    @staticmethod
    def x_AN_upper_limit():
        return 0.25

    # Inlet liquid mole fraction of component A lower limit
    @staticmethod
    def x_AN_lower_limit():
        return 0.00

    # Attempt to open the Constants.txt file so the constants can later be imported
    try:
        f_constants = open("inputs/Constants.txt", "r")
    except FileNotFoundError as e:
        clear()
        FormattedTextMenu.error_title(
            "Critical Error: The Constants.txt file can not be found or could not be opened!")
    except Exception as e:
        clear()
        FormattedTextMenu.error_title(
            "Critical Error: Unknown exception occured when attempting to open Constants.txt!")

    # Attempt to open the EquilibriumData.txt file so the equilibrium coefficients can be later imported
    try:
        f_equilibrium = open("inputs/EquilibriumData.txt", "r")
    except FileNotFoundError as e:
        clear()
        FormattedTextMenu.error_title(
            "Critical Error: The EquilibriumData.txt file can not be found or could not be opened!")
    except Exception as e:
        clear()
        FormattedTextMenu.error_title(
            "Critical Error: Unknown exception occured when attempting to open EquilibriumData.txt!")

    # Read in equilibrium coefficients from EquilibriumData.txt
    try:
        f_equilibrium.readline()
