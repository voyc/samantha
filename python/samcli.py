''' samcli.py - cli interface to samd '''

import threading
import time
import ipc
import configparser

configfilename = '../../samd.conf'
config = configparser.ConfigParser()
config.read(configfilename)

exit_command = 'q'

def keyboardLoop(csock):
	while (True):
		s = input()
		if (s == exit_command):
			break
		message = ipc.Message('sam', 'john', s)
		csock.send(message)
		time.sleep(0.01) 

def onReceive(message):
	print( f'--> {message.msg}')

def main():
	ssock_addr = config['addr']['sam']
	csock = ipc.Client(ssock_addr, onReceive)
	print(f'Talking to {ssock_addr}...')

	keyboardThread = threading.Thread(target=keyboardLoop, args=(csock,), daemon=True)
	keyboardThread.start()
	keyboardThread.join()

if __name__ == '__main__':
	main()
