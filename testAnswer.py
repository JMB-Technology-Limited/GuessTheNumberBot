from answer import myBot


# Test
val = myBot(1,100,[])
if (val != 50):
	print "Test No guesses yet failed, got "+str(val)

# test 
val = myBot(1,100,[[2,1]])
if (val != 1):
	print "Test answer is 1, already guessed 2, got "+str(val)


# test 
val = myBot(1,100,[[99,-1]])
if (val != 100):
	print "Test answer is 100, already guessed 99, got "+str(val)



print "All Tests Run!"
