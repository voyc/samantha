''' firstmind.py '''

import mind

sammind = mind.Mind()

mind.Node('root')
mind.Node('empty', 'root')
mind.Node('person', 'root')
mind.Node('place', 'root')
mind.Node('thing', 'root')
mind.Node('action', 'root')
mind.Node('link', 'root')

mind.Node('typeof', 'link')
mind.Node('ownedby', 'link')
mind.Node('where', 'link')
mind.Node('why', 'link')
mind.Node('which', 'link')
mind.Node('when', 'link')
mind.Node('how', 'link')
mind.Node('by', 'link')

mind.Node('this', 'which')
mind.Node('next', 'which')
mind.Node('last', 'which') # previous

mind.Node('time_period', 'thing')
mind.Node('week', 'time_period')
mind.Node('day', 'time_period')
mind.Node('month', 'time_period')
mind.Node('year', 'time_period')

mind.Node('time', 'thing')
mind.Node('now', 'time')
mind.Node('yesterday', 'time')
mind.Node('today', 'time')
mind.Node('tomorrow', 'time')
mind.Node('morning', 'time')
mind.Node('afternoon', 'time')
mind.Node('evening', 'time')

mind.Node('you', 'person')
mind.Node('I', 'person')
mind.Node('friend', 'person')

mind.Node('Sam', 'person')
mind.Node('John', 'person')
mind.Node('Naiyana', 'person')
mind.Node('Juan', 'person')
mind.Node('Joe', 'person')
mind.Node('Nui', 'person')
mind.Node('Nid', 'person')

mind.Node('city', 'place')
mind.Node('island', 'place')
mind.Node('businesstype', 'thing')
mind.Node('bank', 'businesstype')
mind.Node('coffeeshop', 'businesstype')
mind.Node('restaurant', 'businesstype')
mind.Node('salon', 'businesstype')
mind.Node('market', 'businesstype')
mind.Node('mall', 'businesstype')
mind.Node('pharmacy', 'businesstype')
mind.Node('cinema', 'businesstype')
mind.Node('doctor', 'businesstype')
mind.Node('hospital', 'businesstype')
mind.Node('clinic', 'businesstype')
mind.Node('dentist', 'businesstype')
mind.Node('embassy', 'businesstype')
mind.Node('house', 'place')
mind.Node('Bangkok', 'city')
mind.Node('Phuket', 'city')
mind.Node('Koh_Samui', 'island')
mind.Node('Krabi', 'city')
mind.Node('Pattaya', 'city')
mind.Node('Hua_Hin', 'city')
mind.Node('Chiang_Mai', 'city')
mind.Node('Pai', 'city')
mind.Node('Udon_Thani', 'city')
mind.Node('Sukothai', 'city')
mind.Node('Ayutthaya', 'city')

mind.Node('food', 'thing')
mind.Node('vacation', 'thing')
mind.Node('business', 'thing')
mind.Node('money', 'thing')
mind.Node('coffee', 'food')
mind.Node('breakfast', 'food')
mind.Node('hair', 'thing')
mind.Node('pedicure', 'thing')
mind.Node('manicure', 'thing')
mind.Node('medicine', 'thing')
mind.Node('movie', 'thing')
mind.Node('checkup', 'thing')
mind.Node('headache', 'thing')
mind.Node('covid', 'thing')
mind.Node('tooth', 'thing')
mind.Node('teeth', 'thing')
mind.Node('filling', 'thing')
mind.Node('whitening', 'thing')
mind.Node('toothache', 'thing')
mind.Node('braces', 'thing')

mind.Node('transport', 'thing')
mind.Node('train', 'transport')
mind.Node('bus', 'transport')
mind.Node('airplane', 'transport')
mind.Node('ship', 'transport')

mind.Node('car', 'transport')
mind.Node('Grab', 'transport')
mind.Node('taxi', 'transport')
mind.Node('citybus', 'transport')
mind.Node('songtaew', 'transport')
mind.Node('tuktuk', 'transport')
mind.Node('walk', 'action')
mind.Node('run', 'action')

