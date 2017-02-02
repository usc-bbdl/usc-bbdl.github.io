%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% NEUROMECHANICS  %%%%%%%%%%%%%
% (c) Francisco Valero-Cuevas & Emily Lawrence
% June 2014, version 1.0
% Filename: FiveDOF_ArmModel_Neuromechanics_V5.m
% Example of fiber length changes and fiber velocities
% for a frisbee throw motion with a 5-DOF, 17-muscle arm model

%%%%%% Requires file %%%%%%
%     FiveDOF_Model.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all 
clear all
clc

% This file contains the set of postures for the arm during the throw
load FiveDOF_Model

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%% Define Movement duration  %%%%%%%%
% delta_t_ms is the amount of time between successive postures of
% the arm.  There are 44 postures during the throwing motion,
% from start to release.
% delta_t_ms = 3.8 produces a throw movement duration of 167.2 ms
% from start to release, indicated by a red arm in the plot of arm
% postures. movement_duration, originally set to 1, lengthen
% the duration by that factor. 

speed_up_factor = 1
delta_t_ms = 3.8/speed_up_factor 



%% Nominal Model - Joint Angles

% Initiaion 34 postures: from posture  1 to 34
% Throw-to-release 29 postures: from posture 35 to 64
% Deceleration of throw 15 postures: from posture 65 to 78

% The first 34 postures are initiation of the throw, as subject starts
% pointing frisbee at target (arm straight out to side) then draws the
% frisbee back to posture 35. The subject initiates the throw from posture
% 35 to release at posture 64. 

% Read joint angles from variables in FiveDOF_Model.mat file
q = [angle_ext_rot_ds_rad, angle_add_ds_rad, angle_horiz_add_ds_rad, angle_elbow_ds_rad, angle_wrist_ds_rad];    
q = q(35:78, :);
q_deg = q*180/pi;

% Figure 1: Plot joint angles q for the throw and decelaration phases
figure(1)
hold on
plot(q_deg(:,1))
plot(q_deg(:,2), 'r')
plot(q_deg(:,3), 'g')
plot(q_deg(:,4), 'c')
plot(q_deg(:,5),'m')
xlabel('Postures')
ylabel('Joint angles - Degrees')
legend('External Rotation', 'Adduction', 'Horizontal Adduction', 'Elbow Flexion', 'Wrist Flexion')
title('Joint angles during throw phase')


% Figure 2: Create and plot geometric model for the throw and decelaration phases

q1=q;
origin = [0,0,0];

for i = 1:length(q1)
    
    Ex(:,i) = L1*cos(q1(i,2))*cos(q1(i,3));
    Ey(:,i) = L1*[(cos(q1(i,1))*sin(q1(i,3))) + (cos(q1(i,3))*sin(q1(i,1))*sin(q1(i,2)))];
    Ez(:,i) = L1*[(sin(q1(i,1))*sin(q1(i,3))) - (cos(q1(i,1))*cos(q1(i,3))*sin(q1(i,2)))];

    Wx(:,i) = L2*(cos(q1(i,2))*cos(q1(i,3))*cos(q1(i,4)) - cos(q1(i,2))*sin(q1(i,3))*sin(q1(i,4))) + Ex(i);
    Wy(:,i) = L2*(cos(q1(i,4))*(cos(q1(i,1))*sin(q1(i,3)) + cos(q1(i,3))*sin(q1(i,1))*sin(q1(i,2))) + sin(q1(i,4))*(cos(q1(i,1))*cos(q1(i,3)) - sin(q1(i,1))*sin(q1(i,2))*sin(q1(i,3)))) + Ey(i);
    Wz(:,i) = L2*(cos(q1(i,4))*(sin(q1(i,1))*sin(q1(i,3)) - cos(q1(i,1))*cos(q1(i,3))*sin(q1(i,2))) + sin(q1(i,4))*(cos(q1(i,3))*sin(q1(i,1)) + cos(q1(i,1))*sin(q1(i,2))*sin(q1(i,3)))) + Ez(i);

    Tx(:,i) = L3*(sin(q1(i,2))*sin(q1(i,5)) + cos(q1(i,5))*(cos(q1(i,2))*cos(q1(i,3))*cos(q1(i,4)) - cos(q1(i,2))*sin(q1(i,3))*sin(q1(i,4)))) + Wx(i);
    Ty(:,i) = L3*(cos(q1(i,5))*(cos(q1(i,4))*(cos(q1(i,1))*sin(q1(i,3)) + cos(q1(i,3))*sin(q1(i,1))*sin(q1(i,2))) + sin(q1(i,4))*(cos(q1(i,1))*cos(q1(i,3)) - sin(q1(i,1))*sin(q1(i,2))*sin(q1(i,3)))) - cos(q1(i,2))*sin(q1(i,1))*sin(q1(i,5))) + Wy(i);
    Tz(:,i) = L3*(cos(q1(i,5))*(cos(q1(i,4))*(sin(q1(i,1))*sin(q1(i,3)) - cos(q1(i,1))*cos(q1(i,3))*sin(q1(i,2))) + sin(q1(i,4))*(cos(q1(i,3))*sin(q1(i,1)) + cos(q1(i,1))*sin(q1(i,2))*sin(q1(i,3)))) + cos(q1(i,1))*cos(q1(i,2))*sin(q1(i,5))) + Wz(i);

    elbow(i,:) = [Ex(i), Ey(i), Ez(i)];
    wrist(i,:) = [Wx(i), Wy(i), Wz(i)];
    last(i,:) = [Tx(i), Ty(i), Tz(i)];

