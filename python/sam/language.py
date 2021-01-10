''' language.py - speech to thot to speech '''

#import sam.mind
#import sam.base
#import importlib
#
#class TranslateException(Exception):
#	pass
#
#class Translator(sam.base.Skill):
#	'''
#	'''
#	sameseprefix = ':'
#
#	def __init__(self, me):
#		super().__init__(me)
#		self.mind = sam.mind.Mind()
#		self.mind.load()
#		self.mind.buildGrammar()
#	
#	def wernicke(self, message):  # samese to thot
#		lang = self.identifyLang(message.msg)
#		thot = self.me.languages[lang].wernike(message)
#
#		# identify command
#
#		# match grammar patterns: string to thot
#
#		thot = sam.mind.Claws(w[0], w[1], w[2])
#		return thot
#
#	def broca(self, thot):  # thot to samese
#		s = str(thot)
#		return s
#
#	def identifyLang(self, s):
#		lang = 'en'
#		firstchar = s[0:1]
#		if firstchar >= '\u0E00' and firstchar <= '\u0E7F':
#			lang = 'th'
#		if firstchar == Translator.sameseprefix:
#			lang = 's3'
#		return lang	
