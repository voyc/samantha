# tpp.py

class Node:
	def __init__(self,word,lvl=0,tree=[],expr=''):
		self.word = word # $sen, $static, $list, $opt, $name, $num
		self.lvl = lvl	
		self.expr = expr
		self.tree = tree

	def print(self):
		s = ''
		for i in range(0,self.lvl):
			s += '\t'
		x = ''
		if self.word in ['$static','$name','$num']:
			x = self.expr
		print(s, self.lvl, self.word, x)
		for o in self.tree:
			o.print()

def parse(expr,lvl=0):
	tree = []
	wordi = -1
	cmdi = -1
	i = 0
	max = len(expr)
	while i < max:
		t = expr[i:i+1]
		print(lvl, i, t)
		if t == '$':
			cmdi = i
		if t == '(':
			cmd = expr[cmdi:i]
			subtree,ndx = parse(expr[i+1:],lvl+1)
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
				print(x)
				nm = '$static'
				if x[0:1] == '@':
					nm = '$name'
				tree.append(Node(nm,expr=x,lvl=lvl))
			return tree,i
		elif t == ' ':
			if wordi >= 0:
				tree.append(Node('$static',expr=expr[wordi:i],lvl=lvl))
			wordi = -1
		else:
			if wordi < 0:
				wordi = i
		i += 1
	return tree,i

test1h = 'hoo bloody {[xyc 123 45]} [bafs [x1 s2 x3] $num(1,5,1) fjlk] {@quest} {not} [sa dfj] hah'
test1 = '$sen(hoo bloody $opt($list(xyc 123 45)) $list(bafs $list(x1 s2 x3) $static(at the farm) $num(1,5,1) fjlk) $opt(@quest) $opt(not) $list(sa dfj) hah)'

tree,ndx = parse(test1)
print(ndx, len(test1))
for o in tree:
	o.print()

