from random import randint
import random


minNumber = 1
maxNumber = 100

theNumber = randint(minNumber, maxNumber)

found = False
attempts = 0
while found == False:
	attempts += 1
	guess = int(input('Take a guess: '))

	if guess < theNumber:
		print "To Low!"
	elif guess > theNumber:
		print "To High!"
	else:
		print 'Well Done, you guessed it in ' + str(attempts) + ' attempts'
		found = True
