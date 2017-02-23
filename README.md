# The Hangman Challenge

Hangman is an old game where player one picks a secret word and draws a horizontal line for each letter in the word. 
Player two then guesses letters. Each time player two guesses a letter in the secret word, player one fills in that 
letter wherever it appears. If player two guesses a letter not in the word, player one draws one part of the hangman.
The hangman has six parts, head, body, left arm, right arm, left leg, and right leg. If player two guesses incorrectly 
six times, the hangman is drawn and player one loses.

Most people played this when they were kids, though it seems a bit creepy now. I think I'd rather Zombie! or LegoMan! where
when you have 6 incorrect guesses you have built a Zombie, which means you lose cause they're after your brains! Or LegoMan, 
where you start with a whole lego man and lose a part for ever wrong guess, ending with no lego man if you lose, which 
would be very sad. But I digress...

This challenge came with most of the same rules that would be part of pen and paper hangman, except player one, the keeper of 
the secret word is the computer and the words are randomly generated from a collection of words here provided by my challengers!

### Prerequisites

The game is written in python and played through the command line. 
In order to play, you'll need Python 2.7 and a virtual environment with the requirements.txt installed.
Pip install is a good way to go.

### Installing

To play the game clone hmchallenge to your local machine and using the virtual environment you created, 
call it with "python hmchallenge.com" in your terminal.

You should see the welcome message and it will give you the length of the word you're meant to guess.

  $ git clone [git-repo-url] hmchallenge

  $ cd hmchallenge

  $ virtualenv env

  $ source env/bin/activate

  $ pip install -r requirements.txt

  $ python hmchallenge.py

## Built With

* [Python](https://www.python.org/) - powerful programming language

## Versioning

Version 1.0

## Author

* **Kelly Hoffer**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to my lovely and supportive engineering community

