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
import os
import unittest
import random
from list_sorter import *

class ListSorter_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def create_csvfile_with_content(self, filename: str, content: list):
    #     """ Creates a file
    #     Arguments:
    #     filename -- File Name that will be used to create a file
    #     content -- This content will be copied to the file after is created
    #     """
    #     if isinstance(filename, str) and isinstance(content, list):
    #         with open(filename, "w") as my_file:
    #             file_writer = csv.writer(my_file, delimiter = ',', quoting=csv.QUOTE_NONNUMERIC)
    #             file_writer.writerow(content)

    def create_csvfile_random_content(self, filename: str, size: int):
        """ Creates a csv file with random float content
        Arguments:
        filename -- File Name that will be used to create a file
        size -- quantity of float numbers to create
        """
        low_limit = 0
        high_limit = 5000
        if isinstance(filename, str) and isinstance(size, int):
            with open(filename, "w") as my_file:
                file_writer = csv.writer(my_file, delimiter = ',', quoting=csv.QUOTE_NONNUMERIC)
                file_writer.writerow([random.uniform(low_limit, high_limit) for x in range(size)])
        

    def create_file_with_content(self, filename: str, content: str):
        """ Creates a file
        Arguments:
        filename -- File Name that will be used to create a file
        content -- This content will be copied to the file after is created
        """
        if isinstance(filename, str) and isinstance(content, str):
            with open(filename, "w") as my_file:
                my_file.write(content)

    def delete_file(self, filename: str):
        os.remove(filename)

    # Tests for "is_float" function
    def test_isFloat_ValidFloat(self):
        self.assertTrue(is_float('5.0'))

    def test_isFloat_ValidNegativeFloat(self):
        self.assertTrue(is_float('-5.0'))

    def test_isFloat_ValidInt(self):
        self.assertTrue(is_float('5'))

    def test_isFloat_ValidNegativeInt(self):
        self.assertTrue(is_float('-5'))

    def test_isFloat_NotAFloat(self):
        self.assertFalse(is_float('abc'))

    # Tests for "set_input_data" function
    def test_listsorter_InvalidCSVFile(self):
        ls = ListSorter()
        filename = "InvalidFile.csv"
        self.create_file_with_content(filename, "123  456   765\n567 876 987 hi")
        self.assertEqual(StatusCode.FILE_ERROR, ls.set_input_data(filename))
        self.delete_file(filename)

    def test_listsorter_NotACVSFile(self):
        ls = ListSorter()
        filename = "NotACSVFile.txt"
        self.create_csvfile_random_content(filename, 10)
        self.assertEqual(StatusCode.INVALID_FILE_EXTENSION, ls.set_input_data(filename))
        self.delete_file(filename)

    def test_listsorter_NotAFile(self):
        ls = ListSorter()
        filename = "IDoNotExist.txt"
        self.assertEqual(StatusCode.NOT_A_FILE, ls.set_input_data(filename))

    def test_listsorter_InvalidFilename(self):
        ls = ListSorter()
        filename = 55
        self.assertEqual(StatusCode.PARAM_ERROR, ls.set_input_data(filename))

    def test_listsorter_ValidCSVFile(self):
        ls = ListSorter()
        filename = "ValidFile.csv"
        self.create_csvfile_random_content(filename, 50000)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(filename))
        self.delete_file(filename)

    # Tests for "set_output_data" function
    def test_listsorter_ValidOutput(self):
        ls = ListSorter()
        in_filename = "ValidFile.csv"
        out_filename = "OutputFile.csv"
        self.create_csvfile_random_content(in_filename, 50)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.delete_file(in_filename)
        self.delete_file(out_filename)

    def test_listsorter_InvalidParam(self):
        ls = ListSorter()
        out_filename = 55
        self.assertEqual(StatusCode.PARAM_ERROR, ls.set_output_data(out_filename))

    # testing merge_sort
    def test_listsorter_MergeSort(self):
        ls = ListSorter()
        in_filename = "MergeSort.csv"
        out_filename = "SortedMergeSort.csv"
        self.create_csvfile_random_content(in_filename, 5)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_merge_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.delete_file(in_filename)
        self.delete_file(out_filename)
    
    def test_listsorter_MergeSortAlreadySorted(self):
        ls = ListSorter()
        in_filename = "MergeSort.csv"
        out_filename = "SortedMergeSort.csv"
        self.create_csvfile_random_content(in_filename, 10)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_merge_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.assertEqual(StatusCode.LIST_ALREADY_SORTED, ls.execute_merge_sort())
        self.delete_file(in_filename)
        self.delete_file(out_filename)

    def test_listsorter_MergeSortEmptyList(self):
        ls = ListSorter()
        self.assertEqual(StatusCode.LIST_IS_EMPTY, ls.execute_merge_sort())

    # testing heapSort
    def test_listsorter_HeapSort(self):
        ls = ListSorter()
        in_filename = "HeapSortData.csv"
        out_filename = "SortedByHeapSort.csv"
        self.create_csvfile_random_content(in_filename, 5)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_heap_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.delete_file(in_filename)
        self.delete_file(out_filename)
    
    def test_listsorter_HeapSortAlreadySorted(self):
        ls = ListSorter()
        in_filename = "HeapSortData.csv"
        out_filename = "SortedByHeapSort.csv"
        self.create_csvfile_random_content(in_filename, 10)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_heap_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.assertEqual(StatusCode.LIST_ALREADY_SORTED, ls.execute_heap_sort())
        self.delete_file(in_filename)
        self.delete_file(out_filename)

    def test_listsorter_HeapSortEmptyList(self):
        ls = ListSorter()
        self.assertEqual(StatusCode.LIST_IS_EMPTY, ls.execute_heap_sort())

    # testing quickSort
    def test_listsorter_QuickSort(self):
        ls = ListSorter()
        in_filename = "QuickSortData.csv"
        out_filename = "SortedByQuickSort.csv"
        self.create_csvfile_random_content(in_filename, 5)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_quick_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.delete_file(in_filename)
        self.delete_file(out_filename)
    
    def test_listsorter_QuickSortAlreadySorted(self):
        ls = ListSorter()
        in_filename = "QuickSortData.csv"
        out_filename = "SortedByQuickSort.csv"
        self.create_csvfile_random_content(in_filename, 10)
        self.assertEqual(StatusCode.SUCCESS, ls.set_input_data(in_filename))
        self.assertEqual(StatusCode.SUCCESS, ls.execute_quick_sort())
        self.assertEqual(StatusCode.SUCCESS, ls.set_output_data(out_filename))
        self.assertEqual(StatusCode.LIST_ALREADY_SORTED, ls.execute_quick_sort())
        self.delete_file(in_filename)
        self.delete_file(out_filename)

    def test_listsorter_QuickSortEmptyList(self):
        ls = ListSorter()
        self.assertEqual(StatusCode.LIST_IS_EMPTY, ls.execute_quick_sort())

if __name__ == '__main__':
    unittest.main()