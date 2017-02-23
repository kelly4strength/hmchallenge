"""helper functions"""

from model import word, user_guess, partial_word

def show_correct_guess_letter(word, user_guess, partial_word):
	"""function to show current guess letter if it is in the word"""

########### works for letter combinations but doesn't print them
	for i in range(len(word)):
		if user_guess != word[i]:
			partial_word =  partial_word + "_ "
		else:
			partial_word = partial_word + word[i]
	return partial_word

