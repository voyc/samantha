''' test.py '''
import pdb
import uuid
import datetime

class Thot:
	def __init__(self):
		self.id = uuid.uuid4()
		self.attrs = {}

class Entity(Thot):
	def __init__(self,word):
		super().__init__()
		self.word = word

	def __str__(self):
		s = f'{self.word}'
		#for key,value in self.attrs.items():
		#	s += f' {key.__str__()} {value.__str__()}'
		return s

	def __repr__(self):
		s = f'{self.word}'
		for key,value in self.attrs.items():
			s += f' {key.__str__()} {value.__str__()}'
		return s

class Relation(Thot):
	def __init__(self, a, link, b):
		super().__init__()
		self.a = a
		self.link = link
		self.b = b

	def __str__(self):
		s = f'{self.a.__str__()} {self.link.__str__()} {self.b.__str__()}'
		for key,value in self.attrs.items():
			if isinstance(value,Relation):
				s += f' {key.__str__()}'
			s += f' {value.__str__()}'
		return s

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)

class Mind:
	def __init__(self):
		self.entities = {}
		self.relations = {}

mind = Mind()
empty = Entity('')  # None

age = Entity('age')  # attributes of a person
gender = Entity('gender')
man = Entity('man')
english = Entity('English')  # language, nationality
thai = Entity('Thai')

sam = Entity('Sam')  # persons
nid = Entity('Nid')
john = Entity('John')
host = sam
guest = john

chiangmai = Entity('Chiang Mai')  # places
bangkok = Entity('Bangkok')

moon = Entity('moon')  # things

go_to = Entity('go_to')  # actions
pay = Entity('pay')
know = Entity('know')
learn = Entity('learn')
rise = Entity('rise')

ifthen = Entity('if')  # conditional
when = Entity('when')
how = Entity('how')

quickly = Entity('quickly')  # adverb

john.attrs[age] =  Number(43)  # describe a person
john.attrs[gender] = man
john.attrs[know] = english
john.attrs[learn] = thai

johngo = Relation(john, go_to, bangkok)
nidgo = Relation(nid, go_to, chiangmai)
johnpay = Relation(john, pay, empty)
nidgo.attrs[ifthen] = johnpay
moonrise = Relation(moon, rise, empty)

samgo = Relation(host, go_to, bangkok)

samgo.attrs[how] = quickly   # describe an action
samgo.attrs[ifthen] = johngo 
samgo.attrs[when] = moonrise

nidgo.attrs[when] = datetime.datetime.now()

print(repr(john))
print(str(nidgo))
print(str(samgo))

print('done')
