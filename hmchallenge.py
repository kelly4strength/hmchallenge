"""hangman challenge!!"""

from model import word, guesses, max_guesses, guess_list, partial_word, guess_letter

from helpers import show_correct_guess_letter, limit_guesses, entire_word_guessed

def guess_word(word):
	"""function determines a random word and asks user to guess letters in the word"""

# welcome user to game and give rules, number of letters in word and max number of guesses available
print """
	Welcome to something man!
	I've chosen a super secret word for you, it has %d characters
	You can guess a letter or the entire word.
	You get %d guesses to put your man together \n""" % (len(word), max_guesses)

print word

# using a while loop to limit number of guesses
# while guesses < max_guesses and guess_letter != word:
while guesses < max_guesses:

	# prompting the user that keyboard input is expected/requested
	guess_letter = raw_input("Guess a letter or word: \n")

	# break this out
	if guess_letter in guess_list:
		# You get to guess again and that guess doesn't count against you
		print "Sorry, you already tried %s. Try again!\n " % (guess_letter)

	else:
		# appends guess to guess_list so you can track # of guesses
		guess_list.append(guess_letter)
		
		# if it's the last guess need to let them know the game is over
		if guess_letter not in word:
			guesses += 1
			print "Sorry, %s is not in the word!\n" %(guess_letter)

		if guess_letter in word:
			guesses += 1
			print "Yes, %s is in the word %s \n" % (guess_letter, show_correct_guess_letter(word, guess_letter, partial_word))

	# if user guesses entire word, break out of loop
	# have to add break to function because it's within the while loop so it will keep going until condition is false
	entire_word_guessed(guess_letter)

	
	limit_guesses(guesses)



	
	# CURRENT BUG, IF YOU GUESS ALL THE LETTERS INDIVIDUALLY, YOU DON'T WIN!
	# IF LETTERS IN GUESS LIST = WORD THEN WIN!!!

		

























