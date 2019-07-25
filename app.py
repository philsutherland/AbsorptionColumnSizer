from resources.text_menu import TextMenu
from formatting.formatted_text_menu import FormattedTextMenu
from exceptions.could_not_construct_object_exception import CouldNotConstructObjectException
from staticresources.constant import Constant
import os
import datetime

print(Constant.num_step_upper_limit())


# print("\n" + FormattedTextMenu.main_title("Welcome to AbsorbSim Pro V2.0"))


# def print_equilibrium_profile_to_CSV(equilibrium_profile):
#     datetime_object = datetime.datetime.now()
#     file_name = "outputs/Simulation results " + \
#         str(datetime_object).replace(
#             " ", " at time ").replace(":", "-").split(".")[0] + ".csv"

#     # If file exists, wipe contents
#     if (os.path.isfile(file_name)):
#         f = open(file_name, "a+")
#         f.write("")
#     else:
#         f = open(file_name, "w+")

#     f.write(equilibrium_profile)
#     f.close()


# def size_absorption_column(previous_menu):
#     # Do some calculations
#     content = """ Final parameters:
#       x_Ai: %6.3f
#       y_Ai: %6.3f
#       x_AL: %6.3f
#       y_AG: %6.3f
#       dZ_L: %6.3f
#       dZ_V: %6.3f
#       Liquid Height: %6.3f
#       Vapour Height: %6.3f
#       Required Height: %6.3f


#       The equilibrium data profile may be found in /Outputs"""

#     print_equilibrium_profile_to_CSV(content)

#     results_menu = TextMenu(title="Results", message=content)
#     results_menu.navigate(previous_menu)


# def optimize_absorption_column(previous_menu):
#         # Do some calculations
#         # Create a string with final answers
#         # Create a menu object with the final answer string as the message
#         # Call meun object -> object.navigate(previous_menu)
#     pass


# about_us = """ This program was designed and built by Phil Sutherland
#  with some help from:
#    - Iain Bowie
#    - Dave Evans
#    - Rachel Elizabeth
#    - Ben King"""

# sizing_instructions = """   a) Open the file containing the software .java files
#    b) Double click on the 'Inputs' folder to access files
#       for input parameters, constants and equlibirum data
#    c) Open the text file called InputValues and enter
#       desired user-specified values for your column
#    d) Save the InputValues text file
#    e) Go to the AbsorptionDriver class, compile and run!
#    f) Find outputs for data analysis in the Outputs folder"""

# optimizing_instructions = """ a) Enter your user-inputs
#  b) Select 'Optimize Absorption Column'
#  c) The column will now be optimized"""

# about = TextMenu(
#     title="About", message=about_us)

# size_absorption_column_instructions = TextMenu(
#     title="Size Absorption Column Instructions", message=sizing_instructions)

# optimize_absorption_column_instructions = TextMenu(
#     title="Optimize Absorption Column Instructions", message=optimizing_instructions)

# size_absorption_column_menu = TextMenu(title="Size Absorption Column Menu", options={'Size Absorption Column': size_absorption_column,
#                                                                                      'Instructions': size_absorption_column_instructions.navigate, 'Return': 'return', 'Exit': 'exit'})

# optimize_absorption_column_menu = TextMenu(title="Optimize Absorption Column Menu",  options={'Optimize Absorption Column': optimize_absorption_column,
#                                                                                               'Instructions': optimize_absorption_column_instructions.navigate, 'Return': 'return', 'Exit': 'exit'})


# main_menu = TextMenu(title="Main Menu", options={'Size Absorption Column Menu': size_absorption_column_menu.navigate,
#                                                  'Optimize Absorption Column Menu': optimize_absorption_column_menu.navigate, 'About': about.navigate, 'Exit': 'exit'})


# main_menu.navigate(None)
