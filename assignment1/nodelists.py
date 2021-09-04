##################################################################################################
#
# nodelists.py
#
#
#
##################################################################################################

import queue, node, state, sys
from typing import Final

class Nodelists:

    def __init__ (self): 
        MAX_SIZE: Final  = 4 
        self.openList = queue.PriorityQueue(MAX_SIZE)
        self.closedlist = {}
    
    def push_to_openL(self, child_node, priority):
        self.openlist.put(child_node, priority)

    def pop_openL(self):
        self.openlist.get()

    def push_to_closedL(self, node):
        self.closedlist[node.state.get_hash()] = node
    
    def openL_contains(self, hash):
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



