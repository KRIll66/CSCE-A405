


"""
Marshall Pratt  -- mpratt6@alaska.edu
Lydia Stark     -- lydiarstark@gmail.com
Chris Hill      -- rhill66@alaska.edu

Assignment 1
CSCE A405 

main.py

This acts as user interface module, for a 15-puzzle solver application. 
It uses a PuzzleSolver.py to find a solution from  a Start State and a Goal state entered by the user.
The user has the option to use either Breadth-First Search , a greedy best-first search , or an A* search to solve the puzzle.

Inputs:
Start State = digits [0-15], (seperated by commas), in any order as a START state for your 15-puzzle problem. Where 0 represents the blank space on the puzzle.
Goal State = digits [0-15], (seperated by commas), in any order as a START state for your 15-puzzle problem. Where 0 represents the blank space on the puzzle.


Outputs, (prints):
Total  number of nodes expanded
The maximum number of nodes 'represented' in the search space
The length of the Solution path
A Sequence of the Solution path 

@author Chris Hill
"""

import node, nodelists, PuzzleSolver, state, copy, sys 

# helper function that looks for any repeating values in a set of numbers, (any set of char's really), and throws error is it finds a repeat
def find_repeat(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            raise ValueError('repeating values!')
        seen.add(num)

    

def main():
    acceptable_values = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
    start = ""
    goal = ""
    # Start State user input error Checking
    print("\nWelcome to 15-puzzle solver. Please follow the prompts for input. If you'd like to exit at any time, press (ctrl + c ) on your keyboard.")
    trigger = True
    while trigger:
        start = input("\nEnter digits [0-15], (seperated by commas), in any order as a START state for your 15-puzzle problem.\nWhere 0 represents the balnk space on the puzzle.\nExample: 0,1,2,9,14,5,6,7,8,3,11,12,10,13,4,15\n\n") 
        start = start.split(",")
        if len(start) < 16:
                print('\nToo few digits! Please try again.\n')
                start.clear()
                continue
        if len(start) > 16:
                print('\nToo many digits! Please try again.\n')
                start.clear()
                continue
        try: 
            find_repeat(start)
        except(ValueError):
            print('\nDo not repeat values. Please try again.\n')
            start.clear()
            continue
        for  index,  item in enumerate(start):
            if item not in acceptable_values:
                print("\nInvalid digit at position: " + str(index) + "\nValue must be a whole number 1-15. Please try again.\n")
                start.clear()
                continue
            else:
                trigger = False
                break
    # Goal State user input error checknig
    trigger = True
    while trigger:
        goal = input("\nNow using the same format as before, enter digits [0-15] as a GOAL state for your 15-puzzle problem.\n") 
        goal = goal.split(",")
        if len(goal) < 16:
                print('\nToo few digits! Please try again.\n')
                goal.clear()
                continue
        if len(goal) > 16:
                print('\nToo many digits! Please try again.\n')
                goal.clear()
                continue
        try: 
            find_repeat(goal)
        except(ValueError):
            print('\nDo not repeat values. Please try again.\n')
            goal.clear()
            continue
        for index, item in enumerate(goal):
            if item not in acceptable_values:
                print("\nInvalid digit at position: " + str(index) + "\nValue must be a whole number 1-15. Please try again.\n")
                goal.clear()
                continue
            else:
                trigger = False
                break
    
    # Type of search user input error checking
    user_selection = 0
    search_str = ""
    trigger = True
    while trigger:
        user_selection = input("\nPlease enter one of the following numbers to select a type of search:\n    1 - Breadth-First Search \n    2 - Greedy Best-First Search using the Manhattan Distance heuristic\n    3 - A* Search using the Manhattan Distance heuristic\n")
        temp = int(user_selection)
        if temp == 1 or temp == 2 or temp == 3:
            if temp == 1:
                search_str = "Breadth-First Search"
            elif temp == 2:
                search_str = "Greedy Best-First Search"
            else:
                search_str = "A* search"
            trigger = False
            break
        else:
            print("Invalid entry. Please try again.\n")
            continue
    
    # once user input error checking is satisfied. prepare data for algorithm

    #start list to matrix w/out numpy
    temp_arr1 = []
    start_table =[]
    for index, item in enumerate(start):
        temp = int(item)
        temp_arr1.append(temp)
        if index % 4 == 3:
            start_table.append(copy.deepcopy(temp_arr1))
            temp_arr1.clear()
    
    #goal list to matrix w/out numpy
    temp_arr2 = []
    goal_table =[]
    for index, item in enumerate(goal):
        temp = int(item)
        temp_arr2.append(temp)
        if index % 4 == 3:
            goal_table.append(copy.deepcopy(temp_arr2))
            temp_arr2.clear()

    #pass tables into puzzle solver along with BFS, Greedy BFS, or A* code selection
    thisPuzzle = PuzzleSolver.PuzzleSolver(goal_table, start_table)
    #we must now pass the opcode 0, 1, or 2 into BFS
    # 1 = BFS, 2 = GBFS, 3 = A star
    print("\n.\n. .\n.  .\n.    .\n.       .\n.           .\n.....thinking........\n.           .\n.       .\n.    .\n.  .\n. .\n.\n")
    hasSolution, solution = thisPuzzle.solvePuzzle(int(user_selection))
    print("\nThe "+ search_str + " algorithm has completed.\n")
    if hasSolution:
        thisPuzzle.displayPuzzle(solution)
    else: print ("There is no solution.\n\n\n           ¯\_ (ツ)_/¯      \n\n\n")

    print("Goodbye.\n")
    
     
        
if __name__=='__main__':
        main()