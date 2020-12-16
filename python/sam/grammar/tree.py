''' tree.py - implement hierarchical tree '''

class Tree:
	''' base class '''
	def __init__(self,parent=None):
		'''
		The first instance must have parent=None. It is the "root" or "maximal" node.
		All other instances must specify a parent. 
		'''
		self.parent = parent 
		self.level = 0
		self.children = []
		if parent:
			self.level = parent.level + 1
			parent.children.append(self)

	def process(self,fn,bubble=True):
		''' Call a callback fn(m) for every node, in either bubble up or trickle down order. '''
		if not bubble:
			fn(self)  # trickle down (self first, then children )
		for child in self.children:
			child.process(fn,bubble) # recursive
		if bubble:
			fn(self)  # bubble up (self after children)

	def isLeaf(self):
		''' Nodes with no children are called "leaf" or "terminal" or "minimal" nodes. '''
		return len(self.children) <= 0

''' example '''
if __name__ == '__main__':
	class Hoo(Tree):
		def __init__(self, name, parent=None):
			self.name = name
			super().__init__(parent)
		
	animal = Hoo('animal')
	dog = Hoo('dog', animal)
	Hoo('schnauser', dog)
	Hoo('collie', dog)
	Hoo('corgi', dog)
	cat = Hoo('cat', animal)
	Hoo('persian', cat)
	Hoo('siamese', cat)

	def fn(m):
		indent = '\t' * m.level
		terminal = '|' if m.isLeaf() else '...'
		print(f'{indent} {m.name} {terminal}')
		
	animal.process(fn,False)
