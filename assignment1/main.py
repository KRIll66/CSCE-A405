


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

import node, nodelists, state, sys 

# slowly developing argument parser. 

def find_repeat(numbers):
    seen = set()
    for num in numbers:
        #print(num)
        if num in seen:
            raise ValueError('repeating values!')
        seen.add(num)

    

def main():
    trigger = True
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

        for index, item in enumerate(start):
            #print(index, item)
            temp = int(item)
            if temp > 15 or temp < 0:
                print('\nInvalid digit, must be 1-15. Please try again.\n')
                start.clear()
                continue
            start[index] = temp
            if index % 4 == 3:
                print("\nmod\n")
                trigger = False
                break
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

        for index, item in enumerate(goal):
            #print(index, item)
            temp = int(item)
            if temp > 15 or temp < 0:
                print('\nInvalid digit, must be 1-15. Please try again.\n')
                goal.clear()
                continue
            goal[index] = temp
            if index % 4 == 3:
                print("\nmod\n")
                trigger = False
                break
    print("\n MADE IT TO END\n")
    
    
       

        
if __name__=='__main__':
        main()