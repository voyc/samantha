''' firstmind.py '''

import mind

sammind = mind.Mind()
mind.Thot.mind = sammind

mind.Klas('empty')

#Relation(you, go, where)  # 24 places, destinations
mind.Klas('person')
mind.Klas('place')
mind.Klas('thing')
mind.Klas('action')
mind.Klas('link')

mind.Klas('typeof', 'link')
mind.Klas('ownedby', 'link')
mind.Klas('where', 'link')
mind.Klas('why', 'link')
mind.Klas('which', 'link')
mind.Klas('when', 'link')
mind.Klas('how', 'link')
mind.Klas('by', 'link')

mind.Klas('this', 'which')
mind.Klas('next', 'which')
mind.Klas('last', 'which') # previous

mind.Klas('time_period', 'thing')
mind.Klas('week', 'time_period')
mind.Klas('day', 'time_period')
mind.Klas('month', 'time_period')
mind.Klas('year', 'time_period')

mind.Klas('time', 'thing')
mind.Klas('now', 'time')
mind.Klas('yesterday', 'time')
mind.Klas('today', 'time')
mind.Klas('tomorrow', 'time')
mind.Klas('morning', 'time')
mind.Klas('afternoon', 'time')
mind.Klas('evening', 'time')

mind.Klas('you', 'person')
mind.Klas('I', 'person')
mind.Klas('friend', 'person')

mind.Klas('Sam', 'person')
mind.Klas('John', 'person')
mind.Klas('Naiyana', 'person')
mind.Klas('Juan', 'person')
mind.Klas('Joe', 'person')
mind.Klas('Nui', 'person')
mind.Klas('Nid', 'person')

mind.Klas('city', 'place')
mind.Klas('island', 'place')
mind.Klas('businesstype', 'thing')
mind.Klas('bank', 'businesstype')
mind.Klas('coffeeshop', 'businesstype')
mind.Klas('restaurant', 'businesstype')
mind.Klas('salon', 'businesstype')
mind.Klas('market', 'businesstype')
mind.Klas('mall', 'businesstype')
mind.Klas('pharmacy', 'businesstype')
mind.Klas('cinema', 'businesstype')
mind.Klas('doctor', 'businesstype')
mind.Klas('hospital', 'businesstype')
mind.Klas('clinic', 'businesstype')
mind.Klas('dentist', 'businesstype')
mind.Klas('embassy', 'businesstype')
mind.Klas('house', 'place')
mind.Klas('Bangkok', 'city')
mind.Klas('Phuket', 'city')
mind.Klas('Koh_Samui', 'island')
mind.Klas('Krabi', 'city')
mind.Klas('Pattaya', 'city')
mind.Klas('Hua_Hin', 'city')
mind.Klas('Chiang_Mai', 'city')
mind.Klas('Pai', 'city')
mind.Klas('Udon_Thani', 'city')
mind.Klas('Sukothai', 'city')
mind.Klas('Ayutthaya', 'city')

mind.Klas('food', 'thing')
mind.Klas('vacation', 'thing')
mind.Klas('business', 'thing')
mind.Klas('money', 'thing')
mind.Klas('coffee', 'food')
mind.Klas('breakfast', 'food')
mind.Klas('hair', 'thing')
mind.Klas('pedicure', 'thing')
mind.Klas('manicure', 'thing')
mind.Klas('medicine', 'thing')
mind.Klas('movie', 'thing')
mind.Klas('checkup', 'thing')
mind.Klas('headache', 'thing')
mind.Klas('covid', 'thing')
mind.Klas('tooth', 'thing')
mind.Klas('teeth', 'thing')
mind.Klas('filling', 'thing')
mind.Klas('whitening', 'thing')
mind.Klas('toothache', 'thing')
mind.Klas('braces', 'thing')

mind.Klas('transport', 'thing')
mind.Klas('train', 'transport')
mind.Klas('bus', 'transport')
mind.Klas('airplane', 'transport')
mind.Klas('ship', 'transport')

mind.Klas('car', 'transport')
mind.Klas('Grab', 'transport')
mind.Klas('taxi', 'transport')
mind.Klas('citybus', 'transport')
mind.Klas('songtaew', 'transport')
mind.Klas('tuktuk', 'transport')
mind.Klas('walk', 'action')
mind.Klas('run', 'action')

mind.Klas('go', 'action')
mind.Klas('eat', 'action')
mind.Klas('visit', 'action')
mind.Klas('pickup', 'action')
mind.Klas('deliver', 'action')
mind.Klas('get', 'action')
mind.Klas('drink', 'action')
mind.Klas('meet', 'action')
mind.Klas('wash', 'action')
mind.Klas('cut', 'action')
mind.Klas('buy', 'action')
mind.Klas('shop', 'action')
mind.Klas('watch', 'action')
mind.Klas('fix', 'action')
mind.Klas('test', 'action')
mind.Klas('see', 'action')
mind.Klas('clean', 'action')
mind.Klas('remove', 'action')

