'''
samd.py   instantiate the first Sam daemon, usually as a service at boot
'''

configfilename = '../../samd.conf'

import configparser
config = configparser.ConfigParser()
config.read(configfilename)

ssock_addr = config['addr']['sam']

import lobby
lobby = lobby.Lobby(ssock_addr)
