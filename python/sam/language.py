''' language.py - speech to thot to speech '''

import sam.mind

class TranslateException(Exception):
	pass

class Language():
	''' base class '''
	def wernicke(self, message):
		''' parse string to thot '''
		thot = sam.mind.Thot()
		return thot

	def broca(self, thot):
		''' generatee thot to string '''
		s = ''
		return s

class Translate():
	'''
	'''
	sameseprefix = ':'

	def __init__(self, me):
		super().__init__(me)
		self.mind = sam.mind.Mind()
		self.mind.load()
		self.mind.buildGrammar()
		self.languagenames = 's3,en,th'
		self.languages = {}
		self.loadLanguages()
	
	def wernicke(self, message):  # samese to thot
		lang = self.identifyLang(message.msg)
		thot = self.languages[lang].wernike(message)

		# identify command

		# match grammar patterns: string to thot

		thot = sam.mind.Claws(w[0], w[1], w[2])
		return thot

	def broca(self, thot):  # thot to samese
		s = str(thot)
		return s

	def identifyLang(self, s):
		lang = 'en'
		firstchar = message.msg[0:1]
		if firstchar >= '\u0E00' && firstchar <= '\u0E7F':
			lang = 'th'
		if firstchar == Language.sameseprefix:
			lang = 's3'
		return lang	

	def loadLanguages(self):
		for name in self.languagenames:
			self.languages[name] = self.loadLanguage(name)	

	@staticmethod
	def loadLanguage( name):
		modname = f'sam.lang{name}'
		mod = importlib.import_module(modname)  # import module
		kls = getattr(mod, name.title())        # get class from module
		obj = kls(owner)                        # instantiate object
		return obj

