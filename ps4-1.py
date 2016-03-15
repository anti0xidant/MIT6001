def getSublists(L, n):
    '''
    L: list of integers.
    n: length of sublist to return
    Returns a list of all possible subsets in L of length n
    '''
    sublists = []

    begin = 0
    end = n - 1

    while end < len(L):
        # generate sublist from begin to end
        sublist = L[begin:end+1]
        
        # add it to the sublist
        sublists.append(sublist)

        #shift begin and end up by 1
        begin += 1
        end += 1

    return sublists


def test():
    #case[0]: L
    #case[1]: n
    #case[2]: sublists
    cases = [([1,2,3], 1, [[1], [2], [3]]),
             ([], 1, []),
             ([1, 2, 3], 0, []),
             ([1, 2, 3], 3, [[1, 2, 3]]),
             ([1, 2, 3], 4, []),
             ([1, 2, 3, 4], 3, [[1, 2, 3], [2, 3, 4]]),
             ([], 4, []),
             ([1, 2, 3, 4], 2, [[1, 2], [2, 3], [3, 4]])]
    print 'Testing getSublists()'
    print 'Number of test cases:', len(cases)
    for i in range(len(cases)):
        actual = getSublists(cases[i][0], cases[i][1])
        expected = cases[i][2]

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test case', i + 1, '-', result
        print '    expected =', expected
        print '    actual = ', actual
    print 'End of tests.'
