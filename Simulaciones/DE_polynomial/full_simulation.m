%%Replacement Phase
rng(1);
N =100;
Min = [-10, -10];
Max = [10, 10];
Population = zeros([N, 2]);
%%Initialization
Population(:,1) = Min(1) + rand([N, 1])*(Max(1)-Min(1));
Population(:,2) = Min(2) + rand([N, 1])*(Max(2)-Min(2));
x = Min:0.2:Max;
y = Min:0.2:Max;
x = linspace(Min(1),Max(1), 100); 
y = linspace(Min(2),Max(2), 100);

FinalP = Population;
[X,Y] = meshgrid(x,y);
%Z = -X.^2 - Y.^2;
Z = X;
for i = 1:length(X)
    for j = 1:length(Y)
        Z(j,i) = evaluation([X(j,i), Y(j,i)]);
    end
end
%Z = sin(X) + cos(Y);
figure('Renderer', 'painters', 'Position', [10 10 2000 900])
s = contour(X,Y,Z,'ShowText','on');
%hold on
%s = scatter(start(:,1),start(:,2), 10, 'filled','black');
hold on
Di = 0.5;
%Z = (1-X).^2 + 100*(Y-X.^2).^2;
F_Population = zeros(length(Population),1);
Population(1,:)=[1,1];

FinalP=[];
F_Children = zeros(length(Population),1);
for i =1:length(Population)
    F_Population(i) = evaluation(Population(i,:));
 end
%F_Population = sin(Population(:,1)) + cos(Population(:,2));
%sin(x) + cos(y)

Generations = 500;
count = 0;
 hold on;
while Generations > count
   % Dt = 0.5;
    Dt = Di*(1.0 - (1.0*count/(Generations)))
    %Dt = max(0.01, Dt);
    %Generation new individuals...
    Children = DE_operators(Population, Min, Max);
    %Evaluation
    for i = 1:length(Children)
        F_Children(i) = evaluation(Children(i,:));
    end
    %clf;
    %s = contour(X,Y,Z,'ShowText','on');
    %s = contour(X,Y,Z);

    %replacement phase
    Population = replacement([Population; Children], [F_Population; F_Children], Dt, N);
    
    hold on;
    s = scatter(Children(:,1),Children(:,2), 10, 'filled','red');
    hold on;
    s = scatter(Population(:,1),Population(:,2), 10, 'filled','black');
%    F_Population = sin(Population(:,1)) + cos(Population(:,2));
    for i =1:length(Population)
       F_Population(i) = evaluation(Population(i,:));
    end
    count = count+1
    %FinalP = [FinalP; Population];
    pause(0.1);
end
cr1 = FinalP((length(FinalP)-99):length(FinalP),:)

%s = contour(X,Y,Z);
%hold on;
%s = scatter(FinalP(:,1),FinalP(:,2), 10, 'filled','red');


 
 