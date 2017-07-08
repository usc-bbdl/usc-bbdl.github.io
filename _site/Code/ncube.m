function [vertices,count] = ncube(dim)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% NEUROMECHANICS %%%%%%%%%%%%%
% (c) Francisco Valero-Cuevas
% October 2013, version 1.0
% Filename: ncube.m

% ncube returns the vertices of an n-cube for dimensions 3 or higher.
% (c) Francisco Valero-Cuevas 2013
% [vertices,count] = ncube(dim)  returns:
% the matrix 'vertices' with the vertices of the n-cube
% the number 'count' of vetices 
if dim <3
error('low dim', 'enter a dimension 3 or greater'   ) 
else

        vertices = [0 0;1 0; 0 1 ; 1 1];
        new = [0 1];
        dim = dim-1;
        for n=2:dim
            temp2 = [];
            for i=1:length(vertices')
                row =  vertices(i,:);
                temp1 = [0 row;
                     1 row];
                 temp2 = [temp2;temp1];
            end
           vertices = temp2;

        end
        vertices = sortrows(vertices);
        count = length(vertices');

end