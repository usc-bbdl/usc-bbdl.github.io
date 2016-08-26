#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%% NEUROMECHANICS  %%%%%%%%%%%%%
# (c) Daniel A Hagen
# August 2016, version 1.0
# Filename: J2D2DOF.py
# Jacobian of 2D, 2DOF linkage system

import numpy as np 
import sympy as sp 

# Define the symbolic variables
G, J = sp.symbols('G J', real = True) # Vector Functions
angle1, angle2, x, y = sp.symbols('angle1 angle2 x y', real = True) # Degrees of Freedom
link1, link2 = sp.symbols('link1 link2', real = True) # System Parameters

# Define x and y coordinates of the endpoint
# Create Matrix for Geometric Model
x = link1*sp.cos(angle1) + link2*sp.cos(angle1+angle2)
y = link1*sp.sin(angle1) + link2*sp.sin(angle1+angle2)
G = sp.Matrix([x,y])

#Create Jacobian and its permutations
J = G.jacobian([angle1,angle2])
J_inv = J**-1
J_trans = J.T
J_inv_transpose = (J**-1).T 

print("G\n",G,"\n")
print("J\n",J,"\n")
print("J Inverse\n",J_inv,"\n")
print("J Transpose\n",J_trans,"\n")
print("J Inverse Transpose\n",J_inv_transpose,"\n")

# Numerical Example 1
# Define Link Lengths (m)
Link1 = 1
Link2 = 1
#Define Joint Angles (radians)
Angle1 = 0 # 0 degrees
Angle2 = np.pi/2 # 90 degrees

print("Evaluate the functions for these parameters:\n")
print("G:\n",G.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)]),"\n")
print("J:\n",J.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)]),"\n")
print("J Inverse:\n",J_inv.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)]),"\n")
print("J Transpose:\n",J_trans.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)]),"\n")
print("J Inverse Transpose:\n",J_inv_transpose.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)]),"\n")

# Numerical Example 2
print("Example of applying a positive angular velocity at Angle1 to find the resulting instantaneous endpoint velocity\n")
AngularVelocity1 = 1
AngularVelocity2 = 0
Velocity = J.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)])*np.matrix([[AngularVelocity1],[AngularVelocity2]])
print("Velocity:\n",Velocity,"\n")

print("Example of applying that same endpoint velocity to find the resulting instantaenous angular velocities\n")
AngularVelocities = J_inv.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)])*Velocity
print("Angular Velocities:\n",AngularVelocities,"\n")

print("Example of finding which torques produce a horizontal endpoint force vector in equilibrium\n")
Tau = J_trans.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)])*np.matrix([[1],[0]])
print("Torques:\n",Tau,"\n")

print("Example of applying those joint torques to find the resulting endpoint force vector in equilibrium\n")
Force = J_inv_transpose.subs([(angle1, Angle1), (angle2, Angle2), (link1, Link1), (link2, Link2)])*Tau
print("Force:\n",Force,"\n")
