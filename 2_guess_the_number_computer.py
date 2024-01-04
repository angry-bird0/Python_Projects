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
