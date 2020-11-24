''' samd.py - instantiate the first Sam daemon, usually as a service at boot '''

import sam.user
import configparser

configfilename = '../../samd.conf'

config = configparser.ConfigParser()
config.read(configfilename)
name = config['comm']['name']
addr = config['comm']['addr']
skills = config['features']['skills']

sam = sam.user.Sam(name, addr, skills)
