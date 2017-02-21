word = "bubbles"
guess_letter = ""
guesses = None

def guess_word(word):
	"""trying to figure out what's wrong"""

guess_letter = raw_input("put a letter here: ")

for letter in word:
	if letter != guess_letter:
		print "nope"
