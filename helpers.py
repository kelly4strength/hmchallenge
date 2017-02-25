"""helper functions"""

# from model import word, user_guess, partial_word
# import unnecessary 

# def show_correct_guess_letter(word, user_guess, partial_word):
# 	"""function to show current guess letter if it is in the word"""

# 	for i in range(len(word)):

# 		if user_guess != word[i]:
# 			partial_word =  partial_word + "_ "
	
# 		else:
# 			partial_word = partial_word + word[i]
	
# 	return partial_word


def generate_partial_word(word, correct_guess_list):
	"""generates the word with all correctly chosen letters"""

	temp_partial_word = ""

	# for each letter either put a dash or a letter
	for i in range(len(word)):
		matches = False

		for letter in correct_guess_list:

			if letter == word[i]:

				temp_partial_word = temp_partial_word + letter
				matches = True

		if matches == False:

			temp_partial_word = temp_partial_word + "_"

	return temp_partial_word

				#if there is no match to word[i] then add a underscore for that index
				# only append underscore after all matches are determined


		




