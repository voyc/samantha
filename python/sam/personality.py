''' personality.py   characteristics of a user '''

class Personality:
	def __init__(self):
		# personality big five (temperament)
		openness = 0.0           # +1=inventive/curious       -1=consistent/cautious
		conscientiousness = 0.0  # +1=efficient/organized     -1=extravagant/careless
		extraversion = 0.0       # +1=outgoing/energetic      -1=solitary/reserved
		agreeableness = 0.0      # +1=friendly/compassionate  -1=challenging/callous
		neuroticism = 0.0        # +1=sensitive/nervous       -1=resilient/confident
		
		# intelligence
		iq = 0.0   # +1=150  0=100  -1=50   # human iq median=100  sd=15  3sd=>55 to 145
	
		# values (beliefs, goals, motivation)

