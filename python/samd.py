''' samd.py - instantiate the first Sam daemon, usually as a service at boot '''

import sys
import sam.user
import configparser
import multiprocessing

configfilename = '../../samd.conf'

config = configparser.ConfigParser()
config.read(configfilename)

def createClone(name,addr,skills,languages):
	clone = sam.user.Sam(name, addr, skills, languages)
	clone.join()
	
labels = config['samd']['clones']
clones = []
for label in labels.split(','):
	name = config[label]['name']
	addr = config[label]['addr']
	skills = config[label]['skills']
	languages = config[label]['languages']
	
	if 'debug' in sys.argv:  # pdb cannot penetrate a process
		clones.append( sam.user.Sam(name, addr, skills, languages))
		break;

	proc = multiprocessing.Process(target=createClone, args=(name,addr,skills,languages))
	proc.start()
	clones.append(proc)

for clone in clones:
	clone.join() # blocking

