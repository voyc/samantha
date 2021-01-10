''' mind.py '''

import uuid
import sam.tree
import datetime
import sam.base

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
	mind = None  # global variable, not class variable

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
			param = Mind().nodes[param]
			if not param:
				raise NodeNotFoundException
		return param 

class Node(sam.tree.Tree, Thot):
	''' a Node is a word (entity, thing, action, idea), class or object, in the mind '''
	def __init__(self,word,pos,parent=None):
		''' word is a string.  parent can be string or object. '''
		self.word = word
		self.pos = pos
		parent = Thot.nfs(parent) # convert string to object 
		if not parent: # first time only, init the tree
			if Mind().nodetree:
				raise NoParentException
			Mind().nodetree = self
		sam.tree.Tree.__init__(self,parent)
		Thot.__init__(self)
		if word in Mind().nodes:
			raise DupeNodeException
		Mind().nodes[word] = self

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
		Mind().objeks[self.id] = self

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
		Mind().claws[self.id] = self

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

class Mind(sam.base.Singleton):
	''' 
	singleton class
	defines a mind 
	contains thots, which are nodes, objeks, and claws
	contains grammar, patterns
	'''
	def __init__(self):
		if 'nodes' in dir(self): return # init only once
		self.nodes = {}  # string-keyed Node objects
		self.nodetree = None
		self.objeks = {}
		self.claws = {} # uuid-keyed Clause objects
		self.patterns = {}

	def setup(self,me):
		self.me = me  # the user object, the owner of this mind
		self.loadDictionary()
		self.loadMemory()

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

	def loadDictionary(self):
		''' s3 dictionary '''
		#     word         pos    parent
		Node('root'       ,'n'   ,None  )
		Node('empty'      ,'j'   ,'root')
		Node('person'     ,'n'   ,'root')
		Node('place'      ,'n'   ,'root')
		Node('thing'      ,'n'   ,'root')
		Node('action'     ,'n'   ,'root')
		Node('link'       ,'n'   ,'root')

		Node('typeof'     ,'p'   ,'link')
		Node('ownedby'    ,'p'   ,'link')
		Node('by'         ,'p'   ,'link')

		Node('question'   ,'n'   ,'link')
		Node('which'      ,'p'   ,'question') # apply to noun

		Node('where'      ,'p'   ,'question') # apply to verb
		Node('why'        ,'p'   ,'question')
		Node('when'       ,'p'   ,'question')  # default "now"
		Node('how'        ,'p'   ,'question')
		Node('what'       ,'p'   ,'question')  # applies only to "do"

		Node('this'       ,'j'   ,'which')
		Node('next'       ,'j'   ,'which')
		Node('last'       ,'j'   ,'which') # previous

		Node('time_period','n'   ,'thing')
		Node('week'       ,'n'   ,'time_period')
		Node('day'        ,'n'   ,'time_period')
		Node('month'      ,'n'   ,'time_period')
		Node('year'       ,'n'   ,'time_period')

		Node('time'       ,'n'   ,'thing')
		Node('now'        ,'a'   ,'time')
		Node('yesterday'  ,'a'   ,'time')
		Node('today'      ,'a'   ,'time')
		Node('tomorrow'   ,'a'   ,'time')
		Node('morning'    ,'a'   ,'time')
		Node('afternoon'  ,'a'   ,'time')
		Node('evening'    ,'a'   ,'time')

		Node('you'        ,'p'   ,'person')
		Node('I'          ,'p'   ,'person')
		Node('friend'     ,'p'   ,'person')
		Node('family'     ,'p'   ,'person')

		Node('Nid'        ,'np'  ,'person')
		Node('Pin'        ,'np'  ,'person')
		Node('May'        ,'np'  ,'person')
		Node('Som'        ,'np'  ,'person')
		Node('Nui'        ,'np'  ,'person')
		Node('Memi'       ,'np'  ,'person')
		Node('Fern'       ,'np'  ,'person')
		Node('Bella'      ,'np'  ,'person')
		Node('Jenny'      ,'np'  ,'person')
		Node('Penny'      ,'np'  ,'person')
		Node('Milky'      ,'np'  ,'person')
		Node('Donut'      ,'np'  ,'person')
		Node('Namtip'     ,'np'  ,'person')
		Node('Tangmo'     ,'np'  ,'person')
		Node('Chompoo'    ,'np'  ,'person')
		Node('Naiyana'    ,'np'  ,'person')

		Node('Sam'        ,'np'  ,'person')
		Node('Joe'        ,'np'  ,'person')
		Node('John'       ,'np'  ,'person')
		Node('Juan'       ,'np'  ,'person')

		Node('city'        ,'n'  ,'place')
		Node('island'      ,'n'  ,'place')
		Node('house'       ,'n'  ,'place')
		Node('businesstype','n'  ,'thing')
		Node('bank'        ,'n'  ,'businesstype')
		Node('coffeeshop'  ,'n'  ,'businesstype')
		Node('restaurant'  ,'n'  ,'businesstype')
		Node('salon'       ,'n'  ,'businesstype')
		Node('market'      ,'n'  ,'businesstype')
		Node('mall'        ,'n'  ,'businesstype')
		Node('pharmacy'    ,'n'  ,'businesstype')
		Node('cinema'      ,'n'  ,'businesstype')
		Node('doctor'      ,'n'  ,'businesstype')
		Node('hospital'    ,'n'  ,'businesstype')
		Node('clinic'      ,'n'  ,'businesstype')
		Node('dentist'     ,'n'  ,'businesstype')
		Node('embassy'     ,'n'  ,'businesstype')

		Node('Bangkok'     ,'np' ,'city')
		Node('Phuket'      ,'np' ,'city')
		Node('Koh_Samui'   ,'np' ,'island')
		Node('Krabi'       ,'np' ,'city')
		Node('Pattaya'     ,'np' ,'city')
		Node('Hua_Hin'     ,'np' ,'city')
		Node('Chiang_Mai'  ,'np' ,'city')
		Node('Pai'         ,'np' ,'city')
		Node('Udon_Thani'  ,'np' ,'city')
		Node('Sukothai'    ,'np' ,'city')
		Node('Ayutthaya'   ,'np' ,'city')

		Node('food'        ,'n'  ,'thing')
		Node('vacation'    ,'n'  ,'thing')
		Node('business'    ,'n'  ,'thing')
		Node('money'       ,'n'  ,'thing')
		Node('coffee'      ,'n'  ,'food')
		Node('breakfast'   ,'n'  ,'food')
		Node('hair'        ,'n'  ,'thing')
		Node('pedicure'    ,'n'  ,'thing')
		Node('manicure'    ,'n'  ,'thing')
		Node('medicine'    ,'n'  ,'thing')
		Node('movie'       ,'n'  ,'thing')
		Node('checkup'     ,'n'  ,'thing')
		Node('headache'    ,'n'  ,'thing')
		Node('covid'       ,'n'  ,'thing')
		Node('tooth'       ,'n'  ,'thing')
		Node('teeth'       ,'n'  ,'thing')
		Node('filling'     ,'n'  ,'thing')
		Node('whitening'   ,'n'  ,'thing')
		Node('toothache'   ,'n'  ,'thing')
		Node('braces'      ,'n'  ,'thing')
		Node('fun'         ,'n'  ,'thing')

		Node('transport'   ,'n'  ,'thing')
		Node('train'       ,'n'  ,'transport')
		Node('bus'         ,'n'  ,'transport')
		Node('airplane'    ,'n'  ,'transport')
		Node('ship'        ,'n'  ,'transport')

		Node('Grab'        ,'np' ,'transport')
		Node('car'         ,'n'  ,'transport')
		Node('taxi'        ,'n'  ,'transport')
		Node('citybus'     ,'n'  ,'transport')
		Node('songtaew'    ,'n'  ,'transport')
		Node('tuktuk'      ,'n'  ,'transport')

		Node('walk'        ,'v'  ,'action')
		Node('run'         ,'v'  ,'action')

		Node('do'          ,'v'  ,'action')
		Node('go'          ,'v'  ,'action')
		Node('come'        ,'v'  ,'action')
		Node('eat'         ,'v'  ,'action')
		Node('visit'       ,'v'  ,'action')
		Node('pickup'      ,'v'  ,'action')
		Node('deliver'     ,'v'  ,'action')
		Node('get'         ,'v'  ,'action')
		Node('drink'       ,'v'  ,'action')
		Node('meet'        ,'v'  ,'action')
		Node('wash'        ,'v'  ,'action')
		Node('cut'         ,'v'  ,'action')
		Node('buy'         ,'v'  ,'action')
		Node('shop'        ,'v'  ,'action')
		Node('watch'       ,'v'  ,'action')
		Node('fix'         ,'v'  ,'action')
		Node('test'        ,'v'  ,'action')
		Node('see'         ,'v'  ,'action')
		Node('clean'       ,'v'  ,'action')
		Node('remove'      ,'v'  ,'action')

		Node('cook'        ,'v'  ,'action')
		Node('brew'        ,'v'  ,'action')
		Node('read'        ,'v'  ,'action')
		Node('listen'      ,'v'  ,'action')
		Node('play'        ,'v'  ,'action')
		Node('is'          ,'v'  ,'action')
		Node('feel'        ,'v'  ,'action')
		Node('relax'       ,'v'  ,'action')
		Node('chat'        ,'v'  ,'action')
		Node('talk'        ,'v'  ,'action')
		Node('give'        ,'v'  ,'action')
		Node('have'        ,'v'  ,'action')
		Node('study'       ,'v'  ,'action')
		Node('work'        ,'v'  ,'action')

		Node('animal'      ,'n'  ,'root')
		Node('cow'         ,'n'  ,'animal')

		Node('foodtype'    ,'n'  ,'root')
		Node('rice'        ,'n'  ,'foodtype')
		Node('tea'         ,'n'  ,'foodtype')

		Node('book'        ,'n'  ,'thing')
		Node('music'       ,'n'  ,'thing')
		Node('game'        ,'n'  ,'thing')
		Node('homework'    ,'n'  ,'thing')
		Node('assignment'  ,'n'  ,'thing')
		Node('computer'    ,'n'  ,'thing')
		Node('job'         ,'n'  ,'thing')
		Node('garden'      ,'n'  ,'thing')
		Node('weed'        ,'n'  ,'thing') 
		Node('harvest'     ,'n'  ,'thing') 
		Node('plant'       ,'n'  ,'thing') 

		Node('due'         ,'n'  ,'thing') # state, adj
		Node('many'        ,'n'  ,'thing') # adv 
		Node('howmuch'     ,'n'  ,'link') # adv 
		Node('too'         ,'n'  ,'howmuch') # adv 

		Node('feeling'     ,'n'  ,'root')
		Node('hungry'      ,'n'  ,'feeling')

		Node('kitchen'     ,'n'  ,'place')
		Node('backyard'    ,'n'  ,'place')
		Node('upstairs'    ,'n'  ,'place')
		Node('bedroom'     ,'n'  ,'place')
		Node('livingroom'  ,'n'  ,'place')

		Node('online'      ,'a'  ,'place')

	def loadMemory(self):
		''' prelearned thots, included in dna '''
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

