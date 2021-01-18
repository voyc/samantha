''' en.py '''

import sam.lang


class En(sam.lang.Language):
	def __init__(self, dik):
		self.dik = dik

	def broca(self,thot):
		''' outgoing thot to english '''
		s3 = super().broca(thot)
		en = s3
		return en

	def wernicke(self,en):
		''' incoming english to thot ''' 
		s3 = en
		thot = super().wernicke(s3)
		return thot

