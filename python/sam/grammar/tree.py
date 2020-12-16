''' tree.py - implement hierarchy tree '''

class Tree:
	level = 0
	s = ''

	def __init__(self,key):
		self.key = key 
		self.tree = []

	#def print(self):
	#	def fn(m):
	#		indent = '\t' * (Tree.level-1)
	#		x = '' if m.isTerminal() else '---'
	#		print(indent, Tree.level, m.key, x)
	#	self.process(fn,False)

	#def __str__(self):
	#	def fn(m):
	#		indent = '\t' * (Tree.level-1)
	#		x = '' if m.isTerminal() else '---'
	#		Tree.s += f'{indent} {str(Tree.level)} {m.key} {x} \n'
	#	self.process(fn,False)
	#	return Tree.s
		

	def process(self,fn,bubble=True):
		Tree.level += 1
		if not bubble:
			fn(self, Tree.level)  # trickle down (self first, then tree )
		for tree in self.tree:
			tree.process(fn,bubble) # recursive
		if bubble:
			fn(self, Tree.level)  # bubble up (self after tree)
		Tree.level -= 1

	def copyBranch(self,frm):
		#self.tree = copy.deepcopy(frm.tree)
		self.tree = frm.tree

	def isTerminal(self):
		return len(self.tree) <= 0
