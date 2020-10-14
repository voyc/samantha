# numgen.py

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
def numgen(start, end, interval, user):
	a = range(start,end,interval)
	b = chooseForUser(a,user)
	return choice(b)

# translate and format a number
#	language:, en, th
#	format: digit, words
def translateNumber(n,language,format):
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
		j = 0
		p = 0
		for j in t:
			if len(s):
				s += wordbreak
			p = nd - len(s)

			dig = word[la][int(j)]
			#mag = magnitude[la][p]

			s += dig

			#// exception: trailing zeros
			#if (j == 0 && n > 0) {
			#	dig = mag = '';
			#}

			#// exception: one, หนึ่ง to เอ็ด
			#if (p == 0 && j == 1) {
			#	dig = 'เอ็ด';
			#}

			#// exception: teens
			#if (p == 1 && j == 1) {
			#	dig = mag = '';
			#}

			#// exception: twenties, สอง to ยี่
			#if (p == 1 && j == 2) {
			#	dig = 'ยี่';
			#}

			#s += dig;
			#if (mag.length) {
			#	s += wordbreak;
			#}
			#s += mag;
	return s


testdata = [0,23,23400,234120,237025074,2350973450298]
for n in testdata:
	print(translateNumber(n,'en','digit'))
	print(translateNumber(n,'th','digit'))
	print(translateNumber(n,'en','word'))
	print(translateNumber(n,'th','word'))
