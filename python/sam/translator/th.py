''' th.py '''

import sam.lang
import pythainlp

class Th(sam.lang.Language):
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
		''' outgoing thot to thai '''
		# thot to s3
		s3 = super().broca(thot)

		# s3 to thai
		thwords = []
		for word in s3.split():
			thwords.append(self.gen(word))	
		th = ''.join(thwords)
		return th

	def wernicke(self,th):
		''' incoming thai to thot '''
		# thai to s3
		tok = pythainlp.word_tokenize(th)
		tag = pythainlp.pos_tag(tok)  # says you is verb
		npos = []
		for i in range(len(tag)): 
			npos.append(tag[i][1])

		s3words = []
		for each in tok:
			w = self.parse(each)
			s3words.append(w)
		s3 = ' '.join(s3words)

		# s3 to thot
		thot = super().wernicke(s3)
		return thot

	def gen(self,s3):
		th = ''
		try: 
			th = self.s3[s3]
		except:
			print(f'Cannot find Thai translation for s3 word: {s3}')
		return th

	def parse(self,th):
		s3 = ''
		try:
			s3 = self.th[th]
		except:
			print(f'Cannot find s3 translation for Thai word: {th}')
		return s3

