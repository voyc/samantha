''' grammar.py - implement thai grammar '''

import re
import random
import os 
import sam.grammar.vocab as vocab
import sam.grammar.numgen as numgen

thispath = os.path.dirname(os.path.realpath(__file__)) + '/'

scfilename = 'semanticconventions.txt'

uservocab = vocab.UserVocab()
#uservocab.onLogin('xxx')

class Node:
	level = 0

	def __init__(self,word,tree=[],expr='',pos='',line=''):
		self.word = word  # $expr, $static, $list, $opt, $name, $num or @name
		self.expr = expr  # used when word is $static, $name, $num
		self.tree = tree
		self.pos = pos    # at this time, used only in the root node
		self.line = line  # used only on the root, and only for testing
		self.value = ''   # used temporarily during gensen

	def print(self):
		def fn(m):
			if (Node.level == 1):
				print(m.line)
			indent = '\t' * (Node.level-1)
			x = m.expr if m.word in ['$static','$name','$num'] else ''
			print(indent, Node.level, m.word, m.pos, x)
		self.process(fn,False)

	def process(self,fn,bubble=True):
		Node.level += 1
		if not bubble:
			fn(self)  # trickle down (tree after)
		for node in self.tree:
			node.process(fn,bubble) # recursive
		if bubble:
			fn(self)  # bubble up (tree first)
		Node.level -= 1

	def copyBranch(self,frm):
		#self.tree = copy.deepcopy(frm.tree)
		self.tree = frm.tree

def parseExpr(expr):
	tree = []
	wordi = -1
	cmdi = -1
	i = 0
	max = len(expr)
	while i < max:
		t = expr[i:i+1]
		#print( i, t)
		if t == '$':
			cmdi = i
		if t == '(':
			cmd = expr[cmdi:i]
			subtree,ndx = parseExpr(expr[i+1:])
			st = []
			if cmd not in ['$num','$static']:
				st = subtree
			node = Node(cmd,expr=expr[i+1:i+1+ndx],tree=st)
			tree.append(node)
			i += ndx+1
			wordi = -1
		elif t == ')':
			if wordi >= 0:
				x = expr[wordi:i]
				nm = '$static'
				if x[0:1] == '@':
					nm = '$name'
				tree.append(Node(nm,expr=x))
			return tree,i
		elif t == ' ':
			if wordi >= 0:
				x = expr[wordi:i]
				nm = '$static'
				if x[0:1] == '@':
					nm = '$name'
				tree.append(Node(nm,expr=x))
				#tree.append(Node('$static',expr=expr[wordi:i]))
			wordi = -1
		else:
			if wordi < 0:
				wordi = i
		i += 1
	return tree,i

#test1h = 'hoo bloody {[xyc 123 45]} [bafs [x1 s2 x3] $num(1,5,1) fjlk] {@quest} {not} [sa dfj] hah'
#test1 = '$expr(hoo bloody $opt($list(xyc 123 45)) $list(bafs $list(x1 s2 x3) $static(at the farm) $num(1,5,1) fjlk) $opt(@quest) $opt(not) $list(sa dfj) hah)'
#
#tree,ndx = parseExpr(test1)
#print(ndx, len(test1))
#for o in tree:
#	o.print()

def parseGrammar(textfilename):
	# scan the input text file, and build a dictionary of objects, one line => one object
	sc = {}
	fh = open(textfilename,'r')
	textlines = fh.readlines()
	fh.close()
	for line in textlines:
		# skip comments and empty lines
		w = line.strip()
		if w[0:1] == '#':
			continue
		if len(w) == 0:
			continue

		# break line into name, pos, expr 
		m = re.match(r'(.*) (@.*) > (.*)',w);
		if m:
			name = m.group(2)
			pos = m.group(1)
			expr = m.group(3)
		else:
			print('no match')
		
		# replace [] with $list()
		expr = re.sub(r'\[', '$list(', expr);
		expr = re.sub(r'\]', ')', expr);
	
		# replace {} with $opt()
		expr = re.sub(r'\{', '$opt(', expr);
		expr = re.sub(r'\}', ')', expr);
	
		expr = f'$expr({expr})'
		#print(name,pos,expr)

		tree,ndx = parseExpr(expr)
		tree = tree[0].tree
		sc[name] = Node(name,tree,expr,pos,w)
	return sc	

