from random import choice

while(True):
    userInput = input("\n\nGive your input: 'r' for rock, 'p' for paper, 's' for scissors\n")
    if (userInput not in ['r', 'p', 's']):
        print("Invalid input!!! Try again.")
        continue
    computerChoice = choice(['r', 'p', 's'])
    if (userInput == computerChoice):
        print("It is a tie. Try again.")
        continue
    if (((userInput == 'r') and (computerChoice == 's')) or ((userInput == 'p') and (computerChoice == 'r')) or ((userInput == 's') and (computerChoice == 'p'))):
        print("You won!!!\n\n")
        break
    print("You lost!!!\n\n")
    break
