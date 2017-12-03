
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
surf(x,y,z);
mesh(x,y,z);

