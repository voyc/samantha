''' mind.py '''

import uuid
import sam.tree
import datetime
import sam.base
import sam.dik
import sam.mem

''' 
usage:
	from sam.mind import Thot, Glos, Node, Number, Fray, Dik, Mind
	Mind is a singleton, implemented via a class variable, 
		and therefore, each Mind must be instantiated within a separate process
'''

class Mod:
	def __init__(self,at):
		self.at = at

class Thot:
	''' base class, add modifiers and accesscount  '''
	def __init__(self):
		self.modifiers = []
		self.accesscount = 0

	def modify(self, mod=None):
		mod = Mind().dik.get(mod)
		self.modifiers.append(mod)
		return self

	def isTop(self):
		return self.accesscount <= 0

class Glos(sam.tree.Tree, Thot):
	''' a Glos is a word (entity, thing, action, idea), class or object, in the mind '''
	def __init__(self, dik, word, pos, parent, en, th):
		''' word is a string.  parent can be string or object. '''
		self.word = word
		self.pos = pos
		self.en = en
		self.th = th

		parent = dik.get(parent) # convert string to object 
		if not parent: # first time only, init the tree
			if dik.tree:
				raise Exception(f'no parent for glos {self.word}')
			dik.tree = self

		sam.tree.Tree.__init__(self,parent) # init parent, level, child
		Thot.__init__(self)                 # init modifier, accesscount ? needed in dik ?

		if word in dik.glos:
			raise Exception(f'dupe glos {self.word}')
		dik.glos[word] = self

	def __str__(self):
		return self.word

	def dump(self):
		print(self.word)
		print(self.parent.word)
		print(self.level)
		for m in self.modifiers:
			print( f' {m.lk.word} {m.at.word}')

class Dik:
	''' s3 dictionary, list of glos, keyed by word '''
	def __init__(self):
		self.glos = {}
		self.tree = None
		self.postable = ['noun','pron','name','verb','adv','adj','prep','conj','intj','qw']

	def iterate(self, cb):
		for glos in self.glos.values():
			cb(glos) 
		
	def get(self, glos): # input param is str or Glos
		if isinstance(glos, str):
			try: glos = self.glos[glos]
			except: glos = None 
		return glos 

	def getPos(self,w):
		return self.glos[w].pos

	def addGlos(self, word, pos, parent, en, th):
		glos = Glos(self, word, pos, parent, en, th)

	def load(self):
		for x in sam.dik.sdik:
			self.addGlos( x[0], x[1], x[2], x[3], x[4])

	def printTree(self):
		print('Dik Glos Tree')
		def fn(m):
			indent = '\t' * (m.level)
			x = '' if m.isLeaf() else '---'
			print( f'{indent} {str(m.level)} {m} {m.accesscount} {x}')
		self.tree.process(fn, False)
		return

class Fray:
	def __init__(self,lk=None,at=None):
		self.lk = lk
		self.at = at

	def __str__(self):
		return f'{self.lk} {self.at}'

class Node(Glos):
	''' object, an instance of a Node '''
	def __init__(self, glos):
		sglos = glos
		glos = Mind().dik.get(sglos) # convert string to object 
		if not glos:
			raise Exception(f'glos not found: {sglos}')
		self.word = glos.word
		self.glos = glos
		Thot.__init__(self)
		self.ts = datetime.datetime.timestamp(datetime.datetime.now())
		self.id = ''.join(str(self).split(' ')) + '_' + str(self.ts)
		Mind().objeks[self.id] = self

	def __str__(self):
		s = self.word
		for m in self.modifiers:
			s += f' {str(m.lk)} {str(m.at)}'
		return s

class Claw(Thot):
	''' clause: subjek, verb, {object} '''
	def __init__(self, subjek='empty', verb='empty', objek=None):
		super().__init__()
		self.subjek = Node(Mind().dik.get(subjek))
		self.verb = Node(Mind().dik.get(verb))
		self.objek = Node(Mind().dik.get(objek)) if objek else None
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

	def state(self):
		if self.objek and self.objek.word != 'empty':
			return 'haveobjek'
		elif self.verb and self.verb.word != 'empty':
			return 'haveverb'
		elif self.subjek and self.subjek.word != 'empty':
			return 'havesubjek'
		else:
			return 'open'

class Cmd(Claw):
	def __init__(self,verb):
		self.verb = verb
		self.arguments = {}

class Qws(Claw):
	def __init__(self,verb):
		self.verb = verb
		self.arguments = {}

class Ans(Claw):
	def __init__(self,verb):
		self.verb = verb
		self.arguments = {}

class Number(Thot):
	def __init__(self,value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)

class Mind(sam.base.Singleton):
	''' singleton, defines a mind, thinks, contains dik, mem, gram '''
	def __init__(self):
		if 'dik' in dir(self): return # init only once
		self.dik = None

		# memory: 
		self.objeks = {}
		self.claws = {} # uuid-keyed Clause objects

		# grammar:
		self.patterns = {}

	def setup(self,me=None):
		self.me = me  # the user object, the owner of this mind
		self.dik = Dik() 
		self.dik.load()
		#sam.mem.initMemory()

	def think(self, conversation):
		prevmessage = conversation.messages[-1]

		'''
		previous message
		match to grammar patterns
		find need for name and password
		'''

		claws = Claw( Node('name').modify(Fray('of', 'you')), 'what')
		claws = Claw( Node('password').modify(Fray('of', 'you')), 'what')

		return claws

	# should be in Dik
	#def hasParent(self,param,match):
	#	node = self.dik.get(param)
	#	while node.word != 'root':
	#		node = self.dik.glos[node.word].parent
	#		if node.word == match:
	#			return True
	#	return False 

	def buildGrammar(self):
		for claw in self.claws.values():
			subjek = claw.subjek #self.findBranchNode(self.dik.get(claw.subjek.word))
			if subjek not in self.patterns:
				self.patterns[subjek] = {}

			verb = claw.verb # claw.verb.parent #self.findBranchNode(claw.verb)
			if verb not in self.patterns[subjek]:
				self.patterns[subjek][verb] = {}

			objek = claw.objek
			what = self.dik.get('what')
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
		print(f'Glos {len(self.dik.glos)}, Node {len(self.objeks)}, Claw {len(self.claws)}, Pattern {len(self.patterns)}\n')
		if detail:
			self.dik.printTree()
			self.printTopClaw()
			#self.printSubClaw()
			#self.printGrammar()

	def printTopClaw(self):
		tlate = translate.Translate()
		print('\nTop Claw')
		for v in self.claws.values():
			if v.isTop():
				print( tlate.getThai(str(v)))

	def printSubClaw(self):
		print('\nSub Claw')
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
