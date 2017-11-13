import numpy as np  
import matplotlib.pyplot as plt  
import math

def graph(title, formula1, label1, *more, x_range=np.arange(-10,11,.1)):
	# first plot
	x = np.array(x_range)
	plt.plot(x, formula1(x), label=label1)
	
	# additional optional plots
	if len(more) > 0:
		form = more[0]
		label = more[1]
		plt.plot(x, form(x), label=label)
	if len(more) > 2:
		form = more[2]
		label = more[3]
		plt.plot(x, form(x), label=label)
	
	# format graph
	fig = plt.gcf()
	fig.set_size_inches(4,3)
	ax = plt.gca();
	ax.spines['right'].set_position('zero')
	ax.spines['top'].set_position('zero')
	ax.spines['bottom'].set_linewidth(0)
	ax.spines['left'].set_linewidth(0)
	plt.grid()
	plt.title(title)
	plt.legend(loc=9)
	fname = title.replace(' ', '_');
	fname = fname.replace(',', '');
	fname = fname.replace('\'', '');
	fname = fname.lower();
	fname = '../../image/plot/' + fname + '.png'
	fig.savefig(fname);
	plt.show()
	return;


graph('Straight Line', lambda x: 2*x+30, 'y = 2x + 3')
graph('Parabola', lambda x: 3*x**2-100, 'y = 3x² - 100', lambda x: -3*x**2+100, 'y = -3x² + 100')

graph('Quadratic 1', lambda x: 3*x**2+4*x+7, 'y = 3x² + 4x + 7')
graph('Quadratic 2', lambda x: 2*x**3 + 3*x**2+4*x+7, 'y = 2x³ + 3x² + 4x + 7')
graph('Quadratic 3', lambda x: 4*x**2 + 2.1*x + 22, 'y = ax2 + bx + c ')

# polynomials
graph('Polynomial 0 Degree', lambda x: 7*x**0, 'ƒ(x) = 7x⁰')
graph('Polynomial 1 Degree', lambda x: 3*x + 7*x**0, 'ƒ(x) = 3x¹ + 7x⁰')
graph('Polynomial 2 Degree', lambda x: 1.2*x**2 + 3*x + 7*x**0, 'ƒ(x) = 1.2x² + 3x¹ + 7x⁰', x_range=np.arange(-5,5,.1))
graph('Polynomial 3 Degree', lambda x: .5*x**3 + 1.2*x**2 + 3*x + 7*x**0, 'ƒ(x) = .5x³ + 1.2x² + 3x¹ + 7x⁰', x_range=np.arange(-5,3,.1))
graph('Polynomial 4 Degree', lambda x: .2*x**4 + .5*x**3 + 1.2*x**2 + 3*x + 7*x**0, 'ƒ(x) = .2x⁴ + .5x³ + 1.2x² + 3x¹ + 7x⁰', x_range=np.arange(-3,1.5,.1))

# http://philschatz.com/precalculus-book/contents/m49347.html#Figure_03_04_009
graph('Polynomial x', lambda x: (x+3)*((x-2)**2)*((x+1)**3), 'ƒ(x)=(x+3)(x−2)²(x+1)³', x_range=np.arange(-3.1,2.5,.1))
graph('Polynomial xx', lambda x: x**4 - x**3 - 4*x**2 + 4*x, 'ƒ(x)=x⁴−x³−4x²+4x', x_range=np.arange(-2.5,3,.1))

# more polynomials
graph('Polynomial xxx', lambda x: 2/x + 3, 'y = 2/x + 3', x_range = np.arange(-5, 5, .1))
graph('Polynomial xxxx',lambda x: 2*(1/x) + 3, 'y = 2(1/x) + 3', x_range = np.arange(-.1, .1, .01))

# Bill Stranger Calculus Big Picture youtube
graph('Squared and Derivative', lambda x: x**3, 'y = x³', lambda x: 3*x**2, 'y′ = 3x²')
graph('Cubed and Derivative', lambda x: x**3, 'y = x³', lambda x: 3*x**2, 'y′ = 3x²')   # derivative, power rule
graph('Sine, Derivative, and Second Derivative', lambda x: np.sin(x), 'y = sin(x)', lambda x: np.cos(x), 'y′ = cos(x)', lambda x: -np.sin(x), 'y″ = -sin(x)')

# euler's number
graph('Euler\'s number', lambda x: (1 + (1/x))**x, 'y = (1 + (1/x))**x)', x_range=np.arange(.1,5,.1))
e = 2.7182818284590452353602874713527
# http://www.mathsisfun.com/numbers/e-eulers-number.html

# sigmoid
graph('Sigmoid', lambda x: 1 / (1 + e**-x), 'y = 1 / (1 + e**-x)') # Octave: y = 1 ./ (1 + e.^-x);
# https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Sigmoid_function.html


# linear regression
y = a1x1 + a2x2 + a3x3 + b
y = A . X + b

# straighten the parabola, e.g. u=(1+x)^2; that's trivial. 
# Reference https://www.physicsforums.com/threads/transforming-parabola-to-straight-line.301713/



# earlier versions of the graph function
def graph1(formula, x_range=range(-10, 11)):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)
    plt.show()
    return;

def graph2(formula1, label1, formula2, label2, x_range=range(-10, 11)):
	x = np.array(x_range)
	plt.plot(x, formula1(x), label=label1)
	plt.plot(x, formula2(x), label=label2)
	ax = plt.gca();
	ax.spines['right'].set_position('zero')
	ax.spines['top'].set_position('zero')
	ax.spines['bottom'].set_linewidth(0)
	ax.spines['left'].set_linewidth(0)
	plt.grid()
	plt.legend(loc=9)
	plt.show()
	return;
