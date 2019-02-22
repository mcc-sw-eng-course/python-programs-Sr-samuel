"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

Development Exercises - L6 (Unit Tests)
Unit tests for the ListSorter class
"""
import sys
sys.path.append('/L6')
import unittest
from list_sorter import ListSorter

class ListSorter_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_listsorter_InputDataValid(self):
        ls = ListSorter()
        ls.set_input_data("L6/data1.csv")
        print(ls.working_list)

if __name__ == '__main__':
    unittest.main()