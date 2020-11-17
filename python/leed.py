'''
leed.py   instantiate Lee, the first clone
'''

import configparser
import user

configfilename = '../../samd.conf'
name = 'Lee'

config = configparser.ConfigParser()
config.read(configfilename)
addr = config['addr'][name]

lee = user.Sam(name, addr)

saddr = config['addr']['Sam']
sock = lee.connect(saddr)
#lee.converse(sock)
