import json

class Message():
	def __init__(self, to='', frm='', msg=''):
		self.to = to
		self.frm = frm
		self.msg = msg

	def serialize(self):
		return json.dumps(self.__dict__)

	def deserialize(self,data):
		self.__dict__ = json.loads(data)

	def print(self):
		print(f'to {self.to}, from {self.frm}: {self.msg}')

msg = Message('sam', 'john', 'login john over')
s = msg.serialize()
print(s)

s = '{"to": "joe", "frm": "sara", "msg": "token abc123" }'

g = Message()
g.deserialize(s)
g.print()

