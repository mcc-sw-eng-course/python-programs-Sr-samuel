import sys
sys.path.append('../L1.8')
import unittest
from l1_8_module import *

class test_l1_8_module_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mean_SameValueList(self):
        test_list = [2,2,2,2,2]
        self.assertEqual(2, get_sample_mean(test_list))

    def test_mean_OneElementList(self):
        test_list = [2]
        self.assertEqual(2, get_sample_mean(test_list))

    def test_mean_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_mean(test_list))

    def test_mean_InvalidList(self):
        test_list = 789
        self.assertEqual(0, get_sample_mean(test_list))

    def test_mean_ListWithNumberStrings(self):
        test_list = ["5", "5", "5", "5", "5"]
        self.assertEqual(5, get_sample_mean(test_list))

    def test_mean_ListWithTextStrings(self):
        test_list = ["abc", "def", "ghi", "jkl", "mno"]
        self.assertRaises(ValueError, get_sample_mean, test_list)

    def test_stdDev_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_NotAlList(self):
        test_list = 200
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_ListWithNumberStrings(self):
        test_list = ["5", "5", "5", "5", "5"]
        self.assertEqual(0, get_sample_standard_dev(test_list))

    def test_stdDev_ListWithTextStrings(self):
        test_list = ["abc", "def", "ghi", "jkl", "mno"]
        self.assertRaises(ValueError, get_sample_standard_dev, test_list)

    def test_stdDev_ValidList(self):
        test_list = [1,2,3,4,5]
        self.assertEqual(1.4142135623730951, get_sample_standard_dev(test_list))

    def test_median_ValidListOdd(self):
        test_list = [1,2,3,4,5]
        self.assertEqual(3, get_sample_median(test_list))

    def test_median_ValidListEven(self):
        test_list = [1,2,3,4,5,6]
        self.assertEqual(3.5, get_sample_median(test_list))

    def test_median_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_sample_median(test_list))

    def test_median_NotAList(self):
        test_list = 450
        self.assertEqual(0, get_sample_median(test_list))

    def test_quartil_NotAList(self):
        test_list = 450
        self.assertEqual(0, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_LowQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(3, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_LowQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(3, get_n_quartil(Quartil.LOW, test_list))

    def test_quartil_MidQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(5.5, get_n_quartil(Quartil.MID, test_list))

    def test_quartil_MidQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(6, get_n_quartil(Quartil.MID, test_list))

    def test_quartil_HighSQuartilEven(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(8, get_n_quartil(Quartil.HIGH, test_list))

    def test_quartil_HighQuartilOdd(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(9, get_n_quartil(Quartil.HIGH, test_list))

    def test_quartil_InvalidQuartil(self):
        test_list = [1,2,3,5,4,6,7,10,9,8,11]
        self.assertEqual(None, get_n_quartil(5, test_list))

    def test_percentil_NotAList(self):
        test_list = 50
        self.assertEqual(0, get_n_percentil(0, test_list))

    def test_percentil_EmptyList(self):
        test_list = []
        self.assertEqual(0, get_n_percentil(0, test_list))

    def test_percentil_ValidPerc(self):
        test_list = [1,2,3,5,4,6,7,10,9,8]
        self.assertEqual(6, get_n_percentil(0.5, test_list))
    
if __name__ == "__main__":
    unittest.main()