# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:25:01 2021

This is a simple program to test the functionality of node and state classes
this creates two state tables, makaes objects of them, and then calculates their 
manhattan distance

Display:
    goal state, starting state, hashvalue, manhattan distance

@author: marsh
"""
import node
import state
import childstates

def main():
    
    
    table1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    table2 = [[2,5,3,4], [1,14,7,8], [9,10,11,12], [13,6,0,15]]
    
    #creates a source Node
    source = node.Node(table2, None, 1)
    #creates a goal Node
    goal = node.Node(table1, None, 1)
    print ("Goal:", end = "")
    goal.display()
    print ("Starting State:", end = "")
    source.display()
    
    #gets manhattan distance from sourcestate to goal state
    mhd = source.state.manhattanDistance(goal)
    print ("The hashvalue for source is :", source.state.value)
    print ("The hashvalue for goal is :", goal.state.value)
    print ("the manhattan distance is:", mhd)
    
    #gets index of desired value, returns  tuple
    indexOfBlank = source.state.getIndex(0)
    print ("index of blank space is: ", indexOfBlank)

    testState = state.State(table2)
    expandedState = childstates.ChildStates(testState)
    expandedState.startingstate.display()

    temp = expandedState.moveUp()
    temp.display()
    temp = expandedState.moveRight()
    temp.display()
    temp = expandedState.moveLeft()
    temp.display()



    
if __name__=='__main__':
        main()


def BFS (start, goal):
    """
    VARIABLES 
    frontier = fifo queue of next nodes to search
    explored = set of explored nodes for comparison to child nodes 
    currentNode = our first node, no parent and path cost of 0
    TODO: change all instances of closedlist and openlist using list class
    """
    currentNode = node.Node(start, None, 0)
    #list = nodelists.Nodelsits()
    
    #if start state is the goal, return solution
    if start == goal:
        return currentNode

    #execute loop until solution or failure
    while True:
        #reached end of possible options
        """"
        if list.openList.empty():
            return "no solution"

        #pop top node from queue and add to closedList
        currentNode = list.pop_openL
        list.push_to_closedL(currentNode)

        #get children from current node and push them onto the openList
        #if a child is the answer, return that node to main()
        TODO: children = childstate.Childstates(currentNode.state)
        TODO: for child in children:
                if child.hashVal not in openList or child.hashVal not in closedList:
                    if child.state == start:
                        return child
                    openList.push_to_openL(child, 1)
        """
