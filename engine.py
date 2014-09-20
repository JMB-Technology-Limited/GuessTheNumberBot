from random import randint
from bot import myBot
import time

minNumber = 1
maxNumber = 100

theNumber = randint(minNumber, maxNumber)

print "The number is: " + str(theNumber)

numberOfTries = 0
found = False
guesses = []
while found == False:
	numberOfTries += 1;
	print "Guess Number " + str(numberOfTries)
	theGuess = myBot(minNumber, maxNumber, guesses)
	print "Got Guess " + str(theGuess)
	if theGuess == theNumber:
		print "Well done!"
		found = True
	elif theGuess < theNumber:
		print "Too Low!"
		guesses.append([theGuess ,-1])
	elif theGuess > theNumber:
		print "Too High!"
		guesses.append([theGuess , 1])
	time.sleep(1)



