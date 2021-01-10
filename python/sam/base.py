''' base.py - some base classes '''

import importlib

class Skill:
	''' base class for skill classes '''
	''' skillname "lobby" -> module "sam.skill.lobby" -> file "skill/lobby.py" -> class sam.skill.Lobby '''
	def __init__(self, me):
		self.me = me

	@staticmethod
	def load( name, me):
		modname = f'sam.{name}'
		mod = importlib.import_module(modname)  # import module
		kls = getattr(mod, name.title())        # get class from module
		obj = kls(me)                        # instantiate object
		Commander.load(obj,me)

	#	# add cmds to list in dispatcher
	#	for cmd in dir(obj):
	#		if cmd[0:4] == 'cmd_':
	#			cmdname = cmd.split('_')[1]
	#			me.cmds[cmdname] = obj
	#	for obj in dir(obj):
	#		if isinstance(obj, sam.base.Commander): 
	#			for cmd in dir(obj):
	#				if cmd[0:4] == 'cmd_':
	#					cmdname = cmd.split('_')[1]
	#					me.cmds[cmdname] = obj
		return obj

	def join(self):
		pass

class Commander:
	''' base class for a class that contains cmd_x commands '''
	@staticmethod
	def load( obj, me):
		# add cmds to list in dispatcher
		if isinstance(obj, Commander): 
			for cmd in dir(obj):
				if cmd[0:4] == 'cmd_':
					cmdname = cmd.split('_')[1]
					me.cmds[cmdname] = obj
		for mem in obj.__dict__.values():
			if isinstance(mem, Commander): 
				for cmd in dir(mem):
					if cmd[0:4] == 'cmd_':
						cmdname = cmd.split('_')[1]
						me.cmds[cmdname] = mem

class TranslateException(Exception):
	pass

class Language:
	''' base class '''
	def __init__(self, me):
		self.me = me

	def wernicke(self, message):
		''' parse string to thot '''
		pass
		# return sam.mind.Thot()

	def broca(self, thot):
		''' generatee thot to string '''
		pass
		# return s

	@staticmethod
	def load( name, me):
		''' instantiate a language object '''
		modname = f'sam.lang{name}'
		mod = importlib.import_module(modname)  # import module
		kls = getattr(mod, name.title())        # get class from module
		obj = kls() # kls(me)                        # instantiate object
		return obj

class Singleton:
	''' base class, makes derived class a singleton '''
	_instance = None
	def __new__(cls, *args, **kwargs):
		if cls._instance:
			return cls._instance
		else:
			cls._instance = object.__new__(cls, *args, **kwargs)
			return cls._instance

