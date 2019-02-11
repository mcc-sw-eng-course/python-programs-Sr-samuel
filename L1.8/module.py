"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L1 - 8
Write a module containing different function that computes the:
- Sample Mean
- Sample standard deviation
- Median
- A function that returns the n-quartil
- A function that returns the n-percentil
"""
def get_sample_mean(sample):
    mean = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            for x in sample:
                number = float(x)
                mean = mean + number
            mean = mean / len(sample)
    return mean

import math
def get_sample_standard_dev(sample):
    sdev = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            mean = get_sample_mean(sample)
            variance = 0
            for x in sample:
                number = mean - float(x)
                variance = variance + (number*number)
            variance = variance / len(sample)
            sdev = math.sqrt(variance)
    return sdev

def get_sample_median(sample):
    median = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            if length % 2 == 0 :
                middle = int(length/2)
                median = ( float(sample_sorted[middle-1]) + float(sample_sorted[middle])) / 2.0
            else:
                middle = int((length)/2)
                median = sample_sorted[middle]
    return median

class Quartil:
    LOW, MID, HIGH = range(0, 3)

def get_n_quartil(quart, sample):
    lowQ = 0
    highQ = 0
    midQ = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            middle = int(length/2)
            if (length % 2 == 0):
                lowQ = get_sample_median(sample_sorted[:middle])
                highQ = get_sample_median(sample_sorted[middle:])
            else:
                lowQ = get_sample_median(sample_sorted[:middle])
                highQ = get_sample_median(sample_sorted[middle+1:])
            midQ = get_sample_median(sample_sorted)
    if quart == Quartil.LOW:
        return lowQ
    elif quart == Quartil.MID:
        return midQ
    elif quart == Quartil.HIGH:
        return highQ
    else:
        return None

def get_n_percentil(per, sample):
    perc = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            index = per * length # get the % index in the array
            index = int(index + 1) # round it up
            perc = sample_sorted[index-1]
    return perc

def get_list_from_file(filename):
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def main():
    working_sample = get_list_from_file("dataset_1.txt")
    print(f'The Mean is: {get_sample_mean(working_sample)}')
    print(f'The Std. Dev is: {get_sample_standard_dev(working_sample)}')
    print(f'The Median is: {get_sample_median(working_sample)}')
    print(f'The Low Quartil is: {get_n_quartil(Quartil.LOW, working_sample)}')
    print(f'The Mid Quartil is: {get_n_quartil(Quartil.MID, working_sample)}')
    print(f'The High Quartil is: {get_n_quartil(Quartil.HIGH, working_sample)}')
    print(f'The 50th Percentil is: {get_n_percentil(0.5, working_sample)}')
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
