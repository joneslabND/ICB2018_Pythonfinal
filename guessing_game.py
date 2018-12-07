import numpy

# randomly draw an integer between 1 and 100
myNumber=numpy.random.choice(range(1,50,1))

# create a while loop that runs until we indicate the guesser is correct
correct=0
while correct==0:
	# prompt the user for a guess
	guess=raw_input(promp="Guess:")

	if int(guess)<theNumber
		print("Higher")
	else:
		print("Lower")

	if guess=myNumber:
		print("Correct")
		correct=1
