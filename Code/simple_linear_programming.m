% Simple Linear Programming Example
% using the Diet Problem from Ch 5.2.2 
% of Fundamentals of Neuromechanics
% (c) Daniel A Hagen
% August 2016
% University of Southern California

OatmealCost = 3;
OatmealEnergy = 110;
OatmealProtein = 4;
OatmealCalcium = 2; 
OatmealMaxServings = 4;

ChickenCost = 24;
ChickenEnergy = 205; 
ChickenProtein = 32; 
ChickenCalcium = 12;
ChickenMaxServings = 3;

EggsCost = 13; 
EggsEnergy = 160;
EggsProtein = 13; 
EggsCalcium = 54; 
EggsMaxServings = 2;

WholeMilkCost = 9;
WholeMilkEnergy = 160;
WholeMilkProtein = 8;
WholeMilkCalcium =285;
WholeMilkMaxServings = 8;

CherryPieCost = 20;
CherryPieEnergy = 420;
CherryPieProtein = 4;
CherryPieCalcium = 22;
CherryPieMaxServings = 2;

PorkAndBeansCost = 19; 
PorkAndBeansEnergy = 260;
PorkAndBeansProtein = 14;
PorkAndBeansCalcium = 80;
PorkAndBeansMaxServings = 2;

% Define Cost Function TO BE MINIMIZED
Cost = [OatmealCost ChickenCost EggsCost ...
        WholeMilkCost CherryPieCost PorkAndBeansCost];

fprintf(['Cost Function Array to be Minimized (c)\n[' num2str(Cost) ']\n'])

% Define Constraint functions
% NOTE: Because we want to have MORE than a prescribed amount
% of Energy, Protein, and Calcium, they will be negative values 
% in each Constraint array. This will make the constraint functions
% 'greater than or equal to' the Energy, Protein, and Calcium 
% benchmarks (to be defined below). If you  wanted to have less than 
% a certain amount, remove the negative sign.
Energy = -[OatmealEnergy ChickenEnergy, EggsEnergy ...
            WholeMilkEnergy CherryPieEnergy PorkAndBeansEnergy];
Protein = -[OatmealProtein ChickenProtein EggsProtein ...
            WholeMilkProtein CherryPieProtein PorkAndBeansProtein];
Calcium = -[OatmealCalcium ChickenCalcium EggsCalcium ...
            WholeMilkCalcium CherryPieCalcium PorkAndBeansCalcium];
A = [   Energy; ...
        Protein; ...
        Calcium; ...
        eye(6); ...
        -eye(6) ];
        

fprintf('Constraint Matrix A:\n');
disp(A);

% Define b array (equality conditions for constraint functions)
% NOTE: Because we want to have MORE than a prescribed amount
% of Energy, Protein, and Calcium, they will be negative values 
% in our b array. This will make the constraints 'greater than or
% equal to' the Energy, Protein, and Calcium benchmarks. If you
% wanted to have less than a certain amount, remove the negative sign.
b = [   -2000;...
        -55; ...
        -800; ...
        OatmealMaxServings; ...
        ChickenMaxServings; ...
        EggsMaxServings; ...
        WholeMilkMaxServings; ...
        CherryPieMaxServings; ...
        PorkAndBeansMaxServings; ...
        zeros(6,1)  ];

fprintf('b array for Constraint Matrix A:\n');
disp(b)

% Find and print optimal solution
x = linprog(Cost,A,b);

fprintf('With these dietary restrictions the optimal choice will be to eat:\n')
fprintf([ num2str(x(1),'%.2f') ' Oatmeal\n']);
fprintf([ num2str(x(2),'%.2f') ' Chicken\n']);
fprintf([ num2str(x(3),'%.2f') ' Eggs\n']);
fprintf([ num2str(x(4),'%.2f') ' Whole Milk\n']);
fprintf([ num2str(x(5),'%.2f') ' Cherry Pie\n']);
fprintf([ num2str(x(6),'%.2f') ' Pork and Beans\n']);