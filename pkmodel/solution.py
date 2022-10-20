#
# Solution class
#
#

import numpy as np
import scipy.integrate

class Solution:
    """A Pharmokinetic (PK) model solution,
    running from t_0 to t_end with N time steps
    """
    def __init__(self, t_0=0, t_end=1, numsteps=1001):
        '''
        params:
        t_0: start time
        t_end: end time
        numsteps: number of time steps
        '''
        self.t_0 = t_0
        self.t_end = t_end
        self.numsteps = numsteps

    def solve(self, model, args,y0:list):
        '''
        Solve the model ODE with initial value y0
        params:
        model: the ODE
        args: value of parameters in the ODE,
        y0: the initial value, length should be the same as ODE's variables.
        return
        sol: solution class returned by scipy.integrate.solve_ivp 
        '''
        t_eval = np.linspace(self.t_0, self.t_end, self.numsteps)
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: model(t, y, *args),
            t_span=[self.t_0,self.t_end],
            y0=y0, t_eval=t_eval,
        )
        return sol

def dose(t, X):
    return X
'''
def dose(t,x, doze_time:list):
    # for the continuous part,
    # No matter t, we return x
    if protocol == 'continuous':
        return X
    elif: 
    # If the protocol is delta
    #we only return x at specific time point
        if t in doze_time:
            return X
        else:
            return 0
'''
def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]
         

# The purpose of the following code is just to play and learn with the solver.
# It should never be run within the whole package

if __name__ == '__main__':

    ### Now we just need to write a small demo here
    t_0 = 0.0
    t_end = 1.0
    numsteps = 101
    t_eval = np.linspace(t_0,t_end,numsteps)
    y0 = [0.0]
    dosefn = DoseFn(0.0,[0.25,0.5,0.75],[2,1,1])
    #dozefn = GaussConvFn(0.25,1)
    xs = t_eval
    ys = []
    for x in xs:
        ys.append(dosefn.eval_at(x))
    import matplotlib.pyplot as plt
    plt.plot(xs,np.array(ys))
    plt.title('Input delta function')
    plt.savefig('Input_delta_function_2.jpg')
    plt.close()
    '''
    sol = scipy.integrate.solve_ivp(fun=lambda t,y:const_increase(t,y),
                                    t_span=[t_0,t_end],
                                    y0=y0,
                                    t_eval=t_eval)
    print(sol.y)
    print('#########################')
    '''
    sol = scipy.integrate.solve_ivp(fun=lambda t,y:dozefn.eval_at(t),
                                    t_span=[t_0,t_end],
                                    y0=y0,
                                    t_eval=t_eval)
    print(sol.y.shape)
    print(sol.t.shape)
    plt.plot(sol.t,sol.y[0,:])
    plt.title('Solution')
    plt.savefig('Result_2.jpg')
    plt.close()
    #print(sol.t)
    #print(sol.y)
    '''
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
    '''



