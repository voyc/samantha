''' echo.py - skill demo '''

import sam.base

class Echo(sam.base.Skill, sam.base.Commander):
	def __init__(self,owner):
		super().__init__(owner)

	# echo on, echo off
	# put mode in user
	# mode = converse
	#    every incoming msg is to be replied to
	# mode = drill
	#    every msg is answer to a question
	
	# also institute a sleep mode
	#    temporarily close switchboard to non admin commands
	#    let sam work only on background tasks
	
	# keep thread list
	#    join to all open threads
	#    temp threads, for one command
	#    permanent threads, like switchboard
	#    status: list threads, etc, how are you?

	def cmd_echo(self,msgin):
		return sam.comm.Message( f'echo: {msgin.msg}')

