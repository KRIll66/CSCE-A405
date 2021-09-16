
"""
Created on Tue Aug 31 18:25:01 2021

This is a simple program to test the functionality of node and state classes
this creates two state tables, makaes objects of them, and then calculates their 
manhattan distance

Display:
    goal state, starting state, hashvalue, manhattan distance
"""
import node, state, childstates, nodelists, PuzzleSolver





def main():
    
    
    table1 = [[0,2,3,4], [1,6,7,8], [5,10,11,12], [9,13,14,15]]
    table3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    
    #BFS class test
    print ("start of test")

    thisPuzzle = PuzzleSolver.PuzzleSolver(table1, table3)
    #we must now pass the opcode 0, 1, or 2 into BFS
    # 0 = BFS, 1 = GBFS, 2 = A star
    hasSolution, solution = thisPuzzle.solvePuzzle(3)
    if hasSolution:
        print ("there is a solution!:")
        thisPuzzle.displayPuzzle(solution)
    else: print ("no solution found")


    

if __name__=='__main__':
        main()


