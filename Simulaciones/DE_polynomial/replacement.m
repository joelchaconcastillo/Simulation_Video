function [survivors] = replacement(Current, F_Current, Di, N)
    
    Penalized=[];
    count = 0;
    survivors = [];
      while count < N && length(Current) > 0
        %Select the best individual with max fitness
        [Reference_Point, I] = min(F_Current);
        Reference_Point = Current(I,:);        
        [Current, PS] = removerows(Current,'ind',I);
        F_Current(I)=[];
        if(length(Current)>0)
            %Find the nearest points to the reference
            [ID, D] = knnsearch(Current, Reference_Point, 'k', size(Current,1));
            Penalized = [Penalized ; Current(ID(D<Di),:)];
            [Current, PS] = removerows(Current,'ind',ID(D<Di));
            F_Current(ID(D<Di))=[];
        end
        survivors = [ survivors; Reference_Point];   
        count = count+1;
      end     
%       mindcn = ones(length(Penalized))*10000;
%       for i =1:length(Penalized)
%          for j = 1:length(survivors)
%              mindcn(i) = min(mindcn(i), pdist2(Penalized(i,:), survivors(j,:), 'euclidean'));
%          end
%       end
%       while count < N
%           maxdcn = -1000000;
%           maxidx = -1;
%           for i = 1:length(Penalized)
%               if mindcn(i) > maxdcn 
%                  maxdcn = mindcn(i);
%                  maxidx = i;
%               end
%           end
%           %update maxdcn
%           for i=1:length(Penalized)
%              mindcn(i) = min(mindcn(i), pdist2(Penalized(i,:), Penalized(maxidx,:), 'euclidean'));
%           end
%           survivors = [survivors; Penalized(maxidx,:)];
%          [Penalized, PS] = removerows(Penalized,'ind',maxidx);
%          [mindcn, PS] = removerows(mindcn,'ind',maxidx);
%          count = count+1;
%       end
      while count < N
           [ID, D] = knnsearch(survivors, Penalized, 'k', 1);
           [D, I] = max(D);
           survivors = [survivors; Penalized(I,:) ];
           [Penalized, PS] = removerows(Penalized,'ind',I);
           count = count +1;
      end
end