# setting up classes so game is easily understood and altered


class man(object):
"""6 hangman parts""" 
	pass
# creates man based on incorrect guesses 
# head
# body
# l_arm
# r_arm
# l_leg
# r_leg


class word(object):
	"""random word chosen by link right now"""
	pass
# number of letters
# if it's been generated before? - this should be in tests
# partial word


class guess(object):
"""user input"""
	pass
# guess_letter

# guess_length
	# if guess_length > len(word) INVALID
# guess_number

