# samhttp.py  ajax webserver

# http.server.HTTPServer is a socketserver.TCPServer subclass
# http.server.BaseHTTPRequestHandler, no handlers
# http.server.SimpleHTTPRequestHandler, includes do_GET and do_HEAD
# python -m http.server 8000 # start server with SimpleHTTPRequestHandler

import http.server
import os

PORT = 8080
IP = '' # in browser, localhost:8080 or 127.0.0.1:8080 or 192.168.1.103:8000
server_address = (IP, PORT)

def processRequest(req,data):
	[path,svc] = os.path.split(req)
	code = 200
	out = ''
	if svc in ['start','stop','resume','home','kill']:
		monad.cortex.command(svc)
	elif svc == 'getwifi':
		out = monad.eyes.getConnection()
	elif svc == 'getstate':
		out = monad.eyes.getState() 
	else:
		code = 403
	return [code,out]

class AjaxServer(http.server.SimpleHTTPRequestHandler):
	#def do_GET(self):
	#	global shtml
	#	code = 200
	#	output = ''
	#	if self.path == '/favicon.ico':
	#		file_contents = open(self.path[1:], 'rb').read()
	#		output = bytes(file_contents)
	#	else:
	#		if self.path == '/':
	#			file_contents = shtml
	#		else:
	#			file_contents = "File not found"
	#			code = 404
	#		output = bytes(file_contents, 'utf-8')

	#	self.send_response(code)
	#	self.send_header("Content-type", "text/html")
	#	self.end_headers()
	#	self.flush_headers()
	#	self.wfile.write(output)

	def do_POST(self):
		length = int(self.headers.get_all('content-length')[0])
		req = self.path
		postin = self.rfile.read(length)
		postout = 'response to ajax call'
		[code,postout] = processRequest(req,postin)
		self.send_response(code)  # 200
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.flush_headers()
		self.wfile.write(postout.encode())

server = http.server.HTTPServer(server_address, AjaxServer)
server.serve_forever()

