sample_1 = '''A ___1___ in Python is any bit of text stored between a pair of quotations marks.  Double 
quotes are ideal, as ___2___ quotes can cause issues if you use certain routine punctuation.  ___3___ 
stored between quotes count as ___1___s.  A ___1___ can be converted to a list using the ___4___ 
function: ___1___.___4___().'''

sample_2 = '''A ___1___ in Python is any set of values separated by ___2___ and contained between two 
brackets.  Values can be strings (which must be between quotation marks) or ___3___.  ___1___s can even be 
___4___ within ___1___s.  Accessing ___1___ values is accomplisted by indexing the ___1___ value in sequence, 
starting with ___5___.'''

sample_3 = '''A Python ___1___ allows for a block of code to be executed multiple times.  ___2___ ___1___s 
execute a code block as long as a given condition is ___3___.  ___4___ ___1___s will run for every instance of 
a given ___5___ in a sequence.  When incorporating ___1___s, it's important to specify a limit or an end-point 
so the code doesn't run in an ___6___ ___1___.'''

sample_1_answers  = [["___1___","string"], ["___2___","single"], ["___3___","Numbers"], ["___4___","split"]]

sample_2_answers  = [["___1___","list"], ["___2___","commas"], ["___3___","numbers"], ["___4___","nested"], 
					["___5___","zero"]]

sample_3_answers  = [["___1___","loop"], ["___2___","While"], ["___3___","true"], ["___4___","For"], 
					["___5___","variable"], ["___6___","infinite"]]

sample_answer_list = [[sample_1,sample_1_answers], [sample_2, sample_2_answers], [sample_3,sample_3_answers]]

def challenge():
	'''Sets the challenge level for the game, based on user input.
	User is prompted to choose one of three given levels.  A choice not in the given list
	results in an error message.  A correct choice prints the sample paragraph for the 
	chosen game level, and returns the variable name of the sample paragraph.  The returned 
	output is used in def answers_list and def FIB_game.
	'''
	sample = ""
	while sample == "":
		user_input = raw_input("Easy, medium or hard? ")
		if user_input == "easy" or user_input == "Easy":
			sample = sample_1
		elif user_input == "medium" or user_input == "Medium":
			sample = sample_2
		elif user_input == "hard" or user_input == "Hard":
			sample = sample_3
		else:
			print "That's an invalid selection!"
			sample = ""
	print sample
	return sample
	
def answers_list(sample, answers_list):
	'''Sets the correct answers for the game, based on the challenge level of the game (chosen by 
	user; output of def challenge).
	Returns a list of correct answers, which is used in def FIB_game.
	'''
	index = 0
	answers_list = sample_answer_list
	FIB_answers_list = []
	while FIB_answers_list == []:
		if sample == answers_list[index][0]:
			FIB_answers_list = answers_list[index][1]
		else:
			index = index + 1
	return FIB_answers_list

def FIB_game():
	'''Incorporating parameters returned by previous two functions, executes full game of 
	fill-in-the-blanks.  A paragraph with blank entries is printed for the player, who is then prompted 
	to provide the appropriate word to correctly complete the blank entry.  Incorrect choices result 
	in a printed error message and prompt for a new choice is provided.  Correct answers print an updated 
	paragraph, and a prompt for the next blank entry is printed.  When all blanks have been correctly filled, 
	the completed paragraph is returned.
	'''
	index = 0
	sample = challenge()
	blanks_list = answers_list(sample,sample_answer_list)
	while index < len(blanks_list):
		blank = blanks_list[index][0]
		answer = blanks_list[index][1]
		user_input = raw_input("Type the word that completes " + blank + ": ")
		if user_input == answer:
			sample = sample.replace(blank, user_input)
			print "Excellent.  Look what you've done: "
			print sample
			index = index + 1
		else:
			print "Foolish and wrong.  Try again."
			index = index + 0
	print "You did it!  See all your good work: "
	return sample

print FIB_game()