''' samcli.py - cli interface to samd '''

import asyncio
import websockets
import configparser

configfilename = '../../samd.conf'
config = configparser.ConfigParser()
config.read(configfilename)

host = config['chat']['host']
port = config['chat']['port']
addr = f'ws://{host}:{port}'

exit_command = 'q'


class Message():
	def __init__(self, to='', frm='', msg=''):
		self.to = to
		self.frm = frm
		self.msg = msg

	def serialize(self):
		#return json.dumps(self.__dict__)
		return f'login~{self.frm}~{self.msg}'

	#def deserialize(self,data):
	#	self.__dict__ = json.loads(data)

	@classmethod
	def deserialize(cls,data):
		a = json.loads(data)
		return cls(a['to'], a['frm'], a['msg'])

	def toString(self):
		return f'to {self.to}, from {self.frm}: {self.msg}'

	def print(self):
		print( self.toString())

async def keyboardLoop(uri):
	while (True):
		s = input()
		if (s == exit_command):
			break
		message = Message('sam', 'john', s)
		await websocket.send(message.serialize())

async def socketLoop(uri):
	while (True):
		incoming = await websocket.recv()
		print( incoming)

#class ClientSocket(websockets.connect, websockets.WebSocketClientProtocol):
#	def __init__():
#		super()
class ClientSocket(websockets.connect, websockets.client.WebSocketClientProtocol):
	def __init__(self) -> websockets.client.WebSocketClientProtocol:
		websockets.client.WebSocketClientProtocol.__init__(self)
		super().__init__(addr)
	
scheduler = asyncio.get_event_loop()
#websocket = websockets.WebSocketClientProtocol()
#websocket = websockets.connect.unix_connect(uri=addr)
#websocket.connect(addr)
#websocket = websockets.client.Connect(addr)  # Connect object has no attribute "send"

websocket = ClientSocket()
#websocket = websockets.client.WebSocketClientProtocol()
print(websocket.__class__)
print(dir(websocket))
print(websocket.state)
print(websocket.side)
print(websocket.is_client)
#print(websocket.path)
print(websocket.__module__)
print(websocket.open)
print(websocket.host)
print(websocket.port)


websocket = websockets.connect(addr)
print(websocket.__class__)
print(dir(websocket))
#print(websocket.state)
print(websocket.side)
print(websocket.is_client)
#print(websocket.path)
print(websocket.__module__)
print(websocket.open)
print(websocket.host)
print(websocket.port)


try:
	asyncio.ensure_future(keyboardLoop(websocket))
	#asyncio.ensure_future(socketLoop(websocket))
	scheduler.run_forever()
except KeyboardInterrupt:
	pass
finally:
	scheduler.close()
	websocket.close()


async def hello(uri):
	async with websockets.connect(uri) as websocket:
		#await websocket.send("Hello world!")
		message = Message('sam', 'john', 'god damn i hate you')
		await websocket.send(message.serialize())
		msg = await websocket.recv()
		print(msg)

#scheduler.run_until_complete(hello(addr))




#import threading
#import time
#import lib.ipc as ipc
#import configparser
#
#configfilename = '../../samd.conf'
#config = configparser.ConfigParser()
#config.read(configfilename)
#
#exit_command = 'q'
#
#def keyboardLoop(csock):
#	while (True):
#		s = input()
#		if (s == exit_command):
#			break
#		message = ipc.Message('sam', 'john', s)
#		csock.send(message)
#		time.sleep(0.01) 
#
#def onReceive(message):
#	print( f'--> {message.msg}')
#
#def main():
#	ssock_addr = config['addr']['sam']
#	csock = ipc.Client(ssock_addr, onReceive)
#	print(f'Talking to {ssock_addr}...')
#
#	keyboardThread = threading.Thread(target=keyboardLoop, args=(csock,), daemon=True)
#	keyboardThread.start()
#	keyboardThread.join()
#
#if __name__ == '__main__':
#	mait
()
