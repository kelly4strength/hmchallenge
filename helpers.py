# helpers

from hmchallenge import 
import re

def six_guesses(guesses):
	""" function to count and limit user to 6 guesses """  
	for guesses in range 6:

	if guesses = 6:
		break


def show_word(guess_letter):
	""" function to show the word being filled in (in progress) """
# _ _ _ _ _ is word is "hello" and user picks "l" should show _ _ l l _
	for char in word:



def confirm_letters(word):
	"""function to confirm input is letters, that the input doesn's 
	exceed the char in the word and allows for either case"""

	# maybe a try and except here


input_str = raw_input("Please provide some info: ")
if not re.match("^[a-z]*$", input_str):
    print "Error! Only letters a-z allowed!"
    sys.exit()
elif len(input_str) > 15:
    print "Error! Only 15 characters allowed!"
    sys.exit()

print "Your input was:", input_str

def hints():
	""" function to give an option for a hint at the 5th and 6th guesses """


			# shouldn't this just be len(word)
# def number_of_letters_in_word(word):
# 	""" function to determine number of letters in word """






