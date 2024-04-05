# DOCUMENTATION
# This program takes input from the user and compares it with a random choice (between rock, paper, and scissor) made by the compter.

# FUNCTIONS:
# choice (List[String]) -> (String): Choses and returns a pseudo-random element from that list.

# VARIABLES:
# userInput (string): Stores input from the user.
# computerChoice (string): Stores the choice of the computer.

# CODE
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
