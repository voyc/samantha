''' mind.py '''

import uuid
import sam.tree
import datetime
import sam.translate
import sam.mind

class Converse:
	def __init__(self):
		self.history = []
		pass

	def setHost(self,host):
		self.host = host
	
	def setGuest(self,guest):
		self.guest = guest
	
	def initiate(self):
		gowhere = Claws(self.guest, 'go').modify('where', 'question')
		return str(gowhere)

	def respond(self,q):
		s = 'I am fine.'
		return s

class DupeNodeException(Exception):
	pass

class NodeNotFoundException(Exception):
	pass

class NoParentException(Exception):
	pass

class Modifier:
	def __init__(self,link,attribute):
		self.lk = link
		self.at = attribute

class Thot:
	''' base class, add modifiers and accesscount  '''
	mind = None

	def __init__(self):
		self.modifiers = []
		self.accesscount = 0

	def modify(self,link,attribute):
		link = Thot.nfs(link)
		if isinstance(attribute,str):
			attribute = Objek(Thot.nfs(attribute))
		self.modifiers.append(Modifier(link, attribute))
		link.accesscount += 1
		attribute.accesscount += 1
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

class Node(sam.tree.Tree, Thot):
	''' a Node is a word (entity, thing, action, idea), class or object, in the mind '''
	def __init__(self,word,parent=None):
		''' word is a string.  parent can be string or object. '''
		self.word = word
		parent = Thot.nfs(parent) # convert string to object 
		if not parent: # first time only, init the tree
			if Thot.mind.nodetree:
				raise NoParentException
			Thot.mind.nodetree = self
		sam.tree.Tree.__init__(self,parent)
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
		for m in self.modifiers:
			print( f' {m.lk.word} {m.at.word}')

