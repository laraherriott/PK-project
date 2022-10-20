#
# Solution class
#
#

import numpy as np
import scipy.integrate


class Solution:

    """A Pharmokinetic (PK) model solution
    """

    def __init__(self, models: list, t_0=0, t_end=1, numsteps=1001, y0=None):
        """
        params:
        models: list of model objects
        t_0: numeric, optional
            start time
        t_end: numeric, optional
            end time
        numsteps: numeric, optional
            number of time steps
        y0: list, optional
            initial values in order: peripheral compartments, central compartment, dosage compartment
            If no y0 is specified by the user, y0=0 for each equation.
        """
        self.models = models
        self.t_eval = np.linspace(t_0, t_end, numsteps)
        
        if self.y0 is None:
            self.y0 = [0.0]*model.total_comp
        else:
            self.y0 = y0


    def generate_solutions(self):
        """
        Solve the model ODE for each model specified.

        return
        all_solutions: list containing the solution class for each model returned by scipy.integrate.solve_ivp
        all_specifications: list containing user specifications for each model, for visualisation
        """
        all_solutions = []
        all_specifications = []
        for model in self.models:
        
            solution = scipy.integrate.solve_ivp(fun=lambda t, y: model.equations(t, y), t_span=[self.t_eval[0], self.t_eval[-1]], y0=self.y0, t_eval=self.t_eval)
            specifications = [model.comp_num, model.constinput, model.dose_comp]

            all_solutions.append(solution)
            all_specifications.append(specifications)

        return all_solutions, all_specifications
