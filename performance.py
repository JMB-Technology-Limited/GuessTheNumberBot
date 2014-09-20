from random import randint
from bot import myBot
import time

minNumber = 1
maxNumber = 100
rounds = (maxNumber - minNumber) * 10

data = []
for roundNo in range(rounds):
	theNumber = randint(minNumber, maxNumber)
	numberOfTries = 0
	found = False
	guesses = []
	print "Number: " + str(theNumber)
	while found == False:
		numberOfTries += 1;
		theGuess = myBot(minNumber, maxNumber, guesses)
		if theGuess == theNumber:
			found = True
		elif theGuess < theNumber:
			guesses.append([theGuess ,-1])
		elif theGuess > theNumber:
			guesses.append([theGuess , 1])
	print "Number of tries: " + str(numberOfTries)
	data.append(numberOfTries)

average = sum(data)/len(data)

print "Average number of tries: " + str(average)
