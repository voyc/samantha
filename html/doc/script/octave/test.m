
dotproduct = @(w,x) (sum(w .* x,2));

# linear function 1
X = [-10:1:10];
f = @(x,a,b) (a*x + b);
plot(X, f(X,3,15));

# linear function 2
theta = [15;3];
xa = [ones(size(X));X]';
h = @(theta,x) (dotproduct(theta',x));
plot(X, h(theta, xa));
