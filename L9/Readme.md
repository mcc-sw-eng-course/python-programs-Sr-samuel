# Python Programs for MCC SW Engineering Course

Author: Samuel Solorzano Ramirez (A00354798)

Course: Analysis, Design, and Construction of Software Systems

Teacher: Dr. Gerardo Padilla

### Optimizations done to improve the Algorithm from L6:

- The csv is now read as a binary file
- The csv file is parsed with a Regular Expression
- There are two implementation
  - Single Process
    - The csv file is read one line a time, and immediately the line is sorted
    - Each line is added to a list using a generator
    - heapq.merge is used to merge all the sorted lists
  - Multiple Process 
    - The csv file is divided in chunk, depending on the file size (file size / core_count)
    - each chunk is handled by one process. This process sorts the chunk
    - heapq.merge is used to merge all the sorted chunks

### Performance data:

CPU used AMD Ryzen 5 1600x

#### 500k Float values (File size: 8.8 MiB)

Single Process:
```
Sorted with 1 Process in 1318.3606 ms
Merged 500 lists in 300.6513 ms
Total time: Len(500000) in  1619.0119 ms
```

Multi Process: 
```
Sorted with 9 Processes in 389.2829 ms
Merged 9 lists in 194.9699 ms
Total time: Len(500000) in  584.2528 ms
```

#### 1m Float values (File size: 17.5 MiB)

Single Process:
```
Sorted with 1 Process in 2720.5145 ms
Merged 1000 lists in 652.4737 ms
Total time: Len(1000000) in  3372.9882 ms
```

Multi Process: 
```
Sorted with 12 Processes in 567.0099 ms
Merged 12 lists in 391.8083 ms
Total time: Len(1000000) in  958.8182 ms
```

#### 10m Float values (File size: 175.4 MiB)

Single Process:
```
Sorted with 1 Process in 27490.9608 ms
Merged 10000 lists in 10145.2851 ms
Total time: Len(10000000) in  37636.2460 ms
```

Multi Process: 
```
Sorted with 12 Processes in 6673.6963 ms
Merged 12 lists in 4174.1056 ms
Total time: Len(10000000) in  10847.8019 ms
```

#### 50m Float values (File size: 877 MiB)

Single Process:
```
Sorted with 1 Process in 134348.0389 ms
Merged 50000 lists in 93664.5560 ms
Total time: Len(50000000) in  228012.5949 ms
```

Multi Process: 
```
Sorted with 12 Processes in 35127.5425 ms
Merged 12 lists in 20628.2051 ms
Total time: Len(50000000) in  55755.7476 ms
```

#### 100m Float Values (File size: 1.7 GiB)

Single Process:
```
Not Tested
```

Multi Process: 
```
Sorted with 12 Processes in 75273.7057 ms
Merged 12 lists in 42377.7840 ms
Total time: Len(100000000) in  117651.4897 ms
```

Multi Process (Using MMAP to access the file) ~ 4 sec faster: 
```
Sorted with 12 Processes in 71919.8825 ms
Merged 12 lists in 43048.8040 ms
Total time: Len(100000000) in  114968.6866 ms
```