"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L1 - 9
Write a function that converts a decimal number into a Roman format
"""

limit = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

def to_roman_format(dec):
    result = ""
    if dec > 0:
        if dec < 5000:
            for idx, val in enumerate(limit):
                while dec >= val:
                    result += roman[idx]
                    dec -= val
    return result

import random
def main():
    decimal = random.randint(1,5000)
    roman_fmt = to_roman_format(decimal)
    print(f'The Roman Format of {decimal} is: {roman_fmt}')
    
if __name__ == "__main__":
    # execute only if run as a script
    main()