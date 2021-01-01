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

	def think(self):
		'''
		current thought
		previous thought
		priority of open thoughts

		need to
			answer question
			ask question
			make comment
			protocol
		need to 
			initiate
			respond
		need to 
			switch subject
			switch thot

		save message in memory
			along with thot?
		save thots separate from message?
		save thot, with messages attached
		message is often a partial thot, maybe just a modifier
			should the partial be done in translation?
			is it different between english and thai?
		
		John go where?
		where are you going?
			bank
			John go bank
			I go to bank

		John go
		John go where
		John go where bank
		John go :
		bank: add to previou
		
		

		'''

	def cmd_converse(self,msgin):
		notunderstand = [
			'What?',
			'I don''t understand',
			'Sorry, I don\'t  understand',
			'Huh?',
			'What do you mean by that?'
		]
		s = random.choice(notunderstand)
		msgout = sam.comm.Message(s)

		s = msgin.thot.subjek.word
		msgout = sam.comm.Message(s)

		msgout = sam.mind.Claws('Sam', 'go', 'where')
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
