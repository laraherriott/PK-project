import numpy as np

class Protocol:
    def __init__(self, protocol, peak, dose_time=0):
        self.protocol = protocol
        self.peak = peak
        self.dose_time = dose_time

    @property
    def set_up(self):
        if self.protocol == 'continuous':
            return self.peak
        if self.protocol == 'delta':
            dose_matrix = np.column_stack((self.dose_time, self.peak))
            return dose_matrix


protocol1 = Protocol('delta', [3, 2, 1], [0.1, 0.5, 0.7])
protocol2 = Protocol('continuous', 3)
protocols = [protocol1, protocol2]

class Model:
    def __init__(self):
        # xyz
        return

    def create_equations(self):
        # xyz
        return  # [equations]


model1 = Model('model paramaters and specifications')
model2 = Model('another set of specifications')


models = [model1, model2]

class Solution:

    def __init__(self, models, protocols, t_eval, y0=None):
        self.models = models
        self.protocols = protocols
        self.t_eval = t_eval
        self.y0 = y0

    @property
    def generate_solutions(self):
        all_solutions = []
        for model in self.models:

            if self.y0 is None:
                self.y0 = [0.0]*model.comp_num

            if type(self.protocols.protocol) == 'continuous':
                # model_choice = model.create_equations()
                dose = self.protocols.set_up  # value input into Protocol class for dose peak
                solution = scipy.integrate.solve_ivp(fun=lambda t, y: model.equations, t_span=[t_eval[0], t_eval[-1]], y0=y0, t_eval=t_eval)
                all_solutions.append(solution)

            if type(self.protocols.protocol) == 'delta':
                # model_choice =  model.create_equations()
                dose = 0
                final_solution = []
                t_count = 0
                for i in range(dim(self.protocols.set_up[1]):
                    t_max = self.protocols.set_up[i, 0]
                    # solve...
                    # but with t_span = [t_count, t_max]
                    # and y0 = y0
                    solution = scipy.integrate.solve_ivp(fun=lambda t, y: model.equations, t_span=[t_count, t_max], y0=y0, t_eval=t_eval)
                    final_solution.append(solution)
                    t_count += t_max
                    y0[-1] = solution[-1, t_max] + self.protocols.set_up[i, 1]
                    for j in range(0,len(y0)-1):
                        y0[j] = solution[j, t_max]

                # solve...
                # with t_span = [t_count, t_eval[-1]]
                # and y0 = y0
                solution = scipy.integrate.solve_ivp(fun=lambda t, y: model.equations, t_span=[t_count, t_eval[-1]], y0=y0, t_eval=t_eval)
                final_solution.append(solution)
                all_solutions.append(final_solution)
        return all_solutions


solution = Solution(model1, dose_protocol)
solution.generate_solutions
