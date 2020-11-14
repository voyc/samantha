# samd.py

import ipc

class Switchboard():
	# create socket server
	# read and write messages
	# pass to Security
	pass

def server_process_request(object):
    response = Message('sarah', 'joe', 'token abc123')
    response.print()
    return response


if __name__ == '__main__':
    server_address = ('127.0.0.1', 5795)
    print(['listening', server_address])
    Server(server_address, server_process_request).serve_forever()


class Security():
	# check credentials
	# pass message to Reception
	pass



class Reception():
	# Reception is a skill.  Not all clones have it.
	# organize users and groups
	# route Message to Broca of recepient
	pass
