"""
ChildStates class is a class that generates all the possible expanded
states from a starting state and returns them in a tuple.

INPUTS:
starting state: stores a State object that needs to be expanded

OUPUTS:
getChildStates: returns all possible state expansions of startingstate
as State objects in the following order: up state, right state,
down state, left state


FUNCTIONS:
getChildStates: returns all possible state expansions of the startingstate
 as State objects in the following order: up state, right state,
down state, left state
moveUp: moves the blank space up
moveRight: moves the blank space right
moveDown: moves the blank space down
moveLeft: moves the blank space left


VARIABLES:
startingstate = holds a State object
blankrow = holds the row coordinate of the blank space in startingstate's grid
blankcol = holds the column coordinate of the blank space in startingstate's grid


@author: Marshall Pratt
"""
import self as self
import state

class ChildStates:

    #constructor is initialized with a state object, the coordinates of
    #the blank space, and the max size of the grid (note that we could have
    #just used the number 3 instead, but using a variable for the size of
    # the grid allows for future change.
    def __init__(self, state):
        self.startingstate = state
        tuple = self.startingstate.getIndex(0)
        self.blankrow = tuple[0]
        self.blankcol = tuple[1]
        print("row ", self.blankrow)
        print("col ", self.blankcol)


    def moveUp(self):
        copyOfState = self.startingstate
        if(self.blankrow - 1 >= 0):
            copyOfState.swap(self.blankrow, self.blankcol, self.blankrow - 1, self.blankcol)
            return copyOfState

    def moveRight(self):
        copyOfState = self.startingstate
        if(self.blankcol + 1 <= 3):
            copyOfState.swap(self.blankrow, self.blankcol, self.blankrow, self.blankcol + 1)
            return copyOfState

    def moveDown(self):
        copyOfState = self.startingstate
        if(self.blankrow + 1 <= 3):
            copyOfState.swap(self.blankrow, self.blankcol, self.blankrow + 1, self.blankcol)
            return copyOfState

    def moveLeft(self):
        copyOfState = self.startingstate
        if(self.blankcol - 1 >= 0):
            copyOfState.swap(self.blankrow, self.blankcol, self.blankrow, self.blankcol - 1)
            return copyOfState

    #This method returns the possible expanded states of startingstate as
    # a tuple of State objects
    def getChildStates(self):
        row = self.blankrow
        col = self.blankcol

        #The next four if-statements deal with corner spaces
        if (row == 0 and col == 0):
            temp1 = self.moveRight()
            temp2 = self.moveDown()
            return temp1, temp2

        if (row == 0 and col == 3):
            temp1 = self.moveDown()
            temp2 = self.moveLeft()
            return temp1, temp2

        if (row == 3 and col == 0):
            temp1 = self.moveUp()
            temp2 = self.moveRight()
            return temp1, temp2

        if (row == 0 and col == 0):
            temp1 = self.moveUp()
            temp2 = self.moveLeft()
            return temp1, temp2

        #The next four if-statements deal with edge spaces
        if((row == 1 or row == 2) and (col == 0)):
            temp1 = self.moveUp()
            temp2 = self.moveRight()
            temp3 = self.moveDown()
            return temp1, temp2, temp3

        if ((row == 1 or row == 2) and (col == 3)):
            temp1 = self.moveUp()
            temp2 = self.moveDown()
            temp3 = self.moveLeft()
            return temp1, temp2, temp3

        if ((row ==0) and (col == 1 or col == 2)):
            temp1 = self.moveRight()
            temp2 = self.moveDown()
            temp3 = self.moveLeft()
            return temp1, temp2, temp3

        if ((row ==3) and (col == 1 or col == 2)):
            temp1 = self.moveUp()
            temp2 = self.moveRight()
            temp3 = self.moveLeft()
            return temp1, temp2, temp3

        #This if statement deals with middle spaces
        if((row ==1 or row == 2) and (col == 1 or col == 2)):
            temp1 = self.moveUp()
            temp2 = self.moveRight()
            temp3 = self.moveDown()
            temp4 = self.moveLeft()
            return temp1, temp2, temp3, temp4





