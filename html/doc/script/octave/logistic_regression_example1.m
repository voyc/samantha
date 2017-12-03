
# training data set
X = [1;2;4;6;8;9];
Y = [0;0;0;1;1;1];

# starting parameters
theta = [3 15];

# basic sigmoid curve
#s = @(x) (1 ./ (1 + e.**-x));

# sigmoid curve with parameters to fit data
f = @(x, theta) ((1 ./ (1 + e.**(-theta(1)*x +theta(2)))));

# plot training data
scatter(X,Y, 'r', 'filled')
hold on

# plot sigmoid curve with starting parameters
fd=linspace(-1,10);
plot(fd, f(fd, theta));

# cost function, MSE
m = size(X,1);
j = @(theta) ((1/m) .* sum( Y .* log(f(X,theta)) + (1-Y) .*  log(1-f(X,theta))));

# gradient calculation
pa = @(theta) ((1/m) .* sum((f(X,theta) - Y)));
pb = @(theta) ((1/m) .* sum((f(X,theta) - Y) .* X));
g  = @(theta) ([pa(theta) pb(theta)]);

# gradient descent
function theta = gradient_descent(theta, gradient_func, num_iterations, learning_rate)
  for i=1:num_iterations
    gradient = gradient_func(theta);
    theta = theta - (learning_rate * gradient);
  end
end

num_iterations = 1500;
learning_rate = .1;
theta = [3 15];
gtheta = gradient_descent(theta, g, num_iterations, learning_rate);

# output
gtheta
plot(fd, f(fd, gtheta));
# save
title('Logistic Regression Example 1.');
xlabel('x');
ylabel('y');
print([imagedir 'logistic_regression_example1.png'], '-S400,300');