class Objek(Node):
	''' object, an instance of a Node '''
	def __init__(self, parent):
		parent = Thot.nfs(parent) # convert string to object 
		if not parent:
			raise NoParentException
		self.word = parent.word
		self.parent = parent
		Thot.__init__(self)
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())
		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Thot.mind.objeks[self.id] = self

	def __str__(self):
		s = self.word
		for m in self.modifiers:
			s += f' {str(m.lk)} {str(m.at)}'
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
		for m in self.modifiers:
			s += f' {str(m.lk)} {str(m.at)}'
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

			verb = claw.verb # claw.verb.parent #self.findBranchNode(claw.verb)
			if verb not in self.patterns[subjek]:
				self.patterns[subjek][verb] = {}

			objek = claw.objek
			what = Thot.nfs('what')
			if what not in self.patterns[subjek][verb]:
				self.patterns[subjek][verb][what] = {}
			if objek not in self.patterns[subjek][verb][what]:
				self.patterns[subjek][verb][what][objek] = {}

			for m in claw.modifiers:
				if m.lk not in self.patterns[subjek][verb]:
					self.patterns[subjek][verb][m.lk] = {}
				if m.at not in self.patterns[subjek][verb][m.lk]:
					self.patterns[subjek][verb][m.lk][m.at] = 'x'

	def findBranchNode(self,node):
		unode = node
		while unode.level > 1:
			unode = unode.parent
		return unode
	
	def dump(self,detail=False):
		print(f'Nodes {len(self.nodes)}, Objeks {len(self.objeks)}, Claws {len(self.claws)}, Patterns {len(self.patterns)}\n')
		if detail:
			#self.printNodeTree()
			self.printTopClaws()
			#self.printSubClaws()
			#self.printGrammar()

	def printNodeTree(self):
		print('Nodes Tree')
		def fn(m):
			indent = '\t' * (m.level)
			x = '' if m.isLeaf() else '---'
			print( f'{indent} {str(m.level)} {m} {m.accesscount} {x}')
		self.nodetree.process(fn, False)
		return

	def printTopClaws(self):
		tlate = translate.Translate()
		print('\nTop Claws')
		for v in self.claws.values():
			if v.isTop():
				print( tlate.getThai(str(v)))

	def printSubClaws(self):
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

	def load(self):
		#sam= Mind()

		Node('root')
		Node('empty', 'root')
		Node('person', 'root')
		Node('place', 'root')
		Node('thing', 'root')
		Node('action', 'root')
		Node('link', 'root')

		Node('typeof', 'link')
		Node('ownedby', 'link')
		Node('by', 'link')


		Node('question', 'link')
		Node('which', 'question') # apply to noun

		Node('where', 'question') # apply to verb
		Node('why', 'question')
		Node('when', 'question')  # default "now"
		Node('how', 'question')
		Node('what', 'question')  # applies only to "do"

		Node('this', 'which')
		Node('next', 'which')
		Node('last', 'which') # previous

		Node('time_period', 'thing')
		Node('week', 'time_period')
		Node('day', 'time_period')
		Node('month', 'time_period')
		Node('year', 'time_period')

		Node('time', 'thing')
		Node('now', 'time')
		Node('yesterday', 'time')
		Node('today', 'time')
		Node('tomorrow', 'time')
		Node('morning', 'time')
		Node('afternoon', 'time')
		Node('evening', 'time')

		Node('you', 'person')
		Node('I', 'person')
		Node('friend', 'person')
		Node('family', 'person')

		Node('Nid', 'person')
		Node('Pin', 'person')
		Node('May', 'person')
		Node('Som', 'person')
		Node('Nui', 'person')
		Node('Memi', 'person')
		Node('Fern', 'person')
		Node('Bella', 'person')
		Node('Jenny', 'person')
		Node('Penny', 'person')
		Node('Milky', 'person')
		Node('Donut', 'person')
		Node('Namtip', 'person')
		Node('Tangmo', 'person')
		Node('Chompoo', 'person')
		Node('Naiyana', 'person')

		Node('Sam', 'person')
		Node('Joe', 'person')
		Node('John', 'person')
		Node('Juan', 'person')

		Node('city', 'place')
		Node('island', 'place')
		Node('businesstype', 'thing')
		Node('bank', 'businesstype')
		Node('coffeeshop', 'businesstype')
		Node('restaurant', 'businesstype')
		Node('salon', 'businesstype')
		Node('market', 'businesstype')
		Node('mall', 'businesstype')
		Node('pharmacy', 'businesstype')
		Node('cinema', 'businesstype')
		Node('doctor', 'businesstype')
		Node('hospital', 'businesstype')
		Node('clinic', 'businesstype')
		Node('dentist', 'businesstype')
		Node('embassy', 'businesstype')
		Node('house', 'place')
		Node('Bangkok', 'city')
		Node('Phuket', 'city')
		Node('Koh_Samui', 'island')
		Node('Krabi', 'city')
		Node('Pattaya', 'city')
		Node('Hua_Hin', 'city')
		Node('Chiang_Mai', 'city')
		Node('Pai', 'city')
		Node('Udon_Thani', 'city')
		Node('Sukothai', 'city')
		Node('Ayutthaya', 'city')

		Node('food', 'thing')
		Node('vacation', 'thing')
		Node('business', 'thing')
		Node('money', 'thing')
		Node('coffee', 'food')
		Node('breakfast', 'food')
		Node('hair', 'thing')
		Node('pedicure', 'thing')
		Node('manicure', 'thing')
		Node('medicine', 'thing')
		Node('movie', 'thing')
		Node('checkup', 'thing')
		Node('headache', 'thing')
		Node('covid', 'thing')
		Node('tooth', 'thing')
		Node('teeth', 'thing')
		Node('filling', 'thing')
		Node('whitening', 'thing')
		Node('toothache', 'thing')
		Node('braces', 'thing')
		Node('fun', 'thing')

		Node('transport', 'thing')
		Node('train', 'transport')
		Node('bus', 'transport')
		Node('airplane', 'transport')
		Node('ship', 'transport')

		Node('car', 'transport')
		Node('Grab', 'transport')
		Node('taxi', 'transport')
		Node('citybus', 'transport')
		Node('songtaew', 'transport')
		Node('tuktuk', 'transport')
		Node('walk', 'action')
		Node('run', 'action')

		Node('do', 'action')
		Node('go', 'action')
		Node('come', 'action')
		Node('eat', 'action')
		Node('visit', 'action')
		Node('pickup', 'action')
		Node('deliver', 'action')
		Node('get', 'action')
		Node('drink', 'action')
		Node('meet', 'action')
		Node('wash', 'action')
		Node('cut', 'action')
		Node('buy', 'action')
		Node('shop', 'action')
		Node('watch', 'action')
		Node('fix', 'action')
		Node('test', 'action')
		Node('see', 'action')
		Node('clean', 'action')
		Node('remove', 'action')

		Node('cook', 'action')
		Node('brew', 'action')
		Node('read', 'action')
		Node('listen', 'action')
		Node('play', 'action')
		Node('is', 'action')
		Node('feel', 'action')
		Node('relax', 'action')
		Node('chat', 'action')
		Node('talk', 'action')
		Node('give', 'action')
		Node('have', 'action')
		Node('study', 'action')
		Node('work', 'action')

		Node('animal', 'root')
		Node('cow', 'animal')

		Node('foodtype', 'root')
		Node('rice', 'foodtype')
		Node('tea', 'foodtype')

		Node('book', 'thing')
		Node('music', 'thing')
		Node('game', 'thing')
		Node('homework', 'thing')
		Node('assignment', 'thing')
		Node('computer', 'thing')
		Node('job', 'thing')
		Node('garden', 'thing')
		Node('weed', 'thing') 
		Node('harvest', 'thing') 
		Node('plant', 'thing') 

		Node('due', 'thing') # state, adj
		Node('many', 'thing') # adv 
		Node('howmuch', 'link') # adv 
		Node('too', 'howmuch') # adv 

		Node('feeling', 'root')
		Node('hungry', 'feeling')

		Node('kitchen', 'place')
		Node('backyard', 'place')
		Node('upstairs', 'place')
		Node('bedroom', 'place')
		Node('livingroom', 'place')
		Node('online', 'place')

		friendhouse = Objek('house').modify('ownedby', 'friend')
		Claws('you', 'go').modify('where', friendhouse).modify('why', Claws('you', 'pickup', 'food'))
		Claws('Sam', 'go').modify('where', friendhouse).modify('why', Claws('Sam', 'deliver', 'food'))
		Claws('John', 'go').modify('where', friendhouse).modify('why', Claws('John', 'eat', 'food'))
		Claws('Naiyana', 'go').modify('where', 'Bangkok').modify('why', Claws('Naiyana', 'visit'))
		Claws('Sam', 'go').modify('where', 'Chiang_Mai').modify('why', 'vacation')
		Claws('John', 'go').modify('where', 'Pai').modify('why', Claws('John', 'go', 'embassy'))
		Claws('Juan', 'go').modify('where', 'bank').modify('why', Claws('Juan', 'get', 'money'))

		Claws('John', 'go').modify('where', 'coffeeshop').modify('why', Claws('John', 'drink', 'coffee'))
		Claws('Sam', 'go').modify('where', 'coffeeshop').modify('why', Claws('Sam', 'eat', 'breakfast'))
		Claws('Juan', 'go').modify('where', 'coffeeshop').modify('why', Claws('Juan', 'meet', 'friend'))

		def work(who, where, whyv, whyo=None):
			Claws(who, 'go').modify('where', where).modify('why', Claws(who, whyv, whyo))
		
		work('John', 'restaurant', 'eat', 'food')
		work('Sam', 'restaurant', 'meet', 'friend')
		work('Naiyana', 'salon', 'wash', 'hair')
		work('Juan', 'salon', 'cut', 'hair')
		work('John', 'salon', 'get', 'pedicure')
		work('Sam', 'salon', 'get', 'manicure')
		work('Sam', 'market', 'buy', 'food')
		work('Naiyana', 'mall', 'shop')
		work('Juan', 'pharmacy', 'buy', 'medicine')
		work('Juan', 'cinema', 'watch', 'movie')
		work('Sam', 'doctor', 'get', 'checkup')
		work('Juan', 'doctor', 'fix', 'headache')
		work('Naiyana', 'doctor', 'test', 'covid')
		work('you', 'hospital', 'visit', 'friend')
		work('I', 'clinic', 'see', 'doctor')
		work('Sam', 'clinic', 'see', 'dentist')
		work('Sam', 'dentist', 'clean', 'teeth')
		work('Naiyana', 'dentist', 'get', 'filling')
		work('John', 'dentist', 'get', 'whitening')
		work('Juan', 'dentist', 'fix', 'toothache')
		work('you', 'dentist', 'remove', 'tooth')
		work('I', 'dentist', 'get', 'braces')
		
		def work(who, which, period):
			Claws(who, 'go').modify('when', Objek(period).modify('which', which))
		
		work('Sam', 'this', 'morning') 
		work('Joe', 'this', 'afternoon') 
		work('Nid', 'this', 'evening') 
		work('Nui', 'last', 'week') 
		work('Sam', 'this', 'week') 
		work('Joe', 'next', 'week') 
		work('Nid', 'last', 'month') 
		work('Nui', 'this', 'month') 
		work('Sam', 'next', 'month') 
		work('Joe', 'last', 'year') 
		work('Nid', 'this', 'year') 
		work('Nui', 'next', 'year') 

		Claws('Nui', 'go').modify('when', 'now')
		Claws('Sam', 'go').modify('when', 'yesterday')
		Claws('Joe', 'go').modify('when', 'today')
		Claws('Nid', 'go').modify('when', 'tomorrow')

		# where and how: local vs distant destinations and mode of travel
		def work(who, where, how):
			Claws(who, 'go').modify('where', where).modify('how', how)
		
		work('Nui', 'Bangkok', 'train') 
		work('Nid', 'Chiang_Mai', 'bus') 
		work('Joe', 'Udon_Thani', 'airplane') 
		work('Sam', 'Koh_Samui', 'ship') 
		
		work('Joe', 'bank'      , 'car')      
		work('Nid', 'coffeeshop', 'Grab')    
		work('Nui', 'restaurant', 'taxi')    
		work('Sam', 'salon'     , 'citybus')     
		work('Joe', 'market'    , 'songtaew')
		work('Nid', 'mall'      , 'tuktuk')       
                             
		Claws('Sam', 'go').modify('where', 'dentist').modify('how', 'run')
		Claws('Joe', 'go').modify('where', 'clinic').modify('how', 'walk')

		def work(who, where, how):
			Claws(who, 'go').modify('where', where).modify('how', Claws('by', how))
		
		# you do what?

		Claws('Sam', 'eat', 'rice')
		Claws('Joe', 'cook', 'food')
		Claws('Nid', 'brew', 'coffee')
		Claws('Nui', 'brew', 'tea')
		Claws('Sam', 'read', 'book')
		Claws('Joe', 'watch', 'movie')
		Claws('Nid', 'listen', 'music')
		Claws('Joe', 'play', 'game')

		#chat online
		#homework
		#work on computer
		#work in garden

		Claws('Sam', 'eat', 'rice').modify('where', Objek('house'))
		Claws('Joe', 'cook', 'food').modify('where', Objek('house').modify('ownedby', 'friend'))
		Claws('Nid', 'cook', 'food').modify('where', 'kitchen')
		Claws('Joe', 'brew', 'coffee').modify('where', 'backyard')

		Claws('Nid', 'read', 'book').modify('where', 'upstairs')
		Claws('Nui', 'listen', 'music').modify('where', 'bedroom')
		Claws('Sam', 'watch', 'movie').modify('where', 'livingroom')
		Claws('Nid', 'play', 'game').modify('where', 'backyard')

		# Why
		Claws('Nid', 'cook', 'food').modify('why', Claws(Objek('family').modify('ownedby', 'Nid'), 'is', 'hungry'))

		Claws('Joe', 'brew', 'coffee').modify('why', Claws('Joe', 'relax'))
		Claws('Joe', 'brew', 'coffee').modify('why', Claws('Joe','give','friend'))
		Claws('Nid', 'read', 'book').modify('why', Claws('Nid', 'have', 'fun'))
		Claws('Penny', 'chat', 'online').modify('why', Claws('Penny', 'talk', 'friend'))

		Claws('Bella', 'do', 'homework').modify( 'why', Claws( 'assignment', 'is', 'due').modify('when', 'tomorrow'))
		Claws('Pin', 'do', 'homework').modify( 'why', Claws('Pin', 'study', 'test'))
		Claws('May', 'work').modify( 'where', 'computer').modify( 'why', 'job')
		Claws('Som', 'work').modify( 'where', 'garden').modify( 'why', Claws( 'weed', 'is', Objek('many').modify('howmuch', 'too')))
		Claws('Milky', 'work').modify( 'where', 'garden').modify( 'why', Objek('time').modify('what', 'harvest'))
		Claws('Chompoo', 'work').modify( 'where', 'garden').modify( 'why', Objek('time').modify('what', 'plant'))

