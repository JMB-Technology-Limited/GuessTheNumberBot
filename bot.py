
def myBot(minNumber, maxNumber, guesses):
	# the first guess
	if len(guesses) == 0:
		return minNumber
	# look at previous guesses
	maxGuessed = minNumber
	for guess,result in guesses:
		maxGuessed = guess
	# make our new guess
	return maxGuessed+1

