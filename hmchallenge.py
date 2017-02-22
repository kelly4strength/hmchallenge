"""hangman challenge!!"""

from model import word, guesses, max_guesses, guess_list, partial_word

from helpers import word_so_far

def guess_word(word):
	"""function determines a random word and asks user to input guesses"""

# welcome user to game and give rules, number of letters in word and max number of guesses available
print """
	Welcome to something man!
	I've chosen a super secret word for you, it has %d characters
	You can guess a letter or the entire word.
	You get %d guesses to put your legoman together \n""" % (len(word), max_guesses)

print word

# using a while loop to limit number of guesses
while guesses < max_guesses:

	# prompting the user that keyboard input is expected/requested
	guess_letter = raw_input("Guess a letter or word: \n")

	if guess_letter in guess_list:
		# You get to guess again and that guess doesn't count against you
		print "Sorry, you already tried %s. Try again!\n " % (guess_letter)

	else:
		# appends guess to guess_list so you can track # of guesses
		guess_list.append(guess_letter)
		
		if guess_letter not in word:
			guesses += 1
			print "Sorry, %s is not in the word! Try again!\n" %(guess_letter)

		if guess_letter in word:
			guesses += 1
			print "Yes, %s is in the word %s \n" % (guess_letter, word_so_far(word, guess_letter, partial_word))

	if guess_letter == word:
		print "Well done! You've guessed the word %s" % (word) 
		# ADD would you like to play again?
		break

	if 	guesses == max_guesses:
		print """Sorry, you've run out of guesses! 
		The word was %s.""" % (word)

		

























