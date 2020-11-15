# samd.py

import ipc
import configparser

switchboard = None
security = None
reception = None

class Switchboard():
	def __init__(self):
		pass

	def listen(self):
		config = configparser.ConfigParser()
		config.read('../../sam.conf')
		server_address = (config['samd']['host'], int(config['samd']['port']))
		print(f'Listening on {server_address}')
		ipc.Server(server_address, self.receive).serve_forever()

	def receive(self,message):
		print(f'recv: {message.toString()}')
		reply = security.process(message)
		print(f'send: {reply.toString()}')
		return reply

class Security():
	def __init__(self):
		pass

	def process(self, message):
		return reception.process(message)


class Reception():
	def __init__(self):
		pass

	# Reception is a skill.  Not all clones have it.
	# organize users and groups
	# route Message to Broca of recepient

	def process(self, message):
		response = ipc.Message(message.frm, message.to, f'echo {message.msg}')
		return response

if __name__ == '__main__':
	switchboard = Switchboard()
	security = Security()
	reception = Reception()
	switchboard.listen()  # does not return
