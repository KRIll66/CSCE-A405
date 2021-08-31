import argparse


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

"""


# place holder for initial argument parseer

def main():
                parser = argparse.ArgumentParser()  # creating object of a class
                parser.add_argument("expr", help = 'Enter an 15-puzzle')
                args = parser.parse_args()  # parsing the args
                print(args.expr)  # printing the arguement
                # rpnstack = rpn_stack.Rpn.Stack()
                # use split method to split string
                for token in args.expr.split():
                        # rpnstack.rpn_push(token)
                        print("\n is token " + token)
if __name__=='__main__':
        main()