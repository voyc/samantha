''' firstmind.py '''

import mind

sammind = mind.Mind()
mind.Thot.mind = sammind

mind.Entity('empty')
mind.Entity('typeof')

#Relation(you, go, where)  # 24 places, destinations
mind.Entity('person')
mind.Entity('place')
mind.Entity('thing')
mind.Entity('action')
mind.Entity('link')

mind.Entity('ownedby', 'link')
mind.Entity('where', 'link')
mind.Entity('why', 'link')
mind.Entity('which', 'link')
mind.Entity('when', 'link')
mind.Entity('how', 'link')
mind.Entity('by', 'link')

mind.Entity('this', 'which')
mind.Entity('next', 'which')
mind.Entity('last', 'which') # previous

mind.Entity('time_period')
mind.Entity('week', 'time_period')
mind.Entity('day', 'time_period')
mind.Entity('month', 'time_period')
mind.Entity('year', 'time_period')

mind.Entity('now')
mind.Entity('yesterday')
mind.Entity('today')
mind.Entity('tomorrow')
mind.Entity('morning')
mind.Entity('afternoon')
mind.Entity('evening')

mind.Entity('you', 'person')
mind.Entity('I', 'person')
mind.Entity('friend', 'person')

mind.Entity('Sam', 'person')
mind.Entity('John', 'person')
mind.Entity('Naiyana', 'person')
mind.Entity('Juan', 'person')
mind.Entity('Joe', 'person')
mind.Entity('Nui', 'person')
mind.Entity('Nid', 'person')

mind.Entity('city', 'place')
mind.Entity('island', 'place')
mind.Entity('businesstype')
mind.Entity('bank', 'businesstype')
mind.Entity('coffeeshop', 'businesstype')
mind.Entity('restaurant', 'businesstype')
mind.Entity('salon', 'businesstype')
mind.Entity('market', 'businesstype')
mind.Entity('mall', 'businesstype')
mind.Entity('pharmacy', 'businesstype')
mind.Entity('cinema', 'businesstype')
mind.Entity('doctor', 'businesstype')
mind.Entity('hospital', 'businesstype')
mind.Entity('clinic', 'businesstype')
mind.Entity('dentist', 'businesstype')
mind.Entity('embassy', 'businesstype')
mind.Entity('house', 'place')
mind.Entity('Bangkok', 'city')
mind.Entity('Phuket', 'city')
mind.Entity('Koh_Samui', 'island')
mind.Entity('Krabi', 'city')
mind.Entity('Pattaya', 'city')
mind.Entity('Hua_Hin', 'city')
mind.Entity('Chiang_Mai', 'city')
mind.Entity('Pai', 'city')
mind.Entity('Udon_Thani', 'city')
mind.Entity('Sukothai', 'city')
mind.Entity('Ayutthaya', 'city')

mind.Entity('food', 'thing')
mind.Entity('vacation')
mind.Entity('business')
mind.Entity('money')
mind.Entity('coffee')
mind.Entity('breakfast')
mind.Entity('hair')
mind.Entity('pedicure')
mind.Entity('manicure')
mind.Entity('medicine')
mind.Entity('movie')
mind.Entity('checkup')
mind.Entity('headache')
mind.Entity('covid')
mind.Entity('tooth')
mind.Entity('teeth')
mind.Entity('filling')
mind.Entity('whitening')
mind.Entity('toothache')
mind.Entity('braces')

mind.Entity('train')
mind.Entity('bus')
mind.Entity('airplane')
mind.Entity('ship')

mind.Entity('car')
mind.Entity('Grab')
mind.Entity('taxi')
mind.Entity('citybus')
mind.Entity('songtaew')
mind.Entity('tuktuk')
mind.Entity('walk')
mind.Entity('run')

