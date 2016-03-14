def selSort(L):
    '''
    L is an unsorted list.
    Assumes L's content is of homogenous type.
    Returns original L with contents sorted in ascending order
    '''

    #Loop Invariant: Elements in the prefix are sorted and
    #    no element in the prefix are greater than the
    #    smallest element in the suffix.
    
    firstElement = 0
    #While suffix still contains elements:
    while firstElement != len(L):

        #For ever element e in the suffix:
        for i in range(firstElement, len(L)):

            #If e is smaller than first element f of suffix:
            if L[i] < L[firstElement]:

                #Swap positions between e and f
                L[i], L[firstElement] = L[firstElement], L[i]

        #Append f to the prefix
        firstElement = firstElement + 1
