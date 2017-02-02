% Simple Tendon Excursion Example
% for one joint with 4 muscles.
% (c) Daniel A Hagen
% August 2016
% University of Southern California

% Moment Arm Matrix
R = [1 2 -2 -1];

% Define Joint Angle Trajectory, Reference Angle, and Change in Time
% ChangeInTime must be sufficiently small to find approximated
% Angular Velocity
ChangeInTime = 0.001;
Angle = (pi/2).*sin(4*pi.*(0:ChangeInTime:1));
ReferenceAngle = 0;

% Define optimal tendon length for ReferenceAngle
OptimalLength1 = 10;
OptimalLength2 = 10;
OptimalLength3 = 10;
OptimalLength4 = 10;
OptimalLengths = [  OptimalLength1.*ones(1,length(Angle)); ...
                    OptimalLength2.*ones(1,length(Angle)); ...
                    OptimalLength3.*ones(1,length(Angle)); ... 
                    OptimalLength4.*ones(1,length(Angle))   ];

% Define TotalChangeInAngle to be the difference between 
% Angle and ReferenceAngle. Can only be done for 
% constant moment arm values, otherwise change in 
% angle must be calculated for each time step.	
TotalChangeInAngle = Angle - ReferenceAngle; 

% Calculate change in tendon length (ChangeInExcursion)
ChangeInExcursion = -R'*TotalChangeInAngle;

% Calculate muscle length
MuscleLengths = ChangeInExcursion + OptimalLengths;

figure();
plot(MuscleLengths');
xlabel('Time Step Units');
ylabel('Muscle Length');
xlim([0,length(Angle)]);
legend('Muscle 1', 'Muscle 2', 'Muscle 3', 'Muscle 4');

% Calculate muscle velocity
% We can approximate this value by dividing the change in angle
% for each time step by the ChangeInTime. First you must find the
% change in angle by finding the difference between Angle(i) and 
% Angle(i-1), then divide by a sufficiently small ChangeInTime
% to approximate the AngularVelocity.
ChangeInAngle = zeros(1,length(Angle)-1);
for i = 2:length(Angle)
    ChangeInAngle(i) = Angle(i)-Angle(i-1);
end
AngularVelocity = ChangeInAngle./ChangeInTime;
MuscleVelocities = -R'*AngularVelocity;

figure();
plot(MuscleVelocities');
xlabel('Time Step Units');
ylabel('Muscle Velocity');
xlim([0,length(Angle)]);
legend('Muscle 1', 'Muscle 2', 'Muscle 3', 'Muscle 4');
