# ipcclient.py

# https://gist.github.com/dankrause/9607475

import socket
import struct
import json

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
	g = Message()
	g.deserialize(data)
	return g

def _write_object(sock, object):
	data = object.serialize()
	sock.sendall(struct.pack('!i', len(data) + 4))
	sock.sendall(data.encode())

class Message():
	def __init__(self, to='', frm='', msg=''):
		self.to = to
		self.frm = frm
		self.msg = msg

	def serialize(self):
		return json.dumps(self.__dict__)

	def deserialize(self,data):
		self.__dict__ = json.loads(data)

	def print(self):
		print(f'to {self.to}, from {self.frm}: {self.msg}')

class Client(object):
	def __init__(self, server_address):
		self.addr = server_address
		if isinstance(self.addr, str):
			address_family = socket.AF_UNIX
		else:
			address_family = socket.AF_INET
		self.sock = socket.socket(address_family, socket.SOCK_STREAM)

	def connect(self):
		self.sock.connect(self.addr)

	def close(self):
		self.sock.close()

	def __enter__(self):
		self.connect()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

	def send(self, object):
		_write_object(self.sock, object)
		return _read_object(self.sock)

if __name__ == '__main__':
	server_address = ('localhost', 5795)
	print(['server_address', server_address])
	object = Message('sam', 'john', 'login john pw')
	print( 'Sending object: {}'.format(object))
	with Client(server_address) as client:
		response = client.send(object)
	print( 'Received object: {}'.format(response))
