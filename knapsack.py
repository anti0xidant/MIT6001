#########
#Tools for building and searching
#decision trees. 0/1 Knapsack problem
#########

class binaryNode(object):
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
        leftBranch = buildTree(current+[todo[0]], todo[1:])

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

def weightLimit(node, x):
    '''
    Analyzes the weight of a node.

    Returns True if weight does not surpass 10 lbs. False otherwise
    '''
    weight = 0
    for item in node.value:
        weight += item[1]
    return weight <= x

def DFS(root, pounds, constraint = weightLimit):
    '''
    Depth-first-search of binary decision tree of knapsack problem.
    Returns a tuple which contains best solution and number of nodes visited.

    root: (binaryNode), root node
    pounds: max weight of knapsack
    constraint: (fnc), determines if node exceeds max weight
    '''
    #Initialize stack and best solution variable
    stack = [root]
    bestSolution = None
    nodesVisited = 0

    #While there are nodes left to look at in the stack:
    while len(stack) > 0:

        #Increment nodesVisited counter
        nodesVisited += 1

        #If the top element is legal:
        if constraint(stack[0], pounds):

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
            
    return (bestSolution, nodesVisited)

def BFS(root, pounds, constraint = weightLimit):
    '''
    Breadth first search of knapsack decision tree.
    Returns a tuple containing best node and number of nodes visited.

    root: where in the tree to begin searching
    pounds: max weight of knapsack
    constraint: function which determines if node exceeds the max weight
    '''
    #Initialize queue, best node, and number of nodes visisted counter
    queue = [root]
    bestNode = None
    numberVisited = 0
    
    #While there are still things left to consider in the queue
    while len(queue) > 0:

        #Increment visit counter
        numberVisited += 1
    
        #If the node isn't overweight
        if constraint(queue[0], pounds):

            #If there isn't a best node yet:
            if bestNode == None:

                #Set this as the best node
                bestNode = queue[0]

            #Elif this node is better than the current best
            elif bestNode < queue[0]:

                #Set this as the best node
                bestNode = queue[0]

            #Remove the node
            current = queue.pop(0)
    
            #If left child exists
            if current.getLeft() != None:

                #Add him to the end of the line
                queue.append(current.getLeft())

            #If right child exists
            if current.getRight() != None:

                #Add him to the end of the line
                queue.append(current.getRight())

        #Else (overweight node)
        else:

            #Remove the node
            queue.pop(0)

    #Return (best node, counter)
    return (bestNode, numberVisited)

    
#Items to steal
#(value, weight)
stealable = [(1, 5),
             (2, 4),
             (3, 3),
             (4, 2),
             (5, 1),
             (5, 5),
             (4, 4),
             (2, 2),
             (1, 1)]

#Test Cases

def T_binaryNodeValue():
    '''
    Tests the lt function of binaryNode
    '''
    testCases = [([], [], False),
                 ([], [(1, 5)], True),
                 ([(1, 5)], [], False),
                 ([(1, 5)], [(1, 5)], False),
                 ([(1, 5), (2, 4), (3, 3)], [(5, 5), (2, 2)], True),
                 ([(5, 1), (4, 2), (5, 5), (4, 4), (3, 3)], [(1, 5), (1, 1), (2, 4)], False)]

    print 'Teseting < operator of binaryNode'
    print 'Initializing two binaryNode objects...'
    node1 = binaryNode(None)
    node2 = binaryNode(None)
    print 'Beginning tests...'
    successCount = 0
    for i in range(len(testCases)):
        node1.value = testCases[i][0]
        node2.value = testCases[i][1]
        expected = testCases[i][2]
        actual = node1 < node2

        if actual == expected:
            result = 'Success'
            successCount += 1
        else:
            result = 'FAILURE'
            
        print 'Test', i+1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print 'End of tests.'
    print 'Result:', str(successCount) + '/' + str(len(testCases))
