# ipc.py

# https://gist.github.com/dankrause/9607475

import socketserver
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
                    _write_object(self.request, callback(results))

        if isinstance(server_address, str):
            self.address_family = socket.AF_UNIX
        else:
            self.address_family = socket.AF_INET

        socketserver.TCPServer.__init__(self, server_address, IPCHandler, bind_and_activate)

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
