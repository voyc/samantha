''' user.py - define classes User, Human, and Sam '''

import lobby

class User:
	def __init__(self, name=''):
		self.uuid = ''    # unique id 
		self.name = name  # human readable name 
		self.personality = {}
		self.memory = {}

	def getuuid(self):
		pass

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

	def __init__(self, name='', addr=''):
		super().__init__(name)
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
		self.lobby = lobby.Lobby(self.addr)
		self.lobby.switchboard.listen();
		print(f'{self.name} is Listening on {self.ssock_addr}')

	def connect(self, addr):
		# connect to the server socket of another clone
		pass

	def join(self):
		self.lobby.switchboard.ssock.thread.join()

