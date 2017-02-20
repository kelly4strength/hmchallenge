
# THINGS TO KEEP TRACK OF:

# right now these are all global but will be made into Class objects

# word - for now manually chosen, needs to be hooked up to http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
word = "hello"
# the number of characters in the chosen word, may be multiples of the letters but still same number of chars
word_length = len(word)
# to display the word with the correct guesses filled in i.e. "hello" = "_ _ l l _" when "l" is chosen
# need the character and index to do this

# man = keep track of the body parts 

partial_word = word_length in underscores with correct guesses added
# defining the variable name for the user input
guess_letter = None
# number of guesses (must be 6 or under) -will need to add correct and incorrect guesses
guesses = 0
# letters/strings guesses go into the guess list (all the letters?, yes if we have a you already guessed that clause)
guess_list = []

# player starts with 6 guesses, we need to remove one guess for every legitimate guess (not including letters already guessed)
# remaining_guesses = 6 

#TESTS
# input are letters, case doesn't matter
# input does not exceed number of letters in word
# tries are limited to 6 (or whatever number you wish)
# maybe a front end - but letters are put in correct spaces to fill in the word 
# and all instances of the letter in the word

# if guess == letter in word
# remove 1 from the 6 guesses
# add to word list thingie
# show word thingie to the user

# if guess != letter in word
# add to guess list
# remove 1 from the 6 guesses

# if guess == guess in guess_list
# tell user that has already been guessed and guess again (back to input)


def guess_word(word):
	"""function determines asks user to input guesses """

# welcome user to game and define the number of letter in the word and number of guesses they get
# only want to see this once so outside the for loop
print '''Welcome to Hangman
		Your word has %d characters in it. 
		And you have 6 guesses before your man is doomed
		Guess a letter, any letter!''' % (word_length)

	# if guesses == 6:
	# 	return "you've run out of guesses"

# while guess_letter not in word:
# can't use While cause it's a boolean so when it's true, then what?
for guess_letter in word:

	# prompting the user that keyboard input is expected/requested
	guess_letter = raw_input("")

	if guess_letter in guess_list:
		# You get to guess again and that guess doesn't count against you
		# /n is giving me a space for the next try
		print "Sorry, you already tried %s. Try again!\n " % (guess_letter)

	else:

		# appends guess to guess_list so you can track # of guesses
		guess_list.append(guess_letter)
		
		if guess_letter not in word:
			print '''Sorry, that letter is not in the word! 
					You have %d guesses left 
					And %d characters to fill in
					Try again!\n''' % (guess_list, len(word), guesses) 
			
			# counts guesses
	    	guesses += 1

		if guess_letter in word:
			
			print '''Success, you now have %s 
					You have %d guesses left 
					And %d characters to fill in
					Try again!\n''' % (word, guess_list, len(word), guesses) 

			# counts guesses
	    	guesses += 1


























