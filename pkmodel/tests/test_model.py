import unittest

import sys
sys.path.append("..")
from model import Model
from dose import GaussConvFn, DoseFn



class ModelTest(unittest.TestCase):

    def test_model_list_length(self):
        """
        Tests that an error is thrown when the length of Q_p or V_p is not equal to comp_num.
        """
        with self.assertRaises(IndexError):
            model1 = Model(2, 2, [1], [1,2], 9.0)


    def test_model_comp_num(self):
        """
        Tests that an error is thrown when comp_num is not either 0, 1 or 2.
        """
        with self.assertRaises(TypeError):
            model2 = Model("Hello", 2, [1], [1], 9.0)
            model3 = Model(-6, 2, [1], [1], 9.0)
            model4 = Model(7, 2, [3], [4], 6)


    def test_model_V_c(self):
        """
        Tests that an error is thrown when V_c is not a nonnegative float or integer.
        """
        with self.assertRaises(TypeError):
            model2 = Model(1, -6, [1], [1], 9.0)
            model3 = Model(1, [3,4], [1], [1], 9.0)
            model4 = Model(1, "Hello", [3], [4], 6)



if __name__ == '__main__': 
    unittest.main()
