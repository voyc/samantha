import os
import numpy as np
import matplotlib.pyplot as plt  

os.chdir('/Users/John/_webapps/samantha/html/doc/script/python')

# environment variable PYTHONSTARTUP
# os.getcwd()
# exec(open("./plotequations.py", encoding="utf8").read())

plotfolder = '../../dokuwiki/data-media/'

def run(filename):
	exec(open(filename + '.py', encoding="utf8").read())
	return;

def formatgraph(title):
	fig = plt.gcf()
	fig.set_size_inches(4,3)
	ax = plt.gca();
	ax.spines['right'].set_position('zero')
	ax.spines['top'].set_position('zero')
	ax.spines['bottom'].set_linewidth(0)
	ax.spines['left'].set_linewidth(0)
	plt.grid()
	if title:
		plt.title(title)
	plt.legend() # (loc=9) upper-center
	return;

def savegraph(title):
	fig = plt.gcf()
	fname = title.replace(' ', '_');
	fname = fname.replace(',', '');
	fname = fname.replace('\'', '');
	fname = fname.lower();
	fname = plotfolder + fname + '.png'
	fig.savefig(fname);
	return;
