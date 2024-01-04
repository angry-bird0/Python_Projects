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
