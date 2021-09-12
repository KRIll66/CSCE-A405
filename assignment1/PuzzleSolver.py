import node, state, childstates, nodelists, queue


class PuzzleSolver:


    def __init__(self, goal, start):
        self.currentNode = node.Node(start, None, 1)
        self.goal = node.Node(goal, None, 0)
        self.goalValue = self.goal.hashval
        self.list = nodelists.Nodelists()
        self.nodeCount = 1


    #populates a lifo queue with the path from goal to start
    #displays it all in appropriate order
    def displayPuzzle (self, goal):
        print ("Number of Nodes created: ", self.nodeCount)
        print ("Number of levels: ", goal.level)
        temp = goal
        path = queue.LifoQueue()
        #populate a LIFO queue with the path from goal back to start
        while (temp != None):
            path.put(temp)
            temp = temp.parent
        #display the path from start to goal
        while not path.empty():
            temp = path.get()
            temp.display()
        
    


    #this method solves the puzzle using one of three algorithms:
    #Breadth First Search
    #Greedy Best-First Search
    #A star
    #It takes in an opcode as an integer, and returns a boolean operator
    # and a node object of the found goal
    def solvePuzzle(self, code):

        #if start state is the goal, return solution            
        if self.currentNode.hashval == self.goalValue:
            return True, self.currentNode

        #pushes starting node into openlist and into cache
        self.list.push_to_openL(self.currentNode, 1)
        self.list.push_to_cache(self.currentNode)
        #execute loop until solution or failure
        while True:
            #reached end of possible options
            if self.list.openlist.qsize() == 0:
                return False, None

            #pop top node from queue and add to closedList
            self.currentNode = self.list.pop_openL()
            self.currentNode=  self.currentNode[1]
            self.list.push_to_closedL(self.currentNode)

            #get children from current node and push them onto the openlist
            #if a child is the answer, return that node to main()
            children = childstates.ChildStates(self.currentNode.state)
            childrenStates = children.getChildStates()

            f = 0 #cost of expanding to a state, set by default to BFS

            for child in childrenStates:
                    if child.hashValue not in self.list.closedlist and child.hashValue not in  self.list.cache:
                        #create a new node object for this child
                        newNode = node.Node(child.table, self.currentNode, self.currentNode.level + 1)
                        self.nodeCount += 1

                        if child.hashValue == self.goalValue:
                            return True, newNode
                        #f is always one for BFS
                        if(code == 1):
                            f = 1


                        #f is only the manhattan value for greedy best-first search
                        if(code == 2):
                            f = newNode.state.manhattanDistance(self.goal)

                        #f is the manhattan value and the level for A star
                        if(code == 3):
                            f = newNode.state.manhattanDistance(self.goal) + newNode.level

                        #print(f)
                        self.list.push_to_openL(newNode, f)
                        self.list.push_to_cache(newNode)


