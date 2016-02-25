def mergeSort(L, compare = lessThan):
    '''
    Assumes L is a list.
    compare defines ordering on elements of L. Default is ascending.
    Returns a new sorted list containing the same elements as L.
    '''
    #If L is of zero or one elements long, it is sorted.
    if len(L) < 2:

        #Return L
        return L

    #Else (L can be sorted by mergesort):
    else:

        #Calculate the midpoint
        midpoint = len(L) / 2

        #Mergesort the left half
        leftHalf = mergeSort(L[:midpoint])

        #Mergesort the right half
        rightHalf = mergeSort(L[midpoint:]

        #Left and right half are now sorted. Merge them together

def merge(left, right, compare):
    '''
    Assumes left and right are already sorted.
    Compare is defines an ordering of elements.
    Returns a new list containing the same elements from
    left and right.
    '''
    result = []
    i, j = 0, 0
    #While there is still something left in both left and right to compare:
    while i < len(left) and j < len(right):

        #If one side's first element wins the comparison:
        if compare(left[i], right[i]):

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
