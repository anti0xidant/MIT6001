def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    toRemove = []
    
    # For every element in L
    for element in L:

        # If f(element) is False:
        if f(element) is False:

            # Mark it for removing.
            toRemove.append(element)

    # For every element that was marked:
    for element in toRemove:

        # Remove it from L
        L.remove(element)

    # Return lenght of L
    return len(L)
        

#run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s

def satisfiesFTest():
    # case[0] = list
    # case[1] = expected
    cases = (([], 0),
             (['a'], 1),
             (['a', 'a'], 2),
             (['', ''], 0),
             (['a', ''], 1),
             (['', 'a'], 1),
             (['b'], 0),
             (['b', 'b'], 0),
             (['b', 'c', 'd'], 0),
             (['a', 'b', 'a'], 2),
             (['a', 'b', 'c', 'a', 'd'], 2),
             (['a', 'b', 'a', 'c', 'b', 'b', 'a'], 3),
             (['b', 'c', 'd', 'e'], 0))

    print 'Testing satisfiesF()'
    print 'Number of tests:', len(cases),'\n'

    for i in range(len(cases)):
        expected = cases[i][1]
        actual = satisfiesF(cases[i][0])

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILED'

        print 'Test', i + 1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print '\nEnd of tests.'
