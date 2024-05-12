# DOCUMENTATION
# This program takes a range of numbers as input from the user and the user selects a random number in that range and the computer guesses that number

# FUNCTIONS:
# randint (integer, integer) -> (integer): Imported from the 'random' library. Takes two numbers as input and returns a pseudo-random number

# VARIABLES:
# iMin (integer): The lower limit of the range from which the random number number will be chosen, taken from the user.
# iMax (integer): The upper limit of the range from which the random number will be chosen, taken from the user.
# feedBack (string): Stores feedback from the user regarding the guess of the computer.
# iGuess (Integer): Stores a pseudo-random number between iMin and iMax, generated by the computer

# CODE
from random import randint
iMin = int(input("Enter the minimum number: "))
iMax = int(input("Enter the maximum number: "))
while (iMax < iMin):
    print("Invalid entry!!! Enter again")
    iMin = int(input("Enter the minimum number: "))
    iMax = int(input("Enter the maximum number: "))
feedBack = ""
while(feedBack != "c"):
    iGuess = randint(iMin, iMax)
    feedBack = input(f"\n\nIs {iGuess} correct (c)? If not, then is your number higher (h) or is your number lower (l)? ")
    while (feedBack not in ["c", "h", "l"]):
        feedBack = input("Invalid feedback!!! Try again: ")
    if (feedBack == "h"):
        iMin = iGuess + 1
    elif (feedBack == "l"):
        iMax = iGuess - 1
print("The computer guessed the number correctly!!!")
