imagedir = '../../dokuwiki/data-media/';

function formatplot2(tx)
  set (gca, "xaxislocation", "origin")
  set (gca, "yaxislocation", "origin")
  set (gca, "box", "off")
  title(tx)
end

# unit circle
x = -1:0.01:1;
# x.^2 + y.^2 = 1;  # unit circle equation
y = (1 - x.^2) .^ .5;  # rewrite in terms of y
plot(x,y);
hold on;
plot(x,-y, ';x^2 + y^2 = 1;', 'linewidth',2)
formatplot2('Unit Circle');
print([imagedir 'unit_circle.png'], '-S300,300');

# ellipse
clf
x = -1:0.01:1;
a = 1;
b = .5;
# (x.^2/a.^2) + (y.^2/b.^2) = 1;  # ellipse equation
y = ((1 - (x.^2/a.^2)) * b.^2) .^.5; # rewrite in terms of y
plot(x,y);
hold on;
plot(x,-y, ';(x^2/a^2) + (y^2/b^2) = 1;', 'linewidth',2)
formatplot2('Elipse');
print([imagedir 'ellipse.png'], '-S400,300');

# hyperbola
clear
clf
x = .01:0.01:1;
y = 1./x;
plot(x,y, ';y=1/x;', 'linewidth',2);
hold on;
x = -1:0.01:-.01;
y = 1./x;
plot(x,y, 'linewidth',2);
formatplot2('Hyperbola');
print([imagedir 'hyperbola.png'], '-S400,300');
