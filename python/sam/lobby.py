''' lobby.py - a skill, managing incoming connections '''

import sam.comm
import sam.base

class Lobby(sam.base.Skill):  # do we want a base class Skill() ?
	def __init__(self, me):
		super().__init__(me)
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

		# unique user identified by websocket, stored in users dict 
		if websocket in self.lobby.users.keys():
			frmuser = self.lobby.users[websocket]
		else:
			frmuser = sam.user.Human() 
			frmuser.token = message.frmtoken
			frmuser.addr = f'{websocket.host}:{websocket.port}'
		self.lobby.users[websocket] = frmuser
		message.frmuser = frmuser

		clearance = self.lobby.security.check(message)

		print(f'recv: {message.toString()}') # with cleared flag
		reply = self.lobby.dispatcher.dispatch(message)
		if reply:
			print(f'send: {reply.toString()}')
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

	def add(self,cmd,skillobj):
		self.cmds[cmd] = skillobj # object of a class derived from base.Skill

	def dispatch(self,message):
		owner = self.lobby.me
		cmd = message.msg.split(' ')[0]
		skill = owner.cmds[cmd]
		methname = getattr(skill, f'cmd_{cmd}')
		response = methname(message)	
		return response

