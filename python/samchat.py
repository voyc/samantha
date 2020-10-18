# samchat.py  websockets chat server

import asyncio     # websockets is built on asyncio
import websockets
import datetime
import sys
import socket   # used only to find hostname
import random   # used for generating userid

from numgen import *

port = 50000
ip = '68.66.224.22'  # a2hosting
if socket.gethostname() == 'RacerSwift':
	ip = '127.0.0.1'

hostname = 'Sam'
timeout = datetime.timedelta(seconds=120)
wakeupinterval = 30

def now():
	return datetime.datetime.now()

class User:
	def __init__(self,token,name,websocket):
		self.token = token
		self.name = name
		self.websocket = websocket
		self.group = False
		if websocket:
			users[websocket] = self

	def logout(self):
		account.logout(self.token)
		self.group.removeUser(self)

	async def send(self,msg):
		await self.websocket.send(msg)

class Group:
	def __init__(self,user):
		self.owner = user
		user.group = self
		self.users=[self.owner]
		self.invitees=[]
		self.messages=[]
		groups.append(self)

	def addUser(self,user): 
		self.users.append(user)  # add to this group
		user.group.remove(user)  # remove from previous group
		self.messages.append[Message(user,'join')]

	def removeUser(self,user):
		self.users.remove(user)  # gc user
		if len(self.users) == 0:   # if no users in this group
			groups.remove(self)      # gc group

class Message:
	def __init__(self,to,frm,msg):
		self.to = to
		self.frm = frm  # (from is a python reserved word)
		self.msg = msg
		self.group = self.frm.group if self.frm != host else self.to.group
		self.group.messages.append(self)
		self.timestamp=now()

	def compose(self):
		return f'{self.frm.name}~{self.msg}'

	async def broadcast(self,all=False):
		s = self.compose()
		if all:
			for user in users.values():
				await user.send(s)
		else:
			for user in self.group.users:
				await user.send(s)

class Broca:
	def parse(self,message):
		s = message.split()
		verb = s[0]
		words = s[1:]
		return [verb,words]

	def process(self,message): 
		reply = False
		verb,words = self.parse(message.msg)
		if verb == 'echo':
			s = ' '.join(words)
			reply = Message(message.frm,host,s)

		elif verb == 'number':
			if len(words) > 1:
				n = words[0]
			else:
				n = numgen()
			s = translateNumber(n,'th','word')
			reply = Message(message.frm,host,s)

		elif verb == 'wiki':
			reply = Message(message.frm,host,f'Click here for <a href="wiki">wiki</a>')

		else:
			reply = grammar.process(username,verb,words)

		return reply

class Grammar:
	def process(self,username,verb,words):
		if verb == 'wiki':
			reply = wiki()

		elif verb == 'echo':
			pass

		elif verb == 'translate':
			pass

		elif verb == 'drill':
			pass

class Account:
	def login(self,uname,pw):
		token = random.randrange(1000)
		return token

# thread of websocket server
async def serveloop(websocket, path):
	print(websocket)
	async for message in websocket:
		cmd,uname,msg = message.split('~')
		if cmd == 'login':
			pw = msg
			token = account.login(uname,pw)
			if (token):
				user = User(token,uname,websocket)
				group = Group(user)
				msgin = Message(host,user,'login')
				msgout = Message(user,host,f'welcome, {user.name}')
				await msgout.broadcast()
			else:
				msg = f'{host.name}~Sorry.  Login failed.'
				await websocket.send(msg)

		elif cmd == 'message':
			verb,words = broca.parse(msg)
			user = users[websocket]
			print(verb)
			if verb  == 'logout':
				rmessage = grammar(verb,words,message.to,message.frm)
				reply = Message(message.frm,message.to,replymessage)
				reply.broadcast()	
				message.frm.logout()

			elif verb == 'invite':		
				invitation = Message(host,user,'Join me') 
				print(users)
				print('------------')
				await invitation.broadcast(True)

			elif verb == 'join':		
				joinee = findUserByName(words[0])
				print(joinee.name)
				group = joinee.group.addUser(user)
				reply = Message(user,host,f'Welcome to the group, {user.name}')
				await reply.broadcast()

			elif verb == 'leave':		
				pass

			else:
				msgin = Message(host,user,msg)
				await msgin.broadcast()
				rpl = broca.process(msgin)
				await rpl.broadcast()
		else:
			log('invalid cmd')

# look at timestamp on last message in each group
async def wakeup():
	while True:
		await asyncio.sleep(wakeupinterval)
		now = datetime.datetime.now()
		for group in groups:
			recent = group.messages[-1].timestamp
			diff = now - recent
			if diff > timeout:
				msg = Message(group.owner,host,'Are you still here?')
				await msg.broadcast()

def findUserByName(name):
	r = False;
	for user in users.values():
		if user.name == name:
			r = user
			break;
	return r

broca = Broca()
grammar = Grammar()
account = Account()
groups = []
users ={} 
host = User(False,'Sam',False)

server = websockets.serve(serveloop, ip, port) # create server, wrapping coroutine
event_loop = asyncio.get_event_loop()  # get the scheduler
event_loop.run_until_complete(server)  # make connection, wrapping server object
asyncio.ensure_future(wakeup())
print(f'serving websockets on {ip}:{port}...')
event_loop.run_forever()

