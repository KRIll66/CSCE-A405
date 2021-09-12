


"""
Marshall Pratt  -- mpratt6@alaska.edu
Lydia Stark     -- lydiarstark@gmail.com
Chris Hill      -- rhill66@alaska.edu

Assignment 1
CSCE A405 

main.py

This acts as user interface module, for a 15-puzzle solver application. 
It uses a Breadth-First Search module, a greedy best-first search module, and an A* search module to try to solve the 15-puzzle problem. 

User will enter Start state and Goal state. those will be passed to modules for completion. 

Program returns (prints):
Total  number of nodes expanded
The maximum number of nodes 'represented' in the search space
The length of the Solution path
A Sequence of the Solution path 

@author Chris Hill
"""

import node, nodelists, PuzzleSolver, state, copy, sys 

# slowly developing argument parser. 

def find_repeat(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            raise ValueError('repeating values!')
        seen.add(num)

    

def main():
    trigger = True
   
    goal_table = []
    while trigger:
        start = input("\nEnter digits [0-15], (seperated by commas), in any order as a START state for you 15-puzzle problem.\n") 
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
            print('\nPlease do not repeat values. Please try again.\n')
            start.clear()
            continue
        temp_arr = []
        start_table =[]
        for index, item in enumerate(start):
            temp = int(item)
            if temp > 15 or temp < 0:
                print('\nInvalid digit, must be 1-15. Please try again.\n')
                start.clear()
                continue
            temp_arr.append(temp)
            if index % 4 == 3:
                start_table.append(copy.deepcopy(temp_arr))
                temp_arr.clear()
        trigger = False
        break
    print(start_table)
    trigger = True
    while trigger:
        goal = input("\nNow do using the same format, enter digits [0-15], for a  Goal state.\n") 
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
            print('\nPlease do not type repeating values. Please try again.\n')
            goal.clear()
            continue
        temp_arr2 = []
        goal_table =[]
        for index, item in enumerate(goal):
            temp = int(item)
            if temp > 15 or temp < 0:
                print('\nInvalid digit, must be 1-15. Please try again.\n')
                goal.clear()
                continue
            temp_arr2.append(temp)
            if index % 4 == 3:
                goal_table.append(copy.deepcopy(temp_arr2))
                temp_arr2.clear()
        trigger = False
        break
    print(goal_table)
    trigger = True
    while trigger:
        user_selection = input("\n Please enter one of the following numbers to select a type of search:\n 1    - BFS\n 2    - Greedy BFS\n 3    - A*\n")
        if user_selection != 1 or   user_selection != "2" or   user_selection != "3":
            print("Invalid entry. Please try again.\n")
            continue
        else:
            trigger = False
            break
    #pass tables into puzzle solver along with BFS, Greedy BFS, or A* code selection
    thisPuzzle = PuzzleSolver.PuzzleSolver(start_table, goal_table)
    #we must now pass the opcode 0, 1, or 2 into BFS
    # 1 = BFS, 2 = GBFS, 3 = A star
    hasSolution, solution = thisPuzzle.solvePuzzle(int(user_selection))
    if hasSolution:
        print ("there is a solution!:\n")
        thisPuzzle.displayPuzzle(solution)
    else: print ("no solution found\n")
    print ("end of BFS test\n")
        
if __name__=='__main__':
        main()