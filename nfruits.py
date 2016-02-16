def nfruits(fruitBasket, eatPattern):
    '''
    fruitBasket(dict) - key(str, fruit identifier as 1 letter string) : value(int, count of fruits in basket).
    eatPattern(str) - Sequence of fruit identifiers.
    
    Return(int) - maximum quantity of the different types of fruits in the basket.
    '''   
    # For each fruit eaten before arriving:
    for fruit in eatPattern[:-1]:
        
        # Deduct that fruit from the basket.
        fruitBasket[fruit] = fruitBasket[fruit] - 1        
 
        # Increment the other fruits.
        for i in fruitBasket:
            if i != fruit:
                fruitBasket[i] = fruitBasket[i] + 1

    # Deduct the fruit eaten upon arrival.
    lastFruit = eatPattern[-1]
    fruitBasket[lastFruit] = fruitBasket[lastFruit] - 1

    # Return the greatest quantity.
    return max(fruitBasket.values())


def tnfruits():
    # testCases[i][0] = fruitBasket
    # testCases[i][1] = eatPattern
    # testCases[i][2] = expected value
    testCases = [({'C': 8, 'G': 5, 'L': 7, 'S': 10, 'R': 7, 'U': 6, 'Y': 10, 'X': 10}, 'L', 10),
                 ({'I': 9, 'X': 8, 'E': 9, 'N': 6}, 'INI', 11),
                 ({'Q': 5, 'K': 6, 'R': 6, 'M': 7}, 'KQMRM', 8),
                 ({'D': 10}, 'DDD', 7),
                 ({'Q': 6, 'A': 9, 'K': 9, 'E': 7, 'S': 10}, 'AKAKQ', 14),
                 ({'A': 6, 'B': 6, 'I': 8, 'O': 7, 'Q': 8, 'S': 9, 'X': 5}, 'IOBOX', 13),
                 ({'A': 8, 'B': 6, 'K': 10, 'M': 7, 'N': 8, 'U': 9, 'T': 7, 'Y': 10, 'X': 7}, 'X', 10),
                 ({'H': 6, 'G': 7}, 'HGG', 6),
                 ({'D': 5}, 'DDD', 2),
                 ({'V': 8}, 'VVVV', 4)]

    print 'Testing nfruits()'
    print 'Number of test cases:', len(testCases), '\n'

    for i in range(len(testCases)):
        expected = testCases[i][2]
        actual = nfruitsshit(testCases[i][0], testCases[i][1])
        
        if expected == actual:
            result = 'Success'
        else:
            result = 'Failed'
            
        print 'Test', i + 1, '-', result
        print '    Expected:', expected
        print '    Actual:', actual

    print '\nEnd of tests.'
    
def nfruitsshit(fruitsDict, fruitEaten):
    '''
    Returns the maximum quantity out of the different types of fruits
    Takes dictionary containing type of fruit with its quantity
    and string pattern of the fruits eaten.
    
    fruitsDict: dictionary (capital letters -> int)
    fruitEaten: string
    returns: int
    '''
    tempList = []
    fruitsDict[fruitEaten[0]] -=1 
    for fruit in fruitEaten[1:]:
        for keys in fruitsDict:
            if fruit == keys:
                fruitsDict[keys] -= 1
            else:
                fruitsDict[keys] += 1
    for i in fruitsDict:
        tempList.append(fruitsDict[i])
    return max(tempList)
