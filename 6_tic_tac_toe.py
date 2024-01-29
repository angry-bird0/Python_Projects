# DOCUMENTATION
# This program simulates a game of tic-tac-toe between different players which can be humans, computers (randomly selection blocks), or computers (using mini-max algorithm so that the computer never loses)

# FUNCTIONS:

# VARIABLES:

# CODE
from random import choice

class humanPlayer:
    def getMove(self, gameBoard):
        spaceList = gameBoard.availableMoves()
        while (True):
            try:
                spaceNum = int(input("Enter the position number you want to mark(1-9): ")) - 1
            except:
                print("Invalid input!!! Try again.")
                continue
            if (spaceNum in spaceList):
                break
            print("Invalid input!!! Try again.")
        return spaceNum

class computerPlayer:
    def getMove(self, gameBoard):
        return choice(gameBoard.availableMoves())


class gameBoard:
    def __init__(self):
        self.gameBoard = []
        for iCount in range(9):
            self.gameBoard.append(' ')
            if (iCount in [2, 5, 8]):
                print(iCount + 1)
                continue
            print(iCount + 1, end = '|')
    
    def checkWin(self):
        for rowCount in range(0, 7, 3):
            if ((self.gameBoard[rowCount] != ' ') and (self.gameBoard[rowCount] == self.gameBoard[rowCount + 1]) and (self.gameBoard[rowCount] == self.gameBoard[rowCount + 2])):
                return True
        for colCount in range(3):
            if ((self.gameBoard[colCount] != ' ') and (self.gameBoard[colCount] == self.gameBoard[colCount + 3]) and (self.gameBoard[colCount] == self.gameBoard[colCount + 6])):
                return True
        if ((self.gameBoard[4] != ' ') and (((self.gameBoard[0] == self.gameBoard[4]) and (self.gameBoard[0] == self.gameBoard[8])) or ((self.gameBoard[2] == self.gameBoard[4]) and (self.gameBoard[2] == self.gameBoard[6])))):
            return True
        return False

    def availableMoves(self):
        movesList = []
        for spaceCount in range(9):
            if (self.gameBoard[spaceCount] == ' '):
                movesList.append(spaceCount)
        return(movesList)

    def hasEmptySpace(self):
        for iCount in range(9):
            if (self.gameBoard[iCount] == ' '):
                return True

    def printBoard(self):
        for iCount in range(9):
            if (iCount in [2, 5, 8]):
                print(self.gameBoard[iCount])
                continue
            print(self.gameBoard[iCount], end = '|')

    def makeMove(self, spaceNum, playerLetter):
        self.gameBoard[spaceNum] = playerLetter

def startPlaying(xPlayer, oPlayer, theGame):
    currentPlayer = 'X'
    while theGame.hasEmptySpace():
        print(f"\n\nIt is the turn of {currentPlayer}.")
        if (currentPlayer == 'X'):
            theGame.makeMove(xPlayer.getMove(theGame), currentPlayer)
        else:
            theGame.makeMove(oPlayer.getMove(theGame), currentPlayer)
        theGame.printBoard()
        if theGame.checkWin():
            print(f"Player {currentPlayer} has won!!!\n\n")
            return
        if (currentPlayer == 'X'):
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'
    print("It is a tie")
    return

userOption = None
while userOption not in ['A', 'B', 'C', 'D']:
    userOption = input("Select one option: (A) Player vs Player (B) Player vs Computer (C) Computer vs Computer: ")
    match userOption:
        case 'A':
            xPlayer = humanPlayer()
            oPlayer = humanPlayer()
        case 'B':
            xPlayer = humanPlayer()
            oPlayer = computerPlayer()
        case 'C':
            xPlayer = computerPlayer()
            oPlayer = computerPlayer()
        case _:
            print("Incorrect input!!! Try again.")

theGame = gameBoard()

startPlaying(xPlayer, oPlayer, theGame)
