"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

Development Exercises - L6 (Unit Tests)
Main function for list sorter module

Get's performance data to compare the sorting algorithms
"""

import csv
from list_sorter import *

def main():
    # filename = "L6/test_files/TenRecords.csv"
    # filename = "L6/test_files/HundredRecords.csv"
    # filename = "L6/test_files/ThousandRecords.csv"
    # filename = "L6/test_files/FiftyThousandRecords.csv"
    # filename = "L6/test_files/FiveHundredThousandRecords.csv"
    filename = "L6/test_files/OneMillion.csv"

    MergeSortList = ListSorter()
    MergeSortList.set_input_data(filename)
    MergeSortList.execute_merge_sort()
    MergeSort_perf_data = MergeSortList.get_performance_data()

    HeapSortList = ListSorter()
    HeapSortList.set_input_data(filename)
    HeapSortList.execute_heap_sort()
    HeapSort_perf_data = HeapSortList.get_performance_data()

    QuickSortList = ListSorter()
    QuickSortList.set_input_data(filename)
    QuickSortList.execute_quick_sort()
    QuickSort_perf_data = QuickSortList.get_performance_data()

    # out_filename = "00_TenRecordsRecordsPerfData.csv"    
    # out_filename = "01_HundredRecordsPerfData.csv"
    # out_filename = "02_ThousandRecordsPerfData.csv"
    # out_filename = "03_FiftyThousandRecordsPerfData.csv"
    # out_filename = "04_FiveHundredThousandRecordsPerfData.csv"
    out_filename = "05_OneMillionRecordsPerfData.csv"

    with open(out_filename, "w") as my_file:
        file_writer = csv.writer(my_file, delimiter = ',')
        file_writer.writerow([" ", "Merge Sort", "Heap Sort", "Quick Sort"])
        file_writer.writerow(["NumberOfRecordsSorted"
                            , str(MergeSort_perf_data.NumberOfRecordsSorted)
                            , str(HeapSort_perf_data.NumberOfRecordsSorted)
                            , str(QuickSort_perf_data.NumberOfRecordsSorted)])
        file_writer.writerow(["TimeConsumed"
                            , str(MergeSort_perf_data.TimeConsumed)
                            , str(HeapSort_perf_data.TimeConsumed)
                            , str(QuickSort_perf_data.TimeConsumed)])


if __name__ == '__main__':
    main()