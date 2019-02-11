"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L3 - 20
Given the time.clockfunction
Define a set of test cases that exercisethe function (Remember RightBICEP)
"""

import unittest
from time import clock, sleep

class test_time_clock(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clock_ok(self):
        start = clock()
        self.assertGreaterEqual(clock(), start)    


if __name__ == '__main__':
    unittest.main()