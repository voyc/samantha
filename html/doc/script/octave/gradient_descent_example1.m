1;

# function
f = @(x,y) (x.^2 + y.^2);  # original function

# partial derivatives
px = @(x) (2*x);   # partial derivative with respect to x
py = @(y) (2*y);   # partial derivative with respect to y

# gradient
g = @(x,y) [px(x) py(y)];

# starting point
pt = [.75 -1.5];

# 3D graph axes
x = -2:0.25:2;
y = -2:0.25:2;

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
  gradient = [x0 y0];
  p0 = [x0 y0];
  p1 = p0 + gradient;
  ax = [p0(1), p1(1)];
  ay = [p0(2), p1(2)];
  az = [0,0];
  #plot3(ax,ay,az,tcolor(c), 'linewidth', 2);
  dot(x0, y0, f(x0, y0), .05, mcolor(c,:));
  gradient;
  f(x0, y0);
end

# Plot the original function, a concave 3D parabola
x = -2:0.25:2;
y = -2:0.25:2;
for i=1:size(x,2) 
  for j=1:size(y,2)
    z(i,j) = f(x(i), y(j));
  end
end
#figure('Position',[0,0,400,300]);
mesh(x,y,z); #, 'FaceColor', 'none');
hold on;
#contour(x,y,z);

# iterate step-by-step in the direction towards the minimum
number_of_iterations = 16;
learning_rate = .1;
p = pt;
for k=1:number_of_iterations
  plotgrad(f, px, py, p, 1);
  ptgradient = g(p(1), p(2));
  p = p - (ptgradient * learning_rate);
end

# save
title('Gradient Descent Example 1.')
#print([imagedir 'gradient_descent_example1.png'], '-S400,300');
