function [y] = evaluation(xx)
%y = sin(xx(1)) + cos(xx(2));
%%%%%%%%%%%%%%%%%%Rosenbrock
 d = length(xx);
sum = 0;
for ii = 1:(d-1)
	xi = xx(ii);
	xnext = xx(ii+1);
	new = 100*(xnext-xi^2)^2 + (xi-1)^2;
	sum = sum + new;
end
y = sum;

%%%%%%%%%%%%%%%%%%%dixonpr
% x1 = xx(1);
% d = length(xx);
% term1 = (x1-1)^2;
% 
% sum = 0;
% for ii = 2:d
% 	xi = xx(ii);
% 	xold = xx(ii-1);
% 	new = ii * (2*xi^2 - xold)^2;
% 	sum = sum + new;
% end
% 
% y = term1 + sum;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% x1 = xx(1);
% x2 = xx(2);
% 
% term1 = (4-2.1*x1^2+(x1^4)/3) * x1^2;
% term2 = x1*x2;
% term3 = (-4+4*x2^2) * x2^2;
% 
% y = term1 + term2 + term3;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% 
% d = length(xx);
% sum = 0;
% for ii = 1:d
% 	xi = xx(ii);
% 	sum = sum + (xi^2 - 10*cos(2*pi*xi));
% end
% 
% y = 10*d + sum;

end