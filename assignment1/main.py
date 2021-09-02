


"""
Marshall Pratt  --
Lydia Stark     --
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
"print(i)
                if count%4 == 3:
                        print("mod")
                """

import node

# slowly developing argument parser. 

def find_repeat(numbers):
    seen = set()
    for num in numbers:
        #print(num)
        if num in seen:
            raise ValueError('repeating values!')
        seen.add(num)

def main():
        arr = input(" Enter digits [0-15], (seperated by commas), in any order as a START state for you 15-puzzle problem.\n") 
        arr = arr.split(",")
        if len(arr) < 16:
                raise ValueError('too few digits!')
        if len(arr) > 16:
                raise ValueError('too many digits!')
        find_repeat(arr)

        for index, item in enumerate(arr):
            #print(index, item)
            temp = int(item)
            if temp > 15 or temp < 0:
                raise ValueError('invalid digit, must be 1-15')
            arr[index] = temp
            if index % 4 == 3:
                print("mod")
       

        
if __name__=='__main__':
        main()