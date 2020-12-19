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
mind.Node('by', 'link')


mind.Node('question', 'link')
mind.Node('which', 'question') # apply to noun

mind.Node('where', 'question') # apply to verb
mind.Node('why', 'question')
mind.Node('when', 'question')  # default "now"
mind.Node('how', 'question')
mind.Node('what', 'question')  # applies only to "do"

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
mind.Node('family', 'person')

mind.Node('Nid', 'person')
mind.Node('Pin', 'person')
mind.Node('May', 'person')
mind.Node('Som', 'person')
mind.Node('Nui', 'person')
mind.Node('Memi', 'person')
mind.Node('Fern', 'person')
mind.Node('Bella', 'person')
mind.Node('Jenny', 'person')
mind.Node('Penny', 'person')
mind.Node('Milky', 'person')
mind.Node('Donut', 'person')
mind.Node('Namtip', 'person')
mind.Node('Tangmo', 'person')
mind.Node('Chompoo', 'person')
mind.Node('Naiyana', 'person')

mind.Node('Sam', 'person')
mind.Node('Joe', 'person')
mind.Node('John', 'person')
mind.Node('Juan', 'person')

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
mind.Node('fun', 'thing')

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
mind.Node('do', 'action')

mind.Node('go', 'action')
mind.Node('come', 'action')
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

mind.Node('cook', 'action')
mind.Node('brew', 'action')
mind.Node('read', 'action')
mind.Node('listen', 'action')
mind.Node('play', 'action')
mind.Node('is', 'action')
mind.Node('feel', 'action')
mind.Node('relax', 'action')
mind.Node('chat', 'action')
mind.Node('talk', 'action')
mind.Node('give', 'action')
mind.Node('have', 'action')
mind.Node('study', 'action')
mind.Node('work', 'action')

mind.Node('animal', 'root')
mind.Node('cow', 'animal')

mind.Node('foodtype', 'root')
mind.Node('rice', 'foodtype')
mind.Node('tea', 'foodtype')

mind.Node('book', 'thing')
mind.Node('music', 'thing')
mind.Node('game', 'thing')
mind.Node('homework', 'thing')
mind.Node('assignment', 'thing')
mind.Node('computer', 'thing')
mind.Node('job', 'thing')
mind.Node('garden', 'thing')
mind.Node('weed', 'thing') 
mind.Node('harvest', 'thing') 
mind.Node('plant', 'thing') 

mind.Node('due', 'thing') # state, adj
mind.Node('many', 'thing') # adv 
mind.Node('howmuch', 'link') # adv 
mind.Node('too', 'howmuch') # adv 

mind.Node('feeling', 'root')
mind.Node('hungry', 'feeling')

mind.Node('kitchen', 'place')
mind.Node('backyard', 'place')
mind.Node('upstairs', 'place')
mind.Node('bedroom', 'place')
mind.Node('livingroom', 'place')
mind.Node('online', 'place')

friendhouse = mind.Objek('house').modify('ownedby', 'friend')
mind.Claws('you', 'go').modify('where', friendhouse).modify('why', mind.Claws('you', 'pickup', 'food'))
mind.Claws('Sam', 'go').modify('where', friendhouse).modify('why', mind.Claws('Sam', 'deliver', 'food'))
mind.Claws('John', 'go').modify('where', friendhouse).modify('why', mind.Claws('John', 'eat', 'food'))
mind.Claws('Naiyana', 'go').modify('where', 'Bangkok').modify('why', mind.Claws('Naiyana', 'visit'))
mind.Claws('Sam', 'go').modify('where', 'Chiang_Mai').modify('why', 'vacation')
mind.Claws('John', 'go').modify('where', 'Pai').modify('why', mind.Claws('John', 'go', 'embassy'))
mind.Claws('Juan', 'go').modify('where', 'bank').modify('why', mind.Claws('Juan', 'get', 'money'))

mind.Claws('John', 'go').modify('where', 'coffeeshop').modify('why', mind.Claws('John', 'drink', 'coffee'))
mind.Claws('Sam', 'go').modify('where', 'coffeeshop').modify('why', mind.Claws('Sam', 'eat', 'breakfast'))
mind.Claws('Juan', 'go').modify('where', 'coffeeshop').modify('why', mind.Claws('Juan', 'meet', 'friend'))

