#########
#Tools for building and searching
#decision trees. 0/1 Knapsack problem
#########

class binaryNode(object, value):
    def __init__(self, value):
        '''
        value: a list of items represented as the tuple (value, weight)
        '''
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parentNode = None
    def setLeft(self, node):
        self.leftNode = node
        node.parentNode = self
    def getLeft(self):
        return self.leftNode
    def setRight(self, node):
        self.rightNode = node
        node.parentNode = self
    def getRight(self):
        return self.rightNode
    def getParent(self):
        return self.parent
    def __lt__(self, other):
        '''
        Returns True if value of current node is greater than other node. False otherwise.
        '''
        selfValue = 0
        for item in self.value:
            selfValue += item[0]
        otherValue = 0
        for item in other.value:
            otherValue += item[0]
        return selfValue < otherValue
    def __str__(self):
        return str(self.value)

def buildTree(current, todo):
    '''
    Builds binary decision tree for classic knapsack problem

    current: list of decisions to produce current node
    todo: list of decisions to consider
    '''
    #If there is nothing left todo:
    if len(todo) == 0:

        #Return the current binary node
        return binaryNode(current)

    #Else (things left todo):
    else:

        #Build left branch (includes next todo item)
        leftBranch = buildTree(current+todo[0], todo[1:])

        #Build right branch (excludes next todo item)
        rightBranch = buildTree(current, todo[1:])

        #Create the current node
        here = binaryNode(current)

        #Attach left branch to current node
        here.setLeft(leftBranch)

        #Attahc right branch to current node
        here.setRight(rightBranch)

        #Return the current node
        return here

def DFS(root, constraint):
    '''
    Depth-first-search of binary decision tree of knapsack problem.
    Returns the node which contains the best solution

    root: (binaryNode), root node
    findValue: (fnc), function for determining value of current node
    constraint: (fnc), function to determine if the current node is legal
    '''
    #Initialize stack and best solution variable
    stack = [root]
    bestSolution = None

    #While there are nodes left to look at in the stack:
    while len(stack) > 0:

        #If the top element is legal:
        if constraint(stack[0]):

            #If the best node hasn't been set:
            if bestSolution == None:

                #Set this node as the best
                bestSolution = stack[0]

            #Else(a best value already exists), if this node is better:
            elif bestSolution < stack[0]:

                #Set this node as the best
                bestSolution = stack[0]

            #Remove the top element
            currentSolution = stack.pop(0)

            #If a right child exists:
            if currentSolution.getRight() != None:

                #Push right child to stack
                stack.insert(0, currentSolution.getRight())

            #If a left child exists:
            if currentSolution.getLeft() != None:

                #Push left child to stack
                stack.insert(0, currentSolution.getLeft())

        #Else (node is not legal)
        else:

            #Remove the top element
            stack.pop(0)
            
    return bestSolution

def BFS(root, findValue, constraint):
    raise NotImplementedError
