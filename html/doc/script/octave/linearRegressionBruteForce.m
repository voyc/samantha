1; # brute force version of linear regression

function sse = sumSquaredError( X,y,theta)
  sse = sum((sum(theta' .* X,2) .- y) .^ 2);
end

function drawCircle(pt,r, fmt) 
  t = linspace(0,2*pi,100)'; 
  x = r.*cos(t) + pt(1); 
  y = r.*sin(t) + pt(2); 
  plot(x,y, fmt); 
end

X = [1 1;1 3;1 6;1 9];
y = [4;4;7;8];

# run the costFunction many times
#theta = [-5:.1:5;-5:.1:5];                           # 2.9      0.6
#theta = [-1:.1:7;1.3:-.02:-.3];                      # 3.1      0.56      1.03520
#theta = [linspace(-1,7,100); linspace(-.3,1.3,100)]; # 3.04     0.57273   1.03690
#theta = [linspace(1,5,100); linspace(.3,.9,100)];     # 3.06061  0.56667   1.03419
theta = [linspace(2,4,100); linspace(.4,.8,100)];  # 3.06907  0.56456   1.03402
cost = [];
costg = [];
n = 1;
threshhold = 0;
lowpoint = [10 10 10];

# calculate cost for every theta
for i = 1:size(theta(1,:),2);
  for j = 1:size(theta(2,:),2);
    cost(i,j) = sumSquaredError(X,y,[theta(1,i); theta(2,j)]);

    costg(i,j) = cost(i,j) .* (1/8); # cost function per Andrew Ng
	
    if threshhold > 0 && cost(i,j) > threshhold
      cost(i,j) = threshhold;
    endif

    if cost(i,j) < lowpoint(1,3)
      lowpoint = [theta(1,i) theta(2,j) cost(i,j)];
    endif	  
  end;
end;

n
lowpoint
mesh(theta(1,:), theta(2,:), cost)
xlabel('theta1');
ylabel('theta2');
