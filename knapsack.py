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

    current: value of the current node
    todo: list of items to add
    '''
    #If there is nothing left todo:


        #Return the current binary node


    #Else (things left todo):


        #Build left branch (includes next todo item)


        #Build right branch (excludes next todo item)


        #Create the current node


        #Attach left branch to current node


        #Attahc right branch to current node


        #Return the current node
    

def DFS(root, findValue, constraint):
    raise NotImplementedError

def BFS(root, findValue, constraint):
    raise NotImplementedError
