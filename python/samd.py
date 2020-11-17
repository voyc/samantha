'''
samd.py   instantiate the first Sam daemon, usually as a service at boot
'''

import user
import configparser

configfilename = '../../samd.conf'
name = 'Sam'

config = configparser.ConfigParser()
config.read(configfilename)
addr = config['addr'][name]

sam = user.Sam(name, addr)
sam.listen()
sam.join()
