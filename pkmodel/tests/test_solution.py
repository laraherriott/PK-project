import unittest

import numpy as np

from pkmodel.solution import Solution



class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        class PseudoModel():
            def __init__(self):
                self.comp = 0
                self.comp_num = 1
                self.total_comp = 1
                self.constinput = 0
                self.dose_comp = 0

            def equations(self,t,y):
                return 1.0
        
        
        models = [PseudoModel()]
        
        t_0 = 0.0
        t_end = 1.0
                
        solution = Solution(models,t_0=t_0,t_end=t_end)
        sol,all_attributes = solution.generate_solutions()
        
        self.assertAlmostEqual(1.0,sol[0].y[0,-1])

