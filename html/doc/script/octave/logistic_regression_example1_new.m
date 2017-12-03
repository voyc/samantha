clear
figure(2)
clf
figure(1)
clf

# utility functions
dotProduct = @(w,x) (sum(w .* x,2));
addOneCol = @(x) ([ones(size(x)) x]);

# decision boundary function
db = @(theta,x) (dotProduct(theta',x));

# sigmoid function
s = @(x) (1 ./ (1 + e.**-z));

# classifer function: sigmoid function with decision boundary as z
f = @(theta,x) (1 ./ (1 + e.**-(db(theta,x))));
f = @(theta,x) (1 ./ (1 + e.**-((sum (theta' .* x, 2)))));

# cost function
j = @(theta,x,y) ((1/size(x,1)) .* sum( y .* log(f(theta,x)) + (1-y) .*  log(1-f(theta,x))));
j = @(theta,x,y) ((1/size(x,1)) .* -sum( y .* log(f(theta,x)) + (1-y) .*  log(1-f(theta,x))));

# gradient calculation
#pa = @(theta,x,y) ((1/size(x,1)) * sum((f(theta,x) - y)));
pa = @(theta,x,y) ((1/size(x,1)) * sum(sum((f(theta,x) - y))));
pb = @(theta,x,y) ((1/size(x,1)) * sum(sum((f(theta,x) - y) .* x)));
g  = @(theta,x,y) ([pa(theta,x,y); pb(theta,x,y)]);
#gradient =  (1/(2*m)) * sum(((sum(theta' .* X,2) - y).*2) .* X);

# gradient descent function
function [theta, jHistory] = gradientDescent(theta, x, y, gfunc, jfunc, alpha, iters)
  jHistory = zeros(iters, 1);
  n = 1;
  for i=1:iters
    jHistory(n) = jfunc(theta,x,y);
    gradient = gfunc(theta,x,y);
    theta = theta - (alpha .* gradient);
	n = n+1;
  end
end

# --------------------------------

# training data set
X = [1;2;4;6;8;9];
Y = [0;0;0;1;1;1];

X = [1;2;4;4;6;6;8;9];
Y = [0;0;0;1;0;1;1;1];

# starting parameters
#theta = [15;-3];
theta = [-200;40];
theta = [0;0];
theta = [-15;3];

# plot training data
scatter(X,Y, 'r', 'filled')
hold on

# plot starting decision boundary
fd=linspace(0,10);
fdx = addOneCol(fd');
plot(fd, db(theta,fdx), ';starting db;');
axis([-inf,inf,0,1])
axis([-inf,inf,-.1,1.1])

# plot starting classifer
plot(fd, f(theta,fdx), ';starting classifer;');

# run gradient descent
XA = addOneCol(X);
num_iterations = 10000;
learning_rate = .1;
[opt_theta, j_history] = gradientDescent(theta, XA, Y, g, j, learning_rate, num_iterations);

# optimal parameters
opt_theta

# plot optimal classifer
plot(fd, f(opt_theta, fdx), ';optimal;');

# save
title('Logistic Regression Example 1.');
xlabel('x');
ylabel('y');
legend('location', 'east');
#print([imagedir 'logistic_regression_example1.png'], '-S400,300');

# plot cost function iterations
figure(2);
i = [1:1:num_iterations];
plot(i, j_history(i));
