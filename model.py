"""Model for hangman challenge!"""
import re
import requests
import random

# is there any way to limit these be length of random choice or starts with letter
r = requests.get('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
r.status_code
words = r.content.splitlines()
word = random.choice(words)

# the number of characters in the chosen word, may be multiples of the letters but still same number of chars
word_length = len(word)

# shows the word with the correct guess letters at their proper indices
partial_word = ""

# user guess
user_guess = None

# number of guesses (must be 6 or under) -will need to add correct and incorrect guesses
guesses = 0

# player starts with 6 guesses, we need to remove one guess for every legitimate guess (not including letters already guessed)
max_wrong_guesses = 6

# wrong guess counts againsthe max wrong guesses
wrong_guesses = 0

# list to keep track of guesses
guess_list = []

# keep track of the body parts 
# body_parts = ['head', 'body', 'left_arm', 'right_arm', 'left_leg', 'right_leg'] 
# head = "o"
# body = "()"
# left_arm = ">-"
# right_arm = "-<"
# left_leg = "_|"
# right_leg = "|_"

#   o
# >-()-<	
#  _| |_

# Class ATTRIBUTES vs Instance ATTRIBUTES
# ATTRIBUTES are variables that are glued to an Instance

#  # setting up classes so game is easily understood and altered
# class Game(object):
# 	"""initiates and ends the game"""
# 	pass
# 	# ATTRIBUTES
# 	# game starts
# 	# game ends


# class Man(object):
# 	"""6 hangman parts, creates man based on incorrect guesses """ 
# 	# if guess_letter not in word:
# 	# man loses appendage so method could be
# 	# pass
# 	body_parts = [head, body, left_arm, right_arm, left_leg, right_leg]


# class word(object):
# 	"""random word chosen by link right now"""
# 	pass
# # WOULD THE WORD CLASS MAYBE HAVE THE GUESS CLASS IN IT 
# # AS IT'S DEPENDENT ON IT?
# 	# computer generates
# # # number of letters
# # # if it's been generated before? - this should be in tests
# Words in the have been through list?
# # # partial word - does this belong in guess??


# class guess(object):
# 	"""user input"""
# 	pass
	# ATTRIBUTES
# raw input
# guess_letter
# guess_length (if guess_length > len(word) INVALID)
# max_guesses
# number of unknown letters
# number of guesses remaining
# number of correct guesses
# number of incorrect guesses
#  number of guesses to finished word


# class Game(object):
# 	"""game class"""
# 	startGame
# 	endGame



# def game_over(wrong_guesses):
# 	"""function to limit user to max number of guesses"""  
	
# 	if 	wrong_guesses == max_wrong_guesses:
# 		print """You've run out of guesses! 
# 		The word was %s.""" % (word)

# def game_over(entire_word_guessed):
		
# CURRENT BUG, IF YOU GUESS ALL THE LETTERS INDIVIDUALLY, YOU DON'T WIN!
# IF LETTERS IN GUESS LIST = WORD THEN WIN!!!



# def limit_guess_characters(user_guess):
# 	if user_guess != upper or lower case letter
# 	if user_guess > len(word)
# 	if user_guess = " "


# def ask_ user_to_play_again(guess_word):
# 	play_again = raw_input("Would you like to play again? y or n? \n")
# 	if play_again == "y":
# 		start game game_over
# 	if play_again == "n":
# 		print "Thanks! Bye!"
# 	if play_again != "y" or "no":
# 		print "please respond with y or n"



# def show_correct_guesses(word, guess_list):
# 	"""function to show current guess letter if it is in the word"""

# 	partial_word = ""

# if word[i] == item in guess list, append that item to teh partial word string (or .join)

# 	if partial_word != "": 
#  	partial_word = partial_word
	
# 	for i in range(len(word)):

# 		for item in guess_list:

# 			if item == word[i]:
# 				partial_word = partial_word + word[i]
				
# 		# elif partial_word already has letters, don't replace them with underscores
# 		# possibly use .join
# 		# if guess_letter and/or any letters in the guess_list == the word, print partial word
		
# 			else:
# 				partial_word = partial_word + "_"
# 				# print partial_word

# 	return partial_word

# show_correct_guesses(word, guess_list)

# RIGHT NOW THIS ONLY WORKS WITH SINGLE CHARACTERS
# AND IS CASE SENSITIVE

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

# def number_of_letters_in_word(word):
# 	""" function to determine number of letters in word """

# if guess == guess in guess_list
# tell user that has already been guessed and guess again (back to input)
