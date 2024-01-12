# DICUMENTATION
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

class humanPlayer:
    def getMove(self, iBoard):
        pass

class computerPlayer:
    def getMove(self, iBoard):
        pass

class gameBoard:
    def __init__(self):
        self.gBoard = []
        for iCount in range(9):
            self.gBoard.append(' ')
            if (iCount in [2, 5, 8]):
                print(iCount + 1)
                continue
            print(iCount + 1, end = '|')
    
    def checkWin(self):
        for rowCount in range(0, 7, 3):
            if ((self.gBoard[rowCount] != ' ') and (self.gBoard[rowCount] == self.gBoard[rowCount + 1]) and (self.gBoard[rowCount] == self.gBoard[rowCount + 2])):
                return True
        for colCount in range(3):
            if ((self.gBoard[colCount] != ' ') and (self.gBoard[colCount] == self.gBoard[colCount + 3]) and (self.gBoard[colCount] == self.gBoard[colCount + 6])):
                return True
        return False

    def checkSpace(self):
        for spaceCount in range(9):
            if (self.gBoard[spaceCount] == ' '):
                return True

    def playerTurn(self, spaceNum):
        if (self.spaceNum == ' '):

