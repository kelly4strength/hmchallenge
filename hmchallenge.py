"""hangman challenge!!"""

import re

from helpers import show_correct_guess_letter

from classes import word, user_guess, partial_word, max_wrong_guesses, all_guesses, correct_guess_list, wrong_guesses, wrong_guess_list, guesses

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

	if len(user_guess) > len(word):
		print "Oops! The word only has %d letters. Try again!" %(len(word))
		continue

	# if user hits "return" you get: Yes,  is in the word _ _ _ _ _  
	 # prompt them for an appropiate response

	if user_guess in all_guesses:
		print "Sorry, you already tried %s. Try again!\n " % (user_guess)

	else:

		if user_guess not in word:
			wrong_guess_list.append(user_guess)
			wrong_guesses += 1

			print			"""Sorry, %s is not in the word! 
			You have %d guesses remaining and 
			your incorrect guesses are here: %s \n""" %(user_guess, (max_wrong_guesses - wrong_guesses), wrong_guess_list)

			if wrong_guesses == max_wrong_guesses:
				print "Boo, you've run out of guesses! The word was %s." % (word)

		if user_guess == word:
			print "Well done! You've guessed the secret word %s" % (word)
			break

		if user_guess in word:
			correct_guess_list.append(user_guess)
			guesses += 1

			print "Yes, %s is in the word %s \n" % (user_guess, show_correct_guess_letter(word, user_guess, partial_word))


# WORKING ON THIS
# - as the guesser makes correct guesses, occurences of the guessed letter in the word are 
# shown while unknown letters are still hidden



	

























