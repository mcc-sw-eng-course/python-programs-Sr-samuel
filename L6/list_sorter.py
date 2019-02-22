"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

Development Exercises - L6
Create a class in python that Implements a method to sort large amount of data in lists 
(thousands and millions of items)The data comes into CSV files.
"""

from enum import Enum
from pathlib import Path

class StatusCode(Enum):
    SUCCESS = 0
    FAILURE = 1
    PARAM_ERROR = 2
    NOT_A_FILE = 3
    FILE_ERROR = 4
    INVALID_FILE_EXTENSION = 5

class ListSorter():
    def __init__(self):
        self.working_list = ()
        self.already_sorted = False

    def set_input_data(self, filename: str):
        """ Tries to open the file with the given filename and read the values to a list
        Arguments:
        filename -- File Name that will be used to create a file
        """
        if isinstance(filename, str):
            input_file = Path(filename)
            if input_file.is_file():
                if filename.endswith(".csv"):
                    with open(filename, "r") as my_file:
                        # Todo validate that all elements in the file are float numbers
                        file_content = my_file.read()
                        self.working_list = [float(x) if x.isdigit() else x for x in file_content.split(',')]
                        if all(isinstance(x, float) for x in self.working_list):
                            print("All Float")
                else:
                    return StatusCode.INVALID_FILE_EXTENSION
            else:
                return StatusCode.NOT_A_FILE
        else:
            return StatusCode.PARAM_ERROR
        pass
    

