%%Parametros necesarios: Número de puntos, Tamanio de las muestras,
%%probabilidad de seleccionar individuos del vecindario, probabilidad para
%%seleccionar individuos de todo el conjunto...

N =500;
Min = -1;
Max = 1;
k=20;

%%Generar N números de forma aleatoria en dos dimensiones...
Population = Min + rand(N, 2)*(Max-Min);

Result = []

for i = 1:10
%Obtener lo k individuos más cercanos y definirlo como vecindario en cada
%individuo

%% Obtener una mestra de tamanio k y seleccionar a los dos más distantes
%Sample = Population(randsample(1:N, k),:)
Sample = Population(randi(N, k),:)


[Best I] = pdist2(Sample, Sample, 'euclidean', 'Largest', 1)

%%De cada muestra seleccionar a los dos individuos más alejados y
%%almacenarlos en los resultados...

Result = [Result; Sample(I,:)]; 
a=transpose(Sample(I,1))
b=transpose(Sample(I,2))
%c=transpose(Sample(I,3))
kd=convhull(a,b);
%kd=convhull(a,b,c);
%plot3( a(kd), b(kd), c(kd),'r-');
plot( a(kd), b(kd),'r-');
  hold on
end


 scatter(Population(:,1),Population(:,2), 'g');
 %       scatter3(Population(:,1),Population(:,2), Population(:,3),'g');
  hold on
 scatter( Result(:,1),Result(:,2), 'filled', 'b');
    xlabel('x1');
    ylabel('x2');
%    zlabel('x3');
    title('Simulación de la restricción de emparejamiento');
    
 %   scatter3( Result(:,1),Result(:,2), Result(:,3),'filled','b');
    


    pause(5)
