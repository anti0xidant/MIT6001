def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersectD = {}
    differenceD = {}
    history = []

    # For every element in the first dictionary:
    for key in d1:

        # If it exists in the other dictionary:
        if key in d2:

            # Calculate the intersect add it to intersect ditionary
            intersect = f(d1[key], d2[key])
            intersectD[key] = intersect

            # Mark it as completed in history 
            history.append(key)

        # Else (it is unique):
        else:

            # Add it to difference dictionary
            differenceD[key] = d1[key]

    # For every element in second dictionary:
    for key in d2:

        # If it hasn't been marked in history:
        if key not in history:

            # Add it to difference dictionary.
            differenceD[key] = d2[key]

    # Return.
    return (intersectD, differenceD)


def f(a, b):
    return a + b

def interdiffTest():
    # case[0] = d1
    # case[1] = d2
    # case[2] = expected
    cases = (({}, {}, ({}, {})),
             ({1:10}, {2:10}, ({}, {1:10, 2:10})),
              ({1:10}, {1:20}, ({1:30}, {})),
              ({}, {1:10}, ({}, {1:10})),
              ({1:10, 2:10, 3:10}, {1:10, 2:10, 3:10}, ({1:20, 2:20, 3:20}, {})),
              ({1:10, 2:10, 3:10, 4:10, 5:10}, {1:10, 2:10, 3:10, 6:10, 7:10}, ({1:20, 2:20, 3:20}, {4:10, 5:10, 6:10, 7:10})))

    print 'Testing dict_interdiff()'
    print 'Number of cases:', len(cases)

    for i in range(len(cases)):
        expected = cases[i][2]
        actual = dict_interdiff(cases[i][0], cases[i][1])

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test', i + 1, '-', result
        print 'Epected:', expected
        print 'Actual:', actual

    print '\nEnd of tests.'
  
