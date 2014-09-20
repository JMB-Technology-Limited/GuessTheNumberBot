
def myBot(minNumber, maxNumber, guesses):
	# the first guess
	if len(guesses) == 0:
		return int(maxNumber-minNumber)/2 + minNumber;
	# look at previous guesses
	higherThan = minNumber
	lowerThan = maxNumber
	for guess,result in guesses:
		if result == 1:
			# this guess was to high!
			if guess < lowerThan:
				lowerThan = guess
		else:
			# this guess was to low!
			if guess > higherThan:
				higherThan = guess
	# make our new guess
	if higherThan  == maxNumber -1:
		return higherThan + 1 
	return int(lowerThan-higherThan)/2 + higherThan;

