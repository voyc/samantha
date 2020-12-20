''' tree.py - implement hierarchical tree '''

class Tree:
	''' base class '''
	def __init__(self,parent=None):
		'''
		The first instance must have parent=None. It is the "root" or "maximal" branch.
		All other instances must specify a parent. 
		'''
		self.parent = parent 
		self.level = 0
		self.child = []
		if parent:
			self.level = parent.level + 1
			parent.child.append(self)

	def process(self,fn,bubble=True):
		''' Call a callback fn(m) for every branch, in either bubble up or trickle down order. '''
		if not bubble:
			fn(self)  # trickle down (self first, then children )
		for child in self.child:
			child.process(fn,bubble) # recursive
		if bubble:
			fn(self)  # bubble up (self after children)

	def isLeaf(self):
		''' A branch with no children is called a "leaf" or "terminal" or "minimal" branch. '''
		return len(self.child) <= 0

	def hasparent(self,parentname):
		unode = self
		while unode.level > 0:
			if unode.word == parentname:
				return True
			unode = unode.parent
		return False
		
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
