"""
The ChildStates class is a class that generates all the possible expanded
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

Author:
@Lydia Stark
"""
import state
import copy
class ChildStates:

    #constructor is initialized with a state object
    def __init__(self, state):
        self.startingstate = copy.deepcopy(state)

    #moves the blank space up (if permissable)
    def moveUp(self):
        copyOfState = copy.deepcopy(self.startingstate)
        tuple = copyOfState.getIndex(0)
        blankrow = tuple[0]
        blankcol = tuple[1]
        if(blankrow - 1 >= 0):
            copyOfState.swap(blankrow, blankcol, blankrow - 1, blankcol)
            return copyOfState

    # moves the blank space right (if permissable)
    def moveRight(self):
        copyOfState = copy.deepcopy(self.startingstate)
        tuple = copyOfState.getIndex(0)
        blankrow = tuple[0]
        blankcol = tuple[1]
        if(blankcol + 1 <= 3):
            copyOfState.swap(blankrow, blankcol, blankrow, blankcol + 1)
            return copyOfState

    # moves the blank space down (if permissable)
    def moveDown(self):
        copyOfState = copy.deepcopy(self.startingstate)
        tuple = copyOfState.getIndex(0)
        blankrow = tuple[0]
        blankcol = tuple[1]
        if(blankrow + 1 <= 3):
            copyOfState.swap(blankrow, blankcol, blankrow + 1, blankcol)
            return copyOfState

    # moves the blank space left (if permissable)
    def moveLeft(self):
        copyOfState = copy.deepcopy(self.startingstate)
        tuple = copyOfState.getIndex(0)
        blankrow = tuple[0]
        blankcol = tuple[1]
        if(blankcol - 1 >= 0):
            copyOfState.swap(blankrow, blankcol, blankrow, blankcol - 1)
            return copyOfState

    #This method returns the possible expanded states (i.e. blank space moved up,
    # down, left, right) of a state as a tuple of State objects
    def getChildStates(self):
        tuple = self.startingstate.getIndex(0)
        row = tuple[0]
        col = tuple[1]

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

        if (row == 3 and col == 3):
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





