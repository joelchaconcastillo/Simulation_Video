%%Replacement Phase
N =10000
Min = -10;
Max = 10;

%%Initialization
Population = Min + rand(N, 2)*(Max-Min);
Di=5

x = Min:0.2:Max;
y = Min:0.2:Max;
x = linspace(Min,Max); 
y = linspace(Min,Max);

[X,Y] = meshgrid(x,y);
Z = -X.^2 - Y.^2;
%Z = sin(X) + cos(Y);
figure
s = contour(X,Y,Z,'ShowText','on');
%hold on
%Z = (1-X).^2 + 100*(Y-X.^2).^2;
pcr=0.9
count = 0
%Ranks = zeros(500,2)
s=[]
while count < 1
    count = count +1
%   F = sin(Population(:,1)) + cos(Population(:,2));
   
   % r1 = randi([-10 10],1,1000);
    r2 = randi([1 N],N,1);
    r3 = randi([1 N],N,1);
    CR = rand(N, 2)
    fr=normrnd(0.5,0.2,N,2)
    diff(:,1) = fr(:,1).*(Population(r2,1) - Population(r3,1))
    diff(:,2) = fr(:,2).*(Population(r2,2) - Population(r3,2))
    
    xn = Population + diff
    xn(find(CR(:,1)>pcr),1) = Population( find(CR(:,1)>pcr) ,1)
    xn(find(CR(:,2)>pcr),2) = Population( find(CR(:,2)>pcr) ,2)
    
    F1x = Population(:,1).^2 + Population(:,2).^2;
    Fnx = xn(:,1).^2 + xn(:,2).^2;

    Population(F1x>Fnx,:) = xn(F1x>Fnx,:)
         
         delete(s);
         
%  s = scatter( Population(:,1),Population(:,2), 10, 'filled');
        s = scatter( diff(:,1) , diff(:,2), 10, 'filled');
  pause(0.1)
    hold on



end





 
 