# Simple Linear Programming Example
# using the Diet Problem from Ch 5.2.2 
# of Fundamentals of Neuromechanics
# (c) Daniel A Hagen
# August 2016
# University of Southern California

import numpy as np 
from scipy.optimize import linprog
import matplotlib.pyplot as plt 

Oatmeal = {'Cost': 3, 'Energy': 110, 'Protein': 4, 'Calcium': 2, 'MaxServings': 4}
Chicken = {'Cost': 24, 'Energy': 205, 'Protein': 32, 'Calcium': 12, 'MaxServings': 3}
Eggs = {'Cost': 13, 'Energy': 160, 'Protein': 13, 'Calcium': 54, 'MaxServings': 2}
WholeMilk = {'Cost': 9, 'Energy': 160, 'Protein': 8, 'Calcium': 285, 'MaxServings': 8}
CherryPie = {'Cost': 20, 'Energy': 420, 'Protein': 4, 'Calcium': 22, 'MaxServings': 2}
PorkAndBeans = {'Cost': 19, 'Energy': 260, 'Protein': 14, 'Calcium': 80, 'MaxServings': 2}

# Define Cost Function TO BE MINIMIZED
Cost = np.array([Oatmeal['Cost'], Chicken['Cost'], Eggs['Cost'], \
					WholeMilk['Cost'], CherryPie['Cost'], PorkAndBeans['Cost']])

print("Cost Function Array to be Minimized (c)\n",Cost,"\n")

# Define Constraint functions (for python, the upper and lower
# bounds are handled later in the linprog() function).
# NOTE: Because we want to have MORE than a prescribed amount
# of Energy, Protein, and Calcium, they will be negative values 
# in each Constraint array. This will make the constraint functions
# 'greater than or equal to' the Energy, Protein, and Calcium 
# benchmarks (to be defined below). If you  wanted to have less than 
# a certain amount, remove the negative sign.
Energy = -np.array([Oatmeal['Energy'], Chicken['Energy'], Eggs['Energy'], \
					WholeMilk['Energy'], CherryPie['Energy'], PorkAndBeans['Energy']])
Protein = -np.array([Oatmeal['Protein'], Chicken['Protein'], Eggs['Protein'], \
					WholeMilk['Protein'], CherryPie['Protein'], PorkAndBeans['Protein']])
Calcium = -np.array([Oatmeal['Calcium'], Chicken['Calcium'], Eggs['Calcium'], \
					WholeMilk['Calcium'], CherryPie['Calcium'], PorkAndBeans['Calcium']])
A = np.concatenate(([Energy],[Protein],[Calcium]), axis=0)

print("Constraint Matrix A \n",A,"\n")

# Define b array (equality conditions for constraint functions)
# NOTE: Because we want to have MORE than a prescribed amount
# of Energy, Protein, and Calcium, they will be negative values 
# in our b array. This will make the constraints 'greater than or
# equal to' the Energy, Protein, and Calcium benchmarks. If you
# wanted to have less than a certain amount, remove the negative sign.
b = np.array([-2000,-55,-800])

print("b array for Constraint Matrix A (minus the variable bounds)\n",np.matrix(b).T,"\n")

# Define Bounds to be used by linprog()
OatmealBounds = (0,Oatmeal['MaxServings'])
ChickenBounds = (0,Chicken['MaxServings'])
EggsBounds = (0,Eggs['MaxServings'])
WholeMilkBounds = (0,WholeMilk['MaxServings'])
CherryPieBounds = (0,CherryPie['MaxServings'])
PorkAndBeansBounds = (0,PorkAndBeans['MaxServings'])

# Find and print optimal solution
x = linprog(Cost,A_ub = A, b_ub = b,\
			bounds = (OatmealBounds, ChickenBounds, EggsBounds, \
						WholeMilkBounds, CherryPieBounds, PorkAndBeansBounds))

print("With these dietary restrictions the optimal choice will be to eat:\n")
print("{} Oatmeal\n{} Chicken\n{} Eggs\n{} Whole Milk\n{} Cherry Pie\n{} Pork and Beans\n"\
		.format(x['x'][0],x['x'][1],x['x'][2],x['x'][3],x['x'][4],x['x'][5]))