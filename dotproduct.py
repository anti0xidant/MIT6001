def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA

    Returns dotproduct (int or float)
    '''
    # Check that both lists are of same length.
    assert len(listA) == len(listB), 'Lists must be equal length'

    sum = 0
    # For each index in listA:
    for i in range(len(listA)):

        # Multiply the pairwise elements.
        product = listA[i] * listB[i]

        # Add the product to the total.
        sum = sum + product

    # Return the total.
    return sum

def dotProductTest():
    # case[0] = listA
    # case[1] = listB
    # case[2] = expected
    cases = (([], [], 0),
             ([1], [2], 2),
             ([1, 3, 5], [2, 4, 6], 44))

    print 'Testing function: dotProduct()'
    print 'Number of test cases:', len(cases), '\n'

    for i in range(len(cases)):
        actual = dotProduct(cases[i][0], cases[i][1])
        expected = cases[i][2]
        if actual == expected:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case', i + 1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print '\nEnd of tests.'
