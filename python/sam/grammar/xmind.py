''' mind.py '''

import uuid

class Mind:
	def __init__(self):
		self.entities = {}  # string-keyed Entity objects
		self.relations = {} # uuid-keyed Relation objects

	def __repr__(self):
		s = ''
		for key,value in self.entities.items():
			s += f'{repr(key)} : {repr(value)}\n'
		for key,value in self.relations.items():
			s += f'{repr(key)} : {repr(value)}\n'
		return s

	def __str__(self):
		s = ''
		for key,value in self.entities.items():
			s += f'{str(value)}\n'
		for key,value in self.relations.items():
			s += f'{str(value)}\n'
		return s

class Thot:
	mind = Mind()

	def __init__(self):
		self.id = uuid.uuid4()
		self.modifiers = {}

	def modify(self,link,modifier):
		link = self.entityFromString(link)
		modifier = self.entityFromString(modifier)
		self.modifiers[link] = modifier 
		return self

	def entityFromString(self, param):
		if isinstance(param, str):
			param = Thot.mind.entities[param]
		return param 

class DupeEntityException(Exception):
	pass

#class MissingEntityException(Exception):
#	pass

class Entity(Thot):
	def __init__(self,word,typeof=None):
		super().__init__()
		self.word = word
		if word == 'instance':
			key = self.id
		else:
			key = self.word
			try:
				x = Thot.mind.entities[word]
			except:
				pass
			else:
				raise DupeEntityException(word)
		Thot.mind.entities[key] = self
		if typeof:
			tp = typeof
			if isinstance(typeof, str):
				tp = Thot.mind.entities[typeof]
			link = Thot.mind.entities['typeof']
			self.modifiers[link] = typeof

	def __repr__(self):
		s = f'{self.word}'
		for key,value in self.modifiers.items():
			s += f' {key.__str__()} {value.__str__()}'
		return s

	def __str__(self):
		s = f'{self.word}'
		#for key,value in self.modifiers.items():
		#	s += f' {key.__str__()} {value.__str__()}'
		return s

class Relation(Thot):
	def __init__(self, a, link, b):
		super().__init__()
		self.a = a
		self.link = link
		self.b = b

		if isinstance(self.a, str):
			self.a = Thot.mind.entities[self.a]
			#try:
			#	self.a = Thot.mind.entities[self.a]
			#except:
			#	raise MissingEntityExecption(self.a)
		if isinstance(self.link, str):
			self.link = Thot.mind.entities[self.link]
			#try:
			#	self.link = Thot.mind.entities[self.link]
			#except:
			#	raise MissingEntityExecption(self.link)
		if isinstance(self.b, str):
			self.b = Thot.mind.entities[self.b]
			#try:
			#	self.b = Thot.mind.entities[self.b]
			#except:
			#	raise MissingEntityExecption(self.b)

		Thot.mind.relations[self.id] = self

	def __repr__(self):
		s = ''
		if self.a.word != 'empty':
			s += f'{self.a.__repr__()} '
		s += f'{self.link.__repr__()}'
		if self.b.word != 'empty':
			s += f' {self.b.__repr__()}'
		for key,value in self.modifiers.items():
			s += f' {key.__repr__()}'
			s += f' {value.__repr__()}'
		return s

	def __str__(self):
		s = ''
		if self.a.word != 'empty':
			s += f'{self.a.__str__()} '
		s += f'{self.link.__str__()}'
		if self.b.word != 'empty':
			s += f' {self.b.__str__()}'
		for key,value in self.modifiers.items():
			#if isinstance(value,Relation):
			#s += f' {key.__str__()}'
			s += f' {value.__str__()}'
		return s

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)

def main():
	mind = Mind()
	Thot.mind = mind
	Entity('empty')
	repr(mind)

if __name__ == '__main__':
	main()

