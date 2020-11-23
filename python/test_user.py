''' test_user.py - unittest of user module '''

import sam.user

def test_constructors():
	u = sam.user.User()
	h = sam.user.Human()
	s = sam.user.Sam( 'Lee', 'localhost:7000', 'lobby,translate')
	s.loadSkills()
	print(s.skills['lobby'])

test_constructors()

