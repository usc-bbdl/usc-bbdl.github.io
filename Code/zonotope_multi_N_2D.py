#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%% NEUROMECHANICS %%%%%%%%%%%%%
# (c) Francisco Valero-Cuevas
# August 2016, version 2.0
# Filename: zonotope_muti_N.py

# This script shows how to map N-dimensional N-cubes into 2D and 3D via a
# random H matrix of dimensions 2 x N and 3 x N, respectively.

# It then plots the convex hulls of the zonotopes when considering 
# the input to be between 3 and 8 dimensions. That is, a system having 3 to
# 8 muscles

import numpy as np 
import itertools
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import random

#%%%%%%%%%%%%%%%%%% User Input %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Enter the dimensions of the input space here. Note it must be >=3 
LargestDimension = 8 # this is the largest dimension

# Iterate to calculate the zonotopes for inout dimensions from 3 to 8

def GenerateActivationSpaceVertices(dim):
	"""
	This function takes the place of the Matlab function ncube.m.
	Takes in a dimension (dim) and gives all of the vertices needed 
	for a Minkowski sum.
	"""
	output = np.matrix(list(itertools.product([0, 1], repeat=dim))).T
	return(output)

X = [GenerateActivationSpaceVertices(i) for i in range(3,LargestDimension+1)]
H = np.random.rand(3,LargestDimension)*2-1 # this is the random full 3x8 H matrix.
Vertices = [np.array(H[:2,:i]*X[i-3]) for i in range(3,LargestDimension+1)]
Hull = [ConvexHull(Vertices[i-3].T) for i in range(3,LargestDimension+1)]

def Plot2DConvHull(ax,Vertices,Hull,Matrix):
	#ax.plot(Vertices[:,0],Vertices[:,1],'ko')
	for simplex in Hull.simplices:
	    ax.plot(Vertices[simplex,0],Vertices[simplex,1], color = 'grey')

plt.figure()
ax = plt.gca()
[Plot2DConvHull(ax,Vertices[i-3].T,Hull[i-3],H[:2,:i]) for i in range(3,LargestDimension+1)]
UsedVertices = np.array([0.,0.])
for i in range(3,LargestDimension+1):
	RandomVertex = Vertices[i-3].T[random.choice(random.choice(Hull[i-3].simplices))]
	while np.any(RandomVertex == UsedVertices):
		RandomVertex = Vertices[i-3].T[random.choice(random.choice(Hull[i-3].simplices))]
	plt.text(RandomVertex[0], RandomVertex[1], str(i)+" Muscles")
	UsedVertices = np.concatenate((UsedVertices,RandomVertex),axis=0)
plt.show()