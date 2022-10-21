import unittest
import numpy as np


class DoseTest(unittest.TestCase):
    """
    Tests the class in Dose Module, including GaussConvGn and DoseFn class
    """
    def test_GaussConvFn(self):
        """
        Tests the class GaussConvFn
        """
        from pkmodel.dose import GaussConvFn

        function = GaussConvFn(center=1.0, magnitude=0.5)
        xs = np.array([0.5, 1.0, 1.5])
        ys = function.eval_at(xs)
        self.assertEqual(ys[0], ys[-1])
        self.assertEqual(np.max(ys), ys[1])

        function2 = GaussConvFn(center=2.0, magnitude=0.5)
        self.assertEqual(function.eval_at(1.1), function2.eval_at(2.1))

        function3 = GaussConvFn(center=1.0, magnitude=1.0)
        self.assertEqual(function.eval_at(0.9), 0.5 * function3.eval_at(0.9))

    def test_DoseFn(self):
        """
        Test the class DoseFn
        """
        from pkmodel.dose import DoseFn
        instan_dose_time = [1.0, 2.0, 3.0]
        instan_dose_magnitude = [1., 1., 1.]
        constinput = 1.0
        function = DoseFn(constinput=constinput,
                          centerpoints=instan_dose_time,
                          magnitudes=instan_dose_magnitude)

        self.assertEqual(function.eval_at(1.0), function.eval_at(3.0))
        self.assertEqual(function.eval_at(0.0), 1.0)
        self.assertEqual(function.eval_at(2.0), function.eval_at(1.0))
