# samchat.py  websockets chat server

import asyncio     # websockets is built on asyncio
import websockets
import datetime

from numgen import *

port = 50000
ip = '68.66.224.22'  # a2hosting
ip = '127.0.0.1'     # local, also switch shebang
hostname = 'Sam'
timeout = datetime.timedelta(seconds=120)

clients = {}
recent = datetime.datetime.now()

async def hostinterject(message):
	recent = datetime.datetime.now()
	print(f'{recent} {message}')
	msg = f'{hostname}~{message}'	
	await broadcast(msg)

async def broadcast(msg):
	for usr in clients:
		try:
			await clients[usr].send(msg)
		except:
			pass

async def serveloop(websocket, path):
	global recent
	print(websocket)
	async for message in websocket:
		recent = datetime.datetime.now()
		print(f'{recent} {message}')
		cmd,usr,msg = message.split('~')
		if cmd == 'login':
			clients[usr] = websocket
			reply = f'{hostname}~Welcome, {usr}'	
			await broadcast(reply)
		elif cmd == 'logout':
			del clients[usr]
			reply = f'{hostname}~Goodbye, {usr}'
			await broadcast(reply)
		elif cmd == 'message':
			reply = f'{usr}~{msg}'
			await broadcast(reply)
			rpl = await process(msg)
			if rpl:
				await hostinterject(rpl)

async def wakeup():
	global recent
	while True:
		await asyncio.sleep(30)
		now = datetime.datetime.now()
		diff = now - recent
		if diff > timeout:
			await hostinterject('Are you still here?')
			recent = now

async def process(msg):
	reply = ''
	amsg = await parse(msg)
	if amsg[0] == 'wiki':
		reply = f'Click here for <a href="wiki">wiki</a>'
	elif amsg[0] == 'echo':
		reply = msg[5:]
	elif amsg[0] == 'number':
		reply = translateNumber(amsg[1],'th','word')
	return reply
	
async def parse(s):
	return s.split()

server = websockets.serve(serveloop, ip, port) # create server, wrapping coroutine
event_loop = asyncio.get_event_loop()  # get the scheduler
event_loop.run_until_complete(server)  # make connection, wrapping server object
asyncio.ensure_future(wakeup())
print(f'serving websockets on {ip}:{port}...')
event_loop.run_forever()

