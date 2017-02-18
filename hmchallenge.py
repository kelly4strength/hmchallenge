# A game of hangman
# which can be played by a user against the computer

# secret-keeper is the computer
# user is guesser
# they get 6 guesses

# if the guesses a letter which is part of the word, 
# the secret keeper will reveal all occurences  of that letter in the word 

# if the guesser guesser guesses a correct letter such that all letter are now revealed, 
# the game is over and the guesser has won

# if the guesser runs out of guesses before the whole word is discovered, game is over and computer wins


# Game Rules
#  - At the start of the game, thecomputer/secret-keeper chooses a dictionary word 
#  	# With what number of letters? something you have to be able to get in 6 guesses???
#  - the guesser loses the game if they guess 6 letters that are not in the secret word
#  - the guesser wins the game if they guess all the letters in the secret word correctly 
#  and have not already lost the game per the conditions above
#  #  ???

#  User Interface
#  Any type of user interface is acceptable (command line, mobile app, webpage, etc.) 
#  but the player must have a way of interacting with yout game, including:
# - the length of the secret word is displayed to the guesser( like a set of underscores)
# - as the guesser makes correct guesses, occurences of the guessed letter in the word are 
# shown while unknown letters are still hidden
# - The number of guesses remaining is displayed
# - a list of incorrect guesses are displayed

# Implementation
# - Your program must retrieve a dictionary list of words from the word dictionary REST API provided
# http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
# - You can use whatever combination of programming languages, tools, frameworks and libraries

# import word_list type thing below
# http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
# or word = random.random_word

			# THINGS TO KEEP TRACK OF:
# the number of characters in the chosen word, may be multiples of the letters but still same number of chars


# defining the variable name for the user input
guess_letter = None

# number of guesses (must be 6 or under) -will need to add correct and incorrect guesses
guesses = 6

# letters/strings guesses go into the guess list (all the letters?, yes if we have a you already guessed that clause)
guess_list = []

# player starts with 6 guesses, we need to remove one guess for every legitimate guess (not including letters already guessed)
# remaining_guesses = 6 

def guess_word(word):
	"""function determines asks user to input guesses """

word = "hello"
number_chars_in_word = len(word)

print '''Welcome to Hangman
		Your word has %d characters in it. 
		Guess a letter, any letter!''' % (number_chars_in_word)

# while guess_letter not in word:
# can't use While cause it's a boolean so when it's true, then what?

# THIS IS WHY I'yeah M ONLY GETTING 5 GUESSES!!!
for guess_letter in guesses:

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
					current guesses = %s, and number of letters in word = %s 
					and you have taken %s guesses. 
					Try again!\n''' % (guess_list, len(word), guesses) 
			
			# counts guesses
	    	guesses += 1

	    	# NEED TO BREAK OUT OF THE LOOP AND START AGAIN - NEED A LOOP :P!!!

		# if the number given by the user is less than the cats variable    	
		if guess_letter in word:
			print "yes that letter is in the word\n "

			# counts guesses
	    	guesses += 1


























