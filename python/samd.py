# samd.py

import ipc
import configparser

def server_process_request(object):
	print(f'recv: {object.toString()}')
	response = ipc.Message(object.frm, object.to, f'echo {object.msg}')
	print(f'send: {response.toString()}')
	return response

class Switchboard():
	def __init__(self):
		config = configparser.ConfigParser()
		config.read('../../sam.conf')
		server_address = (config['samd']['host'], int(config['samd']['port']))
		print(f'Listening on {server_address}')
		ipc.Server(server_address, server_process_request).serve_forever()

class Security():
	# check credentials
	# pass message to Reception
	pass


class Reception():
	# Reception is a skill.  Not all clones have it.
	# organize users and groups
	# route Message to Broca of recepient
	pass

if __name__ == '__main__':
	switchboard = Switchboard()
