# (c) Daniel A Hagen
# August 2016, version 1.0
# Filename: FiveDOF_ArmModel_Neuromechanics_V5.py
# Example of fiber length changes and fiber velocities
# for a frisbee throw motion with a 5-DOF, 17-muscle arm model

import numpy as np 
from scipy.io import loadmat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load all data from FiveDOF_Model.mat by using scipy.io.loadmat()
# Conversion from dict to variables is done for easier reading.
# MUST MAKE SURE THAT FiveDOF_Model.mat IS DOWNLOADED TO THE 
# SAME FOLDER AS FiveDOF_model_frisbee_throw.py
# Special thanks to Emily Lawrence for the MATLAB code and sample data.
output = loadmat('FiveDOF_Model.mat')
UpperArm, LowerArm, Hand = float(output['L1']),float(output['L2']),float(output['L3'])
ExtRotation, Adduction = output['angle_ext_rot_ds_rad'].T[0], output['angle_add_ds_rad'].T[0]
HorizAdduction, ElbowFlexion = output['angle_horiz_add_ds_rad'].T[0], output['angle_elbow_ds_rad'].T[0]
WristFlexion = output['angle_wrist_ds_rad'].T[0] 
r, OptimalLength = output['R'].T[0], output['lo'].T[0]
del(output)

# Define Movement Duration
# ChangeInTime is the amount of time between successive postures
# of the arm. There are 44 postures during the throwing motion,
# from start to realease.
# ChangeInTime = 3.8 therefore produces a throw movement duration
# of 167.2 ms from start to release, indicated by a red arm in
# the plot of arm postures. SpeedUpFactor, originally set to 1,
# lengthens the duration by that factor.

SpeedUpFactor = 1
ChangeInTime = 3.8/SpeedUpFactor

# Nominal Model - Joint Angles

# Initiation - 34 postures: from posture  1 to 34
# Throw-to-release - 29 postures: from posture 35 to 64
# Deceleration of throw - 15 postures: from posture 65 to 78

# The first 34 postures are initiation of the throw, as subject starts
# pointing frisbee at target (arm straight out to side) then draws the
# frisbee back to posture 35. The subject initiates the throw from posture
# 35 to release at posture 64. We will only consider post-Initiation phase
# postures (35-78).

Range = range(34,78)

def create_range(Range, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion):
	result = test = np.concatenate((np.array(ExtRotation[Range],ndmin=2), \
									np.array(Adduction[Range],ndmin=2), \
									np.array(HorizAdduction[Range],ndmin=2), \
									np.array(ElbowFlexion[Range],ndmin=2), \
									np.array(WristFlexion[Range],ndmin=2)), axis = 0)
	return(result)

Angles = create_range(Range, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion)

def plot_joint_angles(Angles,Range,Labels):
	"""
	Takes in a list of arrays for angles and the labels you wish to have in the legend. 
	"""
	size = len(Angles)
	plt.figure()
	ax = plt.gca()
	[plt.plot(Range,180*Angles[i]/np.pi) for i in range(size)]
	ax.legend(Labels)
	ax.set_xlabel('Postures')
	ax.set_ylabel('Joint Angles (degrees)')
	ax.set_title('Joint Angles During Throw Phase')
	ax.set_xlim([Range[0],Range[-1]])
	plt.show()

#plot_joint_angles(Angles,Range,['Ext Rot', 'Add', 'Horiz Add', 'EFE', 'WFE'])

# Create and plot geometric model for postures 35-78.

def upper_arm_x(UpperArm, Adduction, HorizAdduction):
	result = UpperArm*np.cos(Adduction)*np.cos(HorizAdduction)
	return(result)
def upper_arm_y(UpperArm, ExtRotation, Adduction, HorizAdduction):
	result = UpperArm*(np.cos(ExtRotation)*np.sin(HorizAdduction) + np.cos(HorizAdduction)*np.sin(ExtRotation)*np.sin(Adduction))
	return(result)
def upper_arm_z(UpperArm, ExtRotation, Adduction, HorizAdduction):
	result = UpperArm*(np.sin(ExtRotation)*np.sin(HorizAdduction) - np.cos(ExtRotation)*np.cos(HorizAdduction)*np.sin(Adduction))
	return(result)

def lower_arm_x(LowerArm, Adduction, HorizAdduction, ElbowFlexion):
	result = LowerArm*(np.cos(Adduction)*np.cos(HorizAdduction+ElbowFlexion))
	return(result)
