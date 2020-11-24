''' test_modules.py - unit tests of modules '''

import unittest
import sam.user
import sam.comm
import time

class TestModules(unittest.TestCase):
	def test_user(self):
		u = sam.user.User()
		h = sam.user.Human()
		s = sam.user.Sam( 'Lee', 'localhost:7000', 'lobby')
		s.loadSkills()
		self.assertIsInstance(s.skills['lobby'], sam.lobby.Lobby)

	
	def test_comm(self):
		addr = 'localhost:50001'

		messages = []
		s = sam.comm.Server()
		def echo(websocket, message): 
			messages.append(message)
			return ''
		s.listen(addr, echo)

		time.sleep(1)

		c = sam.comm.Client()
		c.connect(addr)
		c.send('hey baby')
	
		time.sleep(1)
		self.assertEqual(messages[0], 'hey baby')

if __name__ == '__main__':
	unittest.main()

