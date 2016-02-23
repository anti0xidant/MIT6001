def genPowerset(L):
    '''
    Assumes L is a list.
    Returns a list of lists that contains all possible
    combinations of the elements of L. E.g., if
    L is [1, 2] it will return a list with elements
    [], [1], [2], [1, 2].
    '''
    powerset = []
    #For every number in the range 0 to 2^len(L):
    for n in range(2**len(L)):

        #Convert that number to binary string
        binaryStr = getBinaryRep(n, len(L))

        #Create a temp subset:
        subset = []
        
        #For every position in binary string:
        for i in range(len(binaryStr)):

            #If that position is equal to 1:
            if binaryStr[i] == '1':

                #Store the parallel position of L in temp list
                subset.append(L[i])
                
        #Add that list to powerset
        powerset.append(subset)

    #Return powerset
    return powerset


def getBinaryRep(n, numDigits):
    '''
    Assumes n and numDigits are non-negative ints.
    Returns a numDigits str that is a binary
    representation of n.
    '''
    result = ''
    #While n is greater than zero:
    while n > 0:
        
        #Append the least significant digit
        leastSignificant = n % 2
        result = str(leastSignificant) + result

        #Slice off the least significant digit
        n = n / 2

    #If numDigits is less than length of binary string:
    if numDigits < len(result):

        #Raise ValueError:
        raise ValueError('numDigits: Inappropriate value')
        
    #Add in enough 0's to make length equal to numDigits
    missingZeroes = numDigits - len(result)
    result = missingZeroes*'0' + result

    #Return result
    return result

def genPowersetRecur(L):
    #Base case (L is empty):
    if len(L) == 0:

        #Return a list containing an empty set.
        return [[]]

    #Else (list is not empty):
    else:

        #Cut off the right-most tip.
        tip = L[-1:]
        
        #Generate subsets of the remaining segment.
        subset = genPowersetRecur(L[:-1])

        newsubset = []
        #For every element of this subset:
        for element in subset:
            
            #Append the right-most tip.
            newsubset.append(element+tip)

        #Return concatenation of unmodified subset with modified subset:
        subset.extend(newsubset)
        return subset

def tGetBinaryRep():
    #case[0] = n
    #case[1] = numDigits
    #case[2] = expected
    cases = ((0, 0, ''),
             (0, 2, '00'),
             (0, 4, '0000'),
             (1, 1, '1'),
             (1, 2, '01'),
             (1, 4, '0001'),
             (3, 2, '11'),
             (3, 4, '0011'),
             (8, 4, '1000'),
             (14, 4, '1110'))

    print 'Testing getBinaryRep()'
    print 'Number of test cases:', len(cases)

    for i in range(len(cases)):
        expected = cases[i][2]
        actual = getBinaryRep(cases[i][0], cases[i][1])

        if expected == actual:
            result = 'Success'
        else:
            result = 'FAILURE'

        print 'Test', i+1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print 'End of tests.'
        
def tGenPowerset(f):
    #case[0] = L
    #case[1] = expected
    cases = (([], [[]]),
              ([1], [[], [1]]),
              ([1,2], [[], [1], [2], [1, 2]]),
              ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))

    print 'Testing genPowerset()'
    print 'Number of test cases:', len(cases)

    for i in range(len(cases)):
        expected = cases[i][1]
        actual = f(cases[i][0])

        if len(expected) != len(actual):
            result = 'FAILURE'
        else:
            result = 'Success'
            for e in expected:
                matched = False
                for a in actual:
                    if a == e:
                        matched = True
                        break
                if not matched:
                    result = 'FAILURE'
                    break
            
        print 'Test', i+1, '-', result
        print '    expected:', expected
        print '    actual:', actual

    print 'End of tests.'
