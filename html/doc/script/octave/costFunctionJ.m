function J = costFunctionJ(X,y,theta)

% X = matrix m x n, the training data
% y = vector m x 1, the actual values
% theta = scalar, learning coeffecient
% J will be a real number

% usage: 
% >> X = [1 1; 1 2; 1 3];
% >> y = [1; 2; 3];
% >> theta = [0;1];
% >> j = costFunctionJ(X,y,theta)
% j = 0
% >> theta = [0;0];
% >> j = costFunctionJ(X,y,theta)
% j =  2.3333
% >>

m = size(X,1);  % number of training examples
predictions = X*theta;  % predictions of hypotheses on all m examples
sqrErrors = (predictions-y).^2;  % squared errors

J = 1/(2*m) * sum(sqrErrors);