'''
lobby.py, defines classes: Switchboard, Security, Reception
'''
import ipc

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
		self.ssock = ipc.Server(self.ssock_addr, self.onMessage)
		try:
			print(f'Listening on {self.ssock_addr}')
			self.ssock.listen()
		except KeyboardInterrupt:
			#close the socket and stop the tread
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
		response = ipc.Message(message.frm, message.to, f'echo {message.msg}')
		return response

class Lobby:
	def __init__(self, ssock_addr):
		self.reception = Reception()
		self.security = Security(self.reception)
		self.switchboard = Switchboard(ssock_addr, self.security)
		self.switchboard.listen()
