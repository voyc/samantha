''' gencon.py - generate conversation '''

from datetime import datetime

class Node:
	def __init__(self,word,expr,pos):
		self.word = word
		self.expr = expr
		self.pos = pos
		self.tree = []

	def print(self,work):
		def fn(m,work):
			indent = '\t' * (work['level']-1)
			print(indent, work['level'], m.word, m.pos, m.expr)
		self.process(fn,work,False)

	def process(self,fn,work,bubble=True):
		if 'level' not in work.keys():
			work['level'] = 0
		work['level'] += 1
		if not bubble:
			fn(self,work)  # trickle down (tree after)
		for node in self.tree:
			node.process(fn,work,bubble) # recursive
		if bubble:
			fn(self,work)  # bubble up (tree first)
		work['level'] -= 1

	def copyBranch(self,frm):
		#self.tree = copy.deepcopy(frm.tree)
		self.tree = frm.tree

	def append(self,node):
		self.tree.append(node)

def genq(root):
	def pgenq(node,work):
		if not node.tree:
			work['s'] += node.expr + ' '
	work = {'level':0, 's':''}
	thot.process(pgenq,work)
	work['s'] += thot.currentQuestion
	return work['s']

thot = Node('root','root','s')
thot.timestamp = datetime.now()

subj = Node('subj', 'you', 'n')
verb = Node('verb', 'go', 'v')
thot.append(subj)
thot.append(verb)
thot.currentNode = thot
thot.currentQuestion = 'where'
s = genq(thot)
print(s)

gowhere = Node('where', 'bank', 'n')
verb.append(gowhere)
thot.currentQuestion = 'when'
s = genq(thot)
print(s)

gowhen = Node('when', 'now', 'adv')
verb.append(gowhen)
thot.currentQuestion = 'withwhom'
s = genq(thot)
print(s)

gowith = Node('with', 'gab puan', 'ep')
gowith.append( Node('prep', 'gab', 'p'))
gowith.append( Node('obj', 'puan', 'n'))
verb.append(gowith)
s = genq(thot)
print(s)

thot.currentNode = bank
thot.currentQuestion = 'where'
s = genq(thot)
print(s)

bankwhere = Node('where', 'in the mall', 'ep')
bankwhere.append(Node('prep', 'in', 'p'))
friend = Node('obj', 'mall', 'n')
bankwhere.append(friend)
s = genq(thot)
print(s)

thot.currentNode = friend
thot.currentQuestion = 'whatname'
#genQuest()
#genAnswerList()
#genAnswer()

thot.print({})

