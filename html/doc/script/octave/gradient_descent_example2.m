1;

# linear function
global f = @(a,b) (a.*X .+ b);

# data
global X = [1; 3; 6; 9];
global Y = [4; 4; 7; 8];
global m = 4;

# cost function = 1/2 MSE (mean squared error)
global c = @(a,b) ((1/2) * (1/m) * sum(((a.*X .+ b) .- Y).^2));

# partial derivatives
global pa = @(a,b) ((1/m) * sum((a.*X .+ b) .- Y));        # partial derivative with respect to a
global pb = @(a,b) ((1/m) * sum(((a.*X .+ b) .- Y) .* X));   # partial derivative with respect to b

# gradient
global g = @(a,b) ([pa(a,b) pb(a,b)]);

# starting point
a = .7;
b = 3.5;

global mcolor = [1 0 0; 0 1 0; 0 0 1;1 1 0];
global tcolor = ['r'; 'g'; 'b'; 'y'];

function dot(x,y,z,radius, color)
  [p,q,r] = sphere();
  p = p .* radius;
  q = q .* radius;
  r = r .* radius;
  surf(x+p, y+q, z+r, 'FaceColor', color, 'EdgeColor', color);
end

# plot gradient for a point
function plotgrad(f, px, py, p, c)
  global mcolor tcolor;
  x0 = p(1);
  y0 = p(2);
  dot(x0, y0, f(x0, y0), .005, mcolor(c,:));
end

# Plot the cost function
ap = linspace(.4,.8,50);  # c=3.06907  a=0.56456   b=1.03402
bp = linspace(2,4,50); 
#ap = -10:.5:10;
#bp = -10:.5:10;
for i=1:size(ap,2) 
  for j=1:size(bp,2)
    cp(j,i) = c(ap(i), bp(j));
  end
end
meshc(ap,bp,cp);
hold on;

# iterate step-by-step in the direction towards the minimum
number_of_iterations = 40;
learning_rate = .01;
p = [a b];
for k=1:number_of_iterations
  plotgrad(c, pa, pb, p, 1);
  ptgradient = g(p(1), p(2));
  p = p - (ptgradient .* learning_rate);
end

# result
a = p(1)  # optimal a
b = p(2)  # optimal b
c(a, b)  # lowest cost

# save
title('Gradient Descent Example 2.')
#print([imagedir 'gradient_descent_example2.png'], '-S400,300');
