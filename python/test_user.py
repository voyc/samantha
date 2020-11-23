''' test_user.py - unittest of user module '''

import unittest
import sam.user

class TestUser(unittest.TestCase):
	def test_constructors(self):
		u = sam.user.User()
		h = sam.user.Human()
		s = sam.user.Sam( 'Lee', 'localhost:7000', 'lobby')
		s.loadSkills()
		self.assertIsInstance(s.skills['lobby'], sam.lobby.Lobby)

if __name__ == '__main__':
	unittest.main()

