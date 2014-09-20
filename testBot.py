from bot import myBot


# Test 
val = myBot(1,100,[])
if (val != 1):
	print "Test No guesses yet failed, got "+str(val)


# Test 
val = myBot(1,100,[[1,-1]])
if (val != 2):
	print "Test one guess, got "+str(val)

# Test 
val = myBot(1,100,[[1,-1],[2,-1]])
if (val != 3):
	print "Test two guesses, got "+str(val)


print "All Tests Run!"
