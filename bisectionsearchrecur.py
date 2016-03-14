def search(L, e):
    '''
    Assumes L is a list, the elements of which are in
        ascending order.
    Returns True if e is in L and False otherwise
    '''

    def bSearch(L, e, low, high):
        #Decrements high-low
        if high == low:
            return e == L[low]
        #Else (more to search):
        else:

            #Find the new midpoint
            midpoint = (low + high) / 2

            #If the new midpoint is e:
            if L[midpoint] == e:

                #return True
                return True

            #Elif the new midpoint is greater than e:
            elif L[midpoint] > e:

                #return test of the lower half
                return bSearch(L, e, low, midpoint-1)

            #Else (the new midpoint is less than e):
            else:

                #return test of the upper half
                return bSearch(L, e, midpoint+1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L)-1)
