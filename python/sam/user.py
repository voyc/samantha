''' user.py - define classes User, Human, and Sam '''

import sam.base

class User:
	def __init__(self, name='', addr=''):
		self.name = name
		self.addr = addr
		self.token = ''
		self.traits = Traits()
		self.feelings = Feelings()
		self.memory = Memory() 

	def save(self):
		# write to database
		pass

	def restore(self):
		# read from database
		pass

class Human(User):
	def __init__(self, name='', addr=''):
		super().__init__(name, addr)
		self.vocab = {}

	def isHuman(self):
		return True

class Sam(User):

	def __init__(self, name='', addr='', skills=''):
		super().__init__(name, addr)
		self.skillnames = skills
		self.pid = -1   # each clone is a daemon process running samd
		self.clones = {}
		self.skills = {}
		self.cmds = {}
		self.loadSkills()

	def isHuman(self):
		return False

	def announce(self):
		# announce my presence to the world
		pass
	
	def getuniqueport(self):
		pass

	def connect(self, addr):
		self.csock = ipc.Client(addr, onReceive)

	def send(self, msg):
		message = Message('Sam', self.name, msg)
		self.csock.send(message)

	def join(self):
		''' run join on each skill, block until all threads closed '''
		for skill in self.skills.values():
			skill.join()

	def loadSkills(self):
		for name in self.skillnames.split(','):
			self.addSkill(name)

	def addSkill(self, name):
		self.skills[name] = sam.base.Skill.load(name, self)

class Traits:
	''' personality traits of a user '''
	def __init__(self):
		# personality big five (temperament)
		openness = 0.0           # +1=inventive/curious       -1=consistent/cautious
		conscientiousness = 0.0  # +1=efficient/organized     -1=extravagant/careless
		extraversion = 0.0       # +1=outgoing/energetic      -1=solitary/reserved
		agreeableness = 0.0      # +1=friendly/compassionate  -1=challenging/callous
		neuroticism = 0.0        # +1=sensitive/nervous       -1=resilient/confident
		
		# intelligence
		iq = 0.0   # +1=150  0=100  -1=50   # human iq median=100  sd=15  3sd=>55 to 145
	
		# values (beliefs, goals, motivation)

class Feelings:
	''' immediate emotional states '''
	def __init__(self):
		anger = 0.0
		disgust = 0.0
		fear = 0.0
		happiness = 0.0
		sadness = 0.0
		surprise = 0.0

class Memory:
	def __init__(self):
		pass 
