"""Model for hangman challenge!"""

import requests
import random

# generating the random word for te user to guess
r = requests.get('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
r.status_code
words = r.content.splitlines()
word = random.choice(words)

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

# list to keep track of wrong guesses
wrong_guess_list = []

# list to keep track of correct guesses
correct_guess_list = []

# all guesses in current game
all_guesses = wrong_guess_list + correct_guess_list
