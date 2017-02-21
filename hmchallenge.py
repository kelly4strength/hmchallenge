
# THINGS TO KEEP TRACK OF:

# right now these are all global but will be made into Class objects

# word - for now manually chosen, needs to be hooked up to http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
word = "bubbles"

# the number of characters in the chosen word, may be multiples of the letters but still same number of chars
word_length = len(word)

# to display the word with the correct guesses filled in i.e. "hello" = "_ _ l l _" when "l" is chosen
# need the character and index to do this
# partial_word = word length in _ +str + _ guessed letters // word - unguessed letters

# user guess
guess_letter = None

# number of guesses (must be 6 or under) -will need to add correct and incorrect guesses
guesses = 0

# player starts with 6 guesses, we need to remove one guess for every legitimate guess (not including letters already guessed)
max_guesses = 6

guess_list = []
# man = keep track of the body parts 

def guess_word(word):
	"""function determines a random word and asks user to input guesses"""

# welcome user to game and define the number of letter in the word and number of guesses they get
# only want to see this once, so outside the for loop

print """
	Welcome to my game of hangman!
	You get %d guesses
	You can guess a letter or the entire word
	Your word has %d characters \n""" % (max_guesses, len(word))

# using a while loop to limit number of guesses
while guesses < max_guesses:

	# prompting the user that keyboard input is expected/requested
	guess_letter = raw_input("Guess a letter or word: ")

	if guess_letter in guess_list:
		# You get to guess again and that guess doesn't count against you
		print "Sorry, you already tried %s. Try again!\n " % (guess_letter)

	else:
		# appends guess to guess_list so you can track # of guesses
		guess_list.append(guess_letter)
		
		if guess_letter not in word:
			# counts guesses
			guesses += 1
			
			print "Sorry, that letter is not in the word! Try again!\n"

		if guess_letter in word:
			# counts guesses
			guesses += 1

			print "Yes, %s is in the word\n" %(guess_letter)

	if guess_letter == word:
		print "Well done! You've guessed the word %s" % (word) 
		break

	if 	guesses == max_guesses:
		print "sorry, you've run out of guesses!"

		

























