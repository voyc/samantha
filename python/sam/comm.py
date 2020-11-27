''' comm.py - communications using websockets '''

import concurrent.futures
import asyncio
import websockets
import threading
import queue
import sys
import json

def splitAddr(addr):
	''' has format 52.102.68.4:59205 '''
	host, port = addr.split(':')
	port = int(port)
	uri = f'ws://{host}:{port}'
	return addr, host, port, uri

class Message():
	''' object passed between client and server '''
	def __init__(self, msg='', toname='', frmtoken=''):
		self.msg = msg
		self.toname = ''
		self.frmtoken = ''
		self.mode = None

	def serialize(self):
		return json.dumps(self.__dict__)

	@classmethod
	def deserialize(cls,data):
		a = json.loads(data)
		return cls(a['msg'], a['toname'], a['frmtoken'], )

	def toString(self):
		return f'{self.msg}'

	def parse(self):
		return self.msg.split(' ')

class Client:
	exit_string = 'q'

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

	async def closeSocket(self):
		await self.socket.close()
		await asyncio.sleep(.1)  # give sendLoop time to exit

	def send(self,m):
		self.q.put(m)

	async def sendLoop(self):
		while self.socket.state == 1: # State.OPEN:
			try:
				m = self.q.get(block=False)
			except queue.Empty:
				await asyncio.sleep(.08)  # like yield
			else:	
				await self.socket.send(m.serialize())

	async def receiveLoop(self):
		while self.running:
			try:
				r = await self.socket.recv()
				m = Message.deserialize(r)
			except websockets.exceptions.ConnectionClosed:
				break
			else:
				print(f'--> {m.msg}')

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
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		loop.run_until_complete( websockets.serve(self._onMessage, self.host, self.port))
		loop.run_forever()  # block threadListen

	def join(self):
		self.threadListen.join() # block calling thread until threadListen stops

	async def _onMessage(self, websocket, path):
		''' called by websockets.serve on receipt of a message '''
		async for message in websocket:
			response = self.callback( websocket, Message.deserialize(message))
			await self.reply(websocket, response)

	async def reply(self, websocket, response):
		await websocket.send(response.serialize())
