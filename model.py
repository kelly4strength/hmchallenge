"""Model for hangman challenge!"""

# from flask_sqlalchemy import SQLAlchemy

# import os

import requests

import json

import random

# is there any way to limit these be length of random choice or starts with letter
r = requests.get('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
r.status_code
words = r.content.splitlines()
word = random.choice(words)

# THINGS TO KEEP TRACK OF:

# right now these are all global but will be made into Class objects


# the number of characters in the chosen word, may be multiples of the letters but still same number of chars
# word_length = len(word)

partial_word = ""

# user guess
guess_letter = None

# number of guesses (must be 6 or under) -will need to add correct and incorrect guesses
guesses = 0

# player starts with 6 guesses, we need to remove one guess for every legitimate guess (not including letters already guessed)
max_guesses = 6

guess_list = []
# man = keep track of the body parts 



#  # setting up classes so game is easily understood and altered
# class Game(object):
# 	"""initiates and ends the game"""
# 	pass
# 	# ATTRIBUTES
# 	# game starts
# 	# game ends


# class Man(object):
# 	"""6 hangman parts""" 
# 	pass
# 	# ATTRIBUTES

# if guess_letter not in word:
	# man loses appendage
	
# # # creates man based on incorrect guesses 
# # # head
# # # body
# # # l_arm
# # # r_arm
# # # l_leg
# # # r_leg


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
# max guesses
# number of unknown letters
# number of guesses remaining
# number of correct guesses
# number of incorrect guesses


