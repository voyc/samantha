

% gradient descent
% pick a value for theta, and run the whole training data set
% change theta by an amount, and run it again

% for each run
% cost function
% alpha * 1/m * sum
% cost function

% theta is the vector of weights, also known as regression variables
% theta0 is the bias or y-intercept
% x0 is set to one and prefixed to the input data

% the predictor function is the straight function
f(x) = ax + b

% we rewrite the predictor function to confuse students
f(x) = b + ax                   % 1. reverse the terms
f(x) = theta0 + theta1 * x      % 2. change b to theta1, change a to theta2
f(x) = theta0*x0 + theta1 * x1  % 3. change x to x1, insert x0, always 1 

% X is now a matrix of size m,2
% theta is a matrix of size 1,2

% to run the predictor function on the training set with matrix multiply
% we transform theta from 2x1 to 1x2    % why not just create it that way in the first place
% we will work with the transform of theta
theta' 

% run the predictor function on the training set
% procedural
for i 0 thru m: pyi = f(ix) = theta0*xi0 + theta1 * xi1
% matrix math
py = theta' * x

% py is now a vector of predicted y values
% the error is py - y
% the errorSquared is (py - y)^2
% the sum of all errors for the training set is 
for i: 0 thru m: sumSqErr += (py - y)^2

% what operation sums the rows of a vector or matrix ??

% the cost function is J(theta) = (1/2m) * sumSqErr
% Why do we multiply by 1/2m ??


 
% f(x) = theta0x0 + theta1x1  % the predicted value to compare to y



% f(x) = theta1 * x1 + theta2 * x2, where theta1 is always 1
% f(x) = theta0 + (theta1 * x1) = \theta' * x



\theta = \theta - \delta * (1/m) * sum(h(\theta)a9x)
