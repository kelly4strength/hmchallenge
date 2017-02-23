"""hangman challenge!!"""

import re

from model import word, guesses, max_wrong_guesses, guess_list, partial_word, user_guess, wrong_guesses

from helpers import show_correct_guess_letter, game_over

def guess_word(word):
	"""function determines a random word and asks user to guess letters in the word"""

print """
	Welcome to hangman!
	I've chosen a super secret word for you, it has %d characters
	You can guess a letter or the entire word.
	You get %d guesses to put your man together \n""" % (len(word), max_wrong_guesses)

print word

while wrong_guesses < max_wrong_guesses:

	user_guess = raw_input("Guess a letter or word: \n").lower()

	# In these cases, you get to guess again without adding a wrong guess
	if not re.match("^[a-z]*$", user_guess):
		print "Oops! Only letters a-z allowed! Try again!"
		continue

	elif len(user_guess) > len(word):
		print "Oops! The word only has %d letters. Try again!" %(len(word))
		continue

	if user_guess in guess_list:
		print "Sorry, you already tried %s. Try again!\n " % (user_guess)

	else:
		guess_list.append(user_guess)
		
		if user_guess not in word:
			wrong_guesses += 1
			print "Sorry, %s is not in the word!\n" %(user_guess)

		if user_guess == word:
			print "Well done! You've guessed the word %s" % (word)
			break

		if user_guess in word:
			guesses += 1
			print "Yes, %s is in the word %s \n" % (user_guess, show_correct_guess_letter(word, user_guess, partial_word))

	game_over(wrong_guesses)


	

























