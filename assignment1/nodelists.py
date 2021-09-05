##################################################################################################
#
# nodelists.py
#
# This class is used for keeping track of  open and closed nodes.
#
# A Nodelist object is combination of 2 data srtuctures purposed with keeping track of visited and unvisited nodes by a variety of search algorythms.
# 
# Open, (or unvisted), Nodes are stored in a openList,  ( a dictionary of {Key: (priority, value)}where key is a hashval, priority is manually set, and value is a node object
# Openlist has the following helper functions:
#       - push_to_openL(self, child_node, priority) - pushes node onto openlist
#       - pop_openL(self) - removes and returns node at the top of the openlist
#       - sort_openL(self) - sort without return
#       - openL_contains(self, hash) - checks if openlist contains a node with matching hash value
# 
# Closed, (or visited), nodes are nodes with a unique hash value that are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# ***attention*** Nodes that are visisted but do not have a unique hash are NOT stored in closedlist. Those nonunique nodes are to be discarded by search algorythms.
# closedlist has helper functions: 
#       - push_to_closedL(self, node) - pushed node onto closedlist
#       - closedL_contains(self, hash) - checks if closedlist contains a node with matching hash value
#       - print_closedL(self, goal_state_tble) - prints list of all node state tables in closedlist
#       - purgelist(self) - clears data in openlist and closedlist.
#
# Chris Hill      -- rhill66@alaska.edu
##################################################################################################

import node, state, sys
from typing import Final

class Nodelists:

    def __init__ (self): 
        self.openlist = {}
        self.closedlist = {}
    
    # add node and its priority to open list
    # input: 
    #   child_node - a Node object
    #   priority - a unique iterable value, (int, float, double, etc.)
    # output:
    #   none
    def push_to_openL(self, child_node, priority):
        self.openlist[child_node.state.get_hash()] = { priority, child_node }

    # return node from top of openL
    def pop_openL(self):
        return self.openlist.pop()

    # sort openlist by priority for A* or Greedy BFS
    def sort_openL(self):
        sorted(self.openlist.items(), key=lambda d: d[1])

    # check if open list contains node by compare hash value key
    # returns boolean
    def openL_contains(self, hash):
        if self.openlist.get(hash):
            return True
        else:
            return False

    # add node to closed list
    def push_to_closedL(self, node):
        self.closedlist[node.state.get_hash()] = node

    # check if closed list contains node by compare hash value key
    # returns boolean
    def closedL_contains(self, hash):
        if self.closedlist.get(hash):
            return True
        else:
            return False


    # recursively display node states from closed list
    #input = raw table of gooal state
    def print_closedL(self, goal_state_tble):
        #find hash val for Goal State
        temp = state.State(goal_state_tble).get_hash()
        #if it's in closed list go to helper function for recursive printing
        val = self.closedlist.get(temp)
        print(val)
        if val:
            self.recursive_helper(val)
            
        else:
            print(" cannot find your goal state in the closed list. ¯\_ (ツ)_/¯ ")
            sys.exit()
        
    #helper function for printing closed list    
    def recursive_helper(self, nodey):

        if nodey.parent == 0 or nodey.parent is None:
            nodey.display()
            return
        else:
            nodey.display() 
            nodey = nodey.parent
            self.recursive_helper(nodey)

    #clearing openlist and closedlist data for whebn we switch search type.
    def purgelist(self):
        self.openlist.clear()
        self.closedlist.clear()



