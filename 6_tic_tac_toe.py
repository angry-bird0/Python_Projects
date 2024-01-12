# THINGS I LEARNED
# 1) 'self' refers to the particular instance of the class that has been created.
# 2) If you create an object without parenthesis, you have actually created a variable that sotres the class not itself, not an instance of the class
# 3) Instances methods in a python class are the methods that are associated to specific instances of a class, and they can access and modify attributes of that class. The first parameter of an instances method is the instance itself (self).
# 4) Static methods inside a class do not need the self parameter. Use the decorator '@staticmethod' to create a static method. They don't have acdess to instance specific data, and can be called on the class itself without creating a parameter. 

import random import choice

class iPlayer:
    def __init__(self, playerLetter):
        self.playerLetter = playerLetter

    def getMove(self, gameBoard):
        pas

class humanPlayer(iPlayer):
    def getMove(self, gameBoard):
        spaceNum = input("Enter the position number you want to mark(1-9): ")
        spaceList = gameBoard.availableMoves()
        while (spaceNum not in spaceList):
            try:
                spaceNum = int(spaceNum)
            except:
                spaceNum = input("Invalid input!!! Try again.")
        return spaceNum

class computerPlayer(iPlayer):
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
        if (((self.gameBoard[0] == self.gameBoard[4]) and (self.gameBoard[0] == self.gameBoard[8])) or ((self.gameBoard[2] == self.gameBoard[4]) and (self.gameBoard[2] == self.gameBoard[6]))):
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
            if (self.gameBoard[iCount] = ' '):
                return True

    def printBoard(self):
        for iCount in range(9):
            if (iCount in [2, 5, 8]):
                print(iCount + 1)
                continue
            print(iCount + 1, end = '|')

    def makeMove(self, spaceNum, playerLetter):
        self.gameBoard[spaceNum] = playerLetter

def startPlaying(self, xPlayer, oPlayer, theGame):
    currentPlayer = 'X'
    while theGame.hasEmptySpace():
        print(f"It is the turn of {currentPlayer}.", end = '')
        theGame.makeMove(theGame.getMove, currentPlayer)
        theGame.printBoard()
        if theGame.checkWin():
            return(f"Player {currentPlayer} has won!!!")
            break
        if (currentPlayer == 'X'):
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'
    print("It is a tie")
