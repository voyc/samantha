''' numgen.py - module of functions to generate and translate number '''

import re
import random

class Numgen:
	def __init__(self):
		self.word = {
			'en':[ 
				'zero',
				'one',
				'two',
				'three',
				'four',
				'five',
				'six',
				'seven',
				'eight',
				'nine',
			],
			'th':[
				'ศูนย์',
				'หนึ่ง',
				'สอง',
				'สาม',
				'สี่',
				'ห้า',
				'หก',
				'เจ็ด',
				'แปด',
				'เก้า',
			]
		}
		
		self.digit = {
			'en':[
				'0',
				'1',
				'2',
				'3',
				'4',
				'5',
				'6',
				'7',
				'8',
				'9',
			],
			'th':[
				'๐',	
				'๑',	
				'๒',	
				'๓',	
				'๔',	
				'๕',	
				'๖',	
				'๗',	
				'๘',	
				'๙',	
			]
		}
		
		self.magnitude = {
			'en':[
				'', # one
				'', # ten
				'hundred',
				'thousand', 
				'', # ten thousand
				'', # hundred thousand
				'million',
			],
			'th':[
				'',
				'สิบ',
				'ร้อย',
				'พัน',
				'หมื่น',
				'แสน',
				'ล้าน',
			]
		}
		
		self.wordbreak = ' '
	
	
	# generate a random number within constraints and within user's vocabulary
	def gen(self, lo=1, hi=9999999, step=1, user=''):
		numdiglo = len(str(lo))
		numdighi = len(str(hi))
		numdig = random.choice(range(numdiglo,numdighi,1))
		a = range(10**(numdig-1), (10**numdig) - 1, step)
		b = self.chooseForUser(a,user)
		num = random.choice(b)
		return num
	
	def chooseForUser(self, n,user):
		''' process range against user's vocabulary '''
		return n
	
	# translate and format a number
	def translate(self, n,language='th',format='self.word'):
		n = int(str(n)[0:7])  # int max 7 self.digits
		la = language  # en or th
		fmt = format   # self.digit or self.word
	
		s = ''      # output string
		st = ''     # output string temp
		t = str(n)  # input string
		nd = len(t) # length of input string
		if fmt == 'self.digit':
			j = 0
			p = 0
			for j in t:
				d = self.digit[la][int(j)]
				st += d
				s += d
				p = nd - len(s)
				if p > 0 and (p % 3) == 0:
					s += ','
		elif la == 'en':
			j = 0
			for j in t:
				if len(s):
					s += self.wordbreak
				s += self.word[la][int(j)]
	
		elif la == 'th':
			q = 0
			for j in t:
				if len(s):
					s += self.wordbreak
	
				dig = self.word[la][int(j)]
	
				q += 1
				p = nd - q
				mag = self.magnitude[la][p]
	
	
				# exception: trailing and embedded zeros
				if j == '0' and int(n) > 0:
					dig = mag = ''
	
				# exception: leading one
				if j == '1' and q == 1:
					dig = ''
	
				# exception: one, หนึ่ง to เอ็ด
				if p == 0 and j == '1':
					dig = 'เอ็ด'
	
				# exception: teens
				if p == 1 and j == '1':
					dig = ''
	
				# exception: twenties, สอง to ยี่
				if p == 1 and j == '2':
					dig = 'ยี่'
	
				s += dig + ' ' + mag
				s = re.sub(' +',' ', s).strip()
		return s
