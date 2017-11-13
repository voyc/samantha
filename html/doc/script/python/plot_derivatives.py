def saveplot(fname):
    fig = plt.gcf()
    fname = '../../../dokuwiki/media/' + fname + '.png'
    fig.savefig(fname);
    return;

x = np.linspace(0,4,40);
plt.plot(x,30*x, label='ƒ(x) = 30x'); 
plt.plot(x,0*x+30, label='ƒ′(x) = 0x+30'); 
formatgraph('Constant Rate of Change')
saveplot  ('constant_rate_of_change')
plt.show()

x = np.linspace(0,4,40);
plt.plot(x,32 * x ** 2, label='ƒ(x) = 32x²'); 
plt.plot(x,32*x, label='ƒ′(x) = 32x'); 
formatgraph('Constant Acceleration')
saveplot  ('constant_acceleration')
plt.show()

x = np.linspace(0, 2*np.pi, 50);
plt.plot(x,np.sin(x), label='ƒ(x) = sin(x)'); 
plt.plot(x,np.cos(x), label='ƒ′(x) = cos(x)'); 
plt.plot(x,-np.sin(x), label='ƒ′′(x) = -sin(x)'); 
formatgraph('Sine')
saveplot('sine_derivative_and_second_derivative')
plt.show()

x = np.linspace(-2, 2, 50);
x2 = np.linspace(-1.5, 1.5, 40);
e = np.exp(1);
plt.plot(x,e**x, label='ƒ(x) = eˣ'); 
plt.plot(x2,e**x2, label='ƒ′(x) = eˣ'); 
formatgraph('Exponent')
saveplot('exponent_equals_its_own_derivative')
plt.show()

x = np.arange(-.7, 1.5, .1);
plt.plot(x,(x**3)-(x**2), label='ƒ(x) = x³ - x²');
#plt.plot(x,((3*x)**2)-2*x, label='ƒ′(x) = 3x² - 2x'); 
#plt.plot(x,(6*x)-2, label='ƒ′′(x) = 6x - 2'); 
formatgraph('Polynomial')
saveplot  ('polynomial')
plt.show()

x = np.arange(-.7, 1.5, .1);
plt.plot(x,(3*x**2)-(2*x), label='ƒ′(x) = 3x² - 2x'); 
formatgraph('Polynomial Derivative')
saveplot  ('polynomial_derivative')
plt.show()

x = np.arange(-.7, 1.5, .1);
plt.plot(x,(6*x)-2, label='ƒ′′(x) = 6x - 2'); 
formatgraph('Polynomial Second Derivative')
saveplot  ('polynomial_second_derivative')
plt.show()

x = np.linspace(-5, 5);
plt.plot(x,e**((-x**2)/2)); 
formatgraph('')
fig = plt.gcf()
fig.set_size_inches(4,1)
saveplot  ('bell_curve_limit')
plt.show()

x = np.linspace(-3, 3);
plt.plot(x,e**((-x**2)/2), label='ƒ(x)e**((-x**2)/2)'); 
formatgraph('')
saveplot  ('bell_curve')
plt.show()

x = np.linspace(-3, 3);
plt.plot(x,x*e**((-x**2)/2), label='ƒ′ = x*e**((-x**2)/2)'); 
formatgraph('')
saveplot  ('bell_curve_first_derivative')
plt.show()

x = np.linspace(-3, 3);
plt.plot(x,((x**2)-1)*e**((-x**2)/2), label='ƒ ′′(x) = ((x**2)-1)*e**((-x**2)/2)'); 
formatgraph('')
saveplot  ('bell_curve_second_derivative')
plt.show()

x = np.linspace(-3, 3);
plt.plot(x,e**((-x**2)/2), label='ƒ(x) = e**((-x**2)/2)'); 
plt.plot(x,x*e**((-x**2)/2), label='ƒ ′(x) = x*e**((-x**2)/2)'); 
plt.plot(x,((x**2)-1)*e**((-x**2)/2), label='ƒ ′′(x) = ((x**2)-1)*e**((-x**2)/2)'); 
formatgraph('')
saveplot  ('bell_curve_with_first_and_second_derivative')
plt.show()

#-----------------
#
#x = np.arange(-5,5,.1);
#e = np.exp(1);
#plt.plot(x,x**2, label='ƒ(x) = x²'); 
#plt.plot(x,2*x, label='ƒ′(x) = 2x'); 
#formatgraph('Square and Derivative')
#savegraph('Square and Derivative')
#plt.show()
#
#x = np.arange(-5,5,.1);
#plt.plot(x,x**3, label='ƒ(x) = x³'); 
#plt.plot(x,3*x, label='ƒ′(x) = 3x'); 
#formatgraph('Cube and Derivative')
#savegraph('Cube and Derivative')
#plt.show()
#
#math miscellaneous
#
## note.  In the above, 
#e = np.exp(1) # e is truncated to 16 decimal-place accuracy, therefore
#np.exp(4) # would be more accurate than e ** 4
#
#ƒ(x) = abˣ  # exponential function
#
#ƒ(x,y) = xʸ  # exponentiation
#
#ƒ(x) = xʳ  # power function
#
#The natural exponential function y = ex
#In mathematics, an exponential function is a function of the form
#
#{\displaystyle f(x)=b^{x}\,} {\displaystyle f(x)=b^{x}\,}
#
#
## euler's number
#e = 2.7182818284590452353602874713527
#
#x = np.linspace(.01, 5, 50);
#plt.plot(x, (1 + (1/x))**x, label='y = (1 + (1/x))ˣ')
#formatgraph('Euler`s Number')
#savegraph('Euler`s Number')
#plt.show()
## http://www.mathsisfun.com/numbers/e-eulers-number.html
#
#x cubed minus x squared has a local minimum and a local maximum. The derivative is 3 x squared minus 2X. The second derivative is 6 x -2 a straight 
#
#