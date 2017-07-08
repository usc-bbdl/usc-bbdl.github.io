%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% NEUROMECHANICS  %%%%%%%%%%%%%
% (c) Francisco Valero-Cuevas
% October 2013, version 1.0
% Filename: simple_inverse_kinematics
% Example of linearized inverse kinematics
% for a 2D2DOF_system


% Clear memory and screen
close all;clear all;
clc
% Define variables for symbolic analysis
syms G J            % Vector functions
syms q1 q2 x1 x2    % Degrees of freedom
syms l1 l2          % System parameters
syms r t_x t_y      % trajectory components


%Define x and y coordinates of the endpoint of the linkage system
%Create Matrix for Geometric Model
x1 = l1.*cos(q1) + l2.*cos(q1+q2);
x2 = l1.*sin(q1) + l2.*sin(q1+q2);
G = [x1;x2];
%Create Jacobian and its permutations
J = jacobian(G,[q1,q2]);
J_inv = inv(J);
J_trans = J';
J_trans_inv = inv(J');



% Numerical example of inverse kinematics
%create a trajectory of a circle with radius 5.
r = 5;
q = linspace(0,pi,10); % a sparse trajectory
x = r*cos(q);
y = r*sin(q);
xi = -5:.01:5; % create a finer mesh to interpolate
yi = interp1(x,y,xi, 'cubic'); %use cubic interpolation
plot(x,y,'o',xi,yi), axis equal % plot the priginal points and the interpolation
hold on % Hold figure to plot the rest
X = flipud([xi;yi]'); % this array has all x,y points of the interpolated trajectory of the circle
%point 101 is (3,4), whenthe limb is at q1 = 0, q2 =pi/2.Use this as a
%starting point where you know the joint angles and the endpoint location.
% the X vector of positions has 1001 points.

% Do the inverse kinematics
%Now define Link Lengths (m) to allow the trajectory of a cirle of radius 5
%
l1 = 4 % link 1
l2 = 3 % linek 2. 3, 4 and 5 make a Pythagorean triplet.
% Define joint angles (radians) for a Pythagorean triple
% as the initial angles q_0
fprintf('Initial angles \n')
q1 = 0     % 0 degrees
q2 = pi/2  % 90 degrees
q_0 = [q1 q2]; 
fprintf('Initial location from geometric model \n')
x_0 = subs(G)



% Now implement the linearlized inverse kinematic relationship:  
% q_i = q_(i-1) + dq =   q_(i-1) + J^-1 dX(i-1)
% because dq = J^-1 dX(i-1)
q_last = q_0; % this is the starting point.
q = q_0; % start creating the array of joint angles
% Point X(101) is the starting position. 
% Do the inverse kinematics from point 101 to any other one along the
% trajectory.

% ******************* USER ENTERED last_point ********
% ****************************************************
fprintf('Index of last point along the trajectory, entered by the user\nbetween 102 and 1001 \n')
last_point = 150 %any value from 102 to 1001

for i = 102:last_point % do the inverse kinematics for this subset of the circle
    q1 = q_last(1); %this is q_(i-1)
    q2 = q_last(2);
    dX = (X(i,:)-X(i-1,:) )'; % this is dX(i-1)
    dq = subs(J_inv) * dX; % this is the linearized extrapolation
    q = [q; q_last + dq']; % build up the array of joint angels
    q_last = q_last + dq'; % define the new  q_(i-1)
end

% The vector q has the joint angles that produce the trajectoru

%%%%%%%%%%%%% Sanity Check %%%%%%%%%%%%%%%
% Now test to see what trajectory these q's generate. 
text(0,-0.1, '  Origin') 
plot(0,0, 'k+') 
q1 = q(1,1); %define joint angles for the initial posture
q2 = q(1,2);
X_new = subs(G)';
plot(X_new(1), X_new(2), 'b*') 
text(X_new(1), X_new(2), '  Initial posture') 

for i = 2:length(q)
    q1 = q(i,1);
    q2 = q(i,2);
    X_new = [X_new; subs(G)'];
end
plot(X_new(:,1), X_new(:,2), '-r'), axis equal

%plot the arm configurations
% initial
q1 = q(1,1);
q2 = q(1,2);
x_first = l1*cos(q1);
y_first = l1*sin(q1);
line([0 x_first], [0  y_first] )
    
temp = subs(G);
x_last = temp(1);
y_last = temp(2);
line([x_first x_last], [y_first y_last] )

% final
q1 = q(end,1); %define joint angles for the final posture
q2 = q(end,2);
x_first = l1*cos(q1);
y_first = l1*sin(q1);
line([0 x_first], [0  y_first] )
    
temp = subs(G);
x_last = temp(1);
y_last = temp(2);
line([x_first x_last], [y_first y_last] )
text(x_last, y_last, '  Final posture') 
