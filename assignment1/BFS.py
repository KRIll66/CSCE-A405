import node, state, childstates, nodelists, queue


class BFS:


    def __init__(self, goal, start):
        self.currentNode = node.Node(start, None, 1)
        self.goal = node.Node(goal, None, 0)
        self.goalValue = self.goal.hashval
        self.list = nodelists.Nodelists()
        self.nodeCount = 1


    #populates a lifo queue with the path from goal to start
    #displays it all in appropriate order
    def displayBFS (self, goal):
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
        
    


    #this method performs the BFS search
    #returns a boolean operator and a node object of the found goal
    def runBFS (self):

        #if start state is the goal, return solution            
        if self.currentNode.hashval == self.goalValue:
            return True, self.currentNode

        #pushes starting node into openlist
        self.list.push_to_openL(self.currentNode, 1)
        #execute loop until solution or failure
        while True:
            #reached end of possible options
            if len(self.list.openlist) == 0:
                return False, None

            #pop top node from queue and add to closedList
            self.currentNode = self.list.pop_openL()
            self.list.push_to_closedL(self.currentNode)

            #get children from current node and push them onto the openlist
            #if a child is the answer, return that node to main()
            children = childstates.ChildStates(self.currentNode.state)
            childrenStates = children.getChildStates()
            for child in childrenStates:
                    if child.hashValue not in self.list.closedlist and child.hashValue not in self.list.openlist:
                        #create a new node object for this child
                        newNode = node.Node(child.table, self.currentNode, self.currentNode.level + 1)
                        self.nodeCount += 1
                        if child.hashValue == self.goalValue:
                            return True, newNode
                        self.list.push_to_openL(newNode, 1)
        
