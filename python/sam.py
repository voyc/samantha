# sam.py

import configparser

config = configparser.ConfigParser()
config.read('../../samd.conf')
ssock_address = config['addr']['sam']

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
		# open server socket
		pass

	def connect(self, addr):
		# connect to the server socket of another clone
		pass

def main():
	sam = Sam('Sam', 'localhost:5795')
	lee = Sam('Lee', 'localhost:5796')
	print(sam.isHuman())
	print(lee.isHuman())
	print(sam.name)
	print(lee.name)
	print(lee.addr)
	sam.listen()
	sock = lee.connect(sam.addr)
	lee.converse(sock)
	# shall i clone myself once for every conversation?

if __name__ == '__main__':
	main()
