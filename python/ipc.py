# ipc.py
# https://gist.github.com/dankrause/9607475

import socketserver
import socket
import struct
import json
import threading
import time

class IPCError(Exception):
	pass

class UnknownMessageClass(IPCError):
	pass

class InvalidSerialization(IPCError):
	pass

class ConnectionClosed(IPCError):
	pass

def _read_object(sock):
	header = sock.recv(4)
	if len(header) == 0:
			raise ConnectionClosed()
	size = struct.unpack('!i', header)[0]
	data = sock.recv(size - 4)
	if len(data) == 0:
			raise ConnectionClosed()
	g = Message.deserialize(data)
	return g

def _write_object(sock, object):
	data = object.serialize()
	sock.sendall(struct.pack('!i', len(data) + 4))
	sock.sendall(data.encode())

def addrTuple(s):  # socket addr is stored as string 'ip:port'
	a = s.split(':')
	return (a[0], int(a[1]))

class Message():
	def __init__(self, to='', frm='', msg=''):
		self.to = to
		self.frm = frm
		self.msg = msg

	def serialize(self):
		return json.dumps(self.__dict__)

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

class Server(socketserver.ThreadingUnixStreamServer):
	def __init__(self, server_address, callback, bind_and_activate=True):
		if not callable(callback):
			callback = lambda x: []

		class IPCHandler(socketserver.BaseRequestHandler):
			def handle(self):
				while True:
					try:
						results = _read_object(self.request)
					except ConnectionClosed as e:
						return
					response = callback(results)
					_write_object(self.request, response)

		self.address_family = socket.AF_INET

		socketserver.TCPServer.__init__(self, addrTuple(server_address), IPCHandler, bind_and_activate)

class Client:
	def __init__(self, server_address, callback):
		self.addr = server_address
		self.callback = callback
		address_family = socket.AF_INET
		self.sock = socket.socket(address_family, socket.SOCK_STREAM)
		self.sock.connect(addrTuple(self.addr))

		self.thread = threading.Thread(target=self.recvLoop, args=(), daemon=True)
		self.thread.start()

	def recvLoop(self):
		while (True):
			message = self.recv()
			self.callback(message)
			time.sleep(0.01) 

	def close(self):
		self.sock.close()
		#self.socketThread.

	def send(self, object):
		_write_object(self.sock, object)

	def recv(self):
		return _read_object(self.sock)
