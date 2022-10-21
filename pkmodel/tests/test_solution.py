import unittest
import warnings


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_error(self):
        """
        Tests Warnings are being raised.
        """
        from dose import DoseFn
        from model import Model
        from solution import Solution

        model = Model(comp_num=1, V_c=3, V_p=[3, 4], Q_p=[6, 9], CL=7, dose_comp=9, constinput=5)
        models = [model]
        a = Solution(models, 0, 10, y0=[0.0, 0.0])
        a.generate_solutions()
        with warnings.catch_warnings(record=True) as w:
            self.assertEqual(len(a.y0), model.total_comp)

    def test_list(self):
        """
        Tests non-list is being converted.
        """
        from dose import DoseFn
        from model import Model
        from solution import Solution

        model = Model(comp_num=1, V_c=3, V_p=[3, 4], Q_p=[6, 9], CL=7, dose_comp=9, constinput=5)
        a = Solution(model, 0, 10)
        assert isinstance(a.models, list)

    def test_no_solutions(self):
        """
        Tests model.equation() generates the correct number of equations which are then solved for.
        """
        from dose import DoseFn
        from model import Model
        from solution import Solution

        no_peripherals = 1
        total_compartments = 1 + no_peripherals
        ka = 9
        if ka > 0:
            total_compartments += 1
        model = Model(comp_num=no_peripherals, V_c=3, V_p=[3, 4], Q_p=[6, 9], CL=7, dose_comp=ka, constinput=5)
        a = Solution(model, 0, 10)
        all_solutions, all_specifications = a.generate_solutions()
        self.assertEqual(total_compartments, len(all_solutions[0].y))
