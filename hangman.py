#!/usr/bin/evn python3

word = "Potsdam"	#the word to be guessed
triesLeft = 8		#the total number of wrong guess you have

guesses = []		#a list of all guesses made

found = False		#Did you find the whole word or not


while(triesLeft >= 0 and not found):
	#print text to the screen
	print("We are playing hangman !")
	print("You have " + str(triesLeft) + " tries left!")
	print("Letters you tried so far :")
	print(guesses)
	
	#print word so far

	guess = input("What is your next guess? ")

	#process guess


