''' comm.py - websockets implementation '''

import concurrent.futures
import asyncio
import websockets
import threading
import queue
import sys

def splitAddr(addr):
	''' has format 52.102.68.4:59205 '''
	host, port = addr.split(':')
	port = int(port)
	uri = f'ws://{host}:{port}'
	return addr, host, port, uri

class Client:
	def __init__(self):
		self.socket = None
		self.q = queue.SimpleQueue()

	def connect(self, addr):
		self.addr, self.host, self.port, self.uri = splitAddr(addr)
		self.threadConnect = threading.Thread(target=self._connectLoop, args=(), daemon=True)
		self.threadConnect.start()

	def _connectLoop(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		loop.run_until_complete( self.openSocket( self.uri))
		loop.create_task( self.sendLoop())
		self.running = True
		loop.run_until_complete( self.receiveLoop())
		loop.run_until_complete( self.closeSocket())
		loop.close()

	def close(self):
		self.running = False
		self.send('')

	def join(self):
		self.threadConnect.join()

	async def openSocket(self, uri):
		self.socket = await websockets.connect(uri)
		print(self.socket)

	async def closeSocket(self):
		await self.socket.close()
		await asyncio.sleep(.1)  # give sendLoop time to exit

	def send(self,s):
		self.q.put(s)

	async def sendLoop(self):
		while self.socket.state == 1: # State.OPEN:
			try:
				s = self.q.get(block=False)
			except queue.Empty:
				await asyncio.sleep(.08)  # like yield
			else:	
				await self.socket.send(s)

	async def receiveLoop(self):
		while self.running:
			try:
				s = await self.socket.recv()
			except websockets.exceptions.ConnectionClosed:
				break
			else:
				print(s)

class Server:
	def init(self):
		pass

	def listen(self, addr, callback):
		self.addr = addr
		self.host, port = self.addr.split(':')
		self.port = int(port)
		self.callback = callback
		self.threadListen = threading.Thread(target=self._listen, args=(), daemon=True)
		self.threadListen.start()

	def _listen(self):
		#import pdb; pdb.set_trace()
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		#loop = asyncio.get_running_loop()
		loop.run_until_complete( websockets.serve(self._onMessage, self.host, self.port))
		loop.run_forever()  # block threadListen

	def join(self):
		self.threadListen.join() # block calling thread until threadListen stops

	async def _onMessage(self, websocket, path):
		''' called by websockets.serve on receipt of a message '''
		async for message in websocket:
			response = self.callback(websocket, message)
			await self.reply(websocket, response)

	async def reply(self, websocket, response):
		print(response)
		await websocket.send(response)

def test():
	''' test stub '''
	addr = 'localhost:50001'
	
	if 'server' in sys.argv:
		def echo(websocket, message): return f'echo: {message}'  # one websocket per connection
		s = Server()
		s.listen(addr, echo)
		s.join()  # blocking
	elif 'client' in sys.argv:
		csock = Client()
		csock.connect(addr)
		csock.send('hey baby whats happening')
		if 'keyboard' in sys.argv:
			def _keyboardLoop(csock):
				while True:
					s = input()  # blocking threadKeyboard
					if s == 'q':
						csock.close()
						break;
					csock.send(s)
			threadKeyboard = threading.Thread(target=_keyboardLoop, args=(csock,), daemon=True)
			threadKeyboard.start()
		csock.join()

if __name__ == '__main__':
	test()
