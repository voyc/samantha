''' memtxt.py - one function, init memory from prelearned thots included in dna '''

memtxt = [
	'you go (where) to house of friend of you (why) to pickup food',
	'Sam go to house of friend of Sam to deliver food',
	'John go to house of friend of John to eat food',
	'Naiyana go to Bangkok to visit',
	'Sam go to Chiang Mai for vacation',
	'John go to Pai to go to embassy',
	'John go to bank to get money',
	'John go to coffeeshop to drink coffee',
	'Sam go to coffeeshop to eat breakfast',
	'Juan go to coffeeshop to meet friend',

	def work(who, where, whyv, whyo=None):
		Claw(who, 'go').modify('where', where).modify('why', Claw(who, whyv, whyo))

	'John go to resaurant to eat food',
	
	work('John', 'restaurant', 'eat', 'food')
	work('Sam', 'restaurant', 'meet', 'friend')
	work('Naiyana', 'salon', 'wash', 'hair')
	work('Juan', 'salon', 'cut', 'hair')
	work('John', 'salon', 'get', 'pedicure')
	work('Sam', 'salon', 'get', 'manicure')
	work('Sam', 'market', 'buy', 'food')
	work('Naiyana', 'mall', 'shop')
	work('Juan', 'pharmacy', 'buy', 'medicine')
	work('Juan', 'cinema', 'watch', 'movie')
	work('Sam', 'doctor', 'get', 'checkup')
	work('Juan', 'doctor', 'fix', 'headache')
	work('Naiyana', 'doctor', 'test', 'covid')
	work('you', 'hospital', 'visit', 'friend')
	work('I', 'clinic', 'see', 'doctor')
	work('Sam', 'clinic', 'see', 'dentist')
	work('Sam', 'dentist', 'clean', 'teeth')
	work('Naiyana', 'dentist', 'get', 'filling')
	work('John', 'dentist', 'get', 'whitening')
	work('Juan', 'dentist', 'fix', 'toothache')
	work('you', 'dentist', 'remove', 'tooth')
	work('I', 'dentist', 'get', 'braces')
	
	def work(who, which, period):
		Claw(who, 'go').modify('when', Node(period).modify('which', which))
	
	work('Sam', 'this', 'morning') 
	work('Joe', 'this', 'afternoon') 
	work('Nid', 'this', 'evening') 
	work('Nui', 'last', 'week') 
	work('Sam', 'this', 'week') 
	work('Joe', 'next', 'week') 
	work('Nid', 'last', 'month') 
	work('Nui', 'this', 'month') 
	work('Sam', 'next', 'month') 
	work('Joe', 'last', 'year') 
	work('Nid', 'this', 'year') 
	work('Nui', 'next', 'year') 

	Claw('Nui', 'go').modify('when', 'now')
	Claw('Sam', 'go').modify('when', 'yesterday')
	Claw('Joe', 'go').modify('when', 'today')
	Claw('Nid', 'go').modify('when', 'tomorrow')

	# where and how: local vs distant destinations and mode of travel
	def work(who, where, how):
		Claw(who, 'go').modify('where', where).modify('how', how)
	
	work('Nui', 'Bangkok', 'train') 
	work('Nid', 'Chiang_Mai', 'bus') 
	work('Joe', 'Udon_Thani', 'airplane') 
	work('Sam', 'Koh_Samui', 'ship') 
	
	work('Joe', 'bank'      , 'car')      
	work('Nid', 'coffeeshop', 'Grab')    
	work('Nui', 'restaurant', 'taxi')    
	work('Sam', 'salon'     , 'citybus')     
	work('Joe', 'market'    , 'songtaew')
	work('Nid', 'mall'      , 'tuktuk')       
		     
	Claw('Sam', 'go').modify('where', 'dentist').modify('how', 'run')
	Claw('Joe', 'go').modify('where', 'clinic').modify('how', 'walk')

	def work(who, where, how):
		Claw(who, 'go').modify('where', where).modify('how', Claw('by', how))
	
	# you do what?

	Claw('Sam', 'eat', 'rice')
	Claw('Joe', 'cook', 'food')
	Claw('Nid', 'brew', 'coffee')
	Claw('Nui', 'brew', 'tea')
	Claw('Sam', 'read', 'book')
	Claw('Joe', 'watch', 'movie')
	Claw('Nid', 'listen', 'music')
	Claw('Joe', 'play', 'game')

	#chat online
	#homework
	#work on computer
	#work in garden

	Claw('Sam', 'eat', 'rice').modify('where', Node('house'))
	Claw('Joe', 'cook', 'food').modify('where', Node('house').modify('of', 'friend'))
	Claw('Nid', 'cook', 'food').modify('where', 'kitchen')
	Claw('Joe', 'brew', 'coffee').modify('where', 'backyard')

	Claw('Nid', 'read', 'book').modify('where', 'upstairs')
	Claw('Nui', 'listen', 'music').modify('where', 'bedroom')
	Claw('Sam', 'watch', 'movie').modify('where', 'livingroom')
	Claw('Nid', 'play', 'game').modify('where', 'backyard')

	# Why
	Claw('Nid', 'cook', 'food').modify('why', Claw(Node('family').modify('of', 'Nid'), 'is', 'hungry'))

	Claw('Joe', 'brew', 'coffee').modify('why', Claw('Joe', 'relax'))
	Claw('Joe', 'brew', 'coffee').modify('why', Claw('Joe','give','friend'))
	Claw('Nid', 'read', 'book').modify('why', Claw('Nid', 'have', 'fun'))
	Claw('Penny', 'chat', 'online').modify('why', Claw('Penny', 'talk', 'friend'))

	Claw('Bella', 'do', 'homework').modify( 'why', Claw( 'assignment', 'is', 'due').modify('when', 'tomorrow'))
	Claw('Pin', 'do', 'homework').modify( 'why', Claw('Pin', 'study', 'test'))
	Claw('May', 'work').modify( 'where', 'computer').modify( 'why', 'job')
	Claw('Som', 'work').modify( 'where', 'garden').modify( 'why', Claw( 'weed', 'is', Node('many').modify('howmuch', 'too')))
	Claw('Milky', 'work').modify( 'where', 'garden').modify( 'why', Node('time').modify('what', 'harvest'))
	Claw('Chompoo', 'work').modify( 'where', 'garden').modify( 'why', Node('time').modify('what', 'plant'))

