import node, state, childstates, nodelists


class BFS:


    def __init__(self, start, goal):
        self.currentNode = node.Node(start, None, 0)
        self.goal = node.Node(goal, None, 0)
        self.goalValue = self.goal.hashval
        self.list = nodelists.Nodelists()
        self.nodeCount = 0
    



    def runBFS (self):

        #if start state is the goal, return solution            
        if self.currentNode.hashval == self.goalValue:
            return True, self.currentNode

        #pushes starting node into openlist
        self.list.push_to_openL(self.currentNode, 1)
        #execute loop until solution or failure
        while True:
            #reached end of possible options
            if self.list.openlist.empty():
                return False, None

            #pop top node from queue and add to closedList
            self.currentNode = self.list.pop_openL()
            self.list.push_to_closedL(self.currentNode)

            #get children from current node and push them onto the openlist
            #if a child is the answer, return that node to main()
            children = childstates.ChildStates(self.currentNode.state)
            childrenStates = children.getChildStates()
            for child in childrenStates:
                    if child.hashValue not in self.list.openlist or child.hashValue not in self.list.closedlist:
                        if child.hashValue == self.goalValue:
                            return child
                        self.openlist.push_to_openL(child, 1)
        
