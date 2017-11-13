1; # this is a script file, not a function

function predicted = linearFunction(theta, X)
	predicted = sum(theta' .* X,2);
end

function sse = sumSquaredError( X,y,theta)
	sse = sum((sum(theta' .* X,2) .- y) .^ 2);
end

X = [1 1;1 3;1 6;1 9]
y = [4;4;7;8]

# run the predictor function
theta = [3;1.5]
predictedY = linearFunction(theta,X)
[predictedY y]

# run the costFunction three times
theta = [3;2]    # y = 2x + 3
sumSqEr = sumSquaredError(X,y,theta)

theta = [2;1.5]  # y = 1.5x + 2
sumSqEr = sumSquaredError(X,y,theta)

theta = [2;.8]   # y = .8x + 2
sumSqEr = sumSquaredError(X,y,theta)

# run the costFunction 1000 times
theta0 = [0:.1:10;];
theta1 = [0:.1:10];
j = [];
for i = 1:size(theta0);
	for j = 1:size(theta1);
		j(i,j) = sumSquaredError(X,y,[theta0(i), theta1(j)]);
	end;
end;

