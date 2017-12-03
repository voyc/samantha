1;

#x = [-10:.1:10];
#plot(x, 1 ./ (1 + e.^-x), ';1 ./ (1 + e.^-x);', 'linewidth',2)
#title('Sigmoid')
#print('../../image/plot/sigmoid.png', '-S400,300');
#
#x = [-10:.1:10];
#plot(x, x.^2, ';f(x) = x.^2;', 'linewidth',2)
#hold on
#plot(x, x.*2, ';f`(x) = x.*2;', 'linewidth',2)
#title('Square and Derivative')
#print('../../image/plot/square_and_derivative.png', '-S400,300');
#
#x = [-10:.1:10];
#plot(x, x.^3, ';f(x) = x.^3;', 'linewidth',2)
#hold on
#plot(x, x.*3, ';f`(x) = x.*3;', 'linewidth',2)
#set (gca, "xaxislocation", "origin")
#set (gca, "yaxislocation", "origin")
#set (gca, "box", "off")
#title('Cube and Derivative')
#print('../../image/plot/cube_and_derivative.png', '-S400,300');


x = -1.2:0.01:1.2;
# x.^2 + y.^2 = 1;  # unit circle equation
y = (1 - x.^2) .^ .5;  # rewrite in terms of y
plot(x,y);
hold on;
plot(x,-y);





#t = linspace(0,2*pi,100)'; 
#r = 1;
#circsx = r.*cos(t) + x; 
#circsy = r.*sin(t) + y; 
#plot(circsx,circsy); 
#set (gca, "xaxislocation", "origin")
#set (gca, "yaxislocation", "origin")
#set (gca, "box", "off")
title('Circle')
#print('../../image/plot/cube_and_derivative.png', '-S400,300');
