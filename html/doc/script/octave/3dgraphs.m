# notes on meshgrid
# meshgrid replicates rows of x and cols of y, so that x and y have the same size as z
x=linspace(-2,2,5);
y=linspace(-2,2,5);
[xx,yy]=meshgrid(x,y);

# scatter3 requires the meshgrid format
[xx,yy]=meshgrid(x,y);
zz = 4-(xx.^2+yy.^2);
scatter3(xx,yy,zz);

# plot, mesh, meshc, surf, contour also allow the x,y,z format, where x and y are vectors
x=linspace(-2,2,5);
y=linspace(-2,2,5);
for i=1:size(x,2)
  for j=1:size(y,2)
    z(i,j) = 4-(x(i).^2+y(j).^2);
  end
end
plot3(x,y,z);
mesh(x,y,z)
meshc(x,y,z)
surf(x,y,z)
contour(x,y,z)
#scatter3(x,y,z)  # does not work

# cool surface made with e
x = -2:0.25:2;
y = x;
[X,Y] = meshgrid(x);
F = X.*exp(-X.^2-Y.^2);
surf(X,Y,F)

# spiral around a sphere 
# A sphere with center at the origin may also be specified in spherical coordinates by
# where theta is an azimuthal coordinate running from 0 to  2pi (longitude), phi is a polar coordinate running from 0 to pi (colatitude), and rho is the radius.
radius = 1;
theta = linspace(0,2*pi);
phi = linspace(0,pi);
x = radius .* cos(theta) .* sin(phi);
y = radius .* sin(theta) .* sin(phi);
z = radius .* cos(phi);
scatter3(x(i), y(i), z(i));
hold
for i = 1 : size(x,2)
    scatter3(x(i), y(i), z(i));
end

# unit sphere
[px,py,pz] = sphere();
surf(px,py,pz);

# quadratic, two variables
# z = x^2 + xy + y^2, two corners low, two high
x = linspace(-1,1);
y = linspace(-1,1);
for i = 1 : size(x,2)
  for j = 1 : size(y,2)
    z(i,j) = x(i).^2 + x(i)*y(j) + y(j).^2;
  end
end
mesh(x,y,z);

# z = x^2 + y^2, remove the middle term xy, perfect bowl
x = linspace(-1,1);
y = linspace(-1,1);
for i = 1 : size(x,2)
  for j = 1 : size(y,2)
    z(i,j) = x(i).^2 + y(j).^2;
  end
end
mesh(x,y,z);
