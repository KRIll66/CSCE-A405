##################################################################################################
#
# nodelists.py
#
# This class is used for keeping track of  open and closed nodes.
# Open Nodes are stored in a infinitely sized priority que, (openList), where priority is manually set when pushing a particular node
# Openlist has a couple helper functions, push, and pop
# 
# Closed nodes are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# closedlist has helper functions: push to closed,  contains, (checking if it has a node with certain hash value), a recursive print function, and a purgelist
#
# Chris Hill      -- rhill66@alaska.edu
##################################################################################################

import queue, node, state, sys
from typing import Final

class Nodelists:

    def __init__ (self): 
        #ensuring open list is infinite by setting it it's maxsize to -1
        MAX_SIZE: Final  = -1 
        self.openList = queue.PriorityQueue(MAX_SIZE)
        self.closedlist = {}
    
    # add node and its priority to open list
    def push_to_openL(self, child_node, priority):
        self.openlist.put(child_node, priority)

    # return and remove node from open list
    def pop_openL(self):
        return self.openlist.get()

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

    #clearing p.queue and dictionary data incase we decide to loop program
    def purgelist(self):
        self.openList.queue.clear()
        self.closedlist.clear()