end 

 figure(2)
 title('Limb postures during throw phase. Reference posture in green, release posture in red.')

    xlim([-0.4 0.6])
    ylim([-0.2 0.6])
    hold on
    scatter3(Ex, Ey, Ez, 'r*')
    scatter3(Wx, Wy, Wz, 'g*')
    scatter3(Tx, Ty, Tz, 'k*')
    scatter3(0,0,0, 'b*')
    for i=1:length(Ex)
        line1 = [origin; elbow(i,:)];
        line2 = [elbow(i,:); wrist(i,:)];
        line3 = [wrist(i,:); last(i,:)];
        
        plot3(line1(:,1), line1(:,2), line1(:,3))
        plot3(line2(:,1), line2(:,2), line2(:,3))
        plot3(line3(:,1), line3(:,2), line3(:,3))
        
    end
    %release point indicated in red
    R1 = [origin; elbow(29,:)];
    R2 = [elbow(29,:); wrist(29,:)];
    R3 = [wrist(29,:); last(29,:)];    
    plot3(R1(:,1), R1(:,2), R1(:,3), 'r')
    plot3(R2(:,1), R2(:,2), R2(:,3), 'r')
    plot3(R3(:,1), R3(:,2), R3(:,3), 'r')
    
    %reference posture indicated in green
    Ref1 = [origin; elbow(14,:)];
    Ref2 = [elbow(14,:); wrist(14,:)];
    Ref3 = [wrist(14,:); last(14,:)];    
    plot3(Ref1(:,1), Ref1(:,2), Ref1(:,3), 'g')
    plot3(Ref2(:,1), Ref2(:,2), Ref2(:,3), 'g')
    plot3(Ref3(:,1), Ref3(:,2), Ref3(:,3), 'g')
    hold off
%% Force Length Adjustment

% Determine the difference between the current angle and the reference angle
% for each posture. A necessary assuption is to know the optimal (or
% resting) fiber length (variable lo, pronounced "ell-naught") of each muscle.
% This is the length of the fibers for which sarcomeres are at optimal
% length, and at which it is assumed the parallel elastic element of muscle
% begins to stretch.
% This is usually not known for all muscles in the human arm. See the work of 
%Rick Liber and Jan Friden to get an idea of the current knowledge. In this model, 
%we assume that all muscles are at their lo in a posture towards the middle of the motion,
% shown in green. Posrure 14 is assumed to be the reference posture.
ref_angles = q(14, :);

% Find the difference in join angles for all postures with respect to the
% angles in the reference posture: variable change_q
for k=1:length(q)
    chq(k,:) = q(k,:) - ref_angles;
end
 
change_q = chq';

% Read moment arms  from variables in FiveDOF_Model.mat file
% These are obtained from bibtex reference:
% @inproceedings{
%    author = {EL, Lawrence and FJ, Valero-Cuevas},
%    title = {Can the Force-Velocity Curve Predict Realistic Muscle Forces for High-Speed Athletic Movements?},
%    booktitle = {7th World Congress on Biomechanics},
%    type = {Conference Proceedings}
% }
% Matrix R_Full is 5x17 (5-DOFS, 17-muscles), all assumed to be constant
R_full = [-R(1), -R(2), -R(3), R(4), -R(5), R(6), -R(7), 0, R(9), 0, 0, 0, 0, 0, 0, 0, 0;...
    R(1), R(2), R(3), 0, -R(5), -R(6), 0, -R(8), 0, R(10), -R(11), 0, R(13), 0, 0, 0, 0;...
    -R(1), R(2), 0, -R(4), R(5), -R(6), 0, 0, -R(9), R(10), 0, 0, 0, 0, 0, 0, 0;...
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, R(11), R(12), -R(13), 0, 0, 0, 0;...
    0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, R(14), R(15), -R(16), -R(17)];

