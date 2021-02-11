function [Children] = DE_operators(Population, lowerb, upperb)
    N = length(Population);
    dimension = length(Population(1,:));
    Children = Population;
    CR = 0.0;
    F=ones(N)*0.5;%normrnd(0.5,0.1,N,1);
    %F=normrnd(0.5,0.1,N,1);
    for target = 1:N
        %%DE-mattting..
        r1 = randi([1 N]);
        r2 = randi([1 N]);
        r3 = randi([1 N]);
%         while r1 == target
%           r1 = randi([1 N]);Pp
%         end
%         while r2 == target || r2==r1
%           r2 = randi([1 N]);
%         end
%         while r3 == target || r3==r1 || r3==r2
%           r3 = randi([1 N]);
%         end
        %%DE-crossover and mutation
        idx = randi([1 dimension]);
        %if rand() < 0.5
        %    CR = 0.2;
        %else
        %    CR = 1.0;
        %end
        for d = 1:dimension
            if (rand() < CR)|| (d == idx)
                Children(target,d) = Population(r1, d) + F(target)*(Population(r2, d) - Population(r3, d));
                %Children(target,d) = Population(r1, d) + normrnd(0.5,0.1)*(Population(r2, d) - Population(r3, d));
            else
                Children(target,d) = Population(target, d);
            end
            if Children(target, d) < lowerb(d);
                Children(target, d) = Population(target, d);
                %Children(target, d) = lowerb(d);
            end
            if Children(target, d) > upperb(d);
                Children(target, d) = Population(target, d);
                %Children(target, d) = upperb(d);
            end
        end        
    end
end