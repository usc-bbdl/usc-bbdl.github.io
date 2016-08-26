%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% NEUROMECHANICS %%%%%%%%%%%%%
% (c) Francisco Valero-Cuevas
% October 2013, version 1.0
% Filename: zonotope_muti_N.m
clear all
close all
clc
% This script shows how to map N-dimensional N-cubes into 2D and 3D via a
% random H matrix of dimensions 2 x N and 3 x N, respectively.

% It then plots the convex hulls of the zonotopes when considering 
% the input to be between 3 and 8 dimensions. That is, a system having 3 to
% 8 muscles

%%%%%%%%%%%%%%%%%%% User Input %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Enter the dimensions of the input space here. Note it must be >=3 
input_dim = 8 % this is the largest dimension


H= rand(3,input_dim)*2-1 % this is the random full 3x8 H matrix. 'rand'
% returns values between 0 and 1
figure(2)

% Iterate to calculate the zonotopes for inout dimensions from 3 to 8

for n=3:8 % n us the number if muscles, from 3 to 8 in this example
% use my function ncube to obtain the vertices. Use 'help ncube' for
% details. X is the matrix of all vertices of the n-cube
[X, count] = ncube(n);
H2= H(1:2,1:n); %select the 2D output with n muscles
% H3= H(1:3,1:n); %select the 3D output with n muscles

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2D case
% multiply each vertex by the matrix H
Y=[];
for i=1:count

Y= [Y;(H2*X(i,:)')'];
end

% Find the convex hull
K = convhull(Y);

% plot all points and the convex hull.
figure(2)
hold on
plot(Y(K,1),Y(K,2),'r-')

indices = find(Y(:,2)== max(Y(:,2)));
nlable = indices(1)
text(Y(nlable,1),Y(nlable,2),['\leftarrow ' num2str(n) ' muscles' ] ,'FontSize',18)


end
hold off
