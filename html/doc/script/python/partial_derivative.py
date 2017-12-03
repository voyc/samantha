from sympy import symbols, diff
x, y = symbols('x y', real=True)

# this does not work with run()
# I have to copy-paste into terminal

# gradient example 1
f = 8 - (x**2 + y**2)
diff(f, x)

# gradient example 2
f = (-3*x**2 + 2*y**2 + 15)
diff(f, x)
diff(f, y)

# gradient example 3
f = (x**2 + y**2);
diff(f, x)
diff(f, y)

# linear cost function, 1/2 MSE
m,X,Y,a,b = symbols('m X Y a b', real=True)
c = ((1/2) * (1/m) * sum(((a*X + b) - Y)**2))

c = ((1/2) * (1/m) * sum( ((a*X + b) - Y)**2) )




d = (a*X + b)    # predictor
d = ((a*X + b) - Y)   # error
d = np.power(((a*X + b) - Y),2)  # squared error
d = (np.power(((a*X + b) - Y),2)).sum()   # sum of squared error
d = (1/m) * (np.power(((a*X + b) - Y),2)).sum()   # mean squared error
d = (1/2) * (1/m) * (np.power(((a*X + b) - Y),2)).sum()   # one-half mean squared error

m,X,Y,a,b = symbols('m X Y a b', real=True)
d = (1/2) * (1/m) * (np.power(((a*X + b) - Y),2)).sum()   # one-half mean squared error
diff(d, x)
diff(d, y)
