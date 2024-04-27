# DOCUMENTATION
# This program takes a range of numbers as input from the user and generates a random number which the user has to guess.

# FUNCTIONS:
# randint (Integer, Integer) -> (integer): Imported from the 'random' library. Takes two numbers as input and returns a pseudo-random number

# VARIABLES:
# iMin (integer): The lower limit of the range from which the random number number will be chosen, taken from the user.
# iMax (integer): The upper limit of the range from which the random number will be chosen, taken from the user.
# randNum (integer): Stores the random number generated by randint().
# iGuess (integer): Initialised to 'None'. Stores the number guessed by the use

# CODE
from random import randint
iMin = int(input("Enter the minimum number: "))
iMax = int(input("Enter the maximum number: "))
while (iMax < iMin):
    print("Invalid entry!!! Enter again")
    iMin = int(input("Enter the minimum number: "))
    iMax = int(input("Enter the maximum number: "))
randNum = randint(iMin, iMax)
iGuess = None
while(iGuess != randNum):
    iGuess = int(input("\n\nEnter your guess: "))
    if (iGuess > randNum):
        print("Guess lower")
    elif (iGuess < randNum):
        print("Guess higher")
print("Your guess is correct!!!")
