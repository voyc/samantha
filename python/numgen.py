# numgen.py

import re
import random

word = {
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

digit = {
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

magnitude = {
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

wordbreak = ' '


# generate a random number within constraints and within user's vocabulary
def numgen(start=1, end=9999999, interval=1, user=''):
	a = range(start,end,interval)
	b = chooseForUser(a,user)
	return random.choice(b)

def chooseForUser(n,user):
	return n

# translate and format a number
def translateNumber(n,language='th',format='word'):
	n = int(str(n)[0:7])  # int max 7 digits
	la = language  # en or th
	fmt = format   # digit or word

	s = ''      # output string
	st = ''     # output string temp
	t = str(n)  # input string
	nd = len(t) # length of input string
	if fmt == 'digit':
		j = 0
		p = 0
		for j in t:
			d = digit[la][int(j)]
			st += d
			s += d
			p = nd - len(s)
			if p > 0 and (p % 3) == 0:
				s += ','
	elif la == 'en':
		j = 0
		for j in t:
			if len(s):
				s += wordbreak
			s += word[la][int(j)]

	elif la == 'th':
		q = 0
		for j in t:
			if len(s):
				s += wordbreak

			dig = word[la][int(j)]

			q += 1
			p = nd - q
			mag = magnitude[la][p]


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

# test one
testdata = [0,23,546,9263,23400,234120,2370215]
for n in testdata:
	print(translateNumber(n,'en','digit'))
	print(translateNumber(n,'th','digit'))
	print(translateNumber(n,'en','word'))
	print(translateNumber(n,'th','word'))
	print('-')

# test two
testdata = [10,11,12,20,21,22,31,32,33,100,101,102,111,112,121,1000,1001,1010,1011,1021]
for n in testdata:
	s = translateNumber(n, 'th', 'word')
	print(f'{n} : {s}')
