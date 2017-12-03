1;

function dot(x,y,z,radius)
  [p,q,r] = sphere();
  p = p .* radius;
  q = q .* radius;
  r = r .* radius;
  surf(x+p, y+q, z+r);
end

# the original function
f = @(x,y) 8-(x.^2 + y.^2);

# Plot the original function, a concave 3D parabola
x = -2:0.25:2;
y = -2:0.25:2;
for i=1:size(x,2) 
  for j=1:size(y,2)
    z(i,j) = f(x(i), y(j));
  end
end
meshc(x,y,z);
hold on;

# choose a random point (x0,y0) on that surface
i = 12;
j = 3;
point = [x(i) y(j) z(i,j)]
dot(x(i), y(j), f(x(i), y(j)), .05)

# calculate both partial derivatives
pfpx = -2*x(i);        # partial derivative with respect to x
pfpy = -2*y(j);        # partial derivative with respect to y

gradient = [pfpx pfpy]

p1 = [x(i) y(j)];
p2 = p1 + gradient;

px = [p1(1), p2(1)];
py = [p1(2), p2(2)];
pz = [0,0];
plot(px,py, 'r');

# save
title('Gradient Example 1.')
# print([imagedir 'gradient_example1.png'], '-S400,300');


# https://www.mathworks.com/help/matlab/math/calculate-tangent-plane-to-surface.html
# https://www.gnu.org/software/octave/doc/v4.0.3/Utility-Functions.html

