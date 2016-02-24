def selSort(L):
    '''
    L is an unsorted list.
    Assumes L's content is of homogenous type.
    Returns original L with contents sorted in ascending order
    '''
    firstElement = 0
    #While suffix still contains elements:
    while firstElement != len(L):
        print 'entered loop'
        #For ever element e in the suffix:
        for i in range(firstElement, len(L)):

            #If e is smaller than first element f of suffix:
            if L[i] < L[firstElement]:
                print 'found smaller'
                #Swap positions between e and f
                L[i], L[firstElement] = L[firstElement], L[i]
        print L

        #Append f to the prefix
        firstElement = firstElement + 1
