''' mind.py '''

import uuid
import tree
import datetime

class DupeNodeException(Exception):
	pass

class NodeNotFoundException(Exception):
	pass

class NoParentException(Exception):
	pass

class Thot:
	''' base class, add modifiers and accesscount  '''
	mind = None

	def __init__(self):
		self.modifiers = {}
		self.accesscount = 0

	def modify(self,link,modifier):
		link = Thot.nfs(link)
		if isinstance(modifier,str):
			modifier = Objek(Thot.nfs(modifier))
		self.modifiers[link] = modifier 
		link.accesscount += 1
		modifier.accesscount += 1
		return self

	def isTop(self):
		return self.accesscount <= 0

	@staticmethod
	def nfs(param): # node from string
		if isinstance(param, str):
			param = Thot.mind.nodes[param]
			if not param:
				raise NodeNotFoundException
		return param 

class Node(tree.Tree, Thot):
	''' a Node is a word (entity, thing, action, idea), class or object, in the mind '''
	def __init__(self,word,parent=None):
		''' word is a string.  parent can be string or object. '''
		self.word = word
		parent = Thot.nfs(parent) # convert string to object 
		if not parent: # first time only, init the tree
			if Thot.mind.nodetree:
				raise NoParentException
			Thot.mind.nodetree = self
		tree.Tree.__init__(self,parent)
		Thot.__init__(self)
		if word in Thot.mind.nodes:
			raise DupeNodeException
		Thot.mind.nodes[word] = self

	def __str__(self):
		return self.word

	def dump(self):
		print(self.word)
		print(self.parent.word)
		print(self.level)
		for k,v in self.modifiers.items():
			print( f' {k.word} {v.word}')

class Objek(Node):
	''' object, an instance of a Node '''
	def __init__(self, parent):
		parent = Thot.nfs(parent) # convert string to object 
		if not parent:
			raise NoParentException
		self.word = parent.word
		Thot.__init__(self)
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())
		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Thot.mind.objeks[self.id] = self

	def __str__(self):
		s = self.word
		for k,v in self.modifiers.items():
			s += f' {str(k)} {str(v)}'
		return s

class Claws(Thot):
	''' clause: subjek, verb, {object} '''
	def __init__(self, subjek, verb, objek=None):
		super().__init__()
		self.subjek = Objek(Thot.nfs(subjek))
		self.verb = Objek(Thot.nfs(verb))
		self.objek = Objek(Thot.nfs(objek)) if objek else None
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())
		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Thot.mind.claws[self.id] = self

	def __str__(self):
		s = f'{self.subjek} {self.verb}' 
		if self.objek:
			s += f' {self.objek}' 
		for k,v in self.modifiers.items():
			s += f' {str(k)} {str(v)}'
		return s

	def nextQuestion(self):
		pass

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)

class Mind:
	''' 
	singleton class
	defines a mind 
	contains thots, which are nodes, objeks, and claws
	contains grammar, patterns
	'''
	
	def __init__(self):
		self.nodes = {}  # string-keyed Node objects
		self.objeks = {}
		self.claws = {} # uuid-keyed Clause objects
		self.nodetree = None
		self.patterns = {}
		Thot.mind = self

	def buildGrammar(self):
		for claw in self.claws.values():
			subjek = claw.subjek #self.findBranchNode(Thot.nfs(claw.subjek.word))
			if subjek not in self.patterns:
				self.patterns[subjek] = {}

			link = claw.verb # claw.link.parent #self.findBranchNode(claw.link)
			if link not in self.patterns[subjek]:
				self.patterns[subjek][link] = {}

			objek = claw.objek
			what = Thot.nfs('what')
			if what not in self.patterns[subjek][link]:
				self.patterns[subjek][link][what] = {}
			if objek not in self.patterns[subjek][link][what]:
				self.patterns[subjek][link][what][objek] = {}

			for mk,mv in claw.modifiers.items():
				if mk not in self.patterns[subjek][link]:
					self.patterns[subjek][link][mk] = {}
				if mv not in self.patterns[subjek][link][mk]:
					self.patterns[subjek][link][mk][mv] = 'x'

	def findBranchNode(self,node):
		unode = node
		while unode.level > 1:
			unode = unode.parent
		return unode
	
	def dump(self,detail=False):
		print(f'Nodes {len(self.nodes)}, Objeks {len(self.objeks)}, Claws {len(self.claws)}, Patterns {len(self.patterns)}\n')
		if detail:
			self.printNodeTree()
			self.printClaws()
			self.printGrammar()

	def printNodeTree(self):
		print('Nodes Tree')
		def fn(m):
			indent = '\t' * (m.level)
			x = '' if m.isLeaf() else '---'
			print( f'{indent} {str(m.level)} {m} {m.accesscount} {x}')
		self.nodetree.process(fn, False)
		return

	def printClaws(self):
		print('\nTop Claws')
		for v in self.claws.values():
			if v.isTop():
				print( f'{str(v)} : {str(v.accesscount)}')

		print('\nSub Claws')
		for v in self.claws.values():
			if not v.isTop():
				print( f'{str(v)} : {str(v.accesscount)}')

	def printGrammar(self):
		print('\nGrammar Patterns')
		for subj in self.patterns.keys():
			print(f'{subj.word}')
			for link in self.patterns[subj].keys():
				print(f'{subj.word} {link.word}')
				for lnk in self.patterns[subj][link].keys():
					print(f'{subj.word} {link.word} {lnk.word}')
					for mod in self.patterns[subj][link][lnk].keys():
						print(f'{subj.word} {link.word} {lnk.word} {mod}')


