''' lobby.py, the Lobby includes Switchboard, Security, Reception '''

import sam.comm
import sam.user

class Switchboard:
	def __init__(self, ssock_addr, security):
		self.ssock_addr = ssock_addr
		self.security = security

	def onMessage(self,message):  # callback from server socket
		print(f'recv: {message.toString()}')
		reply = self.security.process(message)
		if reply:
			print(f'send: {reply.toString()}')
		return reply

	def listen(self):
		self.ssock = comm.Server(self.ssock_addr, self.onMessage)
		self.ssock.listen()  # blocking

	def close(self):
		self.ssock.close()

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
		response = comm.Message(message.frm, message.to, f'echo {message.msg}')
		return response

class Lobby(sam.user.Skill):
	def __init__(self, ssock_addr):
		self.reception = Reception()
		self.security = Security(self.reception)
		self.switchboard = Switchboard(ssock_addr, self.security)

