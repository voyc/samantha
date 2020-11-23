''' user.py - define classes User, Human, and Sam '''

import sam.lobby
import importlib

class User:
	def __init__(self, name='', addr='', skills=''):
		self.name = name
		self.addr = addr
		self.skillnames = skills
		self.token = ''
		self.traits = {}
		self.feelings = {}
		self.memory = {}

	def save(self):
		# write to database
		pass

	def restore(self):
		# read from database
		pass

class Human(User):
	def __init__(self, name=''):
		self.vocab = {}

	def isHuman(self):
		return True

class Sam(User):
	clones = {}
	skills = {}  # dict of name/object pairs

	def __init__(self, name='', addr=''):
		super().__init__(name, addr)
		self.addr = addr
		self.pid = -1   # each clone is a daemon process running samd
		Sam.clones[name] = self

	def isHuman(self):
		return False

	def announce(self):
		# announce my presence to the world
		pass
	
	def getuniqueport(self):
		pass

	def listen(self):
		self.lobby = sam.lobby.Lobby(self.addr)
		self.lobby.switchboard.listen();
		print(f'{self.name} is Listening on {self.addr}')

	def connect(self, addr):
		self.csock = ipc.Client(addr, onReceive)

	def send(self, msg):
		message = Message('Sam', self.name, msg)
		self.csock.send(message)

	def join(self):
		self.lobby.switchboard.ssock.thread.join()

	def loadSkills(self, names=self.skillnames):
		for name in names.split(','):
			self.addSkill(name)

	def addSkill(self, name):
		self.skills[name] = Skill.load(name)

class Skill:
	''' module skill/lobby.py defines class Lobby which implements method execute() '''
	def __init__(self, name):
		self.name = name
		self.classname = name.title()
		self.load()

	@staticmethod
	def load( name):
		mod = __import__( name )  # importlib.import_module(.name)
		kls = getattr(mod, name.title())            
		obj = kls('localhost:70000')
		return obj

	def execute(self, *args, **kwargs):
		pass
