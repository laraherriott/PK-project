#
# Solution class
#
#

import numpy as np
import scipy.integrate



def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]
class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, t_0=0, t_end=1, numsteps=1001):
        self.t_0 = t_0
        self.t_end = t_end
        self.numsteps = numsteps

    def solve(self, model, args,y0):
        t_eval = np.linspace(self.t_0, self.t_end, self.numsteps)
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: model(t, y, *args),
            t_span=[self.t_0,self.t_end],
            y0=y0, t_eval=t_eval,
        )
        return sol




# The purpose of the following code is just to play and learn with the solver.
# It should never be run within the whole package

if __name__ == '__main__':
    model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
    }

    model2_args = {
        'name': 'model2',
        'Q_p1': 2.0,
        'V_c': 1.0,
        'V_p1': 1.0,
        'CL': 1.0,
        'X': 1.0,
    }

    #t_eval = np.linspace(0, 1, 1000)
    #y0 = np.array([0.0, 0.0])
    solution = Solution()

    
    for model in [model1_args, model2_args]:
        args = [
            model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
        ]
        y0 = [0.0, 0.0]
        sol = solution.solve(rhs,args,y0)
        #print(sol.y)
        print(sol.y.shape)
        print('######################')


