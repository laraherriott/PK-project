#
# Model class
#




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
    def __init__(self, name, comp_num: int, V_c: float, V_p: list, Q_p: list, CL: float, dose_comp=0):
        """Initialises the class, and provides empty sets for the desired outputs."""
        self.rhs = []
        self.dep_varbs = []
        self.comp_num = comp_num
        self.V_c = V_c
        self.V_p = V_p
        self.Q_p = Q_p
        self.CL = CL
        self.dose_comp = dose_comp
        self.name = name

    @property
    def equations(self):
        """This function generates the lists of dependent variables and right hand sides for the differential equations, 
        based on the inputs of the number of compartments required.
        The function returns two lists: the first list contains the dependent variables that we will solve for.
        The second list contains the right hand sides of the differential equations.
        The indices match between the two lists: for example, if q_c is the third entry in the 
        dependent variables list, it's corresponding differential equation will be in the third entry of
        the right hand side lists.  """
        q_n = [q_p1, q_p2, q_0, q_c]
        transitions = [0, 0]
        for i in range(0, self.comp_num):
            self.dep_varbs.append(q_n[i])
            transition = self.Q_p[i] * (q_n[3] / self.V_c - q_n[i] / self.V_p[i])
            transitions.append(transition)
            self.rhs.append(transition)
        
        if self.dose_comp == 0:
            self.dep_varbs.append(q_n[3])
            self.rhs.append( Dose - q_n[3] * self.CL / self.V_c - transitions[-1] - transitions[-2])
        elif self.dose_comp > 0:
            self.dep_varbs.append(q_n[3])
            self.dep_varbs.append(q_n[2])
            self.rhs.append( self.dose_comp * q_n[2] - q_n[3] * self.CL / self.V_c - transitions[-1] - transitions[-2])
            self.rhs.append( Dose - self.dose_comp * q_n[2])

        return [self.dep_varbs, self.rhs]
    
    def __str__(self):
        """Allows for models to be named."""
        return self.name

Dose = 5
q_p1 = 1
q_p2 = 2
q_0 = 3
q_c = 4

model1 = Model("Model123",comp_num = 2, V_c = 3, V_p = [6,7], Q_p = [3,4], CL = 7, dose_comp = 7)
print(model1)
print(model1.V_p)
print(model1.equations)

