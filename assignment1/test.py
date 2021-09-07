
"""
Created on Tue Aug 31 18:25:01 2021

This is a simple program to test the functionality of node and state classes
this creates two state tables, makaes objects of them, and then calculates their 
manhattan distance

Display:
    goal state, starting state, hashvalue, manhattan distance
"""
import node, state, childstates, nodelists, BFS


def main():
    
    
    table1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    table2 = [[1,2,3,4], [5,6,7,8], [13,9,10,11], [0,15,12,14]]
    
    #BFS class test
    print ("start of BFS test")

    thisBFS = BFS.BFS(table1, table2)
    hasSolution, solution = thisBFS.runBFS()
    if hasSolution:
        print ("there is a solution!:")
        thisBFS.displayBFS(solution)
    else: print ("no solution found")
    print ("end of BFS test")
    

if __name__=='__main__':
        main()


