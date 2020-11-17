'''
samd.py   instantiate the first Sam daemon, usually as a service at boot
'''

import configparser
import user

configfilename = '../../samd.conf'

config = configparser.ConfigParser()
config.read(configfilename)

ssock_addr = config['addr']['sam']

sam = user.Sam('Sam', 'localhost:5795')

def test():
	lee = user.Sam('Lee', 'localhost:5796')
	print(lee.isHuman())
	print(lee.name)
	print(lee.addr)
	sock = lee.connect(sam.addr)
	lee.converse(sock)
	# shall i clone myself once for every conversation?

sam.listen()
sam.join()
