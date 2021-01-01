class NotNewException(Exception):
	pass

class Mind:
	def __init__(self):
		self.thots = {}

	def getThot(self,name):
		thot = None
		if name in self.thots.keys():
			thot = self.thots[name]
		return thot
	
	def newThot(self,name='',kind=''):
		thot = Thot(name,kind)
		self.setThot(thot)
		return thot

	def setThot(self,thot):
		name = thot.name
		if name in self.thots.keys():
			raise NotNewException
		else:
			self.thots[name] = thot

	def find(self,search):
		thotnames = []
		for thot in self.thots.values():
			if 'kind' in thot.adjs.keys() and thot.adjs['kind'] == search:
				thotnames.append(thot.name)
		return thotnames

	def addTendrils(self):
		for thot in self.thots.values():
			thot.lookupPossibleThreads()		

	def gen(self):
		self.addTendrils()
		# look at the disconnected tendrils of each thought
		# give each thought a priority
		# questions
		# statements: observations worth of comment, stories worth telling
		# pick the thought with 
		# previous question, current thot, has a certain priority, just because 
		# it takes a high threshold for one thot to interrupt another

	def print(self,thot):
		print(thot.compose())

class Thot:
	def __init__(self,name='',kind=''):
		self.name = name
		if not self.name:
			self.name = str(uuid.uuid4())
		self.adjs = {}
		if kind:
			self.adjs['kind'] = kind 

	def getAdj(self,key):
		adj = None
		if key in self.adjs.keys():
			return self.adjs[key]

	def setAdj(self,key,value):
		if key in self.adjs.keys():
			raise NotNewException
		else:
			self.adjs[key] = value

	def compose(self):
		s = self.name
		for key,value in self.adjs.items():
			s += ' ' + str(value)
		return s

	def lookupPossibleThreads(self):
		pass

class Entity(Thot):
	def __init__(self,name,kind=''):
		super().__init__(name,kind='')

	def compose(self):
		s = self.name
		for key,value in self.adjs.items():
			s += ' ' + str(value)
		return s

class Relation(Thot):
	def __init__(self, subj='', relate='', obj=''):
		super().__init__(relate,kind='relation')
		self.subj = subj
		self.relate = relate 
		self.obj = obj	

	def compose(self):
		s = self.subj.compose()
		s += self.relate.compose()
		s += self.obj.compose()
		return s


class Dialectic(Thot):
	def __init__(self, thesis, antithesis, synthesis):
		self.thesis = thesis
		self.antithesis = antithesis
		self.synthesis = synthesis


class Syllogism:
	''' a conditional Relation: ifthen, therefore, when, before, after '''
	def __init__(self, a, link, b):
		self.a    = a
		self.link = link
		self.b    = b

def main():
	mind = Mind()
	mind.newThot('category')
	mind.newThot('noun_category', 'category')
	mind.newThot('person', 'noun_cateory')
	mind.newThot('sam', 'person')
	mind.newThot('father', 'person')
	mind.newThot('bank', 'businesstype')
	mind.newThot('Bangkok', 'city')
	mind.newThot('go','movement')

	#e1 = Event(john, go, bank)
	#e2 = Event(father, go, bangkok)

	mind.newThot('Kasikorn', 'bank')

	mind.newThot('corner', 'location')

	naiyana = mind.newThot('Naiyana','person')
	naiyana.setAdj('poss', 'pn')
	naiyana.setAdj('age', 41)
	naiyana.setAdj('gender', 'f')

	mind.newThot('city', 'place')

	udonthani = mind.newThot('Udon Thani', 'city')
	udonthani.setAdj('poss', 'pn')
	udonthani.setAdj('type', 'city')
	udonthani.setAdj('pop', 130000)


	chiangmai = Thot('Chiang Mai', 'city')
	chiangmai.setAdj('pos', 'pn')
	chiangmai.setAdj('type', 'city')
	chiangmai.setAdj('metropop', 1000000)

	john = mind.newThot('john', 'person')
	#john.setAdj('reside', chiangmai)

	reside = mind.newThot('reside', 'verb')
	apartment_building = mind.newThot('apartment_building', 'buildingtype')
	go_to = mind.newThot('go_to', 'action')

	johnreside = Relation(john, reside, apartment_building)
	mind.thots[johnreside.name] = johnreside
	johnreside.setAdj('when', 2020)


	naigo = Relation(naiyana, go_to, chiangmai) 
	mind.thots[naigo.name] = naigo 
	week = Entity('week')
	week.setAdj('what', 'next')
	naigo.setAdj('when', week)
	visitjohn = Relation('Naiyana', 'visit', 'John')
	naigo.setAdj('why', visitjohn)

	print(isinstance(naigo,Thot))
	print(isinstance(naigo,Relation))

	names = mind.find('person')
	for name in names:
		thot = mind.thots[name]
		print(thot.name)
	mind.gen()

	mind.print(naigo)

	for thot in mind.thots.values():
		cls = ''
		if isinstance(thot, Entity):
			cls += 'e'
		if isinstance(thot, Relation):
			cls += 'r'
		print(f'{thot.name} : {thot.__class__} : {cls}')

	print('done')

if __name__ == '__main__':
	main()
	
