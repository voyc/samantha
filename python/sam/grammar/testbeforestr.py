''' test.py '''
import pdb
import uuid

class Thot:
	def __init__(self):
		self.id = uuid.uuid4()
		self.attrs = {}

class Entity(Thot):
	def __init__(self,word):
		super().__init__()
		self.word = word

	def toString(self):
		s = f'{self.word}'
		for key,value in self.attrs.items():
			s += f' {key.toString()} {value.toString()}'
		return s

class Link(Thot):
	def __init__(self,word):
		super().__init__()
		self.word = word

	def toString(self):
		return self.word

class Relation(Thot):
	def __init__(self, a, link, b):
		super().__init__()
		self.a = a
		self.link = link
		self.b = b

	def toString(self):
		s = f'{self.a.toString()} {self.link.toString()} {self.b.toString()}'
		for key,value in self.attrs.items():
			if isinstance(value,Relation):
				s += f' {key.toString()}'
			s += f' {value.toString()}'
		return s

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def toString(self):
		return str(self.value)

class Mind:
	def __init__(self):
		self.entities = {}
		self.relations = {}


mind = Mind()
empty = Entity('')
john = Entity('John')
sam = Entity('Sam')
nid = Entity('Nid')
chiangmai = Entity('Chiang Mai')
bangkok = Entity('Bangkok')

go_to = Link('go_to')  # link or entity, entity: noun, verb, etc
pay = Link('pay')
ifthen = Link('ifthen')  # ifthen: relation or attr of relation

johngo = Relation(john, go_to, bangkok)
nidgo = Relation(nid, go_to, chiangmai)

johnpay = Relation(john, pay, empty)
paygo = Relation(johnpay, ifthen, nidgo)

host = sam
guest = john

moon = Entity('moon')
rise = Entity('rise')
moonrise = Relation(moon, rise, empty)
samgo = Relation(host, go_to, bangkok)
ifthen = Entity('if')
when = Entity('when')
how = Entity('how')
quickly = Entity('quickly')
samgo.attrs[how] = quickly 
samgo.attrs[ifthen] = johngo 
samgo.attrs[when] = moonrise

import datetime
nidgo.attrs[when] = datetime.datetime.now()

print(nidgo.toString())
print(paygo.toString())
print(samgo.toString())

age = Entity('age')
john.attrs[age] =  Number(43)
gender = Entity('gender')
man = Entity('man')
john.attrs[gender] = man
knows = Entity('knows')
english = Entity('English')
john.attrs[knows] = english
learning = Entity('learning')
thai = Entity('Thai')
john.attrs[learning] = thai
print(john.toString())

print('done')
