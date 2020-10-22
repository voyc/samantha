# grammar.py

import re

ssfilename = 'syntacticstructures.txt'
scfilename = 'semanticconventions.txt'

semantics = {} # working memory structure
sentences = [] # output of every call to sengen

class Node:
	def __init__(self,name,pos=None,expr=None,lvl=0,tree=[],list=[]):
		self.name = name
		self.pos = pos
		self.expr = expr
		self.lvl = lvl
		self.tree = tree
		self.list = list
	def print(self):
		s = ''
		for i in range(0,self.lvl):
			s += '\t'
		print(f'{s}{self.name}',self.pos,self.expr,self.lvl,self.tree)

# build working memory object from text file
def buildSemantics():
	# subfunction: resolve nested lists in one pat
	def resolveNestedLists(pat):
		newpat = pat
		ndx = pat.find('$list')
		while pos >= 0:
			m = findClose(pat,ndx)
			funcs.append(m)
			pos = pat.find('$list',pos+5)
		# resolve nested lists
		newfuncs = []
		pe = -1
		for f in funcs:
			pat = f['pat']
			b = int(f['pos'])
			e = int(f['close'])
			if e < pe:
				b2 = b + len(f['cmd'])
				e2 = e + 1
				newpat = pat[0:b] + pat[b2,e] + pat[e2:]
			else:
				newfuncs.append(f)
				pe = e
		return newpat	
		

	# subfunction: scan a pattern and return a list of functions
	def findFuncs(pat):
		# find closing paren
		def findClose(s,pos):
			m = re.search(r'\$(.*?)\(',s[pos:])
			cmd = m.group(1)
			start = pos + len(cmd) + 2
			n = 1
			max = 1
			for i in range(start,len(s),1):
				if s[i:i+1] == '(':
					n += 1
					max += 1  # error: does not distinguish between nested and consecutive
				if s[i:i+1] == ')':
					n -= 1
				if n == 0:
					return {
						'pos':pos,
						'close':i,
						'lvl':max,
						'cmd':cmd
					}
	
		# find all the functions in the input pattern
		funcs = []
		pos = pat.find('$')
		while pos >= 0:
			m = findClose(pat,pos)
			funcs.append(m)
			pos = pat.find('$',pos+1)
	
		# functions can be nested. sort so the inside functions are executed first.
		#funcs.sort(key=lambda x: x.get('lvl'));


		# add s and t to each func 
		#for f in funcs:
		#	f['s'] = f['pat'][f['pos']:f['pos']+f['close']+1]
		#	f['t'] = f['pat'][f['pos']+len(f['cmd'])+2:f['pos']+len(f['cmd'])+2+f['close']]
		return funcs

	# subfunction: recursive parse of expr string into tree 
	def parse(expr,lvl=1):
		tree = []
		list = []
		ndx = 0
		name = -1 
		cmd = -1 
		word = -1
		#for i in range(0,len(expr)):
		max = len(expr)
		i = 0
		while i < max:
			t = expr[i:i+1]
			print(lvl, i, t)
			if t in ' )':
				if name >= 0:
					tree.append(Node(expr[name:i], lvl=lvl, list=list))
					print('name',expr[name:i])
					name = -1
				else:
					list.append(expr[word:i])
					print('word',expr[word:i])
					word = i
			elif t == '@':
				name = i
			elif t == '$':
				cmd = i
			elif t == '(':
				if cmd >= 0:
					subtree,ndx = parse(expr[i+1:],lvl+1)
					if cmd >= 0:
						tree.append(Node(expr[cmd:i], lvl=lvl, expr=expr[cmd:ndx], list=list))
					tree.extend(subtree)
					i += ndx
			i += 1
		return tree,i
			
		
	# scan the semantics text file, and build a dictionary of objects, one line => one object
	sc = {}
	textlines = open(scfilename,'r').readlines()
	for line in textlines:
		# skip comments and empty lines
		w = line.strip()
		if w[0:1] == '#':
			continue
		if len(w) == 0:
			continue

		# break line into name, pos, expr 
		m = re.match(r'(.*) (@.*) > (.*)',w);
		if m:
			name = m.group(2)
			pos = m.group(1)
			expr = m.group(3)
		else:
			print('no match')
		
		# replace [] with $list()
		expr = re.sub(r'\[', '$list(', expr);
		expr = re.sub(r'\]', ')', expr);
	
		# replace {} with $optional()
		expr = re.sub(r'\{', '$optional(', expr);
		expr = re.sub(r'\}', ')', expr);
	
		tree,ndx = parse(f'$expr({expr})')

		sc[name] = Node(name,pos,expr,1,tree)
	return sc	

	def sub(m):
		#print(m.group(1))
		return sc[m.group(1)]['pat']

	# resolve names 
	for name in sc:
		pat = sc[name]['pat']
		sc[name]['pat'] = re.sub(r'(\@[a-zA-Z0-9]*)',sub,pat)
		#m = re.match(r'(\@[a-zA-Z0-9]*)',pat)
		#print(pat)
		#print(m)

	# resolve all nested lists 
	for name in sc:
		pat = sc[name]['pat']
		sc[name]['pat'] = resolveNestedLists(pat)

	# find the functions within each pattern
	for name in sc:
		pat = sc[name]['pat']
		sc[name]['funcs'] = findFuncs(pat)

	return sc

# for testing only
def printSemantics():
	for node in semantics.values():
		#print(f'{node.name} : {node.pos} : {node.expr}')
		print(node.name,node.pos,node.expr,node.list)
		for m in node.tree:
			m.print()

def printSentences():
	for sen in sentences:
		print(f'{sen}\n\n')

def gensen(opt):
	options = {
		'count': 1,
		'pattern': [],
		'target': [],
		'targetOnly': False,
		'masteredOnly': False,
		'shuffle': True,
		'rebuild': False,
	}
	if opt:
		for key in opt:
			options[key] = opt[key]

	# input f: pos,close,lvl,cmd,s,t
	def callFunction(f): 
		r = ''
		a = f['t']
		print(f)
		print('\n')
		fname = f['cmd']
		params = a.split(',')
		if fname == 'number':
			pass
			#args = [];
			#for (var i=0; i<params.length; i++) {
			#	args.push(parseInt(params[i]));
			#r += voyc.genNumber.apply(this, args);
		elif  fname == 'list':
			pass
			#r += this.selectFromList(a);
		elif fname == 'optional':
			pass
			#if (this.target.includes(a) || Math.random() < .5) {
			#	r += a;
		return r

	# generate sentences from each semantic (name,pos,pat,funcs)
	sentens = []
	for name in semantics:
		if len(options['pattern']) > 0 and name in options['pattern']:
			continue 
		pos = semantics[name]['pos']
		if pos != 'sentence':
			continue
		pat = semantics[name]['pat']
		funcs = semantics[name]['funcs']

		# resolve each function to a single word
		for f in funcs:
			sen = pat
			s = sen[f['pos']:f['pos']+f['close']+1]
			t = sen[f['pos']+len(f['cmd'])+2:f['pos']+len(f['cmd'])+2+f['close']]
			f['s'] = s
			f['t'] = t
			r = callFunction(f)
			sen = sen.replace(s,r)
			#var diff = s.length - r.length;
			#for (var j=0; j<funcs.length; j++) {
			#	if (j > i) {
			#		var t = funcs[j];
			#		if (t.pos > f.pos) {
			#			t.pos -= diff;
			#		if (t.close > f.pos) {
			#			t.close -= diff;
			sentens.append(sen)
	return sentens

semantics = buildSemantics()
printSemantics()
#sentences = gensen({'count':100})
#printSentences()


