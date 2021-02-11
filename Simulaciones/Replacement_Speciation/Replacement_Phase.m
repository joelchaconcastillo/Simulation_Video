%%Replacement Phase
N =100
Min = -10;
Max = 10;

%%Initialization
Population = Min + rand(N, 2)*(Max-Min);
Di=0.1

x = Min:0.2:Max;
y = Min:0.2:Max;
x = linspace(Min,Max); 
y = linspace(Min,Max);

[X,Y] = meshgrid(x,y);
%Z = -X.^2 - Y.^2;
Z = sin(X) + cos(Y);
figure
s = contour(X,Y,Z,'ShowText','on');
%hold on
%Z = (1-X).^2 + 100*(Y-X.^2).^2;

%Evaluate points

Penalized = []
pause(1)
count = 0
%Ranks = zeros(500,2)
while count < N
    Niche_i = []
    F = sin(Population(:,1)) + cos(Population(:,2));
  while size(Population,1) > 0
    %Select the best individual with max fitness
    [Reference_Point, I] = max(F);
    Reference_Point = Population(I,:)
    [Population, PS] = removerows(Population,'ind',I)
    F(I)=[]
     if(size(Population,1)>1)
    %Find the nearest points to the reference
    [ID, D] = knnsearch(Population, Reference_Point, 'k', size(Population,1));
    Penalized = [Penalized ; Population(ID(D<Di),:)];
    [Population, PS] = removerows(Population,'ind',ID(D<Di));
    F(ID(D<Di))=[];
     end
    Niche_i = [ Niche_i; Reference_Point];
     
 end
 
 if(size(Niche_i,1)==1)
       [ID, D] = knnsearch(Penalized, Niche_i, 'k', size(Penalized,1));
       [D, I] = max(D)
       Niche_i = [Niche_i; Penalized(ID(I),:) ]
 end
 count = count +size(Niche_i,1)
 Population = Penalized
 Penalized=[]
    %Ranks(i) = Niche_i
  %  s = contour(X,Y,Z,'ShowText','on');
 % hold on
    s = scatter( Niche_i(:,1),Niche_i(:,2), 90, 'filled');
    %hold all
pause(1)
end





 
 