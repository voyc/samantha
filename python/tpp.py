# tpp.py

import re
import copy

scfilename = 'semanticconventions.txt'

class Node:
	level = 0

	def __init__(self,word,lvl=0,tree=[],expr='',pos='',line=''):
		self.word = word # $expr, $static, $list, $opt, $name, $num or @name
		self.lvl = lvl	
		self.expr = expr  # used when word is $static, $name, $num
		self.tree = tree
		self.pos = pos   # at this time, used only in the root node
		self.line = line  # used only on the root, and only for testing

	def print(self):
		Node.level += 1
		if (self.lvl == 0):
			print(self.line)
		indent = '\t' * self.lvl
		x = self.expr if self.word in ['$static','$name','$num'] else ''
		print(indent, Node.level, self.lvl, self.word, x)
		for o in self.tree:
			o.print()  # recursive
		Node.level -= 1

	def process(self,fn):
		for node in self.tree:
			node.process(fn) # recursive
		fn(self)


	def copyBranch(self,frm):
		self.tree = copy.deepcopy(frm.tree)
		def fn(m):
			m.lvl += self.lvl
		for node in self.tree:
			node.process(fn)

	def replaceNode(self,frm):
		newlvl = self.lvl - 1
		print(self.word, frm.word)
		self.word = frm.word
		self.expr = frm.expr
		self.tree = copy.deepcopy(frm.tree)
		#def fn(m):
		#	m.lvl += newlvl
		#for node in self.tree:
		#	node.process(fn)

def parseExpr(expr,lvl=0):
	tree = []
	wordi = -1
	cmdi = -1
	i = 0
	max = len(expr)
	while i < max:
		t = expr[i:i+1]
		#print(lvl, i, t)
		if t == '$':
			cmdi = i
		if t == '(':
			cmd = expr[cmdi:i]
			subtree,ndx = parseExpr(expr[i+1:],lvl+1)
			st = []
			if cmd not in ['$num','$static']:
				st = subtree
			node = Node(cmd,expr=expr[i+1:i+1+ndx],lvl=lvl,tree=st)
			tree.append(node)
			i += ndx+1
			wordi = -1
		elif t == ')':
			if wordi >= 0:
				x = expr[wordi:i]
				nm = '$static'
				if x[0:1] == '@':
					nm = '$name'
				tree.append(Node(nm,expr=x,lvl=lvl))
			return tree,i
		elif t == ' ':
			if wordi >= 0:
				x = expr[wordi:i]
				nm = '$static'
				if x[0:1] == '@':
					nm = '$name'
				tree.append(Node(nm,expr=x,lvl=lvl))
				#tree.append(Node('$static',expr=expr[wordi:i],lvl=lvl))
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

def parseGrammar():
	# scan the semantics text file, and build a dictionary of objects, one line => one object
	sc = {}
	textlines = open(scfilename,'r').readlines()
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
	
		# replace {} with $optional()
		expr = re.sub(r'\{', '$optional(', expr);
		expr = re.sub(r'\}', ')', expr);
	
		expr = f'$expr({expr})'
		#print(name,pos,expr)

		tree,ndx = parseExpr(expr)
		tree = tree[0].tree
		sc[name] = Node(name,0,tree,expr,pos,w)
	return sc	

def resolveNames(sc):
	def fn(m): # callback function passed to process()
		if m.word == '$name':
			name = m.expr	
			trunk = sc[name]  # lvl 0 named node
			print('>>>>>',name,trunk.word,trunk.expr)
			#m.tree = r.tree
			m.copyBranch(trunk)
	for node in semantics.values():
		node.process(fn)

def collapseNestedLists(sc):
	pass

def collapseNames(sc):
	def fn(m):
		for i in range(0,len(m.tree)):
			node = m.tree[i]
			if node.word == '$name':
				m.tree[i:i+1] = node.tree

	for node in sc.values():
		node.process(fn)
	
def printSemantics():
	for node in semantics.values():
		node.print()
		#print(node.lvl,node.word,node.pos,node.expr)
		#for m in node.tree:
		#	m.print()

# semantics is a dictionary of named nodes
semantics = parseGrammar()
printSemantics()
resolveNames(semantics)
collapseNames(semantics)
printSemantics()


