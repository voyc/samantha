''' samd.py - instantiate the first Sam daemon, usually as a service at boot '''

import sam.user
import configparser

configfilename = '../../samd.conf'

config = configparser.ConfigParser()
config.read(configfilename)

labels = config['samd']['clones']
clones = []
for label in labels.split(','):
	name = config[label]['name']
	addr = config[label]['addr']
	skills = config[label]['skills']
	languages = config[label]['languages']
	clone = sam.user.Sam(name, addr, skills, languages)
	clones.append(clone)

for clone in clones:
	clone.join() # blocking
	

#name = config['comm']['name']
#addr = config['comm']['addr']
#skills = config['features']['skills']
#languages = config['features']['languages']
#
#sam = sam.user.Sam(name, addr, skills, languages)
#
## ...
#
#sam.join() # blocking


# sam is used in two different ways: packagename and global variable of master user
# change:
#     boss is variable for master user
#     boss contains collective mind: dick (list and tree), lang tables, gramr
#     boss contains collective memory

# humans each have vocab and memory

# each sam clone has memory and access to full dict

# during sleep, local memories of humans and clones are collected into boss.collective memory

'''
boss, collective, updated during sleep
	dick: list,tree  Dick() whoswho, gazeteer, history, fact book
	lang: en, th, s3  Lang()
	gramr  - Gramr()  collapsed rules derived from thots in conversations
	memri -  Memri()  a list of conversations

sam
	skills
	langs
	, on wake, downloads mind from collective
		dick
		lang
		memri - ? collective or personal, learned from conversation, pulled from collective
		gramr

lee, on wake, downloads mind from collective
	memri
	skills, can connect, but not listen
		no lobby, but can converse
	langs


humans and clones are running in separate processes, separate computers

therefore, each clone must have his own copy of dict and lang

on wakeup from sleep
	each clone reloads dick, memri, gramr

'''