mind.Entity('go', 'action')
mind.Entity('eat', 'action')
mind.Entity('visit', 'action')
mind.Entity('pickup', 'action')
mind.Entity('deliver', 'action')
mind.Entity('get', 'action')
mind.Entity('drink', 'action')
mind.Entity('meet', 'action')
mind.Entity('wash', 'action')
mind.Entity('cut', 'action')
mind.Entity('buy', 'action')
mind.Entity('shop', 'action')
mind.Entity('watch', 'action')
mind.Entity('fix', 'action')
mind.Entity('test', 'action')
mind.Entity('see', 'action')
mind.Entity('clean', 'action')
mind.Entity('remove', 'action')

# 34 reasons why 

friendhouse = mind.Entity('instance', 'house')
friendhouse.modify('ownedby', 'friend')

yougohouse = mind.Relation('you', 'go', 'empty')
yougohouse.modify('where', friendhouse)
yougohouse.modify('why', mind.Relation('empty', 'pickup', 'food'))

samgohouse = mind.Relation('Sam', 'go', 'empty') 
samgohouse.modify('where', friendhouse)
samgohouse.modify('why', mind.Relation('empty', 'deliver', 'food'))

johngohouse = mind.Relation('John', 'go', 'empty') 
johngohouse.modify('where', friendhouse)
johngohouse.modify('why', mind.Relation('empty', 'eat', 'food'))

naigo = mind.Relation('Naiyana', 'go', 'empty')
naigo.modify('where', 'Bangkok')
naigo.modify('why', mind.Relation('empty', 'visit', 'empty'))

samgo = mind.Relation('Sam', 'go', 'empty')
samgo.modify('where', 'Chiang_Mai')
samgo.modify('why', 'vacation')

johngo = mind.Relation('John', 'go', 'empty')
johngo.modify('where', 'Pai')
johngo.modify('why', mind.Relation('empty', 'go', 'embassy'))

juango = mind.Relation('Juan', 'go', 'empty')
juango.modify('where', 'bank')
juango.modify('why', mind.Relation('empty', 'get', 'money'))

work = mind.Relation('John', 'go', 'empty')
work.modify('where', 'coffeeshop')
work.modify('why', mind.Relation('empty', 'drink', 'coffee'))

work = mind.Relation('Sam', 'go', 'empty')
work.modify('where', 'coffeeshop')
work.modify('why', mind.Relation('empty', 'eat', 'breakfast'))

work = mind.Relation('Juan', 'go', 'empty')
work.modify('where', 'coffeeshop')
work.modify('why', mind.Relation('empty', 'meet', 'friend'))

def work(who, where, whyv, whyo):
	work = mind.Relation(who, 'go', 'empty')
	work.modify('where', where)
	work.modify('why', mind.Relation('empty', whyv, whyo))

work('John', 'restaurant', 'eat', 'food')
work('Sam', 'restaurant', 'meet', 'friend')
work('Naiyana', 'salon', 'wash', 'hair')
work('Juan', 'salon', 'cut', 'hair')
work('John', 'salon', 'get', 'pedicure')
work('Sam', 'salon', 'get', 'manicure')
work('Sam', 'market', 'buy', 'food')
work('Naiyana', 'mall', 'shop', 'empty')
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
	mind.Relation(who, 'go', 'empty').modify('when', mind.Entity('instance', period).modify('which', which))

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

mind.Relation('Nui', 'go', 'empty').modify('when', 'now')
mind.Relation('Sam', 'go', 'empty').modify('when', 'yesterday')
mind.Relation('Joe', 'go', 'empty').modify('when', 'today')
mind.Relation('Nid', 'go', 'empty').modify('when', 'tomorrow')

def work(who, where, how):
	mind.Relation(who, 'go', 'empty').modify('where', where).modify('how', mind.Relation('by', how, 'empty'))

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
                             
mind.Relation('Sam', 'go', 'empty').modify('where', 'dentist').modify('how', 'run')
mind.Relation('Joe', 'go', 'empty').modify('where', 'clinic').modify('how', 'walk')

def work(who, where, how):
	mind.Relation(who, 'go', 'empty').modify('where', where).modify('how', mind.Relation('by', how, 'empty'))

# you do what?

mind.Entity('foodtype')
mind.Entity('rice', 'foodtype')
mind.Entity('tea', 'foodtype')

