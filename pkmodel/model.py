#
# Model class
#
from dose import GaussConvFn, DoseFn

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
    constinput, centerpoints, magnitude: see Dose Class documentation.
    """
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

        if not((comp_num == 0 or comp_num == 1 or comp_num ==2)):
            print(f'Invalid Form of Arguments - comp_num:{type(self.comp_num)}')
            raise TypeError('Incompatible parameter types, comp_num must be 0, 1 or 2.')

        if (len(V_p) != comp_num) or (len(Q_p) != comp_num):
            print(f'V_p and Q_p need to be lists of length comp_num')
            raise IndexError('Incompatible list lengths, V_p and Q_p need to be lists of length comp_num.')

        if not((isinstance(V_c, float) or isinstance(V_c, int)) and V_c >=0):
            print(f'Invalid Form of Arguments - V_c:{type(self.V_c)}')
            raise TypeError('Incompatible parameter types, V_c must be a nonnegative number')

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
