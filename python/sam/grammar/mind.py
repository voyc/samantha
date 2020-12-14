''' mind.py '''

import uuid
import tree
import datetime

class Mind:
	def __init__(self):
		self.klases = {}  # string-keyed Klas objects
		self.relations = {} # uuid-keyed Relation objects
		self.klastree = tree.Tree('maximal')
		self.objeks = {}

	def __str__(self):
		s = 'Klass Tree\n'
		s += str(self.klastree)

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

class Thot:
	mind = Mind()

	def __init__(self):
		self.modifiers = {}

	def modify(self,link,modifier):
		link = self.entityFromString(link)
		modifier = self.entityFromString(modifier)
		self.modifiers[link] = modifier 
		if isinstance(modifier, Relation):
			modifier.accesscount += 1
		return self

	def entityFromString(self, param):
		if isinstance(param, str):
			param = Thot.mind.klases[param]
		return param 

class Klas(tree.Tree, Thot):
	def __init__(self,name,pname='maximal'):
		tree.Tree.__init__(self,name)
		Thot.__init__(self)
		self.pname = pname
		Thot.mind.klases[name] = self
			
		Thot.mind.klastree.process(self.store)

	def store(self,m):
		if self.pname == m.key:
			m.tree.append(self)	

	def __str__(self):
		key = self.key
		if self.key == 'instance':
			key = f'#{self.pname}'
		s = f'{key}'
		for k,v in self.modifiers.items():
			s += f' {k.__str__()} {v.__str__()}'
		return s

class Objek(Thot):
	def __init__(self,klas):
		Thot.__init__(self,name)
		self.klas = klass
		self.ts = str(datetime.datetime.timestamp(datetime.datetime.now()))
		key = klass + self.ts
		Thot.mind.objeks[key] = self

class DupeKlasException(Exception):
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

		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Thot.mind.relations[self.id] = self
		self.accesscount = self.countAccess()

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

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)
