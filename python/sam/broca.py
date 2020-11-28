''' broca.py - a skill, the art of conversation '''

import sam.base
import sam.grammar
import sam.grammar.grammar as grammar
import sam.grammar.numgen as numgen
import random


class Broca(sam.base.Skill):
	def __init__(self,owner):
		super().__init__(owner)
		grammar.setupSemantics()

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

	def cmd_number(self,msgin):
		s =  numgen.gen()
		msgout = sam.comm.Message(s)
		return msgout

	def cmd_sentence(self,msgin):
		target = ''
		a = msgin.msg.split(' ')

		if len(a) > 1:
			target = a[1]

		sen = grammar.sengen('คะ')
		msgout = sam.comm.Message(sen)
		return msgout

