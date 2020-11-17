# samd.py

import ipc
import configparser
configfilename = '../../samd.conf'
config = configparser.ConfigParser()
config.read(configfilename)

class Switchboard:
	def __init__(self):
		self.ssock_addr = config['addr']['sam']

	def onMessage(self,message):  # callback from server socket
		print(f'recv: {message.toString()}')
		reply = security.process(message)
		if reply:
			print(f'send: {reply.toString()}')
		return reply

	def listen(self):
		print(f'Listening on {self.ssock_addr}')
		ipc.Server(self.ssock_addr, self.onMessage).serve_forever() # blocking

class Security:
	def __init__(self):
		pass

	def process(self, message):
		return reception.process(message)


class Reception:
	def __init__(self):
		pass

	# Reception is a skill.  Not all clones have it.
	# organize users and groups
	# route Message to Broca of recepient

	def process(self, message):
		response = ipc.Message(message.frm, message.to, f'echo {message.msg}')
		return response

def main():
	global switchboard, security, reception
	switchboard = Switchboard()
	security = Security()
	reception = Reception()
	switchboard.listen()  # blocking 
	
if __name__ == '__main__':
	main()
