# Simple Tendon Excursion Example
# for one joint with 4 muscles.
# (c) Daniel A Hagen
# August 2016
# University of Southern California

import numpy as np 
import matplotlib.pyplot as plt 

# Moment Arm Matrix
R = np.matrix([1,2,-2,-1])

# Define Joint Angle Trajectory, Reference Angle, and Change in Time
# ChangeInTime must be sufficiently small to find approximated
# Angular Velocity
ChangeInTime = 0.001
Angle = (np.pi/2)*np.sin(4*np.pi*np.arange(0, 1, ChangeInTime))
ReferenceAngle = 0

# Define optimal tendon length for ReferenceAngle
OptimalLength1 = 10
OptimalLength2 = 10
OptimalLength3 = 10
OptimalLength4 = 10
OptimalLengths = np.matrix([OptimalLength1,OptimalLength2,OptimalLength3,OptimalLength4])

# Define TotalChangeInAngle to be the difference between 
# Angle and ReferenceAngle. Can only be done for 
# constant moment arm values, otherwise change in 
# angle must be calculated for each time step.	
TotalChangeInAngle = Angle - ReferenceAngle 

# Calculate change in tendon length (ChangeInExcursion)
ChangeInExcursion = -R.T*TotalChangeInAngle

# Calculate muscle length
MuscleLengths = ChangeInExcursion + OptimalLengths.T

plt.figure()
plt.plot(MuscleLengths.T)
plt.xlabel('Time Step Units')
plt.ylabel('Muscle Length')
plt.legend(['Muscle 1','Muscle 2','Muscle 3','Muscle 4'])
ax1 = plt.gca()


# Calculate muscle velocity
# We can approximate this value by dividing the change in angle
# for each time step by the ChangeInTime. First you must find the
# change in angle by finding the difference between Angle[i] and 
# Angle[i-1], then divide by a sufficiently small ChangeInTime
# to approximate the AngularVelocity. 
ChangeInAngle = [Angle[i]-Angle[i-1] for i in range(1,len(Angle))]
AngularVelocity = np.array(ChangeInAngle)/ChangeInTime
MuscleVelocities = -R.T*AngularVelocity

plt.figure()
plt.plot(MuscleVelocities.T)
plt.xlabel('Time Step Units')
plt.ylabel('Muscle Velocity')
plt.legend(['Muscle 1','Muscle 2','Muscle 3','Muscle 4'])
ax2 = plt.gca()
plt.show((ax1,ax2))
