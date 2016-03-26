#########
#Tools for building and searching
#decision trees. 0/1 Knapsack problem
#########

class binaryNode(object, value):
    def __init__(self, value):
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

def DFS(root, findValue, constraint):
    raise NotImplementedError

def BFS(root, findValue, constraint):
    raise NotImplementedError
