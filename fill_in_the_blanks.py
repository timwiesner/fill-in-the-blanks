# Welcome to Fill-in-the-Blanks, a game where the user is presented three difficulty levels and must choose appropriate replacement words for the selected paragraph. 


# BLANKS FOR REPLACEMENT
blanks = ['__1__', '__2__', '__3__', '__4__']

# PARAGRAPHS FOR EASY, MEDIUM, AND HARD
easy_paragraph = '''"Hypertext __1__ Language (HTML) is the standard markup language for creating __2__ pages and __2__ applications. With Cascading Style Sheets (CSS) and __3__ it forms a triad of cornerstone technologies for the World Wide Web.[1] Web __4__ receive HTML documents from a webserver or from local storage and render them into multimedia __2__ pages. HTML describes the structure of a __2__ page semantically and originally included cues for the appearance of the document." [Source: https://en.wikipedia.org/wiki/HTML]'''

medium_paragraph = '''Admiral Grace __1__ is known as one of the pioneers of computing. She was famous for carrying around a __2__, a 30cm piece of wire which represents the distance light is able to travel in one nanosecond. __1__ felt that computer programs should be written in languages that resembled English. This led her to significant role in the development of __3__, a business programming language still in use today. She retired after 42 years of service in the United States __4__. [Source: https://en.wikipedia.org/wiki/Grace_Hopper]'''

hard_paragraph = '''Python is an interpreted, __1__-oriented, high-level __2__ language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid __3__ Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and __4__, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. [Source: https://www.python.org/doc/essays/blurb/]'''

# REPLACEMENT WORDS FOR RESPECTIVE LEVELS
easy_replacement = ['Markup', 'web', 'JavaScript', 'browsers']
medium_replacement = ['Hopper', 'nanostick', 'COBOL', 'Navy']
hard_replacement = ['object', 'programming', 'Application', 'packages']


####################
# HELPER FUNCTIONS #
####################

# GREETING
def greeting(name):
	"""Displays player and game info"""
	"""Inputs: Player name"""
	"""Outputs: Intro paragraph"""

	print "\nHello, " + name + "! Welcome to Fill-in-the-Blanks, a game " \
					"where you a presented with a paragraph and must choose " \
					"appropriate replacement words. Please select a game " \
					"difficulty by typing it in below."

# DIFFICULTY
def get_level(difficulty):
	"""Checks level and returns the appropriate paragraph and replacement"""
	"""Inputs: Selected difficulty"""
	"""Outputs: Paragraph and replacements for selected level"""
	intro = "\nYou've chosen " + difficulty + "!\nYou will get 5 guesses per problem\n\nThe current paragraph reads as such:"
	print intro
	if difficulty == 'easy':
		return easy_paragraph, easy_replacement
	elif difficulty == 'medium':
		return medium_paragraph, medium_replacement
	elif difficulty == 'hard':
		return hard_paragraph, hard_replacement

# REPLACEMENT
"""Checks if user input matches game's replacement word"""
"""Inputs: Selected paragraph and replacement"""
"""Outputs: Paragraph with correctly replaced words"""
def get_replacement(paragraph, replacement):
	replaced = []
	i = 0
	for blank in blanks:
		prompt = ("\n\nWhat should be substituted in for " + blank + "?")
		print prompt
		answer = raw_input().lower()
		while answer != replacement[i].lower():
			print "That isn't the correct answer! Let's try again." + prompt
			answer = raw_input().lower()
		print "Correct!\n\n"
		replaced = paragraph.replace(blank, replacement[i])
		paragraph = replaced
		print paragraph
		i += 1
	if blank[i] < len(blanks):
		return replaced, i
	else:
		print "\nCongratulations! You won the game!"


# PLAY GAME
"""Function to execute game"""
"""Inputs: None"""
"""Outputs: Entire game"""
def play_game():
	name = raw_input("What is your name?\n")
	greeting(name)
	difficulty = raw_input("Your available choices are easy, medium, and hard\nPlease type in your selection:\n").lower()
	if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
		paragraph, replacement = get_level(difficulty)
		print paragraph
		replaced = get_replacement(paragraph, replacement)	
	else:
		print "Input Not Recognized.\nThe game will now restart." 
		play_game()


########
# PLAY #
########
play_game()
