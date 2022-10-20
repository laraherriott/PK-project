from model import Model
from solution import Solution
from visualization import visualization
import matplotlib.pylab as plt

model1 = Model(comp_num=2, V_c=3, V_p=[3, 4], Q_p=[6, 9], CL=7, dose_comp=9, constinput=0, centerpoints=[1, 2, 3, 4], magnitudes=[1, 2, 3, 4])
#model2 = Model(comp_num = 1, V_c = 3, V_p = [3,4], Q_p = [6,9], CL = 7, dose_comp = 9, constinput=0, centerpoints=[1,2,3,4], magnitudes=[1,2,3, 4])

models = [model1]

a = Solution(models, 0, 10)

all_solutions, all_specifications = a.generate_solutions()

visualization(all_solutions, all_specifications)
