''' echo.py - skill demo '''

import sam.base

class Echo(sam.base.Skill, sam.base.Commander):
	def __init__(self,owner):
		super().__init__(owner)

	def cmd_echo(self,msgin):
		msgout = sam.comm.Message(f'{msgin.msg}')
		return msgout
