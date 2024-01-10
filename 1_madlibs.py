# DOCUMENTATION
# This program is for playing a game of mad libs. It takes inputs from the user and inserts the words from the user into a story and gives the story as output.

# VARIABLES:
# iAdj (string): Stores an adjective taken from the user
# firstVerb (string): Stores a verb taken from the user
# secondVerb (string): Stores a second verb taken from the user
# famousPerson (string): Stores the name of a famous person taken from the user
# madLib (string): Stores the basic story for the mad lib as f-string

# CODE
iAdj = input("Enter an adjective: ")
firstVerb = input("Enter a verb: ")
secondVerb = input("Enter another verb: ")
famousPerson = input("Enter the name of a famous person (fictional or real): ")
madLib = (f"\nComputer programming is so {iAdj}! It makes me so excited all the time because I love to {firstVerb}. Stay hydrated and {secondVerb} like you are {famousPerson}.")
print(madLib)
