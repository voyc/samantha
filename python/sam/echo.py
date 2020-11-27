''' echo.py - skill demo '''

import sam.base

class Echo(sam.base.Skill, sam.base.Commander):
	def __init__(self,owner):
		super().__init__(owner)

	def cmd_echo(self,msgin):
		''' echo mode on or off, when on, echo every msg '''
		mode = msgin.mode 
		s = ''
		a = msgin.parse()
		if a[0] == 'echo':
			if a[1] == 'on':
				mode = 'echo'
				s = 'echo on'
			elif a[1] == 'off':
				mode = None
				s = 'echo off'
			else:
				s = ' '.join(a[1:])
		else:
			s = msgin.msg
		msgout = sam.comm.Message(s)
		msgout.mode = mode
		return msgout
