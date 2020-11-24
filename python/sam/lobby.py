''' lobby.py - a skill, managing incoming connections '''

import sam.comm

class Lobby(sam.user.Skill):  # do we want a base class Skill() ?
	def __init__(self, user):
		self.reception = Reception()
		self.security = Security(self.reception)
		self.switchboard = Switchboard(user.addr, self.security)
		self.switchboard.listen()

	def join(self):
		self.switchboard.socket.join()

class Switchboard:
	def __init__(self, addr, security):
		self.addr = addr
		self.security = security

	def onMessage(self,message):  # callback from server socket
		print(f'recv: {message.toString()}')
		reply = self.security.process(message)
		if reply:
			print(f'send: {reply.toString()}')
		return reply

	def listen(self):
		self.socket = sam.comm.Server()
		self.socket.listen(self.addr, self.onMessage)  # blocking
		print(f'switchboard listening on {self.addr}...')

	def close(self):
		self.socket.close()

class Security:
	def __init__(self, reception):
		self.reception = reception

	def process(self, message):
		return self.reception.process(message)


class Reception:
	def __init__(self):
		pass

	# Reception is a skill.  Not all clones have it.
	# organize users and groups
	# route Message to Broca of recepient

	def process(self, message):
		response = sam.comm.Message(message.frm, message.to, f'echo {message.msg}')
		return response
