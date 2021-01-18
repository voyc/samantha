''' lang.py - speech to thot to speech '''

import importlib
from sam.mind import Mind, Thot, Claw, Node, Fray, Mod, Glos, Dik
import copy

class Word:
	def __init__(self, s3, pos, seq):
		self.s3 = s3
		self.pos = pos 
		self.seq = seq
	
class Bit:
	''' this is the working bit during translation '''
	def __init__(self):
		self.words = []
		self.thots = []
		self.ndx = -1   # working during getNextWord

	def getNextWord(self):
		self.ndx += 1
		if self.ndx >= len(self.words):
			return None
		return self.words[self.ndx]

class Language:
	''' base class '''
	def __init__(self, me):
		self.me = me

	def broca(self,thot):
		''' thot to s3 '''
		s3 = str(thot)
		return s3

	def wernicke(self,s3):
		bit = Bit()
		pos = []
		tok = s3.split()
		for each in tok:
			p = self.dik.getPos(each)
			pos.append(p)
		for i in range(len(tok)):
			word = Word(tok[i], pos[i], i)
			bit.words.append(word)

		# count by pos, unused
		cnt = {}
		for tag in self.dik.postable:
			cnt[tag] = 0
		for i in range(len(pos)): 
			cnt[pos[i]] += 1 

		# build thots
		for word in bit.words:
			if word.pos == 'noun' or word.pos == 'pron':
				node = Node(word.s3)
				bit.thots.append(node)
			elif word.pos == 'verb':
				claw = Claw()
				claw.verb = word.s3
				bit.thots.append(claw)
			elif word.pos == 'prep':
				fray = Fray()
				fray.lk = word.s3
				bit.thots.append(fray)
			elif word.pos == 'adj' or word.pos == 'adv':
				mod = Mod(word.s3)
				bit.thots.append(mod)

		# combine thots
		thots = copy.deepcopy(bit.thots)
		runaway = 10
		run = 0
		while len(thots) > 1 and run < runaway:
			run += 1
			for i in range( len(thots) - 2, -1, -1):
				thisthot = thots[i]
				nextthot = thots[i+1]
				if isinstance(thisthot,Fray) and isinstance(nextthot,Node):
					thisthot.at = nextthot
					thots.remove( nextthot)
				if isinstance(thisthot,Claw) and isinstance(nextthot,Node):
					thisthot.objek = nextthot
					thots.remove( nextthot)
				if isinstance(thisthot,Claw) and isinstance(nextthot,Mod):
					thisthot.modify = nextthot
					thots.remove( nextthot)
				if isinstance(thisthot,Node) and isinstance(nextthot,Mod):
					thisthot.modify(nextthot)
					thots.remove( nextthot)
				if isinstance(thisthot,Node) and isinstance(nextthot,Claw):
					nextthot.subjek = thisthot
					thots.remove( thisthot)
				if isinstance(thisthot,Claw) and isinstance(nextthot,Fray):
					thisthot.modify( nextthot)
					thots.remove( nextthot)

		bit.thot = thots[0]
		return bit.thot

	@staticmethod
	def load( name, dik):
		''' instantiate a language object '''
		modname = f'sam.translator.{name}'
		mod = importlib.import_module(modname)  # import module
		kls = getattr(mod, name.title())        # get class from module
		obj = kls(dik)                          # instantiate object
		return obj
