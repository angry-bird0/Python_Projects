# DOCUMENTATION
# This program asks the user for the number of lives and selects a random word from a list of 100 words, and the user has to play the game 'hangman' where they guess which word it is.

# CODE
from random import choice

#I asked ChatGPT to provide me with 100 words encased in quotes and separated by commas
wordList = ['apple', 'banana', 'carrot', 'dog', 'elephant', 'fantastic', 'giraffe', 'happiness', 'imagination', 'jazz', 'kiwi', 'lemon', 'mountain', 'novel', 'ocean', 'penguin', 'quasar', 'rhythm', 'sunshine', 'tangerine', 'umbrella', 'violet', 'whisper', 'xylophone', 'yellow', 'zeppelin', 'adventure', 'butterfly', 'chocolate', 'diamond', 'enigma', 'firefly', 'garden', 'harmony', 'island', 'jasmine', 'kaleidoscope', 'lighthouse', 'melody', 'nightingale', 'orchestra', 'peacock', 'quixotic', 'rose', 'serendipity', 'tranquil', 'utopia', 'velvet', 'wonder', 'xanadu', 'yearning', 'zeal', 'alchemy', 'blossom', 'cascade', 'dream', 'effervescent', 'freedom', 'glisten', 'halcyon', 'innocence', 'journey', 'kismet', 'luminous', 'mystique', 'nirvana', 'opulent', 'prismatic', 'quaint', 'radiant', 'serenity', 'talisman', 'uplifting', 'vivid', 'whimsical', 'zenith', 'amazing', 'bliss', 'cynosure', 'dazzling', 'ecstasy', 'felicity', 'graceful', 'halo', 'intrepid', 'jubilant', 'kaleidoscopic', 'lullaby', 'mesmerize', 'nurturing', 'opulent', 'paradise', 'quasar', 'resplendent', 'serendipity', 'tranquil', 'uplifting', 'vibrant', 'whimsical', 'xylograph', 'yearning', 'zenith']

iWord = choice(wordList)
wordLetters = set(iWord)
remainingAlphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
usedLetters = []
iLives = int(input("\nEnter the number of lives: "))

while ((len(wordLetters) > 0) and (iLives > 0)):
    print(f"\nYou have {iLives} lives left, and you have used: {usedLetters}.")
    print("The word is: ", end = "")
    for iChar in iWord:
        if (iChar in usedLetters):
            print(iChar, end = "")
        else:
            print("_", end = "")
    userLetter = input("\nEnter a letter: ").lower()
    if (userLetter in remainingAlphabets):
        remainingAlphabets.remove(userLetter)
        usedLetters.append(userLetter)
        if (userLetter in wordLetters):
            wordLetters.remove(userLetter)
        else:
            iLives -= 1
            print("This letter is not in the word.")
    elif (userLetter in usedLetters):
        print("You have already used this letter. Try again.")
        continue
    else:
        print("Invalid input!!! Try again.")
        continue

if (iLives == 0):
    print("You lost!!!", end = " ")
else:
    print(f"You won!!!", end = " ")
print(f"The word is '{iWord}'.\n")
