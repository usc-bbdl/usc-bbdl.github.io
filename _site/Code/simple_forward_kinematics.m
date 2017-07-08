%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% NEUROMECHANICS  %%%%%%%%%%%%%
% (c) Daniel A Hagen
% August 2016, version 1.0
% Filename: simple_forward_kinematics.m
% Forward Kinematics for Fig 2.1

% Define the symbolic variables for Fig 3.3
syms Angle1 Angle2 real;
syms Link1 Link2 real;
syms T01 T12 T23 T G real;

% Define Transformation Matrices from initial frame (T0) to endpoint frame (T3)
T01 = [	cos(Angle1),	-sin(Angle1),			0,			0; ...
		sin(Angle1),	cos(Angle1),			0,			0; ...
		0,					0,					1,			0; ...
		0,					0,					0,			1	];
T12 = [	cos(Angle2),	-sin(Angle2),			0,		Link1; ...
		sin(Angle2),	cos(Angle2),			0,			0; ...
		0,					0,					1,			0; ...
		0,					0,					0,			1	];
T23 = [	1,					0,					0,		Link2; ...
		0,					1,					0,			0; ...
		0,					0,					1,			0; ...
		0,					0,					0,			1	];

% Total Transformation
T = simplify(T01*T12*T23);

% Define Geometric Model to be the first two components (x,y) of the position
% vector of the Transformation Matrix (T) and the sum of all angles.
G =[T(1,4); T(2,4); Angle1 + Angle2];
disp('Position vector p from frame 0 to 3 (Our Geometric Model):');
disp(['x = ' char(G(1))]);
disp(['y = ' char(G(2))]);
disp(['alpha = ' char(G(3))]);

% Create Jacobian Matrix
disp('Jacobian Matrix:');
J = jacobian(G,[Angle1,Angle2])

% Numerical Example and plot for Angle 1 = 135 deg, Angle 2 = -120 deg
Angle1 = 135*pi/180;
Angle2 = -120*pi/180;

Link1 = 25.4; % cm
Link2 = 30.5; % cm

x = eval(subs(G(1)));
y = eval(subs(G(2)));
alpha = eval(subs(G(3)));
disp('Position vector p from frame 0 to 3 (Our Geometric Model):');
disp(['x = ' num2str(x)]);
disp(['y = ' num2str(y)]);
disp(['alpha = ' num2str(alpha)]);

figure;
x = [ 	0; ...
		Link1*cos(Angle1); ...
		Link1*cos(Angle1) + Link2*cos(Angle1+Angle2) ];
y = [ 	0; ...
		Link1*sin(Angle1); ...
		Link1*sin(Angle1) + Link2*sin(Angle1+Angle2) ];
plot(x,y,'ko','MarkerSize',16,'MarkerFaceColor','k');
hold on;
xlimits = get(gca,'xlim');
ylimits = get(gca,'ylim');
set(gca,'xlim',[xlimits(1)-5, xlimits(2)+5]);
set(gca,'ylim',[ylimits(1)-5, ylimits(2)]);
xlimits = get(gca,'xlim');
ylimits = get(gca,'ylim');
plot([xlimits(1), xlimits(2)],[0, 0],'color',[0.75, 0.75, 0.75], 'LineWidth', 2);
plot([0, 0],[ylimits(1), ylimits(2)],'color',[0.75, 0.75, 0.75], 'LineWidth', 2);
plot(x,y,'ko-','LineWidth',4,'MarkerSize',16,'MarkerFaceColor','k');
xlabel('x');
ylabel('y');
title(['Simple Forward Kinematics for Fig 2.1 (Angle 1 = ' num2str(Angle1*180/pi) ...
						', Angle 2 = ' num2str(Angle2*180/pi) ')']);
axis equal;

% Numerical examples and plot for same configuration but with unit angular
% velocities for each joint.

J = eval(subs(J));
EndpointVelocity1 = J*[1;0];
EndpointVelocity2 = J*[0;1];

disp('Velocity for rotation about joint 1:');
disp(EndpointVelocity1);
disp('Velocity for rotation about joint 2:');
disp(EndpointVelocity2);

figure;
x = [ 	0; ...
		Link1*cos(Angle1); ...
		Link1*cos(Angle1) + Link2*cos(Angle1+Angle2) ];
y = [ 	0; ...
		Link1*sin(Angle1); ...
		Link1*sin(Angle1) + Link2*sin(Angle1+Angle2) ];
hold on;
quiver(x(3),y(3),EndpointVelocity1(1),EndpointVelocity1(2),'r','LineWidth',2);
quiver(x(3),y(3),EndpointVelocity2(1),EndpointVelocity2(2),'g','LineWidth',2);
ylim([-5,55]);
axis equal;
xlimits = get(gca,'xlim');
plot([xlimits(1), xlimits(2)],[0, 0],'color',[0.75, 0.75, 0.75], 'LineWidth', 2);
plot([0, 0],[-5, 55],'color',[0.75, 0.75, 0.75], 'LineWidth', 2);
plot(x,y,'ko-','LineWidth',4,'MarkerSize',16,'MarkerFaceColor','k');
plot(x(1),y(1),'ro','MarkerSize',16,'MarkerFaceColor','r');
plot(x(2),y(2),'go','MarkerSize',16,'MarkerFaceColor','g');
quiver(x(3),y(3),EndpointVelocity1(1),EndpointVelocity1(2),'r','LineWidth',2);
quiver(x(3),y(3),EndpointVelocity2(1),EndpointVelocity2(2),'g','LineWidth',2);
xlabel('x');
ylabel('y');
title(['Simple Forward Kinematics with Velocities for Fig 2.1 (Angle 1 = ' num2str(Angle1*180/pi) ...
						', Angle 2 = ' num2str(Angle2*180/pi) ')']);
axis equal;
