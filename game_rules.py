
# A game of hangman
# which can be played by a user against the computer

# secret-keeper is the computer
# user is guesser
# they get 6 guessess

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
word = "hello"
guess_list = ['l', 'h']

def show_correct_guesses(word, guess_list):
	"""function to show current guess letter if it is in the word"""

	partial_word = ""
	# if partial_word != "": 
	# 	partial_word = partial_word
	# 	print partial_word, "!"
	
	for i in range(len(word)):

		for item in guess_list:

			if item != word[i]:
				partial_word =  partial_word + " "

		# elif partial_word already has letters, don't replace them with underscores
		# possibly use .join
		# if guess_letter and/or any letters in the guess_list == the word, print partial word
		
			else:
				partial_word = partial_word + word[i]

				print partial_word

	print partial_word

show_correct_guesses(word, guess_list)








