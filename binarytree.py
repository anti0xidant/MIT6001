class binaryNode(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = None
    def setLeft(self, node):
        self.leftNode = node
    def setRight(self, node):
        self.rightNode = node
    def setParent(self, node):
        self.parent = node
    def getLeft(self):
        return self.leftNode
    def getRight(self):
        return self.rightNode
    def getParent(self):
        return self.parent
    def getValue(self):
        return self.value
    def __str__(self):
        return str(self.value)

def DFStree(parent, fnc):
    '''
    Depth-first search which scans left then right node.
    '''
    #Initialize search stack
    stack = [parent]

    #While there are elements in the stack
    while len(stack) > 0:

        #If the front element of stack is the one:
        if fnc(stack[0]):
            print TraceRouteIter(stack[0])
            routeList = TraceRouteRecur(stack[0])
            print PrintRoute(routeList)
            #Return True
            return True

        #else
        else:

            #Remove the front element
            removed_element = stack.pop(0)

            #Push its right element on stack
            if removed_element.getRight() != None:
                stack.insert(0, removed_element.getRight())

            #Push its left element on stack
            if removed_element.getLeft() != None:
                stack.insert(0, removed_element.getLeft())

    #Return False because element was not found
    return False

def BFStree(parent, fnc):
    '''
    Breadth-first search which scans left to right.
    '''
    #Initialize search queue
    queue = [parent]

    #While there are still elements in the queue
    while len(queue) > 0:
        print queue[0]
        #If the front element of the queue is the one:
        if fnc(queue[0]):

            #Return True
            return True

        #Else
        else:

            #Remove the front element
            removed_element = queue.pop(0)

            #If there are kids in the left:
            if removed_element.getLeft() != None:

                #Put them to the back of the line
                queue.append(removed_element.getLeft())

            #If there are kids in the right:
            if removed_element.getRight() != None:
                
                #Put its right kids in the back of the line
                queue.append(removed_element.getRight())

    #Return False because element was not found
    return False

def TraceRouteIter(node):
    route = str(node.getValue())

    #While node has a parent:
    while node.getParent() != None:

        #Store the parent
        parent = node.getParent()
        
        #Add the parent's value to the front of route
        route = str(parent.getValue()) + '-->' + route

        #Shift from node to parent
        node = parent

    #Return route
    return route

def TraceRouteRecur(node):
    #If it is the root node:
    if node.getParent() == None:

        #Return the node in a list
        return [node]

    #Else
    else:

        #Add the node to the end of the route of the rest
        return TraceRouteRecur(node.getParent()) + [node]

def PrintRoute(route_list):
    route = ''

    #While the route_list is not empty:
    while len(route_list) > 0:

        #Remove the last element
        last_element = route_list.pop()

        #Append it to the front of the route string
        route = str(last_element) + '-->' + route


    #Remove the last arrows
    route = route[:-3]
    
    #Return the route string
    return route

def find6(node):
    return node.getValue() == 6
def find10(node):
    return node.getValue() == 10
def find2(node):
    return node.getValue() == 2

n5 = binaryNode(5)
n2 = binaryNode(2)
n1 = binaryNode(1)
n4 = binaryNode(4)
n8 = binaryNode(8)
n6 = binaryNode(6)
n7 = binaryNode(7)
n3 = binaryNode(3)

n5.setLeft(n2)
n2.setParent(n5)
n5.setRight(n8)
n8.setParent(n5)
n2.setLeft(n1)
n1.setParent(n2)
n2.setRight(n4)
n4.setParent(n2)
n8.setLeft(n6)
n6.setParent(n8)
n6.setRight(n7)
n7.setParent(n6)
n4.setLeft(n3)
n3.setParent(n4)

