''' samcli.py - cli interface to samd '''

import sam.comm
import configparser
import threading

configfilename = '../../samd.conf'
config = configparser.ConfigParser()
config.read(configfilename)
addr = config['comm']['addr']

token = ''

csock = sam.comm.Client()
csock.connect(addr)
print(f'connected to {addr}...')

def _keyboardLoop(csock):
	while True:
		s = input()  # blocking threadKeyboard
		if s == sam.comm.Client.exit_string:
			csock.close()
			break;
		m = sam.comm.Message(s)
		m.sendertoken = token
		csock.send(m)

threadKeyboard = threading.Thread(target=_keyboardLoop, args=(csock,), daemon=True)
threadKeyboard.start()
threadKeyboard.join()
