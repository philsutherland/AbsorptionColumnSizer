from resources.text_menu import TextMenu
from formatting.formatted_text_menu import FormattedTextMenu
import os

print("\n" + FormattedTextMenu.main_title("Welcome to AbsorbSim Pro V2.0"))


def size_absorption_column(previous_menu):
    # Do some calculations
    # Create a string with final answers
    # Create a menu object with the final answer string as the message
    pass


def optimize_absorption_column(previous_menu):
    # Do some calculations
    # Create a string with final answers
    # Create a menu object with the final answer string as the message
    # Call meun object -> object.navigate(previous_menu)
    pass


sizing_instructions = """   a) Open the file containing the software .java files
   b) Double click on the 'Inputs' folder to access files
      for input parameters, constants and equlibirum data
   c) Open the text file called InputValues and enter
      desired user-specified values for your column
   d) Save the InputValues text file
   e) Go to the AbsorptionDriver class, compile and run!
   f) Find outputs for data analysis in the Outputs folder"""

optimizing_instructions = """ a) Enter your user-inputs
 b) Select 'Optimize Absorption Column'
 c) The column will now be optimized"""

size_absorption_column_instructions = TextMenu(
    title="Size Absorption Column Instructions", message=sizing_instructions, options={'Return': 'return', 'Exit': 'exit'})

optimize_absorption_column_instructions = TextMenu(
    title="Optimize Absorption Column Instructions", message=optimizing_instructions, options={'Return': 'return', 'Exit': 'exit'})

size_absorption_column_menu = TextMenu(title="Size Absorption Column Menu", message="", options={'Size Absorption Column': size_absorption_column,
                                                                                                 'Instructions': size_absorption_column_instructions.navigate, 'Return': 'return', 'Exit': 'exit'})

optimize_absorption_column_menu = TextMenu(title="Optimize Absorption Column Menu", message="", options={'Optimize Absorption Column': optimize_absorption_column,
                                                                                                         'Instructions': optimize_absorption_column_instructions.navigate, 'Return': 'return', 'Exit': 'exit'})


main_menu = TextMenu(title="Main Menu", message="", options={'Size Absorption Column Menu': size_absorption_column_menu.navigate,
                                                             'Optimize Absorption Column Menu': optimize_absorption_column_menu.navigate, 'About': 'about', 'Exit': 'exit'})


# size_absorption_column_instructions.navigate(None)
main_menu.navigate(None)
