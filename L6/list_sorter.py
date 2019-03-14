"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

Development Exercises - L6
Create a class in python that Implements a method to sort large amount of data in lists 
(thousands and millions of items) 
The data comes into CSV files.
"""

import csv
import os
from pathlib import Path
from enum import Enum
import time
from sort_algorithms import mergeSort, quickSort, heapSort

def is_float(value: str) -> bool:
    return_value = False
    try:
        float(value)
        return_value = True
    except:
        return_value = False
    return return_value

class StatusCode(Enum):
    SUCCESS = 0
    FAILURE = 1
    PARAM_ERROR = 2
    NOT_A_FILE = 3
    FILE_ERROR = 4
    INVALID_FILE_EXTENSION = 5
    LIST_IS_EMPTY = 6
    LIST_ALREADY_SORTED = 7

class PerformanceData():
    def __init__(self):
        self.NumberOfRecordsSorted = 0
        self.TimeConsumed = 0
        self.StartTime = 0
        self.EndTime = 0

    def start_performance_measurement(self, NumberOfRecords: int):
        self.NumberOfRecordsSorted = NumberOfRecords
        self.StartTime = time.time()

    def end_performance_measurement(self):
        self.EndTime = time.time()
        self.TimeConsumed = "{0:.4f} ms".format((self.EndTime - self.StartTime)*1000)


class ListSorter():
    def __init__(self):
        self.working_list = ()
        self.already_sorted = False
        self.performance_data = PerformanceData()

    def set_input_data(self, file_path_name: str) -> StatusCode:
        """ Tries to open the file with the given file_path_name and read the values to a list
        Arguments:
        file_path_name -- File Name that will be used to create a file
        Returns a valid StatusCode:
        SUCCESS     -- Data set from the file stored in the list correctly
        PARAM_ERROR -- file_path_name was not a valid string
        NOT_A_FILE  -- Input file_path_name is not a file
        INVALID_FILE_EXTENSION -- Input file_path_name is not a csv file
        """
        status_code = StatusCode.FAILURE
        if isinstance(file_path_name, str):
            input_file = Path(file_path_name)
            if input_file.is_file():
                if file_path_name.endswith(".csv"):
                    with open(file_path_name, "r") as my_file:
                        dialect = csv.Sniffer().sniff(my_file.read(4096))
                        # very simple detection for a valid csv format
                        if dialect.delimiter != ',':
                            status_code = StatusCode.FILE_ERROR
                        else:
                            my_file.seek(0)
                            file_content = my_file.read()
                            # ToDo Check is csv module can be used to parse the whole file...
                            self.working_list = [float(x) for x in file_content.split(',') if is_float(x)]
                            status_code = StatusCode.SUCCESS
                else:
                    status_code = StatusCode.INVALID_FILE_EXTENSION
            else:
                status_code = StatusCode.NOT_A_FILE
        else:
            status_code = StatusCode.PARAM_ERROR
        return status_code
    
    def set_output_data(self, file_path_name: str) -> StatusCode:
        """ Writes the list to the given file_path_name
        Arguments:
        file_path_name -- File Name that will be used to create a file
        Returns a valid StatusCode:
        SUCCESS     -- File Written correctly
        PARAM_ERROR -- file_path_name was not a valid string
        """
        status_code = StatusCode.FAILURE
        if isinstance(file_path_name, str):
            with open(file_path_name, "w") as my_file:
                csv_writer = csv.writer(my_file, delimiter=',')
                csv_writer.writerow(self.working_list)
            status_code = StatusCode.SUCCESS
        else:
            status_code = StatusCode.PARAM_ERROR
        return status_code

    def execute_merge_sort(self):
        """ It will sort the list using the merge sort.
        List must not be empty, and must not be previously sorted
        """
        status_code = StatusCode.FAILURE
        if len(self.working_list) > 0:
            if self.already_sorted == False:
                self.performance_data.start_performance_measurement(len(self.working_list))
                mergeSort(self.working_list)
                self.performance_data.end_performance_measurement()
                self.already_sorted = True
                status_code = StatusCode.SUCCESS
            else:
                status_code = StatusCode.LIST_ALREADY_SORTED
        else:
            status_code = StatusCode.LIST_IS_EMPTY
        return status_code

    def execute_heap_sort(self):
        if len(self.working_list) > 0:
            if self.already_sorted == False:
                self.performance_data.start_performance_measurement(len(self.working_list))
                heapSort(self.working_list)
                self.performance_data.end_performance_measurement()
                self.already_sorted = True
                status_code = StatusCode.SUCCESS
            else:
                status_code = StatusCode.LIST_ALREADY_SORTED
        else:
            status_code = StatusCode.LIST_IS_EMPTY
        return status_code

    def execute_quick_sort(self):
        if len(self.working_list) > 0:
            if self.already_sorted == False:
                self.performance_data.start_performance_measurement(len(self.working_list))
                quickSort(self.working_list)
                self.performance_data.end_performance_measurement()
                self.already_sorted = True
                status_code = StatusCode.SUCCESS
            else:
                status_code = StatusCode.LIST_ALREADY_SORTED
        else:
            status_code = StatusCode.LIST_IS_EMPTY
        return status_code

    def get_performance_data(self) -> PerformanceData:
        return self.performance_data


# def rows(f, chunksize=1024):
    """
    Read a file where the row separator is ',' lazily.

    Usage:

    >>> with open('big.csv') as f:
    >>>     for r in rows(f):
    >>>         process(row)
    """
    """
    incomplete_row = None
    while True:
        chunk = f.read(chunksize)
        if not chunk: # End of file
            if incomplete_row is not None:
                yield incomplete_row
                break
        # Split the chunk as long as possible
        while True:
            i = chunk.find(',')
            if i == -1:
                break
                
            # If there is an incomplete row waiting to be yielded,
            # prepend it and set it back to None
            if incomplete_row is not None:
                yield incomplete_row + chunk[:i]
                incomplete_row = None
            else:
                yield chunk[:i]
            chunk = chunk[i+1:]
        # If the chunk contained no separator, it needs to be appended to
        # the current incomplete row.
        if incomplete_row is not None:
            incomplete_row += chunk
        else:
            incomplete_row = chunk

in_files = [
    "L6/test_files/01_TenRecords.csv",
    "L6/test_files/02_HundredRecords.csv",
    "L6/test_files/03_ThousandRecords.csv",
    "L6/test_files/04_FiftyThousandRecords.csv",
    "L6/test_files/05_FiveHundredThousandRecords.csv",
    "L6/test_files/06_OneMillion.csv",
    "L6/test_files/07_TenMillion.csv",
    "L6/test_files/08_FiftyMillion.csv"
]

filename = "../L6/test_files/06_OneMillion.csv"

def test():
    a = []
    start = time.time()
    with open(filename) as f:
         for r in rows(f):
            a.append(float(r))
            pass
    end = time.time()
    read_time = end-start
    print("Read file to Memory: {0:.4f} ms".format((end - start)*1000))
    start = time.time()
    quickSort(a)
    end = time.time()
    sort_time = end-start
    print("Sort: Len({0}): {1:.4f} ms".format(len(a),  (end - start)*1000))
    print("Total Time: Len({0}): {1:.4f} ms".format(len(a),  (sort_time + read_time)*1000))

"""