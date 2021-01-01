''' base.py - some base classes '''

import importlib

class Skill:
	''' base class for skill classes '''
	''' skillname "lobby" -> module "sam.skill.lobby" -> file "skill/lobby.py" -> class sam.skill.Lobby '''
	def __init__(self, me):
		self.me = me

	@staticmethod
	def load( name, owner):
		modname = f'sam.{name}'
		mod = importlib.import_module(modname)  # import module
		kls = getattr(mod, name.title())        # get class from module
		obj = kls(owner)                        # instantiate object

		# add cmds to list in dispatcher
		for cmd in dir(obj):
			if cmd[0:4] == 'cmd_':
				cmdname = cmd.split('_')[1]
				owner.cmds[cmdname] = obj

		return obj

class Commander:
	pass
