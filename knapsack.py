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
    raise NotImplementedError

def DFS(root, findValue, constraint):
    raise NotImplementedError

def BFS(root, findValue, constraint):
    raise NotImplementedError