def resolveNames(sc):
	def fn(m): # callback function passed to process()
		if m.word == '$name':
			name = m.expr	
			trunk = sc[name]  # level 1 named node
			#print('>>>>>',name,trunk.word,trunk.expr)
			#m.tree = r.tree
			m.copyBranch(trunk)
	for node in sc.values():
		node.process(fn)

def collapseNames(sc):
	def fn(m):
		for i in range(0,len(m.tree)):
			node = m.tree[i]
			if node.word == '$name':
				m.tree[i:i+1] = node.tree
	for node in sc.values():
		node.process(fn)
	
def collapseNestedLists(sc):
	def fn(m):
		for i in range(0,len(m.tree)):
			node = m.tree[i]
			if m.word == '$list' and node.word == '$list':
				m.tree[i:i+1] = node.tree
	for node in sc.values():
		node.process(fn)

def status(prnt=False):
	maxdepth = 0
	for node in semantics.values():
		if prnt:
			node.print()
		if node.level > maxdepth:
			maxdepth = node.level	
	if prnt:
		print(len(semantics))
		print(maxdepth)

semantics = None

def setupSemantics():
	''' semantics is a dictionary of named nodes, each node is a tree '''
	global semantics
	semantics = parseGrammar(thispath + scfilename)
	resolveNames(semantics)
	collapseNames(semantics)
	collapseNestedLists(semantics)

def gensen(sc,opt=[]):
	options = {
		'count': 1,
		'pattern': [],
		'target': [],
		'targetOnly': False,
		'masteredOnly': False,
		'shuffle': True,
		'rebuild': False,
	}
	if opt:
		for key in opt:
			options[key] = opt[key]

	# generate sentences from each semantic (name,pos,pat,funcs)
	sentens = []
	for node in sc.values():
		if len(options['pattern']) > 0 and name not in options['pattern']:
			continue 
		if node.pos != 'sentence':
			continue
		sen = ''
		def fn(m):
			nonlocal sen
			if m.word == '$static':
				m.value = m.expr
			elif m.word == '$num':
				a = m.expr.split(',')
				n = numgen.gen(int(a[0]), int(a[1]), int(a[2]))
				m.value = numgen.translate(n)
			elif m.word == '$list':
				tlist = list(filter(lambda x: x.expr in options['target'], m.tree))
				if not len(tlist):
					tlist = list(filter(lambda x: x.expr in uservocab.list, m.tree))
					#tlist = m.tree
				tlist = m.tree
				nd = random.choice(tlist)
				m.value = nd.expr 
			elif m.word == '$opt':
				m.value = random.choice(['', m.tree[0].value])
			if Node.level == 2:
				sen += ' ' + m.value
		node.process(fn)
		a = sen.split()
		#tlist = list(filter(lambda x: x in options['target'], a))
		#jvlist = [] # list(filter(lambda x: x.expr in uservocab.list, m.tree))
		#if (len(tlist) or not options['target']) and len(vlist) + len(tlist) >= len(a):
		sen = ' '.join(a)  # remove extra spaces
		sentens.append(sen)

	return sentens

def printSentences(sentences):
	for sen in sentences:
		print(sen)

#sentences = gensen(semantics,{'target':'คะ'})
#sentences = gensen(semantics,{'target':'ตัวใหญ่'})
#sentences = gensen(semantics,{'target':'สวย'})
#sentences = gensen(semantics, {'count':100})
#rintSentences(sentences)

def sengen(s):
	sentences = gensen(semantics, {'target':s})
	return random.choice(sentences)

#def main():
#	s = sengen('คะ')
#	print(s)
#
#if __name__ == 'main':
#	main()
