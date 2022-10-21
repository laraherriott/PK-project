#
# Solution class
#
#

import numpy as np
import scipy.integrate
import warnings


class Solution:

    """A Pharmokinetic (PK) model solution
    """

    def __init__(self, models: list, t_0=0, t_end=1, numsteps=1001, y0=[0.0]):
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
        """

        if isinstance(models, list):
            self.models = models
        else:
            self.models = [models]
        self.t_eval = np.linspace(t_0, t_end, numsteps)
        self.y0 = y0

    def generate_solutions(self):
        """
        Solve the model ODE for each model specified.

        If no y0 is specified by the user, y0=0 for each equation

        return
        all_solutions: list containing the solution class for each model returned by scipy.integrate.solve_ivp
        all_specifications: list containing user specifications for each model, for visualisation
        """

        all_solutions = []
        all_specifications = []
        count = 0
        for model in self.models:
            if self.y0 == [0.0]:
                self.y0 = [0.0]*model.total_comp
            if len(self.y0) != model.total_comp:
                if count == 0:
                    warnings.warn("The specified y0 array does not match the number of model compartments, y0 for all compartments has been taken as 0")
                self.y0 = [0.0]*model.total_comp

            solution = scipy.integrate.solve_ivp(fun=lambda t, y: model.equations(t, y), t_span=[self.t_eval[0], self.t_eval[-1]], y0=self.y0, t_eval=self.t_eval)

            if model.constinput != 0:
                protocol = 1
            else:
                protocol = 0


            if model.dose_comp != 0:
                dose_type = 1
            else:
                dose_type = 0

            specifications = [model.comp_num, dose_type, protocol]


            all_solutions.append(solution)
            all_specifications.append(specifications)
            count += 1

        return all_solutions, all_specifications
