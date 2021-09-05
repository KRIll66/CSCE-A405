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

ATTRIBUTES:
priority: int
Aside from int priority, Node values cannot be compared to one another.
To make the item comparable, one must implement some sort of data structure that utilizes the int priority, (or some other mechanism)


@author: Marshall Pratt & Chris Hill
"""
from dataclasses import dataclass, field
from typing import Any
import state

@dataclass(order=True)
class Node:
    

#constructor
    def __init__ (self, values, parent, level):
        priority: int 
        item: Any=field(compare=False)
        self.state = state.State(values)
        self.parent = parent
        self.level = level
        self.hashval = self.state.hashValue
        
        
#display the node's state
    def display (self):
        self.state.display()


        