def lower_arm_y(LowerArm, ExtRotation, Adduction, HorizAdduction, ElbowFlexion):
	result = LowerArm*(np.cos(ExtRotation)*np.sin(HorizAdduction+ElbowFlexion) + np.sin(ExtRotation)*np.sin(Adduction)*np.cos(HorizAdduction+ElbowFlexion))
	return(result)
def lower_arm_z(LowerArm, ExtRotation, Adduction, HorizAdduction, ElbowFlexion):
	result = LowerArm*(np.sin(ExtRotation)*np.sin(HorizAdduction+ElbowFlexion) - np.cos(ExtRotation)*np.sin(Adduction)*np.cos(HorizAdduction+ElbowFlexion))
	return(result)

def hand_x(Hand, Adduction, HorizAdduction, ElbowFlexion, WristFlexion):
	result = Hand*(np.sin(Adduction)*np.sin(WristFlexion) + \
					np.cos(WristFlexion)*np.cos(Adduction)*np.cos(HorizAdduction+ElbowFlexion))
	return(result)
def hand_y(Hand, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion):
	result = Hand*(np.cos(WristFlexion)*(np.cos(ExtRotation)*np.sin(HorizAdduction+ElbowFlexion) + np.sin(ExtRotation)*np.sin(Adduction)*np.cos(HorizAdduction+ElbowFlexion)) - np.sin(ExtRotation)*np.cos(Adduction)*np.sin(WristFlexion))
	return(result)
def hand_z(Hand, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion):
	result = Hand*(np.cos(WristFlexion)*(np.sin(ExtRotation)*np.sin(HorizAdduction+ElbowFlexion) - np.cos(ExtRotation)*np.sin(Adduction)*np.cos(HorizAdduction+ElbowFlexion)) + np.cos(ExtRotation)*np.cos(Adduction)*np.sin(WristFlexion))
	return(result)

def arm_position_x(UpperArm,LowerArm,Hand,Adduction,HorizAdduction,ElbowFlexion,WristFlexion):
	result = np.cumsum([upper_arm_x(UpperArm,Adduction,HorizAdduction),\
						lower_arm_x(LowerArm, Adduction, HorizAdduction, ElbowFlexion),\
						hand_x(Hand, Adduction, HorizAdduction, ElbowFlexion, WristFlexion)]) 
	return(np.array(result,ndmin = 2))
def arm_position_y(UpperArm,LowerArm,Hand,ExtRotation,Adduction,HorizAdduction,ElbowFlexion,WristFlexion):
	result = np.cumsum([upper_arm_y(UpperArm, ExtRotation, Adduction, HorizAdduction),\
						lower_arm_y(LowerArm, ExtRotation, Adduction, HorizAdduction, ElbowFlexion),\
						hand_y(Hand, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion)]) 
	return(np.array(result,ndmin = 2))
def arm_position_z(UpperArm,LowerArm,Hand,ExtRotation,Adduction,HorizAdduction,ElbowFlexion,WristFlexion):
	result = np.cumsum([upper_arm_z(UpperArm, ExtRotation, Adduction, HorizAdduction),\
						lower_arm_z(LowerArm, ExtRotation, Adduction, HorizAdduction, ElbowFlexion),\
						hand_z(Hand, ExtRotation, Adduction, HorizAdduction, ElbowFlexion, WristFlexion)]) 
	return(np.array(result,ndmin = 2))

X = arm_position_x(UpperArm,LowerArm,Hand,Adduction[Range[0]],HorizAdduction[Range[0]],ElbowFlexion[Range[0]],WristFlexion[Range[0]])
Y = arm_position_y(UpperArm,LowerArm,Hand,ExtRotation[Range[0]],Adduction[Range[0]],HorizAdduction[Range[0]],ElbowFlexion[Range[0]],WristFlexion[Range[0]])
Z = arm_position_z(UpperArm,LowerArm,Hand,ExtRotation[Range[0]],Adduction[Range[0]],HorizAdduction[Range[0]],ElbowFlexion[Range[0]],WristFlexion[Range[0]])
for i in range(Range[1],Range[len(Range)-1]+1):
	X = np.concatenate((X,arm_position_x(UpperArm,LowerArm,Hand,Adduction[i],HorizAdduction[i],ElbowFlexion[i],WristFlexion[i])),axis=0)
	Y = np.concatenate((Y,arm_position_y(UpperArm,LowerArm,Hand,ExtRotation[i],Adduction[i],HorizAdduction[i],ElbowFlexion[i],WristFlexion[i])),axis=0)
	Z = np.concatenate((Z,arm_position_z(UpperArm,LowerArm,Hand,ExtRotation[i],Adduction[i],HorizAdduction[i],ElbowFlexion[i],WristFlexion[i])),axis=0)

