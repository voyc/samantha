#!/usr/bin/python3
# samcli.py
# https://stackoverflow.com/questions/5404068/how-to-read-keyboard-input

import threading
import queue
import time
import ipc

server_address = ('localhost', 5795) # get this from sam.conf

def read_kbd_input(inputQueue):
	print('Ready for keyboard input:')
	while (True):
		input_str = input()
		inputQueue.put(input_str)

def main():
	EXIT_COMMAND = "q"
	inputQueue = queue.Queue()

	inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
	inputThread.start()

	while (True):
		if (inputQueue.qsize() > 0):
			input_str = inputQueue.get()

			if (input_str == EXIT_COMMAND):
				print("Exiting serial terminal.")
				break
			
			object = ipc.Message('sam', 'john', input_str)
			print( f'Send: {object.toString()}')

			with ipc.Client(server_address) as client:
				response = client.send(object)
			print( f'Received: {response.toString()}')

		# The rest of your program goes here.

		time.sleep(0.01) 
	print("End.")

if __name__ == '__main__':
	main()
