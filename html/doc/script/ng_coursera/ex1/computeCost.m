function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

method = 1;  % procedural
method = 2;  % matrix math
method = 3;  % single line of code

if method == 1  % procedural
	% hypothesis given by the linear model
	% y = ax + b   // linear equation
	% y = b + ax   // reverse terms
	% h = theta(1) + (theta(2) * X(2));  // replace b and a with theta(1) and theta(2)
	% h = (theta(1) * X(1)) + (theta(2) * X(2));  // multiply the y-intercept by X(1), knowing that X(1) is always one

	% create vector h containing all predicted values
	for i=1:m
		h(i) = (theta(1) * X(i,1)) + (theta(2) * X(i,2));
	end

	% create vector err containing the err of each point
	for i=1:m
		err(i) = h(i) - y(i);
	end

	% sum the squared errors
	squares = 0;
	for i=1:m
		squares += err(i) ^ 2;
	end
	
	% multiply by 1/2m
	J = (1/(2*m)) * squares;

elseif method == 2  % matrix math

	% create matrix w containing all weighted columns
	w = theta' .* X; 

	% create matrix h of predicted values
	h = sum(w,2);

	% create vector err containing the err of each point
	err = h - y;
	
	% square the errors
	sqErr = err.^2;

	% sum the squared errors
	squares = sum(sqErr);

	% multiply by 1/2m 
	J = (1/(2*m)) * squares;

else % method = 3	% one line of code, but multiple operations same as method 2

	J = (1/(2*m)) * sum((sum(theta' .* X,2) - y).^2);

end 

% =========================================================================

end
