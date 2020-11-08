import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	message = 'It works!\n'
	version = 'Python %s\n' % sys.version.split()[0]
	response = '\n'.join([message, version])
	print(environ)
	return [response.encode()]

	# http://wsgi.tutorial.codepoint.net/parsing-the-request-post
	## the environment variable CONTENT_LENGTH may be empty or missing
	#try:
	#	request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	#except (ValueError):
	#	request_body_size = 0

	## When the method is POST the variable will be sent
	## in the HTTP request body which is passed by the WSGI server
	## in the file like wsgi.input environment variable.
	#request_body = environ['wsgi.input'].read(request_body_size)
	#d = parse_qs(request_body)

	##age = d.get('age', [''])[0] # Returns the first age value.
	##hobbies = d.get('hobbies', []) # Returns a list of hobbies.

	### Always escape user input to avoid script injection
	##age = escape(age)
	##hobbies = [escape(hobby) for hobby in hobbies]

	#svc = d.get('svc')[0]
	#svc = escape(svc)

	#if svc == 'login':
	#	rc = login(d)
	#elif svc == 'logout':
	#	rc = logout(d)

	#
	#response_body = html % { # Fill the above html template in
	#	'checked-software': ('', 'checked')['software' in hobbies],
	#	'checked-tunning': ('', 'checked')['tunning' in hobbies],
	#	'age': age or 'Empty',
	#	'hobbies': ', '.join(hobbies or ['No Hobbies?'])
	#}

	#status = '200 OK'

	#response_headers = [
	#	('Content-Type', 'text/html'),
	#	('Content-Length', str(len(response_body)))
	#]

	#start_response(status, response_headers)
	#return [response_body]

#environ = {
#	'REQUEST_URI': '/account/svc/',
#	'PATH_INFO': '/account/svc/',
#	'SCRIPT_NAME': '',
#	'QUERY_STRING': '',
#	'REQUEST_METHOD': 'POST',
#	'SERVER_NAME': 'samantha.voyc.com',
#	'SERVER_PORT': '80',
#	'SERVER_SOFTWARE': 'Apache/2.4.46 (cPanel) OpenSSL/1.1.1g Apache mod_bwlimited/1.4 Phusion_Passenger/5.3.7',
#	'SERVER_PROTOCOL': 'HTTP/1.1',
#	'REMOTE_ADDR': '96.30.109.152',
#	'REMOTE_PORT': '56160',
#	'CONTENT_TYPE': 'application/x-www-form-urlencoded',
#	'CONTENT_LENGTH': '41',
#	'PASSENGER_CONNECT_PASSWORD': 'E1zESA8Y7Aj40YLK',
#	'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/85.0.4183.83 Safari/537.36',
#	'HTTP_ACCEPT': '*/*',
#	'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9',
#	'HTTP_ORIGIN': 'http://samantha.voyc.com',
#	'HTTP_ACCEPT_ENCODING': 'gzip,deflate',
#	'HTTP_HOST': 'samantha.voyc.com',
#	'HTTP_REFERER': 'http://samantha.voyc.com/?page=home',
#	'UNIQUE_ID': 'X5jWytOp2NT4pdEYZnLx0wAAAAE',
#	'SCRIPT_URL': '/account/svc/',
#	'SCRIPT_URI': 'http://samantha.voyc.com/account/svc/',
#	'wsgi.input': <_io.BufferedReader name=4>,
#	'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>,
#	'wsgi.version': (1,0),
#	'wsgi.multithread': False,
#	'wsgi.multiprocess': True,
#	'wsgi.run_once': False,
#	'wsgi.url_scheme': 'http',
#	'passenger.hijack': <function RequestHandler.process_request.<locals>.hijack at 0x2b9af9881200>
#}
