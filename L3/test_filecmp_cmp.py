"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L3 - 19
Given the filecmp.cmp function
Define a set of test cases that exercisethe function (Remember RightBICEP)
"""

import unittest
from filecmp import cmp

import os

class test_filecmp_cmp(unittest.TestCase):
    # def setUp(self):
    #     with open("test1.txt", "w") as my_file:
    #         my_file.write("equal file")
    #     with open("test2.txt", "w") as my_file:
    #         my_file.write("equal file")
    #     with open("test3.txt", "w") as my_file:
    #         my_file.write("not equal file")

    # def tearDown(self):
    #     os.remove("test1.txt")
    #     os.remove("test2.txt")
    #     os.remove("test3.txt")

    def create_file_with_content(self, filename: str, content: str):
        """ Creates a file
        Arguments:
        filename -- File Name that will be used to create a file
        content -- This content will be copied to the file after is created
        """
        if isinstance(filename, str) and isinstance(content, str):
            with open(filename, "w") as my_file:
                my_file.write(content)

    def create_binary_file_random_content(self, filename: str, size: int):
        """ Creates a binary file with random data
        Arguments:
        filename -- File Name that will be used to create a file
        size -- size in kb of the data to include in the file
        """
        if isinstance(filename, str) and isinstance(size, int):
            with open(filename, "wb") as my_file:
                my_file.write(os.urandom(size))
                
    def delete_file(self, filename: str):
        os.remove(filename)

    def test_cmp_invalidfiles(self):
        self.assertRaises(FileNotFoundError, cmp, "", "")

    def test_cmp_oneInvalidFileInPar1(self):
        test_file = "test1.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.assertRaises(FileNotFoundError, cmp, "test1.txt", "")
        self.delete_file(test_file)

    def test_cmp_oneInvalidFileInPar2(self):
        test_file = "test1.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.assertRaises(FileNotFoundError, cmp, "", "test1.txt")
        self.delete_file(test_file)

    def test_cmp_samefileShallowFalse(self):
        test_file = "test1.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.assertEqual(True, cmp(test_file, test_file, False))
        self.delete_file(test_file)

    def test_cmp_samefileShallowTrue(self):
        test_file = "test1.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.assertEqual(True, cmp(test_file, test_file, True))
        self.delete_file(test_file)

    def test_cmp_diffFileShallowFalse(self):
        test_file = "test1.txt"
        test_file_2 = "test2.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.create_file_with_content(test_file_2, "Different Content!!!")
        self.assertEqual(False, cmp(test_file, test_file_2, False))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

    def test_cmp_diffFileShallowTrue(self):
        test_file = "test1.txt"
        test_file_2 = "test2.txt"
        self.create_file_with_content(test_file, "My Content!!!")
        self.create_file_with_content(test_file_2, "Different Content!!!")
        self.assertEqual(False, cmp(test_file, test_file_2, True))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

    def test_cmp_diffFileSameContentShallowTrue(self):
        test_file = "test1.txt"
        test_file_2 = "test2.txt"
        self.create_file_with_content(test_file, "Same Content :D")
        self.create_file_with_content(test_file_2, "Same Content :D")
        self.assertEqual(True, cmp(test_file, test_file_2, True))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

    def test_cmp_diffFileSameContentShallowFalse(self):
        test_file = "test1.txt"
        test_file_2 = "test2.txt"
        self.create_file_with_content(test_file, "Same Content :D")
        self.create_file_with_content(test_file_2, "Same Content :D")
        self.assertEqual(True, cmp(test_file, test_file_2, False))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

    def test_cmp_diffBinaryFiles(self):
        test_file = "test_binary1.txt"
        test_file_2 = "test_binary2.txt"
        self.create_binary_file_random_content(test_file, 1024*1024)
        self.create_binary_file_random_content(test_file_2, 100*1024)
        self.assertEqual(False, cmp(test_file, test_file_2))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

    def test_cmp_BinFilevsNonBinFile(self):
        test_file = "test_binary1.txt"
        test_file_2 = "test2.txt"
        self.create_binary_file_random_content(test_file, 1024*1024)
        self.create_file_with_content(test_file_2, "My non binary content in the file!!!")
        self.assertEqual(False, cmp(test_file, test_file_2))
        self.delete_file(test_file)
        self.delete_file(test_file_2)

if __name__ == '__main__':
    unittest.main()