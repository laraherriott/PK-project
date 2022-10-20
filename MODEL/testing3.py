#
# Model class
#

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class Model:
    """A Pharmokinetic (PK) model
    Parameters
    ----------
    comp_num: integer
        States the number of peripheral compartments to be included.
        
    V_c: float
        Specifies the volume of the central compartment.

    V_p: list
        Specifies the volumes of the peripheral compartments. If no peripheral compartments are needed, input an empty list.

    Q_p: list
        Specifies the transition rates between the central compartment and any peripheral compartments. If no peripheral compartments are needed, input an empty list.

    CL: float
        Specifies the clearance/elimination rate for the central compartment.

    dose_comp: integer, optional
        If a dose compartment is to be included, input dose_comp as the value of k_a. If no value is given, a dose compartment will not be included.


    """
    def __init__(self, comp_num: int, V_c: float, V_p: list, Q_p: list, CL: float, dose_comp=0):
        """Initialises the class, and provides empty sets for the desired outputs."""
        self.comp_num = comp_num
        self.V_c = V_c
        self.V_p = V_p
        self.Q_p = Q_p
        self.CL = CL
        self.dose_comp = dose_comp

    
    @property
    def total_comp(self):
        """This property provides the total number of compartments present in the model."""
        if self.dose_comp > 0:
            total_number = self.comp_num + 2
        else:
            total_number = self.comp_num + 1
        return total_number


    def equations(self, y):
        """This function generates the right hand sides for the differential equations to be solved.
        The function returns one list containing the right hand sides. The equations corresponding to the 
        peripheral compartments are stored first, followed by the main compartment, and finally the dosing compartment
        (if it is present).
        """
        
        transitions = [0, 0]
        dYdt = [0,0,0,0]
        for i in range(0, self.comp_num):
            transition = (self.Q_p[i] * (y[self.comp_num] / self.V_c - y[i] / self.V_p[i]))
            transitions.append(transition)
            dYdt[i] = (transition)

        for i in range(self.comp_num,2):
            dYdt.pop(i)

        if self.dose_comp == 0:
            dYdt[self.comp_num] =  (Dose - y[self.comp_num] * self.CL / self.V_c - transitions[-1] - transitions[-2])
            dYdt.pop(-1)
        elif self.dose_comp > 0:
            dYdt[self.comp_num] =  (self.dose_comp * y[self.comp_num +1] - y[self.comp_num] * self.CL / self.V_c - transitions[-1] - transitions[-2])
            dYdt[self.comp_num +1] =  (Dose - self.dose_comp * y[self.comp_num +1])

        return dYdt
    


Dose = 50
model1 = Model(comp_num = 1, V_c = 3, V_p = [3], Q_p = [6], CL = 7, dose_comp = 0)
t = np.linspace(0,10, 100)


print(model1.total_comp)

y0 = [0,0]
# ODE solve
Yt = odeint(lambda y,t: model1.equations(y), y0, t)
plt.plot(t,Yt[:,0],linewidth = 1, label='q_p1(t)')
plt.plot(t,Yt[:,1],linewidth = 1, label = 'q_c(t)')
#plt.plot(t,Yt[:,2],linewidth = 1, label = 'q_c(t)')
#plt.plot(t,Yt[:,3],linewidth = 1, label = 'q_0(t)')
plt.legend()
plt.xlabel('Time(sec)')
plt.show()



"""
model1 = Model("Model123",comp_num = 2, V_c = 3, V_p = [6,7], Q_p = [3,4], CL = 7, dose_comp = 7)
print(model1)
print(model1.V_p)
print(model1.equations)
"""