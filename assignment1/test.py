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



def main():
    
    
    table1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    table2 = [[2,5,3,4], [1,14,7,8], [9,10,11,12], [13,6,0,15]]
    
    
    source = node.Node(table2, None)
    goal = node.Node(table1, None)
    print ("Goal:", end = "")
    goal.display()
    print ("Starting State:", end = "")
    source.display()
    
    mhd = source.state.manhattanDistance(goal)
    print ("The hashvalue for source is :", source.state.value)
    print ("The hashvalue for goal is :", goal.state.value)
    print ("the manhattan distance is:", mhd)

    
if __name__=='__main__':
        main()