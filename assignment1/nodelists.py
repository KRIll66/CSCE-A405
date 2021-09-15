##################################################################################################
#
# nodelists.py
#
# This class is used for keeping track of  open and closed nodes.It is used by PuzzleSolver.py
#
# A Nodelist object is combination of 3 data srtuctures purposed with keeping track of visited and unvisited nodes by a variety of search algorythms.
# nodelist helper function:
#       - purgelist(self) - clears data in openlist, cache, and closedlist. 
#
# Openlist is a list of unvisited Nodes that stored as a 3-tuple, (node, priority, count)  in a heapq. Priority is used for GBFS and A*, and count is used to ensure FIFO operation for identical priorities.
# openlist helper functions:
#       - push_to_openL(self, child_node, priority, count) - pushes node object "child_node" onto the openlist
#       - pop_openL(self) - removes and returns node at the top of the openlist
# 
# Closed, (or visited), nodes are nodes with a unique hash value that are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# ***attention*** Nodes that are visisted but do not have a unique hash are NOT stored in closedlist. Those nonunique nodes are to be stored in the cache.
# closedlist has helper functions: 
#       - push_to_closedL(self, node) - pushed node onto closedlist
#       - closedL_contains(self, hash) - checks if closedlist contains a node with matching hash value
#       - print_closedL(self, goal_state_tble) - prints list of all node state tables in closedlist
#
# Cache, stores all nodes in the search, (i.e visted and nonvisted that are created during the search), with a unique hash value that are stored in closedlist, ( a dictionary of {Key: value} pairs), where the key is expected to be a hashvalue of the nodes state. (see node calss and state class) 
# cache has helper functions: 
#       - push_to_cache(self, node) - pushed node onto cache
#       - cache_contains(self, hash) - checks if cache contains a node with matching hash value
#
# @author Chris Hill
##################################################################################################

import state, sys, heapq
from typing import Final

class Nodelists:

    def __init__ (self): 
        self.openlist = [] #openlist as a hashq
        self.closedlist = {}
        self.cache = {}
    
    # push_to_openL(self, child_node, priority, count)
    # adds a node,its priority, and count to the open list
    # input:
    #   child_node - a Node object
    #   priority - a unique iterable value, (int, float, double, etc.)
    #   count   - used to ensure FIFO operation for identical priorities
    # output:
    #   none
    #
    def push_to_openL(self, child_node, priority, count):
        entry = [priority, count, child_node]
        heapq.heappush(self.openlist, entry)    
        
    # pop_openL(self)
    # removes and return node at top of open list
    # input:
    #   none
    # output:
    #   value - a node object
    #
    def pop_openL(self):
        priority, count, value = heapq.heappop(self.openlist)   #retrieve the node object
        return value

    # push_to_closedL(self)
    # adds a node to the closed list
    # input:
    #   node - a Node object
    # output:
    #   none
    #
    def push_to_closedL(self, node):
        self.closedlist[node.state.get_hash()] = node

    # closedL_contains(self, hash)
    # check if closed list contains node by compare hash value key
    # input:
    #   hash - a unique indenitifer variable of a state object, see states class.
    # output:
    #   boolean
    #
    def closedL_contains(self, hash):
        if self.closedlist.get(hash):
            return True
        else:
            return False

    # push_to_cache(self)
    # adds a node to the cache
    # input:
    #   node - a Node object
    # output:
    #   none
    #
    def push_to_cache(self, node):
        self.cache[node.state.get_hash()] = node

    # cache_contains(self, hash)
    # check if cache contains node by comparing hash value key
    # input:
    #   hash - a unique indenitifer variable of a state object, see states class.
    # output:
    #   boolean
    #
    def cache_contains(self, hash):
        if self.cache.get(hash):
            return True
        else:
            return False

    # print_closedL(self, goal_state_table)
    # recursively displays node states from closed list
    # input:
    #   goal_state_table - a table representing the gooal stat
    # output:
    #   prints node states to screen
    #
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

    # purgelist(self)
    # clearing openlist, closedlist, and cache data for looping main
    # input:
    #   none
    # output:
    #   none
    #
    def purgelist(self):
        self.openlist.clear()
        self.closedlist.clear()
        self.cache.clear()



