1;

# function
f = @(x,y) (x.^2 + y.^2);  # original function

# partial derivatives
px = @(x) (2*x);   # partial derivative with respect to x
py = @(y) (2*y);   # partial derivative with respect to y

# sample points
pt = [.75 -1.5; -1.75 -.5; -.25 -.25];

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
  px0 = px(x0);   # partial derivative with respect to x
  py0 = py(y0);   # partial derivative with respect to y
  gradient = [px0 py0];
  p0 = [x0 y0];
  p1 = p0 + gradient;
  ax = [p0(1), p1(1)];
  ay = [p0(2), p1(2)];
  az = [0,0];
  plot3(ax,ay,az,tcolor(c), 'linewidth', 2);
  dot(x0, y0, f(x0, y0), .05, mcolor(c,:));
  gradient
  f(x0, y0)
end

# Plot the original function, a concave 3D parabola
for i=1:size(x,2) 
  for j=1:size(y,2)
    z(i,j) = f(x(i), y(j));
  end
end
mesh(x,y,z); #, 'FaceColor', 'none');
hold on;
contour(x,y,z);

# plot sample points and gradients
for k=1:size(pt,1)
  plotgrad(f, px, py, pt(k,:), k);
end

# save
title('Gradient Example 2.')
print([imagedir 'gradient_example2.png'], '-S400,300');