mind.Node('go', 'action')
mind.Node('eat', 'action')
mind.Node('visit', 'action')
mind.Node('pickup', 'action')
mind.Node('deliver', 'action')
mind.Node('get', 'action')
mind.Node('drink', 'action')
mind.Node('meet', 'action')
mind.Node('wash', 'action')
mind.Node('cut', 'action')
mind.Node('buy', 'action')
mind.Node('shop', 'action')
mind.Node('watch', 'action')
mind.Node('fix', 'action')
mind.Node('test', 'action')
mind.Node('see', 'action')
mind.Node('clean', 'action')
mind.Node('remove', 'action')

friendhouse = mind.Node('instance', 'house').modify('ownedby', 'friend')

mind.Relation('you', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('you', 'pickup', 'food'))
mind.Relation('Sam', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('Sam', 'deliver', 'food'))
mind.Relation('John', 'go', 'empty').modify('where', friendhouse).modify('why', mind.Relation('John', 'eat', 'food'))
mind.Relation('Naiyana', 'go', 'empty').modify('where', 'Bangkok').modify('why', mind.Relation('Naiyana', 'visit', 'empty'))
mind.Relation('Sam', 'go', 'empty').modify('where', 'Chiang_Mai').modify('why', 'vacation')
mind.Relation('John', 'go', 'empty').modify('where', 'Pai').modify('why', mind.Relation('John', 'go', 'embassy'))
mind.Relation('Juan', 'go', 'empty').modify('where', 'bank').modify('why', mind.Relation('Juan', 'get', 'money'))

mind.Relation('John', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('John', 'drink', 'coffee'))
mind.Relation('Sam', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('Sam', 'eat', 'breakfast'))
mind.Relation('Juan', 'go', 'empty').modify('where', 'coffeeshop').modify('why', mind.Relation('Juan', 'meet', 'friend'))

def work(who, where, whyv, whyo):
	mind.Relation(who, 'go', 'empty').modify('where', where).modify('why', mind.Relation(who, whyv, whyo))

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
	mind.Relation(who, 'go', 'empty').modify('when', mind.Node('instance', period).modify('which', which))

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
	mind.Relation(who, 'go', 'empty').modify('where', where).modify('how', how)

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

mind.Node('foodtype', 'root')
mind.Node('rice', 'foodtype')
mind.Node('tea', 'foodtype')

mind.Node('book', 'thing')
mind.Node('music', 'thing')
mind.Node('game', 'thing')

mind.Node('cook', 'action')
mind.Node('brew', 'action')
mind.Node('read', 'action')
mind.Node('listen', 'action')
mind.Node('play', 'action')
mind.Node('is', 'action')
mind.Node('feel', 'action')

mind.Node('feeling', 'root')
mind.Node('hungry', 'feeling')

mind.Node('kitchen', 'place')
mind.Node('backyard', 'place')
mind.Node('upstairs', 'place')
mind.Node('bedroom', 'place')
mind.Node('livingroom', 'place')

mind.Node('family', 'person')

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

mind.Relation('Sam', 'eat', 'rice').modify('where', mind.Node('instance', 'house'))
mind.Relation('Joe', 'cook', 'food').modify('where', mind.Node('instance', 'house').modify('ownedby', 'friend'))
mind.Relation('Nid', 'cook', 'food').modify('where', 'kitchen')
mind.Relation('Joe', 'brew', 'coffee').modify('where', 'backyard')

mind.Relation('Nid', 'read', 'book').modify('where', 'upstairs')
mind.Relation('Nui', 'listen', 'music').modify('where', 'bedroom')
mind.Relation('Sam', 'watch', 'movie').modify('where', 'livingroom')
mind.Relation('Nid', 'play', 'game').modify('where', 'backyard')

mind.Relation('Nid', 'eat', 'food').modify('why', mind.Relation('Nid', 'is', 'hungry'))
mind.Relation('Nid', 'cook', 'food').modify('why', mind.Relation(mind.Node('instance', 'family').modify('ownedby', 'Nid'), 'is', 'hungry'))

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

sammind.buildGrammar()
sammind.dump()

# you go where: set of possible answers
person = mind.Thot.nfs('person')
go = mind.Thot.nfs('go')
where = mind.Thot.nfs('where')
alist = sammind.patterns[person][go][where]

#Thot.nextQuestion()

print(alist)
quit()
