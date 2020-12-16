''' mind.py '''

import uuid
import tree
import datetime

class Mind:
	''' 
	singleton class defines a mind 
	contains thots which are klases and relations
	'''
	
	def __init__(self):
		self.klases = {}  # string-keyed Klas objects
		self.relations = {} # uuid-keyed Relation objects
		self.klastree = None
		self.objeks = {}
		self.patterns = {}

	def setup(self):
		self.klastree = Klas('root')
		Thot.mind = self

	def __str__(self):
		s = 'Klass Tree\n'
		#s += str(self.klastree)
		s += self.printKlasTree()

		s += '\nTop Relations\n'
		for key,value in self.relations.items():
			if value.accesscount <= 0:
				s += f'{str(value)} : {str(value.accesscount)}\n'

		s += '\nSub Relations\n'
		for key,value in self.relations.items():
			if value.accesscount >= 1:
				s += f'{str(value)} : {str(value.accesscount)}\n'

		s += '\nObjeks\n'
		for key,value in self.objeks.items():
			if value.level > 1:
				continue
			s += f'{str(value)}\n'
		return s

	def printKlasTree(self):
		s = ''
		def fn(m):
			nonlocal s
			indent = '\t' * (m.level)
			x = '' if m.isLeaf() else '---'
			s += f'{indent} {str(m.level)} {m} {m.accesscount} {x} \n'
		self.klastree.process(fn, False)
		return s

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
			subjek = self.findBranchKlas(rel.a)
			if subjek not in self.patterns:
				self.patterns[subjek] = {}
			if rel.link not in self.patterns[subjek]:
				self.patterns[subjek][rel.link] = {}
			for mk,mv in rel.modifiers.items():
				if mk not in self.patterns[subjek][rel.link]:
					self.patterns[subjek][rel.link][mk] = {}
				if mv not in self.patterns[subjek][rel.link][mk]:
					self.patterns[subjek][rel.link][mk][mv] = 'x'

	def findBranchKlas(self,klas):
		uklas = klas
		while uklas.level > 1:
			uklas = uklas.parent
		return uklas
	
	def displayGrammar(self):
		for subj in self.patterns.keys():
			print(f'{subj.key}')
			for link in self.patterns[subj].keys():
				print(f'{subj.key} {link.key}')
				for lnk in self.patterns[subj][link].keys():
					print(f'{subj.key} {link.key} {lnk.key}')
					for mod in self.patterns[subj][link][lnk].keys():
						print(f'{subj.key} {link.key} {lnk.key} {mod}')


class Thot:
	mind = Mind()

	def __init__(self):
		self.modifiers = {}
		self.accesscount = 0

	def modify(self,link,modifier):
		link = Thot.efs(link)
		modifier = Thot.efs(modifier)
		self.modifiers[link] = modifier 
		link.accesscount += 1
		modifier.accesscount += 1
		return self

	@staticmethod
	def efs(param): # entity from string
		if isinstance(param, str):
			param = Thot.mind.klases[param]
			if not param:
				raise KlasNotFoundKlasException
		return param 

class Klas(tree.Tree, Thot):
	def __init__(self,name,parent=None):
		self.key = name
		parent = Thot.efs(parent)
		if not parent:
			parent = Thot.mind.klastree
		tree.Tree.__init__(self,parent)
		Thot.__init__(self)
		Thot.mind.klases[name] = self
		#Thot.mind.klastree.process(self.store,False)

	#def store(self,m,level):
	#	if self.parent.key == m.key:
	#		self.level = level+1
	#		m.tree.append(self)	

	def __str__(self):
		key = self.key
		if self.key == 'instance':
			key = f'#{self.parent.key}'
		s = f'{key}'
		for k,v in self.modifiers.items():
			s += f' {k.__str__()} {v.__str__()}'
		return s

	#def __repr__(self):
	#	return f'Klas::{self.key}'

class Objek(Thot):
	def __init__(self,klas):
		Thot.__init__(self,name)
		self.klas = klass
		self.ts = str(datetime.datetime.timestamp(datetime.datetime.now()))
		key = klass + self.ts
		Thot.mind.objeks[key] = self

class DupeKlasException(Exception):
	pass

class KlasFoundException(Exception):
	pass

class Relation(Thot):
	def __init__(self, a, link, b):
		super().__init__()
		self.a = a
		self.link = link
		self.b = b
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())

		if isinstance(self.a, str):
			self.a = Thot.mind.klases[self.a]
		if isinstance(self.link, str):
			self.link = Thot.mind.klases[self.link]
		if isinstance(self.b, str):
			self.b = Thot.mind.klases[self.b]

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
		if self.a.key != 'empty':
			s += f'{str(self.a)} '
		s += f'{str(self.link)}'
		if self.b.key != 'empty':
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
