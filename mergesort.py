def greaterThan(a,b):
    '''
    Returns True if a > b. False otherwise.
    '''
    return a > b

def lessThan(a, b):
    '''
    Returns True if a < b. False otherwise.
    '''
    return a < b

def merge(left, right, compare):
    '''
    Assumes left and right are already sorted.
    Compare defines an ordering of elements.
    Returns a new ordered list containing the same
    elements from left and right.
    '''
    result = []
    i, j = 0, 0
    #While there is still something left in both left and right to compare:
    while i < len(left) and j < len(right):

        #If one side's first element wins the comparison:
        if compare(left[i], right[j]):

            #Append it to result list
            result.append(left[i])
            i = i + 1

        #Else (the other side's first element won):
        else:

            #Append it to result list
            result.append(right[j])
            j = j + 1

    #At this point, one of the sides is "empty" and only one of the following
    #will run.

    #While there is something remaining in the left half:
    while i < len(left):

        #Append each elemen to the result list
        result.append(left[i])
        i = i + 1

    #While there is somethign remaining in the right half:
    while j < len(right):

        #Append each element to the result list
        result.append(right[j])
        j = j + 1

    #Result is now merged. Return it.
    return result

def mergeSortRecur(L, compare):
    '''
    Assumes L is a list.
    compare defines ordering on elements of L.
    Returns a new sorted list containing the same elements as L.
    '''
    #If L is of zero or one elements long, it is sorted.
    if len(L) < 2:

        #Return L
        return L[:]

    #Else (L can be sorted by mergesort):
    else:

        #Calculate the midpoint
        midpoint = len(L) / 2

        #Mergesort the left half
        leftHalf = mergeSortRecur(L[:midpoint], compare)

        #Mergesort the right half
        rightHalf = mergeSortRecur(L[midpoint:], compare)

        #Left and right half are now sorted. Merge them together
        return merge(leftHalf, rightHalf, compare)

def mergeSort(L, ordering = 0):
    '''
    L is a list of numbers.
    Ordering: 0 (ascending) or 1 (descending). Default: 0
    Returns sorted list. Does not mutate L
    '''
    if ordering != 1 and ordering != 0:
        raise ValueError("Invalid parameter: ordering")

    if ordering == 0:
        ordering = lessThan
    else:
        ordering = greaterThan

    return mergeSortRecur(L, ordering)

def mergeTest():
    #case[0]: left
    #case[1]: right
    #case[2]: compare
    #case[3]: expected
    cases = (([], [], lessThan, []),
             ([1], [], lessThan, [1]),
             ([1, 2, 3], [], lessThan, [1, 2, 3]),
             ([], [1], lessThan, [1]),
             ([], [1, 2, 3], lessThan, [1, 2, 3]),
             ([1, 3, 5], [2, 4, 6], lessThan, [1, 2, 3, 4, 5, 6]),
             ([1], [2], greaterThan, [2, 1]),
             ([5, 3, 1], [6, 4, 2], greaterThan, [6, 5, 4, 3, 2, 1]),
             ([1, 3, 5, 7, 10], [2], lessThan, [1, 2, 3, 5, 7, 10]),
             ([7], [1, 3, 9, 11], lessThan, [1, 3, 7, 9, 11]))

    print 'Testing merg().'
    print 'Number of tests:', len(cases)

    for i in range(len(cases)):
        expected = cases[i][3]
        actual = merge(cases[i][0], cases[i][1], cases[i][2])

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case', i + 1, '-', result
        print '    Parameters:', cases[i][0], cases[i][1], cases[i][2]
        print '    Expected:', expected
        print '    Actual:', actual

    print 'End of tests.'

def mergeSortTest():
    #case[0]: L
    #case[1]: ordering
    #case[2]: expected
    cases = (([], 0, []),
             ([], 1, []),
             ([1], 0, [1]),
             ([1] , 1, [1]),
             ([2, 1, 5, 4, 3], 0, [1, 2, 3, 4, 5]),
             ([2, 1, 5, 3, 4], 1, [5, 4, 3, 2, 1]))

    print 'Testing mergeSort()'
    print 'Number of cases:', len(cases)

    for i in range(len(cases)):
        expected = cases[i][2]
        actual = mergeSort(cases[i][0], cases[i][1])

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case:', i + 1, '-', result
        print '    Parameters:', cases[i][0], cases[i][1]
        print '    Expected:', expected
        print '    Actual:', actual

    print 'End of tests.'
