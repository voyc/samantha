#!/usr/bin/python3
# samcli.py
# https://stackoverflow.com/questions/5404068/how-to-read-keyboard-input

import threading
import queue
import time
import ipc
import configparser

config = configparser.ConfigParser()
config.read('../../sam.conf')
server_address = (config['samd']['host'], int(config['samd']['port']))
exit_command = 'q'

def read_kbd_input(inputQueue):
	while (True):
		input_str = input()
		inputQueue.put(input_str)

def main():
	inputQueue = queue.Queue()

	inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
	inputThread.start()
	print(f'Talking to {server_address}...')

	while (True):
		if (inputQueue.qsize() > 0):
			input_str = inputQueue.get()

			if (input_str == exit_command):
				break
			
			message = ipc.Message('sam', 'john', input_str)

			with ipc.Client(server_address) as client:
				response = client.send(message)
				print( f'--> {response.msg}')

		time.sleep(0.01) 

if __name__ == '__main__':
	main()
