''' broca.py - a skill, the art of conversation '''

import sam.base
import sam.grammar
import random

class Broca(sam.base.Skill):
	def __init__(self,owner):
		super().__init__(owner)
		#self.grammar = sam.grammar.Grammar()

	def cmd_converse(self,msgin):
		s = random.choice([
			'What?',
			'I don''t understand',
			'Sorry, I don\'t  understand',
			'Huh?',
			'What do you mean by that?'
		])

		msgout = sam.comm.Message(s)
		return msgout

	def cmd_translate(self,msgin):
		#s =  grammar.translate(msgin.msg)
		s = 'translated'
		msgout = sam.comm.Message(s)
		return msgout