def work(who, where, whyv, whyo=None):
	mind.Claws(who, 'go').modify('where', where).modify('why', mind.Claws(who, whyv, whyo))

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
	mind.Claws(who, 'go').modify('when', mind.Objek(period).modify('which', which))

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

mind.Claws('Nui', 'go').modify('when', 'now')
mind.Claws('Sam', 'go').modify('when', 'yesterday')
mind.Claws('Joe', 'go').modify('when', 'today')
mind.Claws('Nid', 'go').modify('when', 'tomorrow')

# where and how: local vs distant destinations and mode of travel
def work(who, where, how):
	mind.Claws(who, 'go').modify('where', where).modify('how', how)

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
                             
mind.Claws('Sam', 'go').modify('where', 'dentist').modify('how', 'run')
mind.Claws('Joe', 'go').modify('where', 'clinic').modify('how', 'walk')

def work(who, where, how):
	mind.Claws(who, 'go').modify('where', where).modify('how', mind.Claws('by', how))

# you do what?

mind.Claws('Sam', 'eat', 'rice')
mind.Claws('Joe', 'cook', 'food')
mind.Claws('Nid', 'brew', 'coffee')
mind.Claws('Nui', 'brew', 'tea')
mind.Claws('Sam', 'read', 'book')
mind.Claws('Joe', 'watch', 'movie')
mind.Claws('Nid', 'listen', 'music')
mind.Claws('Joe', 'play', 'game')

#chat online
#homework
#work on computer
#work in garden

mind.Claws('Sam', 'eat', 'rice').modify('where', mind.Objek('house'))
mind.Claws('Joe', 'cook', 'food').modify('where', mind.Objek('house').modify('ownedby', 'friend'))
mind.Claws('Nid', 'cook', 'food').modify('where', 'kitchen')
mind.Claws('Joe', 'brew', 'coffee').modify('where', 'backyard')

mind.Claws('Nid', 'read', 'book').modify('where', 'upstairs')
mind.Claws('Nui', 'listen', 'music').modify('where', 'bedroom')
mind.Claws('Sam', 'watch', 'movie').modify('where', 'livingroom')
mind.Claws('Nid', 'play', 'game').modify('where', 'backyard')


# Why
mind.Claws('Nid', 'eat', 'food').modify('why', mind.Claws('Nid', 'is', 'hungry'))
mind.Claws('Nid', 'cook', 'food').modify('why', mind.Claws(mind.Objek('family').modify('ownedby', 'Nid'), 'is', 'hungry'))

mind.Claws('Joe', 'brew', 'coffee').modify('why', mind.Claws('Joe', 'relax'))
mind.Claws('Joe', 'brew', 'coffee').modify('why', mind.Claws('Joe','give','friend'))
mind.Claws('Nid', 'read', 'book').modify('why', mind.Claws('Nid', 'have', 'fun'))
mind.Claws('Penny', 'chat', 'online').modify('why', mind.Claws('Penny', 'talk', 'friend'))

mind.Claws('Bella', 'do', 'homework').modify( 'why', mind.Claws( 'assignment', 'is', 'due').modify('when', 'tomorrow'))
mind.Claws('Pin', 'do', 'homework').modify( 'why', mind.Claws('Pin', 'study', 'test'))
mind.Claws('May', 'work').modify( 'where', 'computer').modify( 'why', 'job')
mind.Claws('Som', 'work').modify( 'where', 'garden').modify( 'why', mind.Claws( 'weed', 'is', mind.Objek('many').modify('howmuch', 'too')))
mind.Claws('Milky', 'work').modify( 'where', 'garden').modify( 'why', mind.Objek('time').modify('what', 'harvest'))
mind.Claws('Chompoo', 'work').modify( 'where', 'garden').modify( 'why', mind.Objek('time').modify('what', 'plant'))

sammind.buildGrammar()

#import pdb; pdb.set_trace()
sammind.dump(True

print('\nGenerative Grammar')

#Thot.nextQuestion()

'''
Joe eat rice this afternoon.
Joe go to bank with friend when friend arrive.

if... then...
If you listen to this song, you will be very happy.
If you listen to this song, I think you will be very happy.

syllogism
Warm beer is better than nothing. Nothing is better than god.  Therefore, warm beer is better than god.

deductive reasoning

inductive reasoning

classical dialectic: thesis, antithesis, synthesis
'''

joeeat = mind.Claws('Joe', 'eat', 'rice').modify('when',mind.Objek('afternoon').modify('which','this'))
print( joeeat)