friendhouse = mind.Klas('instance', 'house').modify('ownedby', 'friend')

mind.Relation('you', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('empty', 'pickup', 'food'))
mind.Relation('Sam', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('empty', 'deliver', 'food'))
mind.Relation('John', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('empty', 'eat', 'food'))
mind.Relation('Naiyana', 'go', 'empty').modify('where', 'Bangkok').modify('why', mind.Relation('empty', 'visit', 'empty'))
mind.Relation('Sam', 'go', 'empty').modify('where', 'Chiang_Mai').modify('why', 'vacation')
mind.Relation('John', 'go', 'empty').modify('where', 'Pai').modify('why', mind.Relation('empty', 'go', 'embassy'))
mind.Relation('Juan', 'go', 'empty').modify('where', 'bank').modify('why', mind.Relation('empty', 'get', 'money'))

mind.Relation('John', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('empty', 'drink', 'coffee'))
mind.Relation('Sam', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('empty', 'eat', 'breakfast'))
mind.Relation('Juan', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('empty', 'meet', 'friend'))

def work(who, where, whyv, whyo):
	mind.Relation(who, 'go', 'empty').modify('where', where).modify('why', mind.Relation('empty', whyv, whyo))

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
	mind.Relation(who, 'go', 'empty').modify('when', mind.Klas('instance', period).modify('which', which))

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

mind.Klas('foodtype')
mind.Klas('rice', 'foodtype')
mind.Klas('tea', 'foodtype')

mind.Klas('book', 'thing')
mind.Klas('music', 'thing')
mind.Klas('game', 'thing')

mind.Klas('cook', 'action')
mind.Klas('brew', 'action')
mind.Klas('read', 'action')
mind.Klas('listen', 'action')
mind.Klas('play', 'action')
mind.Klas('is', 'action')
mind.Klas('feel', 'action')

mind.Klas('feeling')
mind.Klas('hungry', 'feeling')

mind.Klas('kitchen', 'place')
mind.Klas('backyard', 'place')
mind.Klas('upstairs', 'place')
mind.Klas('bedroom', 'place')
mind.Klas('livingroom', 'place')

mind.Klas('family', 'person')

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

mind.Relation('Sam', 'eat', 'rice').modify('where', mind.Klas('instance', 'house'))
mind.Relation('Joe', 'cook', 'food').modify('where', mind.Klas('instance', 'house').modify('ownedby', 'friend'))
mind.Relation('Nid', 'cook', 'food').modify('where', 'kitchen')
mind.Relation('Joe', 'brew', 'coffee').modify('where', 'backyard')

mind.Relation('Nid', 'read', 'book').modify('where', 'upstairs')
mind.Relation('Nui', 'listen', 'music').modify('where', 'bedroom')
mind.Relation('Sam', 'watch', 'movie').modify('where', 'livingroom')
mind.Relation('Nid', 'play', 'game').modify('where', 'backyard')

mind.Relation('Nid', 'eat', 'food').modify('why', mind.Relation('Nid', 'is', 'hungry'))
test = mind.Relation('Nid', 'eat', 'food').modify('why', mind.Relation(mind.Klas('instance', 'family').modify('ownedby', 'Nid'), 'is', 'hungry'))

#import pdb; pdb.set_trace()
print(sammind)
quit()

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


a = mind.Klas('hoo')
a1 = mind.Klas('instance', 'hoo')
b = mind.Relation(a1.modify('which', 'music'), 'go', 'empty')
a2 = mind.Klas('instance', 'hoo').modify('why','play')


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

	option
		subj:Objek -> link/verb:Objek -> obj:Objek
		verb:Objek
			modifier
				subj Objek
				obj  Objek
				why
				where
		
	"object" and "entity" imply a noun		
	"instance" - can also be a verb or a link.  is that true?

	Joe is a terminal klass
	Bangkok is a terminal klass, but we need to make an Objek of it in a thot

	the thot is listed as a thot
		objeks are not listed, but referenced directly within the thot


	a relation names up to three parts
		each of the three can have modifiers

	a klass can have modifiers too


	generate grammar



	common names of persons, Klas?
	who's who, instances of persons, public
	friends, instances of persons, private

	proper names
		persons
			common names, index of  - klas, not objek
			who's who - objek, global mind
			my contacts - objek, private mind
		places Gazetteer
			countries
			provinces
			cities
			neighborhoods
			streets
		businesses directory
			business names and type


		mind.contacts.print()

mind.gazetteer.toString()
mind.whoswho.toString() - including my contacts, global phone book
mind.businessdirectory.toString()
	Ristr8to
	

'''


