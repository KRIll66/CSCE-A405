
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
    table2 = [[2,5,3,4], [1,14,7,8], [9,10,11,12], [13,6,0,15]]
    table3 = [[1,2,3,4], [5,6,7,8], [9,0,11,12], [13,10,14,15]]
    
    #creates a source Node
    source = node.Node(table1, None, 1)
    #creates a middle Node
    middle = node.Node(table2, source, 2)
    #creates a goal Node
    goal = node.Node(table3, middle, 3)
    
    data = nodelists.Nodelists()
    data.push_to_openL(source, 3)
    data.push_to_openL(middle, 2)
    data.push_to_openL(goal, 1)
    
    # printing original 
    print("OG openL : " + str(data.openlist) + "\n")

    data.sort_openL()

    # printing sorted by priority
    print("sorted openL : " + str(data.openlist)+ "\n")

    #BFS class test
    print ("start of BFS test")

    thisBFS = BFS.BFS(table1, table3)
    hasSolution, solution = thisBFS.runBFS()
    if hasSolution:
        print ("there is a solution!:")
        thisBFS.displayBFS(solution)
    else: print ("no solution found")
    print ("end of BFS test")
    

if __name__=='__main__':
        main()


