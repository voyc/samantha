''' langth.py '''

import copy
import sam.base
from sam.mind import Mind, Thot, Claw, Node, Fray, Mod, Glos, Dik

import pythainlp

class Word:
	def __init__(self, word, s3, pos, seq):
		self.word = word
		self.s3 = s3
		self.pos = pos 
		self.seq = seq
	
class Bit:
	''' this is the working bit during translation '''
	def __init__(self, org):
		self.org = org  # original input string
		self.words = []
		self.thots = []
		self.ndx = -1   # working during getNextWord

	def getNextWord(self):
		self.ndx += 1
		if self.ndx >= len(self.tok):
			return None
		return Word(self.s3[self.ndx], self.tag[self.ndx], self.ndx)

class Th(sam.base.Language):
	#def __init__(self, me):
	#	super().__init__(me)
	def __init__(self, dik):
		self.dik = dik
		self.th = {}
		self.s3 = {}
		self.setup()

	def setup(self):
		def one(glos):
			self.s3[glos.word] = glos.th
			self.th[glos.th] = glos.word
		self.dik.iterate(one)

	def broca(self,thot):
		''' translate interal thot to outgoing thai string '''
		s3 = str(thot)
		thwords = []
		for word in s3.split():
			thwords.append(self.genWord(word))	
		th = ''.join(thwords)
		return th

	def wernicke(self,th):
		''' translate incoming thai string to thot '''
		# translate word for word thai to s3, and tag by pos
		tok = pythainlp.word_tokenize(th)
		tag = pythainlp.pos_tag(tok)  # says you is verb
		npos = []
		for i in range(len(tag)): 
			npos.append(tag[i][1])

		s3 = []
		pos = []
		for each in tok:
			w = self.parseWord(each)
			p = self.dik.getPos(w)
			s3.append(w)
			pos.append(p)

		bit = Bit(th)
		for i in range(len(tok)):
			word = Word(tok[i], s3[i], pos[i], i)
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

	def genWord(self,s3):
		th = ''
		try: 
			th = self.s3[s3]
		except:
			print(f'Cannot find Thai translation for s3 word: {s3}')
		return th

	def parseWord(self,th):
		s3 = ''
		try:
			s3 = self.th[th]
		except:
			print(f'Cannot find s3 translation for Thai word: {th}')
		return s3

if __name__ == '__main__':
	tra = Translate()
	print(tra.getThaiWord('month'))
	print(tra.getEngWord('เดือน'))
	print(tra.getThai('Nid eat food where restaurant next month'))
	print(tra.getEng('นิด กิน อาหาร ที่ไหน ร้านอาหาร ต่อไป เดือน'))