def plot_3D_trajectory(X,Y,Z,Range):
	figure_1 = plt.figure()
	ax = figure_1.gca(projection='3d')
	[ax.plot([0, X[i,0], X[i,1], X[i,2]],\
				[0, Y[i,0], Y[i,1], Y[i,2]],\
				[0, Z[i,0], Z[i,1], Z[i,2]], color = '0.75') for i in range(len(Range))]
	ax.plot([0],[0],[0],'k*')
	# Plot Release Posture in red
	ax.plot([0, X[28,0], X[28,1], X[28,2]],\
				[0, Y[28,0], Y[28,1], Y[28,2]],\
				[0, Z[28,0], Z[28,1], Z[28,2]], color = 'r')
	# Plot Reference Posture in green
	ax.plot([0, X[13,0], X[13,1], X[13,2]],\
				[0, Y[13,0], Y[13,1], Y[13,2]],\
				[0, Z[13,0], Z[13,1], Z[13,2]], color = 'g')  
	elbow = ax.plot(X[:,0], Y[:,0], Z[:,0], 'r*')
	wrsit = ax.plot(X[:,1], Y[:,1], Z[:,1], 'g*')
	end = ax.plot(X[:,2], Y[:,2], Z[:,2], 'k*')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_title('Limb postures during throw phase. Reference posture in green, release posture in red')
	ax.set_aspect('equal', 'datalim')
	ax.view_init(elev=66., azim=-72.)
	plt.show(block=True)

plot_3D_trajectory(X,Y,Z,Range)

# Force Length Adjustment

# Determine the difference between the current angle and the reference angle
# for each posture. A necessary assuption is to know the optimal (or
# resting) fiber length (variable OptimalLength) of each muscle.
# This is the length of the fibers for which sarcomeres are at optimal
# length, and at which it is assumed the parallel elastic element of muscle
# begins to stretch.
# This is usually not known for all muscles in the human arm. See the work of 
# Rick Liber and Jan Friden to get an idea of the current knowledge. In this model, 
# we assume that all muscles are at their OptimalLength in a posture towards the middle of the motion,
# shown in green. Posrure 14 is assumed to be the reference posture.

ReferenceAngles = Angles[:,13]

# Find the difference in join angles for all postures with respect to the
# angles in the reference posture: variable RelativeAngles

RelativeAngles = Angles.T - [ReferenceAngles]*len(Angles.T)

# Read moment arms  from variables in FiveDOF_Model.mat file
# These are obtained from bibtex reference:
# @inproceedings{
#    author = {EL, Lawrence and FJ, Valero-Cuevas},
#    title = {Can the Force-Velocity Curve Predict Realistic Muscle Forces for High-Speed Athletic Movements?},
#    booktitle = {7th World Congress on Biomechanics},
#    type = {Conference Proceedings}
# }
# Matrix R is 5x17 (5-DOFS, 17-muscles), all assumed to be constant
R = [	[-r[0], -r[1], -r[2],  r[3], -r[4],  r[5], -r[6],     0,  r[8],     0,      0,     0,      0,     0,     0,      0,     0 ], \
    	[ r[0],  r[1],  r[2],     0, -r[4], -r[5],     0, -r[7],     0,  r[9], -r[10],     0,  r[12],     0,     0,      0,     0 ], \
    	[-r[0],  r[1],     0, -r[3],  r[4], -r[5],     0,     0, -r[8],  r[9],      0,     0,      0,     0,     0,      0,     0 ], \
    	[    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,  r[10], r[11], -r[12],     0,     0,      0,     0 ], \
    	[    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,     0,      0, r[13], r[14], -r[15], -r[16]]	]


# calculate the change in muscle length by multiplying the change in angle
# from the reference posture by the the negative Moment Arm Matrix R.
# ************ Sign convention ********
# Calculate the F-V adjustment wrt change in muscle length based on the FV
# Negative changes in length indicate shortening from OptimalLength.
# Positive changes in length indicate lengthenig from OptimalLength.

