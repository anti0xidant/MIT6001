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

        # Pop the last element off.
        lastElement = aList.pop()

        # Make sure the remaining segment is flat.
        remainingSegment = aList
        remainingSegment = flatten(remainingSegment)

        # If the last element is a list:
        if type(lastElement) == list:
            
            # Make sure it is flat.
            lastElement = flatten(lastElement)

            # Attach it to remainingSegment via .extend():
            remainingSegment.extend(lastElement)

        # Else (last segment is a string or int:
        else:

            # Attach it to remainingSegment via .append():
            remainingSegment.append(lastElement)

        # Return ajoined list.
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
             ([[], []], []),
             (['a'], ['a']),
              (['a', 1, 'b', 2], ['a', 1, 'b', 2]),
              ([[]], []),
              ([['a']], ['a']),
              ([['a', 1]], ['a', 1]),
               ([['a', 1], 3, ['b', 2], 5], ['a', 1, 3, 'b', 2, 5]),
             ([[[['k'], 'h', 'i', 8, 9], 'z', 'y', 4, 5], 'a', 'b', 1, 2, 5, 7, [], [[['k'], 1, 2], 'a', 1]],
             ['k', 'h', 'i', 8, 9, 'z', 'y', 4, 5, 'a', 'b', 1, 2, 5, 7, 'k', 1, 2, 'a', 1]))

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
