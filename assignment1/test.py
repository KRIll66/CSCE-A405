
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
    table2 = [[1,2,3,4], [5,6,7,8], [9,0,11,12], [13,10,14,15]]
    table3 = [[15,8,9,14],[5,10,1,0],[12,4,3,13],[11,2,7,6]]

    #table 4 is table 2 but with a two extra moves to solve
    table4 = [[1, 2, 3, 4], [0, 6, 7, 8], [5, 9, 11, 12], [13, 10, 14, 15]]


    
    #BFS class test
    print ("start of BFS test")


    thisBFS = BFS.BFS(table1, table2)
    #we must now pass the opcode 0, 1, or 2 into BFS
    # 0 = BFS, 1 = GBFS, 2 = A star
    hasSolution, solution = thisBFS.runBFS(2)
    if hasSolution:
        print ("there is a solution!:")
        thisBFS.displayBFS(solution)
    else: print ("no solution found")
    print ("end of BFS test")


    

if __name__=='__main__':
        main()