RelativeMuscleLength = -np.matrix(R).T*RelativeAngles.T

# Determine the total muscle fiber length by adding the change (RelativeMuscleLength) to
# the OptimalLength and normalize by fiber length, and express in percentage.

# Convert optimal lengths to cm
OptimalLength_cm = OptimalLength*100

MuscleLengthPercentChange = RelativeMuscleLength.T*np.matrix(np.identity(17)*(1/OptimalLength_cm))*100
MuscleLength = RelativeMuscleLength.T + [OptimalLength_cm]*len(RelativeMuscleLength.T)
NormalizedMuscleLengths = MuscleLength*np.matrix(np.identity(17)*(1/OptimalLength_cm)) - 1
# [[You subtract 1 because you are using this to calculate the f-l correction]

def plot_percent_change(data):
	plt.figure(figsize=(15,4.5))
	plt.imshow(data,interpolation = 'none')
	plt.colorbar()
	plt.title('Percent Change in Muscle Length from optimal fiber length. Pos = longer. Neg = shorter')
	plt.xlabel('Postures')
	plt.ylabel('Muscles')
	plt.yticks(range(np.shape(data)[0]),range(1,np.shape(data)[0]+1))
	plt.show()

#plot_percent_change(MuscleLengthPercentChange.T)

# calculate the Force-Length adjustment given the curve from the BME504
# homework, only for the active part of the f-l curve.
# This is not plotted.

# Utilizing logical arrays, set abs(NormalizedMuscleLengths) > 0.5 to zero ForceLength
# Shape factor to make it symmetric about 0 percent change
w = 0.5
ForceLength = (1-(np.array(NormalizedMuscleLengths)/w)**2)*(np.array(NormalizedMuscleLengths)<=w)*(np.array(NormalizedMuscleLengths)>=-w)

# Muscle Fiber Velocity

# Calculate the normalized change in length/time (i.e., velocity of each muscle at each time step) given a 
# constant ChangeInTime between postures. 

# Shape factor for force-velocity curve. (not used)
k = 0.25

# Note: This includes only throw and deceleration phases
# Report the total time of the throw motion given the time step between
# postures ChangeInTime

TotalTime = ChangeInTime*np.shape(Angles)[1]
ChangeInMuscleLength = np.array(MuscleLength[:][1:] - MuscleLength[:][:len(MuscleLength)-1])
NormalizedMuscleVelocity = (ChangeInMuscleLength/(ChangeInTime/1000))*np.matrix(np.identity(17)*(1/OptimalLength_cm))
# Divided ChangeInTime by 1000 to convert to seconds

# Figure 4: instantanous normalized fiber velocity at each posture.
# Reported in fiber lengths/second.
# ********** Sign Convention to agree with classical f-v plots ********
# **** Negative velocities are eccentric contractions
# **** Positive velocities are concentric contractions
# Normalized fiber velocities >+/- 5 fiber lengths/second
# Based on the Zajac '89 paper, muscle fibers in concentric contractions
# faster than +5 fiber lengths/s are considered to produce no force.  
# Eccentric contractions are considered to
# produce microdamage in muscle, and if 
# faster than anbout -5 fiber lengths/sec can lead to tissue rupture.

def plot_normalized_muscle_velocity(data):
	plt.figure(figsize=(15,4.5))
	plt.imshow(data,interpolation = 'none')
	plt.colorbar()
	plt.title('Normalized Fiber Velocity in fiber lengths/second')
	plt.xlabel('Postures')
	plt.ylabel('Muscles')
	plt.yticks(range(np.shape(data)[0]),range(1,np.shape(data)[0]+1))
	plt.show()

#plot_normalized_muscle_velocity(NormalizedMuscleVelocity.T)

def plot_muscle_fiber_lengths(data):
	plt.figure(figsize=(15,4.5))
	plt.imshow(data,interpolation = 'none')
	plt.colorbar()
	plt.title('Raw fiber length in cm')
	plt.xlabel('Postures')
	plt.ylabel('Muscles')
	plt.yticks(range(np.shape(data)[0]),range(1,np.shape(data)[0]+1))
	plt.show()

#plot_muscle_fiber_lengths(MuscleLength.T)

def plot_muscle_lengths(MuscleLength):
	plt.figure()
	plt.plot(MuscleLength)
	plt.show()

#plot_muscle_lengths(MuscleLength)




















w = 0.5