% calculate the change in muscle length by multiplying the change in angle
% from the reference posture
% by multiplying the the negative Moment Arm Matrix R_full.
% ************ Sign convention ********
% Calculate the F-V adjustment wrt change in muscle length based on the FV
% Negative changes in length indicate shortening from lo.
% Positive changes in length indicate lengthenig from lo.


% first take the transpose of the moment arm matrix, and then change signs
R_trans = R_full';
R_neg_trans = -1*(R_trans);

% Calculate the change in fiber length from lo
delta_l = R_neg_trans * change_q;


% Determine the total muscle fiber length by adding the change (delta_l) to
% the lo and normalize by fiber length, and express in percentage.

lo_cm = lo*100; %convert from m to cm to match the moment arm values in cm

value = size(delta_l);
for i = 1:value(1)
    delta_l_percent_change(i,:) = (delta_l(i,:)/lo_cm(i))*100;
    l_raw(i,:) = (delta_l(i,:) + lo_cm(i)); 
    new_l_norm(i,:) = ((delta_l(i,:) + lo_cm(i))/lo_cm(i))-1; 
    % [[You subtract 1 because you are using this to calculate the f-l correction]]
end

% Figure 3: Normalize by fiber length, percentage change from lo.

figure(3);
imagesc(delta_l_percent_change);
colorbar;
xlabel('Postures')
ylabel('Muscles')
title('Percent Change in Muscle Length from optimal fiber length. Pos = longer. Neg = shorter')


% calculate the Force-Length adjustment given the curve from the BME504
% homework, only for the active part of the f-l curve.
% This is not plotted.
w = 0.5; % shape factor to make it symmetric about 0 percent change.

value = size(new_l_norm);
force_length = [];
for k = 1:value(1)
    for j = 1:value(2)
        if new_l_norm(k,j) <= -0.5 
            force_length(k,j) = 0;
        elseif new_l_norm(k,j) >= 0.5
            force_length(k,j) = 0;
        else force_length(k,j) = 1 - (new_l_norm(k,j)/ w)^2; 
        end
    end
end


%% Muscle Fiber Velocity

% Calculate the normalized change in length/time (i.e., velocity of each muscle at each time step) given a 
% constant delta_t_ms between postures. 

k = 0.25; % shape factor for force-velocity curve. (not used)

% Note: This includes only throw and deceleration phases
% Report the total time of the throw motion given the time step between
% postures delta_t_ms

TotalTime_ms = delta_t_ms*length(q)


% do a simple delta_x/delta_t estimate of fiber velocity. For each time
% step (outer loop), find that instantanous velocity for all muscles (inner loop)
value = size(new_l_norm);
for k=1:value(2)-1
    for i=1:value(1)
        vel_length_norm(i,k) = (new_l_norm(i,k+1)-new_l_norm(i,k))/(delta_t_ms/1000); 
        % divide delta_t_ms by 1000 to convert to seconds.
    end
end


% Figure 4: instantanous normalized fiber velocity at each posture.
% Reported in fiber lengths/second.
% ********** Sign Convention to agree with classical f-v plots ********
% **** Negative velocities are eccentric contractions
% **** Positive velocities are concentric contractions
% Normalized fiber velocities >+/- 5 fiber lengths/second
% Based on the Zajac '89 paper, muscle fibers in concentric contractions
% faster than +5 fiber lengths/s are considered to produce no force.  
% Eccentric contractions are considered to
% produce microdamage in muscle, and if 
% faster than anbout -5 fiber lengths/sec can lead to tissue rupture.

figure(4);
imagesc(vel_length_norm);
colorbar;
xlabel('Postures')
ylabel('Muscles')
title('Normalized Fiber Velocity in fiber lengths/second')

% Figure 5: Raw muscle fiber lengths
figure(5);
imagesc(l_raw);
colorbar;
xlabel('Postures')
ylabel('Muscles')
title('Raw fiber length in cm')

figure(6)
plot(l_raw');
