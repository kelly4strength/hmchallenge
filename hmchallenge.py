


# word - for now manually chosen, needs to be hooked up to http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
from model import word, guesses, max_guesses, guess_list, partial_word
from helpers import word_so_far

def guess_word(word):
	"""function determines a random word and asks user to input guesses"""

# welcome user to game and give rules, number of letters in word and max number of guesses available
# only want to see this once, so outside the loop

print """
	Welcome to my game of hangman!
	You get %d guesses
	You can guess a letter or the entire word
	Your word has %d characters \n""" % (max_guesses, len(word))

print word

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
			print word_so_far(word, guess_letter, partial_word)

	if guess_letter == word:
		print "Well done! You've guessed the word %s" % (word) 
		break

	if 	guesses == max_guesses:
		print "sorry, you've run out of guesses!"
		print word_so_far(word, guess_letter, partial_word)
		print word

		

