mind.Entity('book', 'thing')
mind.Entity('music', 'thing')
mind.Entity('game', 'thing')

mind.Entity('cook', 'action')
mind.Entity('brew', 'action')
mind.Entity('read', 'action')
mind.Entity('listen', 'action')
mind.Entity('play', 'action')
mind.Entity('is', 'action')
mind.Entity('feel', 'action')

mind.Entity('feeling')
mind.Entity('hungry', 'feeling')

mind.Entity('kitchen', 'place')
mind.Entity('backyard', 'place')
mind.Entity('upstairs', 'place')
mind.Entity('bedroom', 'place')
mind.Entity('livingroom', 'place')

mind.Entity('family', 'person')

mind.Relation('Sam', 'eat', 'rice')
mind.Relation('Joe', 'cook', 'food')
mind.Relation('Nid', 'brew', 'coffee')
mind.Relation('Nui', 'brew', 'tea')
mind.Relation('Sam', 'read', 'book')
mind.Relation('Joe', 'watch', 'movie')
mind.Relation('Nid', 'listen', 'music')
mind.Relation('Joe', 'play', 'game')

#chat online
#homework
#work on computer
#work in garden

mind.Relation('Sam', 'eat', 'rice').modify('where', mind.Entity('instance', 'house'))
mind.Relation('Joe', 'cook', 'food').modify('where', mind.Entity('instance', 'house').modify('ownedby', 'friend'))
mind.Relation('Nid', 'cook', 'food').modify('where', 'kitchen')
mind.Relation('Joe', 'brew', 'coffee').modify('where', 'backyard')

mind.Relation('Nid', 'read', 'book').modify('where', 'upstairs')
mind.Relation('Nui', 'listen', 'music').modify('where', 'bedroom')
mind.Relation('Sam', 'watch', 'movie').modify('where', 'livingroom')
mind.Relation('Nid', 'play', 'game').modify('where', 'backyard')

mind.Relation('Nid', 'eat', 'food').modify('why', mind.Relation('Nid', 'is', 'hungry'))
test = mind.Relation('Nid', 'eat', 'food').modify('why', mind.Relation(mind.Entity('instance', 'family').modify('ownedby', 'Nid'), 'is', 'hungry'))

#Why you eat food?
#i am hungry
#my family is hungry 
#
#Why you brew coffee
#to relax
#for my friends
#
#Why you read book?
#for fun
#
#Why you chat online?
#talk to friends
#
#Why you do homework?
#assignment due tomorrow
#study for test
#
#Why you work on computer?
#for my job 
#
#Why you work in garden?
#too many weeds
#time for harvest
#time for planting


a = mind.Entity('hoo')
a1 = mind.Entity('instance', 'hoo')
b = mind.Relation(a1.modify('which', 'music'), 'go', 'empty')
a2 = mind.Entity('instance', 'hoo').modify('why','play')


##print(repr(sammind))
print(str(sammind))
#
#print(repr(a))
#print(repr(a1))
#print(repr(a2))

'''
goals:
	discrete complex thoughts, including sub-clauses
	sub-Relations NOT idendtified separately in mind
	distinguish classes from instances

	option:
		in every relation, make every entity an instance

note
	whenever a modify is done to a noun
		an instance is required
	every relation is by nature an instance
		the nouns in the relation are not instances unless explicitly stated

	a thought can be about a class or about an instance

	family of Nid      typeof family, no name, owned by Nid
	Jerry              typeof person, named Jerry
	
	instance, named, permanent
	temporary, only for purpose of the current thought
	can we create temp instances, without putting them in the mind.entities dict?

	any propername is an instance
		Bangkok, has a population and area, etc

	Ethel's lasagna - is a class, but can have modifiers
		a dish of Ethel's lasagna is actually an instance
		is Ethel's lasagna a named entity
		car
			petro car
			electric car
		These are classes, but could have modifiers, no?
		in an instance, the modifier delineates the entity
		in a class, the modifier defines the class

		the Honda EV is a class 
			and it has modifiers that define the class
			if John owns one, that is an instance, color red deliniates it
				the class has a name, the instance does not

'''


