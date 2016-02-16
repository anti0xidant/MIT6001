def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # Base case (if aList is flat):
    if isFlat(aList) == True:

        # Return aList.
        return aList

    # Else (aList is not flat):
    else:

        # Pop the last element off and flatten it.
        lastElement = aList.pop()
        print 'Popped off last element:', lastElement
        print 'Flattening lastElement now...'
        if type(lastElement) == list:
            lastElement = flatten(lastElement)
        print 'Last element after flattening...', lastElement

        # Flatten the remaining segment.
        remainingSegment = aList
        print 'Remaining segment:', remainingSegment
        print 'Flattening remaining segment now...'
        remainingSegment = flatten(remainingSegment)
        print 'Remaining segment after flattening...', remainingSegment

        # Piece them together (using extend fnc) and return.
        if type(lastElement) != list:
            remainingSegment.append(lastElement)
        else:
            remainingSegment.extend(lastElement)
        print 'Pieced together last element and remaining segment to get this:', remainingSegment
        return remainingSegment

def isFlat(aList):
    '''
    aList: a List
    Returns True if aList is flat; False otherwise
    '''
    for element in aList:
        if type(element) == list:
            return False

    return True

def flattenTest():
    # case[0] = list
    # case[1] = expected
    cases = (([], []),
             (['a'], ['a']),
              (['a', 1, 'b', 2], ['a', 1, 'b', 2]),
              ([[]], []),
              ([['a']], ['a']),
              ([['a', 1]], ['a', 1]),
               ([['a', 1], 3, ['b', 2], 5], ['a', 1, 3, 'b', 2, 5]))

    print 'Testing flatten()'
    print 'Number of test cases:', len(cases), '\n'

    for i in range(len(cases)):
        expected = cases[i][1]
        actual = flatten(cases[i][0])
        
        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'
            
        print 'Test', i + 1, '-', result
        print '    Expected:', expected
        print '    Actual:', actual

    print '\nEnd of tests.'
