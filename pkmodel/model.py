#
# Model class
#

class Model:
    def __init__(self, comp_num: int, V_c: float, V_p: list, Q_p: list, CL: float, dose_comp=0, constinput=0, centerpoints=None, magnitudes=None):
        """Initialises the class, and allows each of the input parameters to be used in other methods. """
        self.comp_num = comp_num
        self.V_c = V_c
        self.V_p = V_p
        self.Q_p = Q_p
        self.CL = CL
        self.dose_comp = dose_comp
        self.constinput = constinput
        self.centerpoints = centerpoints
        self.magnitudes = magnitudes



    @property
    def total_comp(self):
        """This property provides the total number of compartments present in the model."""
        if self.dose_comp > 0:
            total_number = self.comp_num + 2
        else:
            total_number = self.comp_num + 1
        return total_number


    def equations(self, t, y):
        """This function generates the right hand sides for the differential equations to be solved.
        The function returns one list containing the right hand sides. The equations corresponding to the
        peripheral compartments are stored first, followed by the main compartment, and finally the dosing compartment
        (if it is present).
        """
        dose = DoseFn(self.constinput, self.centerpoints, self.magnitudes)


        transitions = [0, 0]
        dYdt = [0,0,0,0]
        for i in range(0, self.comp_num):
            transition = (self.Q_p[i] * (y[self.comp_num] / self.V_c - y[i] / self.V_p[i]))
            transitions.append(transition)
            dYdt[i] = (transition)

        for i in range(self.comp_num,2):
            dYdt.pop(i)

        if self.dose_comp == 0:
            dYdt[self.comp_num] =  (dose.eval_at(t) - y[self.comp_num] * self.CL / self.V_c - transitions[-1] - transitions[-2])
            dYdt.pop(-1)
        elif self.dose_comp > 0:
            dYdt[self.comp_num] =  (self.dose_comp * y[self.comp_num +1] - y[self.comp_num] * self.CL / self.V_c - transitions[-1] - transitions[-2])
            dYdt[self.comp_num +1] =  (dose.eval_at(t) - self.dose_comp * y[self.comp_num +1])

        return dYdt
