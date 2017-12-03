

x = linspace(-2,2);

# positive square is concave
plot(x,x.^2);

# negative square is convex
plot(x,-x.^2);

plot(x,-x.^3);

plot(x,x.^-3);


plot(x,2*x.^2);


x = linspace(-8,8);
plot(x,x.^2 + 2*x + 3);
