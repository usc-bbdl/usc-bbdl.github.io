#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%% NEUROMECHANICS  %%%%%%%%%%%%%
# (c) Daniel A Hagen
# August 2016, version 2.0
# Filename: simple_inverse_kinematics
# Example of linearized inverse kinematics
# for a 2D2DOF_system

import numpy as np 
import sympy as sp 
from numpy import pi 
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def quick_2D_plot_tool(xlabel,ylabel,title):
	"""
	This will take in the x and y labels as well as a figure title and
	format an already established figure to remove the box, place the
	tick marks outwards, and set aspect ratio to equal.
	"""
	ax = plt.gca()
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_title(title)
	ax.set_aspect('equal', 'datalim')
def InverseJacobianMatrix(Theta1,Theta2,Link1,Link2):
	"""
	Utilizes symbolics to create a Jacobian matrix and its inverse
	transpose. Only appropriate for a 2 link planar model. Theta1 and
	Theta2 must be symbolics. Link lengths must be scalar.
	"""
	G = sp.Matrix([	Link1*sp.cos(Theta1)+Link2*sp.cos(Theta1+Theta2),\
					Link1*sp.sin(Theta1)+Link2*sp.sin(Theta1+Theta2)	])
	J = G.jacobian([Theta1,Theta2])
	J_inv= J**-1
	return(J_inv)
def TwoLinkTrajectory(Angle1,Angle2,Link1,Link2):
	x = Link1*np.cos(Angle1) + Link2*np.cos(Angle1+Angle2)
	y = Link1*np.sin(Angle1) + Link2*np.sin(Angle1+Angle2)
	return(x,y)

radius = 5
X = np.array([[radius*np.cos(theta),radius*np.sin(theta)] for theta in np.linspace(0,np.pi,10)])
Xi = interp1d(X[:,0],X[:,1], kind = 'cubic')
Interpolated_X = np.array([np.arange(-5,5,0.01), Xi(np.arange(-5,5,0.01))])

# Plot interpolated trajectory
def PlotInterpolatedData(X,Interpolated_X):
	plt.figure()
	plt.plot(X[:,0],X[:,1],'ko')
	plt.plot(Interpolated_X[0],Interpolated_X[1])
	quick_2D_plot_tool('','','Circle Trajectory')
	plt.show()

#PlotInterpolatedData(X,Interpolated_X)

# Now implement the linearized inverse kinematic relationship:
# q_i = q_(i-1) + dq = q_(i-1) + (J**-1)*dX(i-1)
start = 101
end = 802
Theta1, Theta2 = sp.symbols('Theta1 Theta2', real = True)
J_inverse = InverseJacobianMatrix(Theta1,Theta2,3,4)
Angle1 = np.zeros(len(range(start,end)))
Angle2 = np.zeros(len(range(start,end)))
Angle1[0] = np.pi/2
Angle2[0] = np.pi/2
for i in range(start,end-1):
	dX = Interpolated_X.T[i]-Interpolated_X.T[i-1]
	dq = J_inverse.subs([(Theta1,Angle1[i-start]),(Theta2,Angle2[i-start])])*dX
	Angle1[i-start+1] = Angle1[i-start] + dq[0]
	Angle2[i-start+1] = Angle2[i-start] + dq[1]

def PlotResults(X,Interpolated_X,Angle1,Angle2):
	plt.figure()
	plt.plot(Interpolated_X[0],Interpolated_X[1],'b--')
	quick_2D_plot_tool('','','Circle Trajectory')
	x,y = TwoLinkTrajectory(Angle1,Angle2,3,4)
	for i in range(100,601,100):
			plt.plot(np.cumsum([0,3*np.cos(Angle1[i]),4*np.cos(Angle1[i]+Angle2[i])]),\
					np.cumsum([0,3*np.sin(Angle1[i]),4*np.sin(Angle1[i]+Angle2[i])]),\
					'o-', lw = 2, color = '0.75', markeredgecolor = '0.75')
	plt.plot(np.cumsum([0,3*np.cos(Angle1[0]),4*np.cos(Angle1[0]+Angle2[0])]),\
				np.cumsum([0,3*np.sin(Angle1[0]),4*np.sin(Angle1[0]+Angle2[0])]),\
				'ko-', lw = 3)
	plt.plot(np.cumsum([0,3*np.cos(Angle1[end-start-1]),4*np.cos(Angle1[end-start-1]+Angle2[end-start-1])]),\
				np.cumsum([0,3*np.sin(Angle1[end-start-1]),4*np.sin(Angle1[end-start-1]+Angle2[end-start-1])]),\
				'ko-', lw = 3)
	plt.plot(x,y,'r')
	plt.show()

PlotResults(X,Interpolated_X,Angle1,Angle2)
