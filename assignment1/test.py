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
import nodelists


def main():
    
    
    table1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    table2 = [[2,5,3,4], [1,14,7,8], [9,10,11,12], [13,6,0,15]]
    table3 = [[2,5,3,4], [1,7,14,8], [9,10,11,12], [13,6,0,15]]
    
    #creates a source Node
    source = node.Node(table1, None, 1)
    #creates a middle Node
    middle = node.Node(table2, source, 2)
    #creates a goal Node
    goal = node.Node(table3, middle, 3)

    dual_list = nodelists.Nodelists()
    dual_list.push_to_closedL(source)
    dual_list.push_to_closedL(middle)
    dual_list.push_to_closedL(goal)
    dual_list.print_closedL(table3)

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