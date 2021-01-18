''' test_modules.py - unit tests of modules '''

import unittest

class TestModules(unittest.TestCase):
	def test_user_constructor(self):
		import sam.user
		u = sam.user.User()
		h = sam.user.Human()
		s = sam.user.Sam()
		self.assertEqual(u.name, '')

	def xtest_user_skill(self):
		import sam.user
		# each Sam object must be instantiated in a separate process  !!
		s = sam.user.Sam( 'Lee', 'localhost:7000', 'lobby')
		self.assertIsInstance(s.skills['lobby'], sam.lobby.Lobby)

	def xtest_comm(self):
		import sam.comm
		import time
		addr = 'localhost:50001'

		messages = []
		s = sam.comm.Server()
		def echo(websocket, message): 
			messages.append(message)
			return sam.comm.Message('ok')
		s.listen(addr, echo)

		time.sleep(1)

		c = sam.comm.Client()
		c.connect(addr)
		c.send(sam.comm.Message('hey baby'))
	
		time.sleep(1)
		self.assertEqual(messages[0].msg, 'hey baby')

	def test_grammar_numgen(self):
		import sam.grammar.numgen as ngen
		x = ngen.gen(500,600,50 )
		self.assertIn( x, [500,550,600])

		self.assertEqual( ngen.translate(0,'th','word'), 'ศูนย์')
		self.assertEqual( ngen.translate(23,'th','word'), 'ยี่ สิบ สาม')
		self.assertEqual( ngen.translate(546,'th','word'), 'ห้า ร้อย สี่ สิบ หก')
		self.assertEqual( ngen.translate(9263,'th','word'), 'เก้า พัน สอง ร้อย หก สิบ สาม')
		self.assertEqual( ngen.translate(23400,'th','word'), 'สอง หมื่น สาม พัน สี่ ร้อย')
		self.assertEqual( ngen.translate(234120,'th','word'), 'สอง แสน สาม หมื่น สี่ พัน หนึ่ง ร้อย ยี่ สิบ')
		self.assertEqual( ngen.translate(2370215,'th','word'), 'สอง ล้าน สาม แสน เจ็ด หมื่น สอง ร้อย สิบ ห้า')
		self.assertEqual( ngen.translate(10,'th','word'), 'สิบ')
		self.assertEqual( ngen.translate(11,'th','word'), 'สิบ เอ็ด')
		self.assertEqual( ngen.translate(12,'th','word'), 'สิบ สอง')
		self.assertEqual( ngen.translate(20,'th','word'), 'ยี่ สิบ')
		self.assertEqual( ngen.translate(21,'th','word'), 'ยี่ สิบ เอ็ด')
		self.assertEqual( ngen.translate(22,'th','word'), 'ยี่ สิบ สอง')
		self.assertEqual( ngen.translate(31,'th','word'), 'สาม สิบ เอ็ด')
		self.assertEqual( ngen.translate(32,'th','word'), 'สาม สิบ สอง')
		self.assertEqual( ngen.translate(33,'th','word'), 'สาม สิบ สาม')
		self.assertEqual( ngen.translate(100,'th','word'), 'ร้อย')
		self.assertEqual( ngen.translate(101,'th','word'), 'ร้อย เอ็ด')
		self.assertEqual( ngen.translate(102,'th','word'), 'ร้อย สอง')
		self.assertEqual( ngen.translate(111,'th','word'), 'ร้อย สิบ เอ็ด')
		self.assertEqual( ngen.translate(112,'th','word'), 'ร้อย สิบ สอง')
		self.assertEqual( ngen.translate(121,'th','word'), 'ร้อย ยี่ สิบ เอ็ด')
		self.assertEqual( ngen.translate(1000,'th','word'), 'พัน')
		self.assertEqual( ngen.translate(1001,'th','word'), 'พัน เอ็ด')
		self.assertEqual( ngen.translate(1010,'th','word'), 'พัน สิบ')
		self.assertEqual( ngen.translate(1011,'th','word'), 'พัน สิบ เอ็ด')
		self.assertEqual( ngen.translate(1021,'th','word'), 'พัน ยี่ สิบ เอ็ด')

	def test_grammar_parse(self):
		import sam.grammar.grammar as grammar

		test1 = 'hoo bloody {[xyc 123 45]} [bafs [x1 s2 x3] $num(1,5,1) fjlk] {@quest} {not} [sa dfj] hah'
		tree,ndx = grammar.parseExpr(test1)
		self.assertEqual( ndx, 88)

		test2 = '$expr(hoo bloody $opt($list(xyc 123 45)) $list(bafs $list(x1 s2 x3) $static(at the farm) $num(1,5,1) fjlk) $opt(@quest) $opt(not) $list(sa dfj) hah)'
		tree,ndx = grammar.parseExpr(test2)
		self.assertEqual( ndx, 148)

		grammar.setupSemantics()
		self.assertIsInstance(grammar.semantics['@not'].tree[0], grammar.Node)

	def test_grammar_sengen(self):
		import sam.grammar.grammar as grammar
		grammar.setupSemantics()
		sen = grammar.sengen('คะ')
		self.assertGreater(len(sen.split(' ')), 0)

	def test_grammar_translate(self):
		pass

	def test_grammar_vocab(self):
		pass

	def test_singleton(self):
		import sam.base
		
		class Martha():
			def __init__(self):
				self.x = 'xyz'
		
		class George(sam.base.Singleton,Martha):
			def __init__(self):
				if 'y' in dir(self): return # do init only once
				super().__init__()
				self.y = 123
	
		sa = George()
		sa.y = 456
		sb = George()
		self.assertEqual( sb.x, 'xyz')
		self.assertEqual( sb.y, 456)

	def test_dik(self):
		import sam.mind
		dik = sam.mind.Dik()	
		dik.load()	
		glos = dik.get('person')
		self.assertEqual( glos.th, 'คน')

	def test_thai(self):
		import sam.mind
		mind = sam.mind.Mind()
		mind.setup(None)
		import sam.langth
		langth = sam.langth.Th(mind.dik)

		th = 'คุณไปทีบ้านของเพื่อนของคุณ' # 'you go to house of friend of you'
		thot = langth.wernicke(th)
		st = langth.broca(thot)
		self.assertEqual( st, th)

		th = 'ทำไมคุณทำงานกับคอมพิวเตอร์' # 'why you work on computer'
		th = 'คุณทำงานกับคอมพิวเตอร์'  # 'you work on computer'
		thot = langth.wernicke(th)
		st = langth.broca(thot)
		self.assertEqual( st, th)

if __name__ == '__main__':
	unittest.main()

