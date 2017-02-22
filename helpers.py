"""helper functions"""

from model import word, guess_letter, partial_word

# RIGHT NOW THIS ONLY WORKS WITH SINGLE CHARACTERS
# AND IS CASE SENSITIVE

def word_so_far(word, guess_letter, partial_word):
	"""function to show current guess letter if it is in the word"""

	# if partial_word != "": 
	# 	partial_word = partial_word
	# 	print partial_word, "!"
	
	for i in range(len(word)):

		if guess_letter != word[i]:
			partial_word =  partial_word + "_ "

		# elif partial_word already has letters, don't replace them with underscores
		# possibly use .join
		# if guess_letter and/or any letters in the guess_list == the word, print partial word
		
		else:
			partial_word = partial_word + word[i]

	return partial_word

word_so_far(word, guess_letter, partial_word)


# word_length in underscores with correct guesses added
# defining the variable name for the user input
# for letter in range(len(word)):
# 	if guess == letter:
# 		print word with letter(s)


# def six_guesses(guesses):
# 	""" function to count and limit user to 6 guesses """  
# 	for guesses in range 6:

# 	if guesses = 6:
# 		break


# def show_word(guess_letter):
# 	""" function to show the word being filled in (in progress) """
# # _ _ _ _ _ is word is "hello" and user picks "l" should show _ _ l l _
# 	for char in word:



# def confirm_letters(word):
# 	"""function to confirm input is letters, that the input doesn's 
# 	exceed the char in the word and allows for either case"""

# 	# maybe a try and except here


# input_str = raw_input("Please provide some info: ")
# if not re.match("^[a-z]*$", input_str):
#     print "Error! Only letters a-z allowed!"
#     sys.exit()

# elif len(input_str) > len(word):
#     print "Error! Only len(word) characters allowed!"
#     sys.exit()

# print "Your input was:", input_str

# def hints():
# 	""" function to give an option for a hint at the 5th and 6th guesses """

# shouldn't this just be len(word)

# def number_of_letters_in_word(word):
# 	""" function to determine number of letters in word """

# if guess == letter in word
# remove 1 from the 6 guesses
# add to word list thingie
# show word thingie to the user

# if guess != letter in word
# add to guess list
# remove 1 from the 6 guesses

# if guess == guess in guess_list
# tell user that has already been guessed and guess again (back to input)

# def find_guess_letter(guess_letter):
# 	"""function to find the letter guessed by the user in the secret word"""
# 	for letter in word:
# 		if guess_letter == letter:
# 			print 
# 		else:
# 			print "nope"




