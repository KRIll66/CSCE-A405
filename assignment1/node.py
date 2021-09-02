# -*- coding: utf-8 -*-
"""
Node class stores node state, parent, and a display function

INPUTS:
parent: pointer to the parent node that expanded this node, allows the
        solution to find its way back to the starting node/state
state: stores the 2D array values, the blank space must be stored as '0'


OUPUTS:
display: prints the state of this node

FUNCTIONS:
display: prints the state of this node


VARIABLES:
state: 2D list with the current values for this Node (TODO: make this an object)
parent: pointer to parent Node


@author: Marshall Pratt
"""
import state


class Node:
    def __init__ (self, values, parent, level):
        self.state = state.State(values)
        self.parent = parent
        self.level = level
        
        
        
#display the current state, recursively display parent states
    def display (self):
        self.state.display()

        