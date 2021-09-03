# -*- coding: utf-8 -*-
"""
Node class stores node state, parent, and a display function

INPUTS:
state: stores the 2D array values, the blank space must be stored as '0'


OUPUTS:
display: prints the state of this node
hashval: calculates a unique code for each state table
mhd:     manhattan distance from this state to the goal state

FUNCTIONS:
display: prints the state of this node
hashval: returns the unique value for this current state

VARIABLES:
table: 2D list with the current values for this Node
value: unique hashvalue for this state table

@author: Marshall Pratt
"""

class State:
    def __init__ (self, table):
        self.table = table
        self.value = self.hashval()
      
 
    
 
    """
    hashval calcualtes a hash valure for the table in the current state.
    To generate a unique number for each possible state this function uses 
    a polynomial approach, this returns a very large and unique integer for 
    each possible state. To make this work the blank value must be stored as 
    a zero in the table.
    
    generates max val of ~ 4.5 x 10^17, min val of ~ 3.3 x 10^6
    
    can return unique value as well as hash value
    
    evaluates [1,2,3] as 1^0 + 2^1 + 3^2...
    """   
    def hashval (self):
        sum = 0             #will be a unique value for every possible state
        hashVal = 0         #choose modulo to generate fewer collisions
        multiplier = 0      #used as the power
    
        
        for i in self.table:
            
            #calculate sum using polynomial 
            for j in i:
                sum = sum + pow(j, multiplier)
                multiplier += 1
             
        
             #if we don't want the full value of sum, choose modulo and 
             #assign to hashVal
        return sum
                
                
   
    #calculate the manhattan distance between self and parent     
    #this appends each state table into a 1D array for easier 
    #navigation for the manhattan distance
    def manhattanDistance (self, goalState):
        
        current=[]  #this state
        goal=[]     #target state
        mhd = 0     #stores manhattan distance
        
        #append self and parent state tables into 1D list for ease of  
        #calcualting manahttan distance values
        for i in self.table:
            for j in i:
                current.append(j)
                
        for i in goalState.state.table:
            for j in i:
                goal.append(j)        

    
        #calculate manhattan distance
        for i in goal:
            if goal.index(i)!=current.index(i):
                mhd = mhd + (abs(goal.index(i)//4 - current.index(i)//4) + abs(goal.index(i)%4 - current.index(i)%4))
                    

        return mhd
    
    
        
#display the current state
    def display (self):
        for i in self.table:
            #newline between rows
            print ("")
            for j in i:
            #replaces 0 with a double underscore for display
                if j != 0:
                    print (j, end = " ")
                else:
                    print ("__", end = "")
            #corrects the display by adding a space to digits < 10
                if j < 10:
                    print (" ", end = "")
        #newlines at end of current state
        print ("")
        print ("")

    #A simple swap function that "moves" the blank space by
    #swapping it with a set of coordinates passed in.
    #Takes in the coordinates in x,y, format, where x is the row and y is the column.
    #First it takes in the coordinates for the blank space, then the
    #coordinates for the space that the blank space is moving to.
    def swap(self, blankx, blanky, intx, inty):
        temp = self.table[inty][intx]
        self.table[inty][intx] = 0
        self.table[blanky][blankx] = temp
   
    
   #a function to return the index of a target value, will be used for swap
    def getIndex (self, val):
        y = 0
        for i in self.table:
            if val in i:
                return y, i.index(val)
            y+=1
    


    
        