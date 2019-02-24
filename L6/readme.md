# Python Programs for MCC SW Engineering Course

Author: Samuel Solorzano Ramirez (A00354798)

Course: Analysis, Design, and Construction of Software Systems

Teacher: Dr. Gerardo Padilla

Development Exercises - L6
-----

Create a class in python that Implements a method to sort large amount of data in lists (thousands and millions of items)The data comes intoCSV files.

### L6 - 25
Implement the method:
```
    set_input_data(file_path_name)
```
    
This methods sets the information about the file that will be used to read the dataDefine custom exceptions or error codes for situations where the parameter is incorrect or the file can not be read

### L6 - 26
Implement the method:
```
    set_output_data(file_path_name)
```
This methods sets the information about the file that will be used to store the sorted dataDefine custom exceptions or error codes for situations where the parameter is incorrect or the file can not be created

### L6 - 27
Implement the method:
```
    execute_merge_sort()
  ```
This methods sorts the data contained in the file specified. Define custom exceptions or error codes for situations where there may be special errors

### L6 - 28
Implement the method:
```
    execute_heap_sort()
  ```
This methods sorts the data contained in the file specified. Define custom exceptions or error codes for situations where there may be special errors

### L6 - 29
Implement the method:
```
    execute_quick_sort()
  ```
This methods sorts the data contained in the file specified. Define custom exceptions or error codes for situations where there may be special errors

### L6 - 29
Implement the method:
```
    get_performance_data()
```
This method returns the performance data associated to the last sorting execution[Number of Records Sorted, TimeConsumed, StartTime, EndTime]

Performance Data
-----

||Merge Sort| Heap Sort | Quick Sort |
|-|--|--|--|
|10 Records|0.1729 ms|0.2334 ms|0.1380 ms|
|100 Records|1.0550 ms|2.1756 ms|0.7780 ms|
|1000 Records|12.3720 ms|24.8044 ms|7.6756 ms|
|50000 Records|662.5686 ms|1849.8445 ms|489.5804 ms|
|500000 Records|7519.7983 ms|23746.1441 ms|5861.4044 ms|
|1000000 Records|16005.8062 ms|49871.1662 ms|12171.2594 ms|