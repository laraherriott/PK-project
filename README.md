[![Run unit tests](https://github.com/laraherriott/PK-project/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/laraherriott/PK-project/actions/workflows/unit-tests.yml)

[![Run on multiple OS](https://github.com/laraherriott/PK-project/actions/workflows/os-tests.yml/badge.svg)](https://github.com/laraherriott/PK-project/actions/workflows/os-tests.yml)

[![codecov](https://codecov.io/gh/laraherriott/PK-project/branch/master/graph/badge.svg?token=T1IG316M0W)](https://codecov.io/gh/laraherriott/PK-project)

# 2022 Software Engineering Project - Pharmacokinetics
This project contains a Python project to set-up, solve and visualise pharmacokinetic models.

## Authors
- [Lara Herriott](https://github.com/laraherriott)
- [Ruby Nixson](https://github.com/rubynixson)
- [Yiming Wei](https://github.com/weiym97)
- [Simiao Zhao](https://github.com/SimiaoZhao)

## Purpose
Pharmacokinetic problems are important to study for the purpose maintaining safe and effective drug concentrations in the body.
This project allows for the building of models that split the body into a main compartment, an optional dosing compartment, and up to two peripheral compartments.
The dosing type can also be specified, with options of either intraveneous or subcutaneous.
Intraveneous dosing provides a constant supply of drug to either the dosing compartment (if one exists), or the main compartment.
On the other hand, subcutaneous dosing supplies the drug in instantaneous bursts of specified magnitudes, at specified points in time.

## Installation
To install this package, we recommend that you first set up a virtual environment from the directory containing this file.

Then install this project:
```bash
pip install -e .[dev,docs]
```

## Using the package
Below is an example of how the classes work together to define, solve and visualise the model.
Two distinct models are defined. The first one has two peripheral compartments, a dose compartment, and operates with instantaneous dosing.
The second model has only one peripheral compartment, a dose compartment, and operates with constant dosing.

```python
from model import Model
from solution import Solution
from visualization import visualization
import matplotlib.pylab as plt

model1 = Model(comp_num=2, V_c=3, V_p=[3, 4], Q_p=[6, 9], CL=7, dose_comp=9, constinput=0, centerpoints=[1, 2, 3, 4], magnitudes=[1, 2, 3, 4])
model2 = Model(comp_num = 1, V_c = 3, V_p = [3], Q_p = [6], CL = 7, dose_comp = 9, constinput=5)

models = [model1, model2]

a = Solution(models, 0, 10)

all_solutions, all_specifications = a.generate_solutions()

visualization(all_solutions, all_specifications)
```
![Example output](https://github.com/laraherriott/PK-project/blob/2998fe1f579f84a9a6e0dd1a42066943854d3f62/pkmodel/model_specific_visual.png)
