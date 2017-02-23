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

