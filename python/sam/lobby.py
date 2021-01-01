''' lobby.py - manage incoming connections '''

import sam.comm
import sam.base
import sam.language

class Lobby(sam.base.Skill):  # do we want a base class Skill() ?
	def __init__(self, me):
		super().__init__(me)
		self.language = sam.language.Language(self)
		self.reception = Reception(self)
		self.security = Security(self)
		self.dispatcher = Dispatcher(self)
		self.switchboard = Switchboard(self)
		self.switchboard.listen()
		self.users = {}

	def join(self):
		self.switchboard.socket.join()  # obsolete?

class Switchboard:
	def __init__(self, lobby):
		self.lobby = lobby

	def onMessage(self,websocket,message):  # callback from server socket
		''' message processing '''
		# 1. unique user identified by websocket, stored in users dict 
		if websocket in self.lobby.users.keys():
			frmuser = self.lobby.users[websocket]
		else:
			frmuser = sam.user.Human() 
			frmuser.token = message.frmtoken
			frmuser.addr = f'{websocket.host}:{websocket.port}'
		self.lobby.users[websocket] = frmuser
		message.frmuser = frmuser

		# 2. security, check token
		clearance = self.lobby.security.check(message)

		# 3. translate into thot
		thot = self.lobby.language.parse(message)
		message.thot = thot

		# 4. broadcast incoming message to group
		print(f'recv: {message.toString()}')  # change to broadcast

		# 5. disppatch, ie. think and respond
		newthot = self.lobby.dispatcher.dispatch(message)

		# 6,7. translate and broadcast the response
		if newthot:
			sreply = self.lobby.language.generate(newthot)
			reply = sam.comm.Message(sreply)
			print(f'send: {reply.toString()}')  # change to broadcast
		return reply

	def listen(self):
		self.socket = sam.comm.Server()
		self.socket.listen(self.lobby.me.addr, self.onMessage)
		print(f'switchboard listening on {self.lobby.me.addr}...')

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

class Group:
	def __init__(self,user):
		global groupnum
		self.owner = user
		user.group = self
		self.members=[self.owner]
		self.invitees=[]
		self.messages=[]
		groupnum += 1
		self.num = groupnum
		groups.append(self)

	def addUser(self,user): 
		self.members.append(user)  # add to this group
		user.group.removeUser(user)  # remove from previous group
		user.group = self

	def removeUser(self,user):
		self.members.remove(user)  # gc user
		if len(self.members) == 0:   # if no users in this group
			groups.remove(self)      # gc group

class Reception(sam.base.Skill):
	def __init__(self,lobby):
		self.lobby = lobby
		super().__init__(self.lobby.me)
		

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
