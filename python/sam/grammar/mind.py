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
	''' base class for Node and Relation '''
	mind = None

	def __init__(self):
		self.modifiers = {}
		self.accesscount = 0

	def modify(self,link,modifier):
		link = Thot.nfs(link)
		modifier = Thot.nfs(modifier)
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
		if word != 'instance' and word in Thot.mind.nodes:
			raise DupeNodeException
		Thot.mind.nodes[word] = self

	def __str__(self):
		word = self.word
		if self.word == 'instance':
			word = f'#{self.parent.word}'
		s = f'{word}'
		for k,v in self.modifiers.items():
			s += f' {k.__str__()} {v.__str__()}'
		return s

	#def __repr__(self):
	#	return f'Node::{self.word}'

class Relation(Thot):
	''' a Relation (Race, Link) relates Nodes together '''
	def __init__(self, a, link, b):
		super().__init__()
		self.a = a
		self.link = link
		self.b = b
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())

		if isinstance(self.a, str):
			self.a = Thot.mind.nodes[self.a]
		if isinstance(self.link, str):
			self.link = Thot.mind.nodes[self.link]
		if isinstance(self.b, str):
			self.b = Thot.mind.nodes[self.b]

		#self.a.accesscount += 1
		#self.link.accesscount += 1
		#self.b.accesscount += 1

		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Thot.mind.relations[self.id] = self

	def countAccess(self):
		'''
		does this same relation already exist?
		has this sam relation been used before?
		if so, what

		separate to top and sub thots
		find how many times this sub-relation is referenced in thots and modifiers
		not need level: only main or sub, so we can list separately
		'''	
		cnt = 0
		for k,v in Thot.mind.relations.items():
			if self == v: continue
			if self == v.a: cnt += 1
			if self == v.b: cnt += 1
			if self == v.link: cnt += 1
			for w,m in v.modifiers.items():
				if m == v: cnt+= 1
		return cnt

	def composeQA(self):
		'''
		for a pattern
			what are valid questions
			what are valid answers to each question
		verb modifiers
		noun modifiers
		pattern
			typeof subj, typeof link
			@person, @action, [who,why,where]
				answers to who
				answers to why
				answers to where
		find pattern
			parent

		do all upfront, or on demand?
		on demand

		for a thot
			compose questions, as multiple choice (with all answers)
			prioritize
		'''
		pass

	def __str__(self):
		s = ''
		if self.a.word != 'empty':
			s += f'{str(self.a)} '
		s += f'{str(self.link)}'
		if self.b.word != 'empty':
			s += f' {str(self.b)}'
		for key,value in self.modifiers.items():
			s += f' {str(key)} {str(value)}'
		return s

	def nextQuestion(self):
		pass
		#self.a
		#self.link
		#self.b
		#self.modifiers
		#for this set of a, link, b, modifiers
		#	what are the additional modifiers found in use already
		#	at level 1 of each bit

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
	contains thots, which are nodes and relations
	contains grammar, patterns
	'''
	
	def __init__(self):
		self.nodes = {}  # string-keyed Node objects
		self.relations = {} # uuid-keyed Relation objects
		self.nodetree = None
		self.patterns = {}
		Thot.mind = self

	def buildGrammar(self):
		'''
		Ambiguities in language, thought: We are trying to flatten a rounded structure
		# patterns is a four-dimensional array
		patterns = [subjek][verb][link][objek] 
		patterns = {}
		patterns['person'] = {}
		patterns['person']['go'] = {}
		patterns['person']['go']['where'] = {}
		'''

		for rel in self.relations.values():
			subjek = self.findBranchNode(rel.a)
			if subjek not in self.patterns:
				self.patterns[subjek] = {}
			if rel.link not in self.patterns[subjek]:
				self.patterns[subjek][rel.link] = {}
			for mk,mv in rel.modifiers.items():
				if mk not in self.patterns[subjek][rel.link]:
					self.patterns[subjek][rel.link][mk] = {}
				if mv not in self.patterns[subjek][rel.link][mk]:
					self.patterns[subjek][rel.link][mk][mv] = 'x'

	def findBranchNode(self,node):
		unode = node
		while unode.level > 1:
			unode = unode.parent
		return unode
	
	def dump(self):
		self.printNodeTree()
		self.printRelations()
		self.printGrammar()

	def printNodeTree(self):
		print('Nodes Tree')
		def fn(m):
			indent = '\t' * (m.level)
			x = '' if m.isLeaf() else '---'
			print( f'{indent} {str(m.level)} {m} {m.accesscount} {x}')
		self.nodetree.process(fn, False)
		return

	def printRelations(self):
		print('\nTop Relations')
		for v in self.relations.values():
			if v.isTop():
				print( f'{str(v)} : {str(v.accesscount)}')

		print('\nSub Relations')
		for v in self.relations.values():
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


