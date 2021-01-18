''' lobby.py - manage incoming connections '''

import sam.comm  # used by switchboard
import sam.base  # contains Skill base class

class Lobby(sam.base.Skill):  # do we want a base class Skill ?
	def __init__(self, me):
		super().__init__(me)
		self.translator = Translator(self)
		self.reception = Reception(self)
		self.security = Security(self)
		self.dispatcher = Dispatcher(self)
		self.switchboard = Switchboard(self)
		self.switchboard.listen()
		self.users = {}  # user objects keyed by websocket
		self.conversations = {} # conversation objects keyed by num

	def join(self):
		self.switchboard.socket.join()  # holds daemon open

class Switchboard:
	def __init__(self, lobby):
		self.lobby = lobby

	def onMessage(self,websocket,message):  # callback from server socket
		''' message processing '''
		if websocket not in self.lobby.users.keys():
			# new conversation, message must be "connect" command
			frmuser = sam.user.User() 
			frmuser.token = message.frmtoken
			frmuser.addr = f'{websocket.host}:{websocket.port}'
			message.frmuser = frmuser
			self.lobby.users[websocket] = frmuser
			self.lobby.reception.addConversation(message)
		else:
			frmuser = self.lobby.users[websocket]
			message.frmuser = frmuser

		print(f'recv: {message.toString()}')  # change to broadcast

		clearance = self.lobby.security.check(message)
		# note that clearance refers to the incoming user, not the message

		message.thot = self.lobby.translator.wernicke(message)
		print(f'thot: {message.thot}')

		frmuser.conversation.addMessage(message)

		#replythot = self.lobby.dispatcher.dispatch(message)
		replythot = self.lobby.me.mind.think(frmuser.conversation)

		# 6,7. translate and broadcast the response
		if replythot:
			sreply = self.lobby.translator.broca(replythot)
			reply = sam.comm.Message(sreply)
			print(f'send: {reply.toString()}')  # change to broadcast
		return reply

	def listen(self):
		self.socket = sam.comm.Server()
		self.socket.listen(self.lobby.me.addr, self.onMessage)
		print(f'{self.lobby.me.name} {self.lobby.me.pid} listening on {self.lobby.me.addr}...')

	def close(self):
		self.socket.close()

class Security():
	def __init__(self, lobby):
		self.lobby = lobby

	def check(self,msg):
		''' check token, return clearance '''
		msg.clearance = 0
		if msg.frmtoken and dbisvalidtoken(msg.frmtoken):
			msg.clearance = 1   # 0:anonymous, 1:loggedin, 2:admin, -1:offender
		return (msg.clearance >= 0)

class Account(sam.base.Commander):
	def __init__(self,lobby):
		self.lobby = lobby
		super().__init__(self.lobby.me)

	def cmd_login(self,msgin):
		username = msgin.msg.split(' ')[1]
		msgin.frm = Human(username)
		msgin.frm.token = 'asrf8oaowfe;kdvlkn;4oa9jsf'  # db 
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_logout(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_changeusername(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_changepassword(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_changeemail(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_register(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_unregister(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

class Conversation:
	conversationnum = 1

	def __init__(self,user,host):
		self.members=[]
		self.members.append( host) # [0] = host
		self.members.append( user) # [1] = owner
		user.conversation = self
		self.messages=[]
		Conversation.conversationnum += 1
		self.num = Conversation.conversationnum

	def addMessage(self, message):
		self.messages.append(message)

	def addUser(self,user): 
		self.members.append(user)  # add to this conversation
		user.conversation.removeUser(user)  # remove from previous conversation
		user.conversation = self

	def removeUser(self,user):
		self.members.remove(user)  # gc user
		if len(self.members) == 0:   # if no users in this conversation
			conversations.remove(self)      # gc conversation

class Reception(sam.base.Skill,sam.base.Commander):
	def __init__(self,lobby):
		self.lobby = lobby
		super().__init__(self.lobby.me)

	def addConversation(self, msgin):
		conversation = Conversation(msgin.frmuser,self.lobby.me)
		conversation.addMessage(msgin)
		self.lobby.conversations[conversation.num] = conversation
		return conversation
		
	def cmd_join(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_leave(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

	def cmd_status(self,msgin):
		return Message(msgin.frm, msgin.to, 'ok')

class Dispatcher:
	''' call the skill.method() for the command, the first word in the message '''
	def __init__(self,lobby):
		self.lobby = lobby
		self.cmds = {} # cmd string : skill object
		self.cmdmode = None

	def add(self,cmd,skillobj):
		self.cmds[cmd] = skillobj # object of a class derived from base.Skill

	def dispatch(self,messagein):
		owner = self.lobby.me
		# parse message for incoming command
		cmdin = None
		action = None
		a = messagein.parse()
		if a[0] in owner.cmds:
			cmdin = a[0]
		if len(a) > 1 and a[1] in ['on', 'off']:
			action = a[1]

		# set or clear command mode, and return
		if self.cmdmode:
			if cmdin == self.cmdmode and action == 'off':
				self.cmdmode = None  # clear command mode
				return sam.comm.Message(f'{cmdin} {action}')
		else:
			if cmdin and action == 'on':
				self.cmdmode = cmdin  # set command mode
				return sam.comm.Message(f'{cmdin} {action}')
			
		# command precedence: mode, incoming, "converse"
		cmd = self.cmdmode
		if not cmd: cmd = cmdin
		if not cmd: cmd = 'converse'

		skillobj = owner.cmds[cmd] 
		method = getattr(skillobj, f'cmd_{cmd}')
		messageout = method(messagein)  # execute the command handler	
		return messageout

class Translator:
	'''
	'''
	sameseprefix = ':'

	def __init__(self,lobby):
		self.lobby = lobby
	
	def wernicke(self, message):  # samese to thot
		lang = self.identifyLang(message.msg)
		s3 = self.lobby.me.languages[lang].wernicke(message)
		return s3

	def broca(self, thot):  # thot to samese
		s = str(thot)
		return s

	def identifyLang(self, s):
		lang = 'en'
		firstchar = s[0:1]
		if firstchar == Translator.sameseprefix:
			lang = 's3'
		elif firstchar >= '\u0E00' and firstchar <= '\u0E7F':
			lang = 'th'
		return lang	
