#!/usr/bin/env python3

word = "Potsdam"	#the word to be guessed
triesLeft = 8		#the total number of wrong guess you have

guesses = []		#a list of all guesses made

found = False		#Did you find the whole word or not


while(triesLeft >= 0 and not found):
	#print text to the screen
	print("\n\nWe are playing hangman !")
	print("You have " + str(triesLeft) + " tries left!")
	print("Letters you tried so far :")
	print(guesses)
	
	#print word so far

	output = []

	for letter in word:
		if (letter.lower() in guesses):
			output.append(letter)
		else:
			output.append("_")

	print("\nThe word we are looking for:")
	print(" ".join(output))
	print("")


	#get the next guess from the user
	guess = input("What is your next guess? ")

	if (len(guess) == 1):					#is the input valid ?
		guess = guess.lower()
		if not (guess in guesses):			#has this character been guessed before ?
			guesses.append(guess)
			if (guess in word.lower()):		#is is a correct guess?
				print("Correct!")

				#check if the word was found
				f = True
				for letter in word:
					f = f and (letter.lower() in guesses)
				found = f
			else:
				print("Wrong Guess!")
				triesLeft -= 1		

		else:
			print("You already tried this character!")

	else:
		print("Incorrect input, you can only guess one character!")

if not found:
	print("\n\nYou Lost!")
	print("We were looking for " + word)
else:
	print("\n\nCongratulations, you guessed the word!")

