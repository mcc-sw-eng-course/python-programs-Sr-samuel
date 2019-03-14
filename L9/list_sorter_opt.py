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

import sys
# sys.path.append('../L6')
import csv  # Generate csv file
import os   # File size of the cvs
import time  # Get performance data
from sort_algorithms import mergeSort, quickSort, heapSort
import array  # it's faster to use the array than the list
import heapq  # to merge the results of all threads
import random # Generate csv file with random content
import re     # Regular Expression
import math  
import mmap   # not use, but can map the file to memory for faster access
from multiprocessing import Process, Manager, cpu_count

def get_chunks(file: str, size=1024*1024):
    """
    Divides the file in chunks
    Arguments:
    file: Name of the file to sort
    size: The size of the chunk to get
    Return:
    Chunk[0] - start position of the chunk (bytes)
    Chunk[1] - end position of the chunk (bytes)
    """
    f = open(file, "br")
    while 1:
        start = f.tell()
        f.seek((size), 1)
        s = f.readline()
        yield start, f.tell() - start
        if not s:
            break

file_under_test = "04_10mNumber.csv"

def read_sort_single():

    iters = [] # store the results of each line
    start = time.time()
    
    pat = re.compile(b"(\d+\.\d+)", re.VERBOSE) # regexp to match the csv file

    # open the file as binay, and use the binary regexpr in the file
    matches = (pat.findall(line) for line in open(file_under_test, 'rb'))
    # get all the matche into an iterator
    results_matches    = (match for match in matches if match)

    # iterates on all matches and sort them using quickSort
    for page in results_matches:
        a = array.array('f')
        a.fromlist([float(i) for i in page])
        quickSort(a)
        iters.append(a)

    end = time.time()
    sort_time = end - start
    print("Sorted with 1 Process in {0:.4f} ms".format((sort_time)*1000))
    start = time.time()
    # all the results are merged back using heapq.merge
    a = array.array('f')
    for x in heapq.merge(*iters):
        a.append(x)
        
    end = time.time()
    merge_time = end - start
    print("Merged {0} lists in {1:.4f} ms".format(len(iters), (merge_time)*1000))
    print("Total time: Len({0}) in  {1:.4f} ms".format(len(a), (sort_time+merge_time)*1000))
    pass

def read_sort_multi_process(my_file, chunk, results):
    """
    This function will sort a chunk from the given file, and store the results in the 
    Manager list
    """
    pat = re.compile(b"(\d+\.\d+)")
    f = open(my_file, 'rb')
    f.seek(chunk[0])
    a = array.array('f')
    a.fromlist([float(i) for i in pat.findall(f.read(chunk[1]))])
    quickSort(a)
    results.append(a)

filemap = None
def read_sort_multi_process_mmap(my_file, chunk, results):
    global filemap, fileobj
    pat = re.compile(b"(\d+\.\d+)")
    if filemap is None or fileobj.name != my_file:
        fileobj = open(my_file, "rb")
        filemap = mmap.mmap(
            fileobj.fileno(), os.path.getsize(my_file), access=mmap.ACCESS_READ
            )
    a = array.array('f')
    a.fromlist([float(i) for i in pat.findall(filemap, chunk[0], chunk[0]+chunk[1])])
    quickSort(a)
    results.append(a)

def read_sort_multi():

    start = time.time()

    my_file = file_under_test
    cpu_qty = cpu_count() # amount of CPU in the computer
    one_mb =  (1024*1024)

    # get the chunk size, minimum is 1 (means everythin in 1 CPU)
    chunksize = max(1, os.path.getsize(my_file) / cpu_qty / one_mb)
    queue = [] # store all the chunks
    
    # distribute the chunks
    for chunk in get_chunks(my_file, math.ceil(chunksize*one_mb)):
        queue.append(chunk)

    manager = Manager() # shared memory for the threads
    results = manager.list()
    jobs = [] # store all the process, in order to wait for them 

    for chunk in queue:
        p = Process(target=read_sort_multi_process, args=(my_file,chunk,results))
        jobs.append(p)
        p.start()
        pass

    for proc in jobs:
        proc.join() # wait for all the process to finished

    end = time.time()
    sort_time = end - start
    print("Sorted with {0} Processes in {1:.4f} ms".format(len(queue), (sort_time)*1000))

    start = time.time()
    a = array.array('f')
    for r in heapq.merge(*results):
        a.append(r)

    # open("Results.txt", "wb").write(a)
        
    end = time.time()
    merge_time = end - start
    print("Merged {0} lists in {1:.4f} ms".format(len(results),  (merge_time)*1000))
    print("Total time: Len({0}) in  {1:.4f} ms".format(len(a), (sort_time+merge_time)*1000))
    pass

def create_csvfile_random_content(filename: str, size: int):
    """ Creates a csv file with random float content
    Arguments:
    filename -- File Name that will be used to create a file
    size -- quantity of float numbers to create
    """
    low_limit = 0
    high_limit = 5000
    numbers_per_line = 1000
    if isinstance(filename, str) and isinstance(size, int):
        amount = 0
        with open(filename, "w") as my_file:
            file_writer = csv.writer(my_file, delimiter = ',')
            while (not amount >= size):
                file_writer.writerow([random.uniform(low_limit, high_limit) for x in range(numbers_per_line)])
                amount += numbers_per_line
    print("created...")

if __name__ == '__main__':
    read_sort_single()
    read_sort_multi()

    pass
