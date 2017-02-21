
# A game of hangman
# which can be played by a user against the computer

# secret-keeper is the computer
# user is guesser
# they get 6 guessess

# if the guesses a letter which is part of the word, 
# the secret keeper will reveal all occurences  of that letter in the word 

# if the guesser guesser guesses a correct letter such that all letter are now revealed, 
# the game is over and the guesser has won

# if the guesser runs out of guesses before the whole word is discovered, game is over and computer wins


# Game Rules
#  - At the start of the game, thecomputer/secret-keeper chooses a dictionary word 
#  	# With what number of letters? something you have to be able to get in 6 guesses???
#  - the guesser loses the game if they guess 6 letters that are not in the secret word
#  - the guesser wins the game if they guess all the letters in the secret word correctly 
#  and have not already lost the game per the conditions above
#  #  ???

#  User Interface
#  Any type of user interface is acceptable (command line, mobile app, webpage, etc.) 
#  but the player must have a way of interacting with yout game, including:
# - the length of the secret word is displayed to the guesser( like a set of underscores)
# - as the guesser makes correct guesses, occurences of the guessed letter in the word are 
# shown while unknown letters are still hidden
# - The number of guesses remaining is displayed
# - a list of incorrect guesses are displayed

# Implementation
# - Your program must retrieve a dictionary list of words from the word dictionary REST API provided
# http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
# - You can use whatever combination of programming languages, tools, frameworks and libraries

# import word_list type thing below
# http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
# or word = random.random_word


# import urllib2 import Request, urlopen, URLError
# import random

# words = urllib.urlopen('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words').read()
# print type(words)
# print words

import requests

import json

# import random

r = requests.get('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
r.status_code
print type(r)
# print r.text
# print r.json


# from urllib2 import Request, urlopen, URLError
# import random

# words = urllib2.Request('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words').random()
# print type(words)
# print words


# random_word = random.words

# print random_word
# try:
# 	response = urlopen(words)
# 	kittens = response.read()
# 	print kittens[559:1000]

# except URLError, e:
#     print 'No kittez. Got an error code:', e







